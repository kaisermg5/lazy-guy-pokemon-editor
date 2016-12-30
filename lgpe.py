#!/usr/bin/env python3

import argparse
import configparser
import sys
import os
import pkmn_parser
import rom_utilities
from translate import check_tmhm_mv_tutor_moves


PBS_POKEMON = os.path.join(sys.path[0], 'pbs/pokemon.txt')


def get_function_matrix(args, rom_object):
    if args.cries:
        print('\nPokémon cry editing is not done yet.\nSorry :(\n')

    full_matrix = (
        (args.pokemon_data, pkmn_parser.get_pokemon_data, rom_object.write_pokemon_data),
        (args.evolutions, pkmn_parser.get_evolutions, rom_object.write_evolutions_data),
        (args.moves, pkmn_parser.get_moves, rom_object.write_pokemon_moves),
        (check_tmhm_mv_tutor_moves(args.tm_hm, 'TM/HM'),
         pkmn_parser.get_tmhm_compatibility, rom_object.write_tmhm_compatibility),
        (check_tmhm_mv_tutor_moves(args.move_tutor, 'move tutor'),
         pkmn_parser.get_move_tutor_compatibility, rom_object.write_move_tutor_compatibility),
        (args.egg_moves, pkmn_parser.get_egg_moves, rom_object.write_egg_moves),
        (args.pokedex_data, pkmn_parser.get_pokedex_data, rom_object.write_pokedex_data),
        (args.names, pkmn_parser.get_name, rom_object.write_pokemon_name),
        (args.dex_order, pkmn_parser.get_dex_order, rom_object.write_dex_order),
        (args.sprite_position, pkmn_parser.get_sprites_position, rom_object.write_sprite_position),
    )

    matrix = ()
    for flag, parse_function, writefunction in full_matrix:
        if flag:
            matrix += (parse_function, writefunction),

    return matrix


def main(args):
    # Load rom
    print('Loading rom...')
    rom = rom_utilities.Rom(args.filename, args.rom_id, not args.dont_delete_repointed_data)
    print('Rom loaded.')

    # Get functions that have to be called
    function_matrix = get_function_matrix(args, rom)
    if len(function_matrix) == 0:
        print('\nNo write flags were given.')
        sys.exit(1)

    # Load pokémon file
    print('Loading pokémon data...')
    if not os.path.exists(PBS_POKEMON):
        print('Pokémon data not found.\nPlace "pokemon.txt" file in pbs directory.')
        sys.exit(1)
    pkmns = configparser.ConfigParser()
    pkmns.read_file(open(PBS_POKEMON, encoding='utf-8'))
    print('Pokémon data loaded.\n')

    # Pokémon loop
    for pk_key in list(pkmns.keys())[1::]:
        # Error message flag
        error = False

        # Get pokémon index
        try:
            index = pkmn_parser.get_index(pkmns[pk_key])
        except rom_utilities.BaseExpectedError as e:
            print('Error inserting pokémon "{0}":\t{1}: {2}'.format(
                pk_key if 'Name' not in pkmns[pk_key] else pkmns[pk_key]['Name'],
                type(e).__name__, e))

        # Functions loop
        for parse_function, write_function in function_matrix:
            try:
                if parse_function is pkmn_parser.get_moves:
                    data = parse_function(pkmns[pk_key], rom.jambo_attack_hack)
                elif parse_function is pkmn_parser.get_dex_order:
                    data = parse_function(pk_key)
                else:
                    data = parse_function(pkmns[pk_key])

                if isinstance(data, tuple):
                    if write_function == rom.write_pokedex_data:
                        write_function(pk_key, *data)
                    else:
                        write_function(index, *data)
                elif write_function == rom.write_egg_moves:
                    write_function(data)
                else:
                    write_function(index, data)
            except rom_utilities.BaseExpectedError as e:
                if not error:
                    print('Error inserting pokémon "{}":'.format(
                        pk_key if 'Name' not in pkmns[pk_key] else pkmns[pk_key]['Name']))
                    error = True
                print('\t{0}: {1}'.format(type(e).__name__, e))
    rom.save()
    print('\n\nPokémon inserted.')


parser = argparse.ArgumentParser(description='Lazy Guy\'s Pokémon Editor (LGPE) is an automatic pokémon '
                                             'editor. It works parsing Pokémon Essentials PBS files, '
                                             'formatting the data to match third generation pokémon games. '
                                             'This is a command line tool, but it needs you to provide some '
                                             'offsets of your rom in the configuration file '
                                             '"./data/roms.ini".\n\n This tool won\'t check at all the data '
                                             'it is overwriting (except for pokémon descriptions and pokémon '
                                             'moves), so make sure to backup your rom before using it, since '
                                             'a simple mistake in your configuration would corrupt you rom.')

parser.add_argument('-i', '--rom-id', metavar='ID',
                    help='identifier of your rom\'s offsets in the file "./data/roms.ini"; '
                         'game code will be read if not specified')


parser.add_argument('-r', dest='dont_delete_repointed_data', action='store_true',
                    help='do not delete data on repoint')


parser.add_argument('-p', '--pokemon-data', action='store_true',
                    help='edit pokémon data')
parser.add_argument('-e', '--evolutions', action='store_true',
                    help='edit pokémon evolutions')
parser.add_argument('-m', '--moves', action='store_true',
                    help='edit pokémon moves')
parser.add_argument('-t', '--tm-hm', action='store_true',
                    help='edit tm/hm pokémon compatibility')
parser.add_argument('-u', '--move-tutor', action='store_true',
                    help='edit move tutor pokémon compatibility')
parser.add_argument('-d', '--pokedex-data', action='store_true',
                    help='edit pokémon pokédex data')
parser.add_argument('-n', '--names', action='store_true',
                    help='edit pokémon names')
parser.add_argument('-o', '--dex-order', action='store_true',
                    help='edit pokémon pokédex order')
parser.add_argument('-g', '--egg-moves', action='store_true',
                    help='edit pokémon egg moves')
parser.add_argument('-s', '--sprite-position', action='store_true',
                    help='edit in-battle pokémon sprites position')
parser.add_argument('-c', '--cries', action='store_true',
                    help='edit pokémon cries *COMING SOON*')


parser.add_argument('filename', help='path to your rom file')


if __name__ == '__main__':
    if len(sys.argv) != 1:
        parsed_args = parser.parse_args()
        main(parsed_args)
    else:
        parser.parse_args(['-h'])

        # Testing...
        # import shutil
        # shutil.copyfile('gen6.gba', 'test.gba')
        # parsed_args = parser.parse_args('-i test -pemtudnogsc test.gba'.split())
        # print(parsed_args)
        # main(parsed_args)
