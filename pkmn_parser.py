
from rom_utilities import BaseExpectedError

import translate


class ParsingError(BaseExpectedError):
    pass


def get_index(pkmn):
    if 'InternalName' not in pkmn:
        raise ParsingError('Parameter "InternalName" missing.')
    return translate.pkmn_index(pkmn['InternalName'])


def get_dex_order(n):
    try:
        n = int(n)
    except ValueError:
        raise ParsingError('Pokémon header "[{}]" is not a number.'.format(n))
    return (translate.to_unsign16(n),) * 2


def get_name(pkmn):
    if 'Name' not in pkmn:
        raise ParsingError('Pokémon name missing.')
    return translate.text(pkmn['Name'])


PKMN_DATA_MATRIX = (('BaseStats', translate.base_stats),
                    ('Type1', translate.pkmn_type),
                    ('Type2', translate.pkmn_type),
                    ('Rareness', translate.to_unsign8),
                    ('BaseEXP', translate.base_exp),
                    ('EffortPoints', translate.evs),
                    ('WildItemUncommon', translate.item),
                    ('WildItemRare', translate.item),
                    ('GenderRate', translate.gender_rate),
                    ('StepsToHatch', translate.steps_to_hatch),
                    ('Happiness', translate.to_unsign8),
                    ('GrowthRate', translate.growth_rate),
                    ('Compatibility', translate.egg_groups),
                    ('Abilities', translate.abilities),
                    ('__RunRate__', b'\x00'),
                    ('Color', translate.color),
                    ('__Padding__', b'\x00\x00'))


def get_pokemon_data(pkmn):
    data = b''
    for key, function in PKMN_DATA_MATRIX:
        if key not in ('__RunRate__', '__Padding__'):
            if key in pkmn:
                data += function(pkmn[key])
            elif key in ('WildItemUncommon', 'WildItemRare'):
                data += translate.to_unsign16(0)
            elif key == 'Type2':
                data += function(pkmn['Type1'])
            else:
                raise ParsingError('Pokémon attribute "{}" missing.'.format(key))
        else:
            data += function
    return data


def get_evolutions(pkmn):
    if 'Evolutions' in pkmn:
        return translate.evolutions(pkmn['Evolutions'])
    else:
        return b''


def get_moves(pkmn, jambo_attack_hack=False):
    if 'Moves' not in pkmn:
        raise ParsingError('Pokémon moves missing.')
    return translate.moves(pkmn['Moves'], jambo_attack_hack)


def get_tmhm_compatibility(pkmn):
    return translate.tmhm_compatibility(pkmn['InternalName'])


def get_move_tutor_compatibility(pkmn):
    return translate.mvtutor_compatibility(pkmn['InternalName'])


def get_egg_moves(pkmn):
    if 'EggMoves' in pkmn:
        return translate.egg_groups(pkmn['EggMoves'])
    else:
        return b''


def get_sprites_position(pkmn):
    if 'BattlerPlayerY' in pkmn and 'BattlerEnemyY' in pkmn and 'BattlerAltitude' in pkmn:
        player_y = translate.to_sign8(pkmn['BattlerPlayerY'])
        enemy_y = translate.to_sign8(pkmn['BattlerEnemyY'])
        altitude = translate.to_sign8(pkmn['BattlerAltitude'])
        return player_y, enemy_y, altitude
    else:
        raise ParsingError('Missing sprite position parameters. '
                           'Needed: BattlerPlayerY, BattlerEnemyY and BattlerAltitude')


def estimate_comparison(height):
    relation = float(height) / 1.6
    if relation < 0.4:
        trainer_scale, pokemon_scale = 256, 704
    elif relation < 0.6:
        trainer_scale, pokemon_scale = 256, 576
    elif relation < 0.8:
        trainer_scale, pokemon_scale = 256, 384
    elif relation < 1.2:
        trainer_scale = pokemon_scale = 256
    elif relation < 2:
        trainer_scale, pokemon_scale = 384, 256
    elif relation < 3:
        trainer_scale, pokemon_scale = 576, 256
    else:
        trainer_scale, pokemon_scale = 704, 256

    return translate.to_unsign16(trainer_scale), translate.to_unsign16(pokemon_scale)


def get_pokedex_data(pkmn):
    if 'Kind' in pkmn and 'Height' in pkmn and 'Weight' in pkmn and 'Pokedex'in pkmn:
        kind = pkmn['Kind']
        if len(kind) > 11:
            kind = ''.join((''.join(kind.split(' ')).split('-')))
            if len(kind) > 11:
                raise ParsingError('Kind is too long. Max. length is 11 characters')
        kind = translate.text(kind)
        if len(kind) < 12:
            kind += b'\x00' * (12 - len(kind))
        height = translate.height_weight(pkmn['Height'])
        weight = translate.height_weight(pkmn['Weight'])
        first_data = kind + height + weight

        description = translate.text(pkmn['Pokedex']) + b'\x00'

        padding = trainer_offset = pokemon_offset = b'\x00\x00'
        trainer_scale, pokemon_scale = estimate_comparison(pkmn['Height'])

        second_data = padding + pokemon_scale + pokemon_offset + trainer_scale + \
                      trainer_offset + padding

        return first_data, description, second_data

    else:
        raise ParsingError('Missing pokédex data parameters.'
                           'Needed: Kind, Height, Weight, Pokédex')


