
import sys
import os

from rom_utilities import BaseExpectedError, StructureError

from data.abilities import ability_dict
from data.items import item_dict
from data.moves import move_dict
from data.types import type_dict
from data.evolutions import evolution_dict
from data.egg_groups import egg_gourp_dict
from data.colors import color_dict
from data.pokemon import pokemon_dict
from data.mvtutor import mvtutor_list
from data.tmhm import tmhm_list
from data.text import character_dict


PBS_TMHM_MVTUTOR = os.path.join(sys.path[0], 'pbs/tm.txt')
tmhm_mvtutor_dict = { }
try:
    with open(PBS_TMHM_MVTUTOR) as f:
        move = None
        for file_line in f:
            if move is not None:
                if move in tmhm_list or move in mvtutor_list:
                    tmhm_mvtutor_dict[move] = file_line[:-1].split(',')
                move = None
            else:
                if file_line[0] == '[':
                    move = file_line[1:-2]
except FileNotFoundError:
    print('TM/HM and move tutor data not found.\nPlace "tm.txt" file in pbs directory.')
    sys.exit(1)

def check_tmhm_mv_tutor_moves(flag, key):
    if not flag:
        return flag
    for move in {'TM/HM': tmhm_list, 'move tutor': mvtutor_list}[key]:
        if move not in tmhm_mvtutor_dict:
            print(('No {0} data about move "{1}". Please add it to "./pbs/the tm.txt" file.\n'
                  'Option ignored.').format(key, move))
            return False
    return True


gender_dict = {
    '__name__': 'pokemon gender rate',
    'AlwaysMale': 0x0,
    'FemaleOneEighth': 0x1f,
    'Female25Percent': 0x3f,
    'Female50Percent': 0x7f,
    'Female75Percent': 0xbf,
    'FemaleSevenEighths': 0xdf,
    'AlwaysFemale': 0xfe,
    'Genderless': 0xff,
}

growth_dict = {
    '__name__': 'pokemon growth rate',
    'Medium': 0x0,
    'MediumFast': 0x0,
    'Erratic': 0x1,
    'Fluctuating': 0x2,
    'Parabolic': 0x3,
    'MediumSlow': 0x3,
    'Fast': 0x4,
    'Slow': 0x5
}


class TranslatingError(BaseExpectedError):
    pass


def pkmn_index(name):
    if name not in pokemon_dict:
        raise TranslatingError('Unknown pokémon "{}".'.format(name))
    return pokemon_dict[name]


to_unsign8 = lambda x: int(x).to_bytes(1, 'little')
to_sign8 = lambda x: int(x).to_bytes(1, 'little', signed=True)
to_unsign16 = lambda x: int(x).to_bytes(2, 'little')


def steps_to_hatch(x):
    return to_unsign8(round(int(x) / 256))


def height_weight(x):
    return to_unsign16(float(x) * 10)


def base_exp(x):
    return b'\xff' if x.isnumeric() and int(x) >= 255 else to_unsign8(x)


def dictionary_search(key, dictionary, function=to_unsign8):
    if key in dictionary:
        return function(dictionary[key])
    else:
        raise TranslatingError('No {0} named "{1}".'.format(dictionary['__name__'], key))


def pkmn_type(line):
    return dictionary_search(line, type_dict)


def item(line):
    return dictionary_search(line, item_dict, to_unsign16)


def gender_rate(line):
    return dictionary_search(line, gender_dict)


def growth_rate(line):
    return dictionary_search(line, growth_dict)


def color(line):
    return dictionary_search(line, color_dict)


def abilities(line):
    data = b''
    for ability in line.split(','):
        data += dictionary_search(ability, ability_dict)
    if len(data) == 1:
        data += to_unsign8(0)
    return data


def moves(line, jambo_hack=False):
    line = line.split(',')
    data = b''
    for i in range(0, len(line), 2):
        if not jambo_hack:
            lvl = int(line[i]) << 9
            move = dictionary_search(line[i + 1], move_dict, lambda x: x)

            if move > 511:
                raise StructureError('Move index "{}" is too big. You should hack your move table.'.format(hex(move)))
            data += to_unsign16(move + lvl)
        else:
            lvl = to_unsign8(line[i])
            move = dictionary_search(line[i + 1], move_dict, to_unsign16)
            data += move + lvl
    return data


def evs(line):
    line = line.split(',')
    n = 0
    for i in range(len(line)):
        n += int(line[i]) << (2 * i)
    return to_unsign16(n)


def text_word(word):
    data = b''
    for char in word:
        try:
            data += character_dict[char]
        except KeyError:
            raise TranslatingError('Unkown character "{}".'.format(char))
    return data


def text(line):
    words = line.split(' ')
    data = text_word(words[0])
    line_weight = len(words[0])
    for i in range(1, len(words)):
        if (line_weight + len(words[i])) > 32:
            data += b'\xfe'
            line_weight = len(words[i])
        else:
            data += character_dict[' ']
            line_weight += 0.6 + len(words[i])

        data += text_word(words[i])
    data += b'\xff'
    return data


def base_stats(line):
    """
    hp, atk, def, speed, sp.atk, sp.def
    """
    data = b''
    for stat in line.split(','):
        data += to_unsign8(stat)
    return data


def egg_groups(line):
    groups = line.split(',')
    data = b''
    for group in groups:
        if group in egg_gourp_dict:
            data += to_unsign8(egg_gourp_dict[group])
        else:
            data += to_unsign8(0)
    if len(data) == 1:
        data *= 2
    return data


EVOLUTIONS_PARAMETER_TYPES_FUNCT = {'lvl': to_unsign16,
                                   'item': lambda x: dictionary_search(x, item_dict, to_unsign16),
                                    'MustDo': lambda x: to_unsign16(0)}


def evolution_parameters(method, parameter):
    if method not in evolution_dict:
        raise TranslatingError('Unknown evolution method "{}".'.format(method))

    method, parameter_type = evolution_dict[method]
    if parameter_type is not None:
        parameter = EVOLUTIONS_PARAMETER_TYPES_FUNCT[parameter_type](parameter)
    else:
        parameter = to_unsign16(0)
    return to_unsign16(method), parameter


def evolutions(line):
    if line != '':
        line = line.split(',')
        if len(line) % 3 != 0:
            raise TranslatingError('Inconsistent number of parameters, evolution parameters, '
                                   'should be always 3.')
        data = b''
        for i in range(0, len(line), 3):
            pkmn = dictionary_search(line[i], pokemon_dict, to_unsign16)
            method, parameter = evolution_parameters(line[i + 1], line[i + 2])

            data += method + parameter + pkmn + b'\x00\x00'
        return data

    return b''


def egg_moves(internal_name, eggmoves_line):
    """
    I'm not sure but i suppose that adding 0x4e20 to the pokemon id is
    done to identify when the word is a pokemon id, since attacks don't
    go that high.
    """
    data = dictionary_search(internal_name, pokemon_dict, lambda x: to_unsign16(x + 0x4e20))
    for move in eggmoves_line.split(','):
        data += dictionary_search(move, move_dict, to_unsign16)
    return data


def move_compatibility(pokemon_name, move_list, data_name):
    n = 0
    for i in range(len(move_list)):
        if move_list[i] not in tmhm_mvtutor_dict:
            raise TranslatingError('No {0} data has been given for move "{1}".'.format(data_name, move_list[i]))

        if pokemon_name in tmhm_mvtutor_dict[move_list[i]]:
            n += 1 << i
    return n


def tmhm_compatibility(pokemon_name):
    return move_compatibility(pokemon_name, tmhm_list, 'TM/HM')


def mvtutor_compatibility(pokemon_name):
    return move_compatibility(pokemon_name, mvtutor_list, 'move tutor')

