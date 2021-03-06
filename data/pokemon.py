pokemon_dict = {
    '__name__': 'pokémon',
    'BULBASAUR': 0x1,
    'IVYSAUR': 0x2,
    'VENUSAUR': 0x3,
    'CHARMANDER': 0x4,
    'CHARMELEON': 0x5,
    'CHARIZARD': 0x6,
    'SQUIRTLE': 0x7,
    'WARTORTLE': 0x8,
    'BLASTOISE': 0x9,
    'CATERPIE': 0xa,
    'METAPOD': 0xb,
    'BUTTERFREE': 0xc,
    'WEEDLE': 0xd,
    'KAKUNA': 0xe,
    'BEEDRILL': 0xf,
    'PIDGEY': 0x10,
    'PIDGEOTTO': 0x11,
    'PIDGEOT': 0x12,
    'RATTATA': 0x13,
    'RATICATE': 0x14,
    'SPEAROW': 0x15,
    'FEAROW': 0x16,
    'EKANS': 0x17,
    'ARBOK': 0x18,
    'PIKACHU': 0x19,
    'RAICHU': 0x1a,
    'SANDSHREW': 0x1b,
    'SANDSLASH': 0x1c,
    'NIDORANfE': 0x1d,
    'NIDORINA': 0x1e,
    'NIDOQUEEN': 0x1f,
    'NIDORANmA': 0x20,
    'NIDORINO': 0x21,
    'NIDOKING': 0x22,
    'CLEFAIRY': 0x23,
    'CLEFABLE': 0x24,
    'VULPIX': 0x25,
    'NINETALES': 0x26,
    'JIGGLYPUFF': 0x27,
    'WIGGLYTUFF': 0x28,
    'ZUBAT': 0x29,
    'GOLBAT': 0x2a,
    'ODDISH': 0x2b,
    'GLOOM': 0x2c,
    'VILEPLUME': 0x2d,
    'PARAS': 0x2e,
    'PARASECT': 0x2f,
    'VENONAT': 0x30,
    'VENOMOTH': 0x31,
    'DIGLETT': 0x32,
    'DUGTRIO': 0x33,
    'MEOWTH': 0x34,
    'PERSIAN': 0x35,
    'PSYDUCK': 0x36,
    'GOLDUCK': 0x37,
    'MANKEY': 0x38,
    'PRIMEAPE': 0x39,
    'GROWLITHE': 0x3a,
    'ARCANINE': 0x3b,
    'POLIWAG': 0x3c,
    'POLIWHIRL': 0x3d,
    'POLIWRATH': 0x3e,
    'ABRA': 0x3f,
    'KADABRA': 0x40,
    'ALAKAZAM': 0x41,
    'MACHOP': 0x42,
    'MACHOKE': 0x43,
    'MACHAMP': 0x44,
    'BELLSPROUT': 0x45,
    'WEEPINBELL': 0x46,
    'VICTREEBEL': 0x47,
    'TENTACOOL': 0x48,
    'TENTACRUEL': 0x49,
    'GEODUDE': 0x4a,
    'GRAVELER': 0x4b,
    'GOLEM': 0x4c,
    'PONYTA': 0x4d,
    'RAPIDASH': 0x4e,
    'SLOWPOKE': 0x4f,
    'SLOWBRO': 0x50,
    'MAGNEMITE': 0x51,
    'MAGNETON': 0x52,
    'FARFETCHD': 0x53,
    'DODUO': 0x54,
    'DODRIO': 0x55,
    'SEEL': 0x56,
    'DEWGONG': 0x57,
    'GRIMER': 0x58,
    'MUK': 0x59,
    'SHELLDER': 0x5a,
    'CLOYSTER': 0x5b,
    'GASTLY': 0x5c,
    'HAUNTER': 0x5d,
    'GENGAR': 0x5e,
    'ONIX': 0x5f,
    'DROWZEE': 0x60,
    'HYPNO': 0x61,
    'KRABBY': 0x62,
    'KINGLER': 0x63,
    'VOLTORB': 0x64,
    'ELECTRODE': 0x65,
    'EXEGGCUTE': 0x66,
    'EXEGGUTOR': 0x67,
    'CUBONE': 0x68,
    'MAROWAK': 0x69,
    'HITMONLEE': 0x6a,
    'HITMONCHAN': 0x6b,
    'LICKITUNG': 0x6c,
    'KOFFING': 0x6d,
    'WEEZING': 0x6e,
    'RHYHORN': 0x6f,
    'RHYDON': 0x70,
    'CHANSEY': 0x71,
    'TANGELA': 0x72,
    'KANGASKHAN': 0x73,
    'HORSEA': 0x74,
    'SEADRA': 0x75,
    'GOLDEEN': 0x76,
    'SEAKING': 0x77,
    'STARYU': 0x78,
    'STARMIE': 0x79,
    'MRMIME': 0x7a,
    'SCYTHER': 0x7b,
    'JYNX': 0x7c,
    'ELECTABUZZ': 0x7d,
    'MAGMAR': 0x7e,
    'PINSIR': 0x7f,
    'TAUROS': 0x80,
    'MAGIKARP': 0x81,
    'GYARADOS': 0x82,
    'LAPRAS': 0x83,
    'DITTO': 0x84,
    'EEVEE': 0x85,
    'VAPOREON': 0x86,
    'JOLTEON': 0x87,
    'FLAREON': 0x88,
    'PORYGON': 0x89,
    'OMANYTE': 0x8a,
    'OMASTAR': 0x8b,
    'KABUTO': 0x8c,
    'KABUTOPS': 0x8d,
    'AERODACTYL': 0x8e,
    'SNORLAX': 0x8f,
    'ARTICUNO': 0x90,
    'ZAPDOS': 0x91,
    'MOLTRES': 0x92,
    'DRATINI': 0x93,
    'DRAGONAIR': 0x94,
    'DRAGONITE': 0x95,
    'MEWTWO': 0x96,
    'MEW': 0x97,
    'CHIKORITA': 0x98,
    'BAYLEEF': 0x99,
    'MEGANIUM': 0x9a,
    'CYNDAQUIL': 0x9b,
    'QUILAVA': 0x9c,
    'TYPHLOSION': 0x9d,
    'TOTODILE': 0x9e,
    'CROCONAW': 0x9f,
    'FERALIGATR': 0xa0,
    'SENTRET': 0xa1,
    'FURRET': 0xa2,
    'HOOTHOOT': 0xa3,
    'NOCTOWL': 0xa4,
    'LEDYBA': 0xa5,
    'LEDIAN': 0xa6,
    'SPINARAK': 0xa7,
    'ARIADOS': 0xa8,
    'CROBAT': 0xa9,
    'CHINCHOU': 0xaa,
    'LANTURN': 0xab,
    'PICHU': 0xac,
    'CLEFFA': 0xad,
    'IGGLYBUFF': 0xae,
    'TOGEPI': 0xaf,
    'TOGETIC': 0xb0,
    'NATU': 0xb1,
    'XATU': 0xb2,
    'MAREEP': 0xb3,
    'FLAAFFY': 0xb4,
    'AMPHAROS': 0xb5,
    'BELLOSSOM': 0xb6,
    'MARILL': 0xb7,
    'AZUMARILL': 0xb8,
    'SUDOWOODO': 0xb9,
    'POLITOED': 0xba,
    'HOPPIP': 0xbb,
    'SKIPLOOM': 0xbc,
    'JUMPLUFF': 0xbd,
    'AIPOM': 0xbe,
    'SUNKERN': 0xbf,
    'SUNFLORA': 0xc0,
    'YANMA': 0xc1,
    'WOOPER': 0xc2,
    'QUAGSIRE': 0xc3,
    'ESPEON': 0xc4,
    'UMBREON': 0xc5,
    'MURKROW': 0xc6,
    'SLOWKING': 0xc7,
    'MISDREAVUS': 0xc8,
    'UNOWN': 0xc9,
    'WOBBUFFET': 0xca,
    'GIRAFARIG': 0xcb,
    'PINECO': 0xcc,
    'FORRETRESS': 0xcd,
    'DUNSPARCE': 0xce,
    'GLIGAR': 0xcf,
    'STEELIX': 0xd0,
    'SNUBBULL': 0xd1,
    'GRANBULL': 0xd2,
    'QWILFISH': 0xd3,
    'SCIZOR': 0xd4,
    'SHUCKLE': 0xd5,
    'HERACROSS': 0xd6,
    'SNEASEL': 0xd7,
    'TEDDIURSA': 0xd8,
    'URSARING': 0xd9,
    'SLUGMA': 0xda,
    'MAGCARGO': 0xdb,
    'SWINUB': 0xdc,
    'PILOSWINE': 0xdd,
    'CORSOLA': 0xde,
    'REMORAID': 0xdf,
    'OCTILLERY': 0xe0,
    'DELIBIRD': 0xe1,
    'MANTINE': 0xe2,
    'SKARMORY': 0xe3,
    'HOUNDOUR': 0xe4,
    'HOUNDOOM': 0xe5,
    'KINGDRA': 0xe6,
    'PHANPY': 0xe7,
    'DONPHAN': 0xe8,
    'PORYGON2': 0xe9,
    'STANTLER': 0xea,
    'SMEARGLE': 0xeb,
    'TYROGUE': 0xec,
    'HITMONTOP': 0xed,
    'SMOOCHUM': 0xee,
    'ELEKID': 0xef,
    'MAGBY': 0xf0,
    'MILTANK': 0xf1,
    'BLISSEY': 0xf2,
    'RAIKOU': 0xf3,
    'ENTEI': 0xf4,
    'SUICUNE': 0xf5,
    'LARVITAR': 0xf6,
    'PUPITAR': 0xf7,
    'TYRANITAR': 0xf8,
    'LUGIA': 0xf9,
    'HOOH': 0xfa,
    'CELEBI': 0xfb,
    'TREECKO': 0x115,
    'GROVYLE': 0x116,
    'SCEPTILE': 0x117,
    'TORCHIC': 0x118,
    'COMBUSKEN': 0x119,
    'BLAZIKEN': 0x11a,
    'MUDKIP': 0x11b,
    'MARSHTOMP': 0x11c,
    'SWAMPERT': 0x11d,
    'POOCHYENA': 0x11e,
    'MIGHTYENA': 0x11f,
    'ZIGZAGOON': 0x120,
    'LINOONE': 0x121,
    'WURMPLE': 0x122,
    'SILCOON': 0x123,
    'BEAUTIFLY': 0x124,
    'CASCOON': 0x125,
    'DUSTOX': 0x126,
    'LOTAD': 0x127,
    'LOMBRE': 0x128,
    'LUDICOLO': 0x129,
    'SEEDOT': 0x12a,
    'NUZLEAF': 0x12b,
    'SHIFTRY': 0x12c,
    'NINCADA': 0x12d,
    'NINJASK': 0x12e,
    'SHEDINJA': 0x12f,
    'TAILLOW': 0x130,
    'SWELLOW': 0x131,
    'SHROOMISH': 0x132,
    'BRELOOM': 0x133,
    'SPINDA': 0x134,
    'WINGULL': 0x135,
    'PELIPPER': 0x136,
    'SURSKIT': 0x137,
    'MASQUERAIN': 0x138,
    'WAILMER': 0x139,
    'WAILORD': 0x13a,
    'SKITTY': 0x13b,
    'DELCATTY': 0x13c,
    'KECLEON': 0x13d,
    'BALTOY': 0x13e,
    'CLAYDOL': 0x13f,
    'NOSEPASS': 0x140,
    'TORKOAL': 0x141,
    'SABLEYE': 0x142,
    'BARBOACH': 0x143,
    'WHISCASH': 0x144,
    'LUVDISC': 0x145,
    'CORPHISH': 0x146,
    'CRAWDAUNT': 0x147,
    'FEEBAS': 0x148,
    'MILOTIC': 0x149,
    'CARVANHA': 0x14a,
    'SHARPEDO': 0x14b,
    'TRAPINCH': 0x14c,
    'VIBRAVA': 0x14d,
    'FLYGON': 0x14e,
    'MAKUHITA': 0x14f,
    'HARIYAMA': 0x150,
    'ELECTRIKE': 0x151,
    'MANECTRIC': 0x152,
    'NUMEL': 0x153,
    'CAMERUPT': 0x154,
    'SPHEAL': 0x155,
    'SEALEO': 0x156,
    'WALREIN': 0x157,
    'CACNEA': 0x158,
    'CACTURNE': 0x159,
    'SNORUNT': 0x15a,
    'GLALIE': 0x15b,
    'LUNATONE': 0x15c,
    'SOLROCK': 0x15d,
    'AZURILL': 0x15e,
    'SPOINK': 0x15f,
    'GRUMPIG': 0x160,
    'PLUSLE': 0x161,
    'MINUN': 0x162,
    'MAWILE': 0x163,
    'MEDITITE': 0x164,
    'MEDICHAM': 0x165,
    'SWABLU': 0x166,
    'ALTARIA': 0x167,
    'WYNAUT': 0x168,
    'DUSKULL': 0x169,
    'DUSCLOPS': 0x16a,
    'ROSELIA': 0x16b,
    'SLAKOTH': 0x16c,
    'VIGOROTH': 0x16d,
    'SLAKING': 0x16e,
    'GULPIN': 0x16f,
    'SWALOT': 0x170,
    'TROPIUS': 0x171,
    'WHISMUR': 0x172,
    'LOUDRED': 0x173,
    'EXPLOUD': 0x174,
    'CLAMPERL': 0x175,
    'HUNTAIL': 0x176,
    'GOREBYSS': 0x177,
    'ABSOL': 0x178,
    'SHUPPET': 0x179,
    'BANETTE': 0x17a,
    'SEVIPER': 0x17b,
    'ZANGOOSE': 0x17c,
    'RELICANTH': 0x17d,
    'ARON': 0x17e,
    'LAIRON': 0x17f,
    'AGGRON': 0x180,
    'CASTFORM': 0x181,
    'VOLBEAT': 0x182,
    'ILLUMISE': 0x183,
    'LILEEP': 0x184,
    'CRADILY': 0x185,
    'ANORITH': 0x186,
    'ARMALDO': 0x187,
    'RALTS': 0x188,
    'KIRLIA': 0x189,
    'GARDEVOIR': 0x18a,
    'BAGON': 0x18b,
    'SHELGON': 0x18c,
    'SALAMENCE': 0x18d,
    'BELDUM': 0x18e,
    'METANG': 0x18f,
    'METAGROSS': 0x190,
    'REGIROCK': 0x191,
    'REGICE': 0x192,
    'REGISTEEL': 0x193,
    'KYOGRE': 0x194,
    'GROUDON': 0x195,
    'RAYQUAZA': 0x196,
    'LATIAS': 0x197,
    'LATIOS': 0x198,
    'JIRACHI': 0x199,
    'DEOXYS': 0x19a,
    'CHIMECHO': 0x19b,
    'TURTWIG': 0x19c,
    'GROTLE': 0x19d,
    'TORTERRA': 0x19e,
    'CHIMCHAR': 0x19f,
    'MONFERNO': 0x1a0,
    'INFERNAPE': 0x1a1,
    'PIPLUP': 0x1a2,
    'PRINPLUP': 0x1a3,
    'EMPOLEON': 0x1a4,
    'STARLY': 0x1a5,
    'STARAVIA': 0x1a6,
    'STARAPTOR': 0x1a7,
    'BIDOOF': 0x1a8,
    'BIBAREL': 0x1a9,
    'KRICKETOT': 0x1aa,
    'KRICKETUNE': 0x1ab,
    'SHINX': 0x1ac,
    'LUXIO': 0x1ad,
    'LUXRAY': 0x1ae,
    'BUDEW': 0x1af,
    'ROSERADE': 0x1b0,
    'CRANIDOS': 0x1b1,
    'RAMPARDOS': 0x1b2,
    'SHIELDON': 0x1b3,
    'BASTIODON': 0x1b4,
    'BURMY': 0x1b5,
    'WORMADAM': 0x1b6,
    'MOTHIM': 0x1b7,
    'COMBEE': 0x1b8,
    'VESPIQUEN': 0x1b9,
    'PACHIRISU': 0x1ba,
    'BUIZEL': 0x1bb,
    'FLOATZEL': 0x1bc,
    'CHERUBI': 0x1bd,
    'CHERRIM': 0x1be,
    'SHELLOS': 0x1bf,
    'GASTRODON': 0x1c0,
    'AMBIPOM': 0x1c1,
    'DRIFLOON': 0x1c2,
    'DRIFBLIM': 0x1c3,
    'BUNEARY': 0x1c4,
    'LOPUNNY': 0x1c5,
    'MISMAGIUS': 0x1c6,
    'HONCHKROW': 0x1c7,
    'GLAMEOW': 0x1c8,
    'PURUGLY': 0x1c9,
    'CHINGLING': 0x1ca,
    'STUNKY': 0x1cb,
    'SKUNTANK': 0x1cc,
    'BRONZOR': 0x1cd,
    'BRONZONG': 0x1ce,
    'BONSLY': 0x1cf,
    'MIMEJR': 0x1d0,
    'HAPPINY': 0x1d1,
    'CHATOT': 0x1d2,
    'SPIRITOMB': 0x1d3,
    'GIBLE': 0x1d4,
    'GABITE': 0x1d5,
    'GARCHOMP': 0x1d6,
    'MUNCHLAX': 0x1d7,
    'RIOLU': 0x1d8,
    'LUCARIO': 0x1d9,
    'HIPPOPOTAS': 0x1da,
    'HIPPOWDON': 0x1db,
    'SKORUPI': 0x1dc,
    'DRAPION': 0x1dd,
    'CROAGUNK': 0x1de,
    'TOXICROAK': 0x1df,
    'CARNIVINE': 0x1e0,
    'FINNEON': 0x1e1,
    'LUMINEON': 0x1e2,
    'MANTYKE': 0x1e3,
    'SNOVER': 0x1e4,
    'ABOMASNOW': 0x1e5,
    'WEAVILE': 0x1e6,
    'MAGNEZONE': 0x1e7,
    'LICKILICKY': 0x1e8,
    'RHYPERIOR': 0x1e9,
    'TANGROWTH': 0x1ea,
    'ELECTIVIRE': 0x1eb,
    'MAGMORTAR': 0x1ec,
    'TOGEKISS': 0x1ed,
    'YANMEGA': 0x1ee,
    'LEAFEON': 0x1ef,
    'GLACEON': 0x1f0,
    'GLISCOR': 0x1f1,
    'MAMOSWINE': 0x1f2,
    'PORYGONZ': 0x1f3,
    'GALLADE': 0x1f4,
    'PROBOPASS': 0x1f5,
    'DUSKNOIR': 0x1f6,
    'FROSLASS': 0x1f7,
    'ROTOM': 0x1f8,
    'UXIE': 0x1f9,
    'MESPRIT': 0x1fa,
    'AZELF': 0x1fb,
    'DIALGA': 0x1fc,
    'PALKIA': 0x1fd,
    'HEATRAN': 0x1fe,
    'REGIGIGAS': 0x1ff,
    'GIRATINA': 0x200,
    'CRESSELIA': 0x201,
    'PHIONE': 0x202,
    'MANAPHY': 0x203,
    'DARKRAI': 0x204,
    'SHAYMIN': 0x205,
    'ARCEUS': 0x206,
    'VICTINI': 0x207,
    'SNIVY': 0x208,
    'SERVINE': 0x209,
    'SERPERIOR': 0x20a,
    'TEPIG': 0x20b,
    'PIGNITE': 0x20c,
    'EMBOAR': 0x20d,
    'OSHAWOTT': 0x20e,
    'DEWOTT': 0x20f,
    'SAMUROTT': 0x210,
    'PATRAT': 0x211,
    'WATCHOG': 0x212,
    'LILLIPUP': 0x213,
    'HERDIER': 0x214,
    'STOUTLAND': 0x215,
    'PURRLOIN': 0x216,
    'LIEPARD': 0x217,
    'PANSAGE': 0x218,
    'SIMISAGE': 0x219,
    'PANSEAR': 0x21a,
    'SIMISEAR': 0x21b,
    'PANPOUR': 0x21c,
    'SIMIPOUR': 0x21d,
    'MUNNA': 0x21e,
    'MUSHARNA': 0x21f,
    'PIDOVE': 0x220,
    'TRANQUILL': 0x221,
    'UNFEZANT': 0x222,
    'BLITZLE': 0x223,
    'ZEBSTRIKA': 0x224,
    'ROGGENROLA': 0x225,
    'BOLDORE': 0x226,
    'GIGALITH': 0x227,
    'WOOBAT': 0x228,
    'SWOOBAT': 0x229,
    'DRILBUR': 0x22a,
    'EXCADRILL': 0x22b,
    'AUDINO': 0x22c,
    'TIMBURR': 0x22d,
    'GURDURR': 0x22e,
    'CONKELDURR': 0x22f,
    'TYMPOLE': 0x230,
    'PALPITOAD': 0x231,
    'SEISMITOAD': 0x232,
    'THROH': 0x233,
    'SAWK': 0x234,
    'SEWADDLE': 0x235,
    'SWADLOON': 0x236,
    'LEAVANNY': 0x237,
    'VENIPEDE': 0x238,
    'WHIRLIPEDE': 0x239,
    'SCOLIPEDE': 0x23a,
    'COTTONEE': 0x23b,
    'WHIMSICOTT': 0x23c,
    'PETILIL': 0x23d,
    'LILLIGANT': 0x23e,
    'BASCULIN': 0x23f,
    'SANDILE': 0x240,
    'KROKOROK': 0x241,
    'KROOKODILE': 0x242,
    'DARUMAKA': 0x243,
    'DARMANITAN': 0x244,
    'MARACTUS': 0x245,
    'DWEBBLE': 0x246,
    'CRUSTLE': 0x247,
    'SCRAGGY': 0x248,
    'SCRAFTY': 0x249,
    'SIGILYPH': 0x24a,
    'YAMASK': 0x24b,
    'COFAGRIGUS': 0x24c,
    'TIRTOUGA': 0x24d,
    'CARRACOSTA': 0x24e,
    'ARCHEN': 0x24f,
    'ARCHEOPS': 0x250,
    'TRUBBISH': 0x251,
    'GARBODOR': 0x252,
    'ZORUA': 0x253,
    'ZOROARK': 0x254,
    'MINCCINO': 0x255,
    'CINCCINO': 0x256,
    'GOTHITA': 0x257,
    'GOTHORITA': 0x258,
    'GOTHITELLE': 0x259,
    'SOLOSIS': 0x25a,
    'DUOSION': 0x25b,
    'REUNICLUS': 0x25c,
    'DUCKLETT': 0x25d,
    'SWANNA': 0x25e,
    'VANILLITE': 0x25f,
    'VANILLISH': 0x260,
    'VANILLUXE': 0x261,
    'DEERLING': 0x262,
    'SAWSBUCK': 0x263,
    'EMOLGA': 0x264,
    'KARRABLAST': 0x265,
    'ESCAVALIER': 0x266,
    'FOONGUS': 0x267,
    'AMOONGUSS': 0x268,
    'FRILLISH': 0x269,
    'JELLICENT': 0x26a,
    'ALOMOMOLA': 0x26b,
    'JOLTIK': 0x26c,
    'GALVANTULA': 0x26d,
    'FERROSEED': 0x26e,
    'FERROTHORN': 0x26f,
    'KLINK': 0x270,
    'KLANG': 0x271,
    'KLINKLANG': 0x272,
    'TYNAMO': 0x273,
    'EELEKTRIK': 0x274,
    'EELEKTROSS': 0x275,
    'ELGYEM': 0x276,
    'BEHEEYEM': 0x277,
    'LITWICK': 0x278,
    'LAMPENT': 0x279,
    'CHANDELURE': 0x27a,
    'AXEW': 0x27b,
    'FRAXURE': 0x27c,
    'HAXORUS': 0x27d,
    'CUBCHOO': 0x27e,
    'BEARTIC': 0x27f,
    'CRYOGONAL': 0x280,
    'SHELMET': 0x281,
    'ACCELGOR': 0x282,
    'STUNFISK': 0x283,
    'MIENFOO': 0x284,
    'MIENSHAO': 0x285,
    'DRUDDIGON': 0x286,
    'GOLETT': 0x287,
    'GOLURK': 0x288,
    'PAWNIARD': 0x289,
    'BISHARP': 0x28a,
    'BOUFFALANT': 0x28b,
    'RUFFLET': 0x28c,
    'BRAVIARY': 0x28d,
    'VULLABY': 0x28e,
    'MANDIBUZZ': 0x28f,
    'HEATMOR': 0x290,
    'DURANT': 0x291,
    'DEINO': 0x292,
    'ZWEILOUS': 0x293,
    'HYDREIGON': 0x294,
    'LARVESTA': 0x295,
    'VOLCARONA': 0x296,
    'COBALION': 0x297,
    'TERRAKION': 0x298,
    'VIRIZION': 0x299,
    'TORNADUS': 0x29a,
    'THUNDURUS': 0x29b,
    'RESHIRAM': 0x29c,
    'ZEKROM': 0x29d,
    'LANDORUS': 0x29e,
    'KYUREM': 0x29f,
    'KELDEO': 0x2a0,
    'MELOETTA': 0x2a1,
    'GENESECT': 0x2a2,
    'CHESPIN': 0x2a3,
    'QUILLADIN': 0x2a4,
    'CHESNAUGHT': 0x2a5,
    'FENNEKIN': 0x2a6,
    'BRAIXEN': 0x2a7,
    'DELPHOX': 0x2a8,
    'FROAKIE': 0x2a9,
    'FROGADIER': 0x2aa,
    'GRENINJA': 0x2ab,
    'BUNNELBY': 0x2ac,
    'DIGGERSBY': 0x2ad,
    'FLETCHLING': 0x2ae,
    'FLETCHINDER': 0x2af,
    'TALONFLAME': 0x2b0,
    'SCATTERBUG': 0x2b1,
    'SPEWPA': 0x2b2,
    'VIVILLON': 0x2b3,
    'LITLEO': 0x2b4,
    'PYROAR': 0x2b5,
    'FLABEBE': 0x2b6,
    'FLOETTE': 0x2b7,
    'FLORGES': 0x2b8,
    'SKIDDO': 0x2b9,
    'GOGOAT': 0x2ba,
    'PANCHAM': 0x2bb,
    'PANGORO': 0x2bc,
    'FURFROU': 0x2bd,
    'ESPURR': 0x2be,
    'MEOWSTIC': 0x2bf,
    'HONEDGE': 0x2c0,
    'DOUBLADE': 0x2c1,
    'AEGISLASH': 0x2c2,
    'SPRITZEE': 0x2c3,
    'AROMATISSE': 0x2c4,
    'SWIRLIX': 0x2c5,
    'SLURPUFF': 0x2c6,
    'INKAY': 0x2c7,
    'MALAMAR': 0x2c8,
    'BINACLE': 0x2c9,
    'BARBARACLE': 0x2ca,
    'SKRELP': 0x2cb,
    'DRAGALGE': 0x2cc,
    'CLAUNCHER': 0x2cd,
    'CLAWITZER': 0x2ce,
    'HELIOPTILE': 0x2cf,
    'HELIOLISK': 0x2d0,
    'TYRUNT': 0x2d1,
    'TYRANTRUM': 0x2d2,
    'AMAURA': 0x2d3,
    'AURORUS': 0x2d4,
    'SYLVEON': 0x2d5,
    'HAWLUCHA': 0x2d6,
    'DEDENNE': 0x2d7,
    'CARBINK': 0x2d8,
    'GOOMY': 0x2d9,
    'SLIGGOO': 0x2da,
    'GOODRA': 0x2db,
    'KLEFKI': 0x2dc,
    'PHANTUMP': 0x2dd,
    'TREVENANT': 0x2de,
    'PUMPKABOO': 0x2df,
    'GOURGEIST': 0x2e0,
    'BERGMITE': 0x2e1,
    'AVALUGG': 0x2e2,
    'NOIBAT': 0x2e3,
    'NOIVERN': 0x2e4,
    'XERNEAS': 0x2e5,
    'YVELTAL': 0x2e6,
    'ZYGARDE': 0x2e7,
    'DIANCIE': 0x2e8,
    'HOOPA': 0x2e9,
    'VOLCANION': 0x2ea
}
