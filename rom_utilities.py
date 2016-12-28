
import configparser
import sys
import os

ini_file = configparser.ConfigParser()
ini_file_path = os.path.join(sys.path[0], 'data/roms.ini')
if not os.path.exists(ini_file_path):
    print('Configuration file not founded.')
    sys.exit(1)
ini_file.read_file(open(ini_file_path, encoding='utf-8'))


class BaseExpectedError(Exception):
    pass


class StructureError(BaseExpectedError):
    pass


ATTACK_END_BYTES = (b'\xff\xff',    #Regular
                    b'\x00\x00\xff')    #Jambo


class Rom:
    def __init__(self, filename, rom_id=None, delete_data_on_repoint=True):
        self.delete_data_on_repoint = delete_data_on_repoint
        self.rom_filename = filename
        try:
            with open(self.rom_filename, 'rb') as rom_file:
                self.rom_contents = bytearray(rom_file.read())
        except FileNotFoundError as e:
            print('{0}: {1}'.format(type(e).__name__, e))
            sys.exit(1)

        if rom_id is None:
            rom_id = self.read(0xac, 4).decode()

        self.tmhm_data_size = ini_file[rom_id].getint('TMHMBytesPerEntry')
        self.move_tutor_data_size = ini_file[rom_id].getint('MoveTutorBytesPerEntry')
        self.evolution_data_size = ini_file[rom_id].getint('MaxNumEvolutions') * 8
        self.jambo_attack_hack = ini_file[rom_id].getboolean('JamboAttackHack')
        self.free_space_byte = int(ini_file[rom_id]['FreeSpaceByte'], base=16).to_bytes(1, 'little')
        self.offsets = { }
        for key in ini_file[rom_id]:
            if key not in ('tmhmbytesperentry', 'movetutorbytesperentry',
                           'maxnumevolutions', 'jamboattackhack', 'freespacebyte'):
                self.offsets[key] = int(ini_file[rom_id][key], base=0)

        self.egg_moves_current_size = 0
        self.deleted_on_repoint = []

    def write(self, address, data):
        if data:
            self.rom_contents[address:address + len(data)] = data

    def read(self, address, amount_of_bytes):
        return self.rom_contents[address:address + amount_of_bytes]

    def load_pointer(self, address):
        pointer = int.from_bytes(self.read(address, 4), 'little')
        if 0x7ffffff < pointer < 0xa000000:
            return pointer - 0x8000000
        else:
            raise StructureError('"{}" is not a valid pointer.'.format(hex(pointer)))

    def write_pointer(self, address_to_write, pointer):
        self.write(address_to_write, (pointer + 0x8000000).to_bytes(4, 'little'))

    def find(self, data, start_address=None):
        return self.rom_contents.find(data, start_address)

    def find_free_space(self, amount_of_bytes, aligment=4):
        address = self.find(self.free_space_byte * (amount_of_bytes + aligment - 1),
                            start_address=self.offsets['searchfreespace'])
        return address + ((0,) + tuple(range(1, aligment)))[address % aligment]

    def delete_data(self, address, amount_of_bytes):
        self.write(address, self.free_space_byte * amount_of_bytes)

    def save(self):
        with open(self.rom_filename, 'wb') as rom_file:
            rom_file.write(self.rom_contents)

    def repoint_data(self, pointer_address, data, end_bytes=b'\xff', alignment=4):
        try:
            original_data_address = self.load_pointer(pointer_address)
            if original_data_address not in self.deleted_on_repoint:
                original_data_size = self.find(end_bytes,start_address=original_data_address) \
                                     - original_data_address + len(end_bytes)
            else:
                original_data_size = 0

        except StructureError:
            original_data_address = 0
            original_data_size = 0

        if len(data) <= original_data_size:
            self.write(original_data_address, data)
            self.delete_data(original_data_address + len(data), original_data_size - len(data))
        else:
            if data[-1::] == self.free_space_byte:
                data += b'\x00'
            new_data_address = self.find_free_space(len(data), alignment)
            self.write(new_data_address, data)
            self.write_pointer(pointer_address, new_data_address)
            if self.delete_data_on_repoint:
                self.delete_data(original_data_address, original_data_size)
                self.deleted_on_repoint.append(original_data_address)

    def table_write(self, index, data, table):
        address = self.offsets[table] + index * len(data)
        self.write(address, data)

    def write_pokemon_data(self, index, data):
        if len(data) != 28:
            raise StructureError('Pokémon data should be 28 bytes, but it is {} bytes '
                                    'long.'.format(len(data)))
        self.table_write(index, data, 'pokemondata')

    def write_evolutions_data(self, index, data):
        data_size = len(data)
        if data_size < self.evolution_data_size:
            data += b'\x00' * (self.evolution_data_size - data_size)
        elif data_size > self.evolution_data_size:
            raise StructureError('Evolution data is too big, expected "{0}" bytes, but '
                                    '"{1}" were received.'.format(self.evolution_data_size, data_size))
        self.table_write(index, data, 'evolutions')

    def write_pokemon_moves(self, index, data):
        data += ATTACK_END_BYTES[self.jambo_attack_hack]
        pointer_address = index * 4 + self.offsets['moves']
        self.repoint_data(pointer_address, data, ATTACK_END_BYTES[self.jambo_attack_hack],
                          (2, 1)[self.jambo_attack_hack])

    def write_tmhm_compatibility(self, index, n):
        """
        n is an int, but each one of its binary digits represents a tm or hm
        """
        try:
            data = n.to_bytes(self.tmhm_data_size, 'little')
        except OverflowError:
            raise StructureError('Too many TM/HM\'s were given.')
        self.table_write(index, data, 'tmhmcompatibility')

    def write_move_tutor_compatibility(self, index, n):
        """
        n is an int, but each one of its binary digits represents a move
        """
        try:
            data = n.to_bytes(self.move_tutor_data_size, 'little')
        except OverflowError:
            raise StructureError('Too many moves\'s were given.')
        self.table_write(index, data, 'movetutorcompatibility')

    def write_egg_moves(self, data):
        self.write(self.offsets['eggmoves'] + self.egg_moves_current_size, data)
        self.egg_moves_current_size += len(data)

    def write_pokemon_name(self, index, data):
        if len(data) < 11:
            data += b'\x00' * (11 - len(data))
        self.table_write(index, data, 'pokemonnames')

    def write_pokedex_data(self, index, first_data, description, second_data):
        if len(first_data) != 16 or len(second_data) != 12:
            raise StructureError('Incorrect pokédex data format.')
        address = index * 32 + self.offsets['pokedexdata']
        self.write(address, first_data)
        address += 16
        self.repoint_data(address, description + b'\x00', alignment=1)
        address += 4
        self.write(address, second_data)

    def write_sprite_position(self, index, player_y, enemy_y, altitude):
        if len(player_y) != 1 and len(enemy_y) != 1 and len(altitude) != 1:
            raise StructureError('Invalid sprites positions.')
        self.table_write(index, altitude, 'altitude')
        for key, data in ('playery', player_y), ('enemyy', enemy_y):
            self.write(self.offsets[key] + 1 + 4 * index, data)

    def write_dex_order(self, index, national, regional):
        if len(national) != 2 or len(regional) != 2:
            raise StructureError('Dex numbers must be 2 bytes long.')
        self.table_write(index, national, 'nationaldex')
        self.table_write(index, regional, 'regionaldex')





