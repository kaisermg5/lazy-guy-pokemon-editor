Lazy Guy's Pokémon Editor (LGPE) is an automatic pokémon editor for gameboy advance pokémon games. It works parsing data from Pokémon Essentials (a RPG Maker XP pokémon engine) text files.

This is a command line tool and it requires Python 3 to work. 
You can check its options by typing: 

  $ python3 lgpe.py -h
  
or just:

  $ python3 lgpe.py

The ussage of this tools is pretty straight forward, you just need to specify the options you want. Although, since typing the offsets of each table of your rom wouldn't be practical, you need to modify the configuration file "roms.ini" allocated in the directory data. There are some offset for BPEE and BPRE already (thanks to Gamer2020 since I took them from his tool PGE).

The files in the repository are ready to insert the data of pokemon up to generation six. But this is an automatic tool, that will only write data to you rom. It won't check what it is overwriting. So, for example, make sure you have expanded pokémon if you are going to insert up to generation six.

All files in the directory "data" need the corresponding index to the differents moves/pokémon/items/evolution/... of your rom. By default they have the ones corresponding to Pokémon Emerald Battle Engine Upgrade, a pokémon emerald project currently being made by users of pokecommunity (be sure to check it out! https://github.com/KDSKardabox/Pokemon-Emerald-Battle-Engine-Upgrade), but you can modify it to match your rom.

You can use this tool with no fear at all, just remember to always make a backup!
