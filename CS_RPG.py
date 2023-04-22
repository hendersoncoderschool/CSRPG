#podcast spottify/youtube ice ninja
#podcast name = The gamers chatverse
#print('https://replit.com/@OverdriveReplit/Fallen-Clicker?v=1')
from time import sleep
from os import system
from random import randint, choice


def textanimation(string):
    for i in range(len(string) + 1):
        system('cls')
        print(string[0:i])
        sleep(0.05)
    sleep(1)


def textanimation2(string):
    for i in range(len(string) + 1):
        system('cls')
        print(string[0:i])
        sleep(0.01)
    sleep(1)

current_room = ""
current_town = "wellspring"
cheat_system = 0

Skystead = {
  'enemy' : {
  '1': {
    #enemy
    'name': 'Storm soldier',
    'health': 50,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'cloud punch',
        'damage': 5,
        'max_damage': 5,
        'min_damge': 1,
        },
      '2': {
        #high damage
        'name': 'water hose',
        'damage': 50,
        'max_damage': 50,
        'min_damge': 10,
        },
      '3': {
        #summons rain
        'name': 'rain cloud',
        'damage': 35,
        'max_damage': 35,
        'min_damge': 10,
        },
      '4': {
        #summons a lightning storm cloud
        'name': 'storm cloud',
        'damage': 50,
        'max_damage': 50,
        'min_damge': 15,
        },
    },
 },
  '2': {
    #enemy
    'name': 'living cloud',
    'health': 75,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'advance cloud punch',
        'damage': 15,
        'max_damage': 15,
        'min_damge': 5,
        },
      '2': {
        #normal sword slash
        'name': 'frozen tears',
        'damage': 15,
        'max_damage': 15,
        'min_damge': 5,
        },
      '3': {
        #summons lightning bolt
        'name': 'ice rain',
        'damage': 25,
        'max_damage': 25,
        'min_damge': 10,
        },
      '4': {
        #a lightning sword slash
        'name': 'cloud punch',
        'damage': 5,
        'max_damage': 5,
        'min_damge': 1,
        },
    },
 },
  '3': {
    #powerfull enemy
    'name': 'Goose',
    'health': 50,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'bite',
        'damage': 25,
        'max_damage': 25,
        'min_damge': 5,
        },
      '2': {
        #normal sword slash
        'name': 'goose charge',
        'damage': 50,
        'max_damage': 25,
        'min_damge': 5,
        },
      '3': {
        #chance to block
        'name': 'goose block',
        'damage': 0,
        'max_damage': 0,
        'min_damge': 0,
        },
      '4': {
        #a lightning sword slash
        'name': 'super bite',
        'damage': 35,
        'max_damage': 35,
        'min_damge': 15,
        },
    },
 },
},
  'mini boss' : {
  '1': {
    #mini boss1 with key
    'name': 'Storm warrior',
    'health': 75,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'punch',
        'damage': 5,
        'max_damage': 5,
        'min_damge': 1,
        },
      '2': {
        #normal sword slash
        'name': 'sword slash',
        'damage': 25,
        'max_damage': 25,
        'min_damge': 5,
        },
      '3': {
        #summons lightning bolt
        'name': 'lightning bolt',
        'damage': 75,
        'max_damage': 75,
        'min_damge': 45,
        },
      '4': {
        #a lightning sword slash
        'name': 'lightning slash',
        'damage': 50,
        'max_damage': 50,
        'min_damge': 30,
        },
    },
 },
  '2': {
    #mini boss2
    'name': 'Storm warrior',
    'health': 75,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'punch',
        'damage': 5,
        'max_damage': 5,
        'min_damge': 1,
        },
      '2': {
        #normal sword slash
        'name': 'sword slash',
        'damage': 25,
        'max_damage': 25,
        'min_damge': 5,
        },
      '3': {
        #summons lightning bolt
        'name': 'lightning bolt',
        'damage': 75,
        'max_damage': 75,
        'min_damge': 45,
        },
      '4': {
        #a lightning sword slash
        'name': 'lightning slash',
        'damage': 50,
        'max_damage': 50,
        'min_damge': 30,
        },
    },
 },
},
  'boss' : {
'1': {
    #boss
    'name': 'Ra the demi god of storms',
    'health': 250,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'punch',
        'damage': 5,
        'max_damage': 5,
        'min_damge': 1,
        },
      '2': {
        #summons different rain clouds like acid and lava rain
        'name': 'master of rain',
        'damage': 100,
        'max_damage': 100,
        'min_damage': 35,
        },
      '3': {
        #
        'name': 'tornado',
        'damage': 50,
        'max_damage': 50,
        'min_damage': 25,
       },
      '4': {
        #chance to block attacks
        'name': 'wall of water',
        'damage': 0,
        'max_damage': 0,
        'min_damage':0,
        },
      '5': {
        #summons icicles
        'name': 'ice storm',
        'damage': 25,
        'max_damage': 25,
        'min_damage': 5,
        },
      

      }
    },
},
  'secret boss' : {
  '1': {
    #secret boss
    'name': 'The sun',
    'health': 10000,
    'movelist': {
      '1': {
        #
        'name': 'sun rays',
        'damage': 250,
        'max_damage': 250,
        'min_damge': 100,
        },
      '2': {
        #
        'name': 'solar flare',
        'damage': 850,
        'max_damage': 850,
        'min_damge': 500,
        },
      '3': {
        #
        'name': 'solar storm',
        'damage': 1000,
        'max_damage': 1000,
        'min_damge': 750,
        },
      '4': {
        #ultimate move can only be blocked by ultimate sunscrean
        'name': 'super nova',
        'damage': 9999,
        'max_damage': 9999,
        'min_damge': 9998,
        },
    },
 },
},

    'spawn room': {
        'North': 'Hall1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
        
    },
    'Hall1': {
        'South': 'spawn room',
        'East': 'enemy room1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'enemy room1': {
        'West': 'Hall1',
        'East': 'mini boss1/key',
        'South': 'Hall2',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'mini boss1/key': {
        'West': 'enemy room1',
        'enemy': False,
        'mini boss': True,
        'boss': False,
        'secret boss': False,
    },
    'Hall2': {
        'north': 'enemy room1',
        'South': 'key_d1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'key_d1': {
        'north': 'Hall2',
        'South': 'Hall3',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'Hall3': {
        'north': 'key_d1',
        'south': 'key_d2',
        'west': 'hallw1',
        'east': 'halle1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hallw1': {
        'west': 'hallw2',
        'east': 'Hall3',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hallw2': {
        'east': 'Hallw1',
        'South': 'mini boss2',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'mini boss2': {
        'north': 'Hall22',
        'South': 'loot room1',
        'enemy': False,
        'mini boss': True,
        'boss': False,
        'secret boss': False,
    },
    'loot room1': {
        'north': 'mini boss2',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'halle1': {
        'west': 'Hall3',
        'east': 'halle2',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'halle2': {
        'west': 'Halle1',
        'east': 'halle3',
        'north': 'enemy2',
        'south': 'enemy3',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'enemy2': {
        'south': 'halle2',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'enemy3': {
        'north': 'halle3',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'halle3': {
        'north': 'enemy4/key',
        'south': 'enemy5',
        'west': 'halle2',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'enemy4': {
        'south': 'halle3',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'enemy5': {
        'north': 'halle3',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'key_d2': {
        'north': 'Hall3',
        'south': 'boss_room',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'boss_room': {
      'north': 'key_d2',
      'south': 'loot_room',
      'enemy': False,
      'mini boss': False,
      'boss': True,
      'secret boss': False,
    },
    'loot_room': {
        'north': 'key_d2',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
}

Knifes_Edge = {
    'spawn room': {
        'south': 'Hall1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'Hall1': {
        'north': 'spawn room',
        'West': 'hallw1',
        'East': 'halle1_enemy',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hallw1': {
        'east': 'Hall1',
        'west': 'mini_b_w1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'mini_b_w1': {
        'South': 'mini_b_w2',
        'North': 'loot_roomw1',
        'enemy': False,
        'mini boss': True,
        'boss': False,
        'secret boss': False,
    },
    'loot_roomw1': {
        'south': 'mini_b_w1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'mini_b_w2': {
        'South': 'loot_roomw2',
        'North': 'mini_b_w1',
        'enemy': False,
        'mini boss': True,
        'boss': False,
        'secret boss': False,
    },
    'loot_roomw2': {
        'north': 'mini_b_w2',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'halle1_enemy': {
        'west': 'hall1',
        'east': 'halle2_enemy',
        'south': 'halls1',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'halle2_enemy': {
        'west': 'halle1_enemy',
        'south': 'mini_be1',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'mini_be1': {
        'north': 'halle2_enemy',
        'east': 'loot_roome1',
        'enemy': False,
        'mini boss': True,
        'boss': False,
        'secret boss': False,
    },
    'loot_roome1': {
        'west': 'mini_be1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'halls1': {
        'north': 'halle1',
        'south': 'halls2',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'halls2': {
        'north': 'halls1',
        'south': 'halls3_enemy',
        'west': 'enemy_buttongrey',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'enemy_buttongrey': {
        'east': 'halls2',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'halls3_enemy': {
        'east': 'blocked_grey/powerfull_enemy',
        'north': 'halls2',
        'south': 'halls4_enemy',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'blocked_grey/powerfull_enemy': {
        'west': 'halls3_enemy',
        'north': 'mini_loot_buttonorange',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'halls4_enemy': {
        'west': 'boss/blockedorange',
        'north': 'halls3_enemy',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'boss/blockorange': {
        'west': 'main_loot_room',
        'east': 'halls4_enemy',
        'enemy': False,
        'mini boss': False,
        'boss': True,
        'secret boss': False,
    },
    'main_loot_room': {
        'east': 'boss/blockorange',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'mini_loot_buttonorange': {
        'south': 'block_grey/powerufull_enemy',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    }
}

Iron_Forge = {
    'spawn room': {
        'south': 'hall1_enemy',
        'west': 'hallw1_enemy',
        'east': 'halle1_enemy',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hallw1_enemy': {
        'east': 'spawn room',
        'west': 'hallw2_enemy',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hallw2_enemy': {
        'south': 'hallws1',
        'east': 'hallw1_enemy',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hallws1': {
        'south': 'hallws2_mini_b',
        'north': 'hallw2_enemy',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hallws2_mini_b': {
        'south': 'hallws3_mini_loot',
        'east': 'hallws4_powerfull_enemy',
        'enemy': False,
        'mini boss': True,
        'boss': False,
        'secret boss': False,
    },
    'hallws3_mini_loot': {
        'north': 'hallws2_mini_b',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hallws4_powerfull_enemy': {
        'north': 'hallws5_mini_loot',
        'west': 'hallws2_mini_b',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hallws5_mini_loot': {
        'south': 'hallws4_powerfull_enemy',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'halle1_enemy': {
        'west': 'spawn room',
        'east': 'mini_boss_e1',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'mini_boss_e1': {
        'south': 'mini_loot_es1',
        'north': 'mini_loot_en1',
        'enemy': False,
        'mini boss': True,
        'boss': False,
        'secret boss': False,
    },
    'mini_loot_es1': {
        'north': 'mini_boss_e1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'mini_loot_en1': {
        'south': 'mimi_boss_e1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hall1_enemy': {
        'north': 'spawn room',
        'south': 'hall2',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hall2': {
        'north': 'hall1_enemy',
        'south': 'hall3_green_lock',
        'west': 'powerfull_enemy1',
        'east': 'hallse1_enemy',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'powerfull_enemy1': {
        'north': 'mini_loots1',
        'east': 'hall2',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'mini_loots1': {
        'south': 'powerfull_enemy1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hallse1_enemy': {
        'west': 'hall2',
        'east': 'hallse2_enemy',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hallse2_enemy': {
        'west': 'hallse1_enemy',
        'east': 'hallse3',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hallse3': {
        'west': 'hallse2_enemy',
        'south': 'mini_boss_hallss1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'mini_boss_hallss1': {
        'west': 'lootss1',
        'east': 'loot_and_green_key',
        'enemy': False,
        'mini boss': True,
        'boss': False,
        'secret boss': False,
    },
    'lootss1': {
        'east': 'mini_boss_hallss1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'loot_and_green_key': {
        'west': 'mini_boss_hallss1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hall3_green_lock': {
        'north': 'hall2',
        'south': 'hall4',
        'west': 'hallee1_powerfull_enemy',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hallee1_powerfull_enemy': {
        'east': 'hall3_green_lock',
        'west': 'mini_loot_purple_key_hallee1',
        'enemy': True,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'mini_loot_purple_key_hallee1': {
        'west': 'hallee1_powerfull_enemy',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hall4': {
        'east': 'boss_eee1',
        'west': 'purple_lock_hall',
        'north': 'hall3_green_lock',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'boss_eee1': {
        'east': 'hall_eee2',
        'west': 'hall4',
        'enemy': False,
        'mini boss': False,
        'boss': True,
        'secret boss': False,
    },
    'boss_eee2': {
        'south': 'boss_eee3',
        'west': 'boss_eee1',
        'enemy': False,
        'mini boss': False,
        'boss': True,
        'secret boss': False,
    },
    'boss_eee3': {
        'west': 'big_loot',
        'north': 'boss_eee3',
        'enemy': False,
        'mini boss': False,
        'boss': True,
        'secret boss': False,
    },
    'big_loot': {
        'east': 'boss_eee3',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'purple_lock_hall': {
        'east': 'hall4',
        'west': 'main_boss',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'main_boss': {
        'east': 'purple_lock_hall',
        'west': 'main_loot',
        'enemy': False,
        'mini boss': False,
        'boss': True,
        'secret boss': False,
    },
    'main_loot': {
        'east': 'main_boss',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    }
}

Death_fall = {
    'spawn room': {
        'north': 'shop',
        'south': 'hall1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'hall1': {
        'north': 'spawn room',
        'south': 'hall2',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    }, 
    'hall2': {
        'north': 'hall1',
        'south': 'hall3',
        'west': 'graveyardnorthw1',
        'east': 'graveyardnorthe1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,

    'hall3': {
        'west': 'graveyardww1',
        'east': 'graveyardee1',
        'north': 'hall2',
        'south': 'hall4',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },

    'graveyardnorthw1': {
        'west': 'graveyardnorthw2',
        'east': 'hall2',
        'south': 'graveyardww1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardnorthw2': {
        'west': 'graveyardnorthw3',
        'east': 'graveyardnorthw1',
        'south': 'graveyardww2',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardnorthw3': {
        'west': 'graveyardnorthw4',
        'east': 'graveyardnorthw2',
        'south': 'graveyardww3',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardnorthw4': {
        'north': 'graveyardnnw1',
        'west': 'graveyardnorthw5',
        'east': 'graveyardnorthw3',
        'south': 'graveyardww4',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardnorthw5': {
        'north': 'graveyardnnw2',
        'west': 'graveyardnorthw6',
        'east': 'graveyardnorthw4',
        'south': 'graveyardww5',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardnorthw6': {
        'north': 'graveyardnnw3',
        'east': 'graveyardnorthw5',
        'south': 'graveyardww6',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },

    },
    'graveyardnorthe1': { 
        'west': 'hall2',
        'east': 'graveyardnorthe2',
        'south': 'graveyardee1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardnorthe2': {
        'south': 'graveyardee2',
        'west': 'graveyardnorthe1',
        'east': 'graveyardnorthe3',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardnorthe3': {
        'south': 'graveyardee3',
        'west': 'graveyardnorthe2',
        'east': 'graveyardnorthe4',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardnorthe4': {
        'south': 'graveyardee4',
        'west': 'graveyardnorthe3',
        'east': 'graveyardnorthe5',
        'north': 'graveyardnne1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardnorthe5': {
        'south': 'graveyardee5',
        'west': 'graveyardnorthe4',
        'east': 'graveyardnorthe6',
        'north': 'graveyardnne2_key',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardnorthe6': {
        'south': 'graveyardee6',
        'west': 'graveyardnorthe5',
        'north': 'graveyardnne3',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardee1': {
        'south': 'graveyardse1',
        'west': 'hall3',
        'east': 'graveyardee2',
        'north': 'graveyardnorthe1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardee2': {
        'south': 'graveyardse2',
        'west': 'graveyardee1',
        'east': 'graveyardee3',
        'north': 'graveyardnorthe2',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardee3': {
        'south': 'graveyardse3',
        'west': 'graveyardee2',
        'east': 'graveyardee4',
        'north': 'graveyardnorthe3',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardee4 ': {
        'south': 'graveyardse4',
        'west': 'graveyardee3',
        'east': 'graveyardee5',
        'north': 'graveyardnorthe4',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardee5': {
        'west': 'graveyardee4',
        'east': 'graveyardee6',
        'north': 'graveyardnorthe5',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
#udshfiu
#hghghg
    'graveyardee6': {
        'west': 'graveyardee5',
        'north': 'graveyardnorthe6',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardse1': {
        'west': 'hall4',
        'east': 'graveyards2',
        'north': 'graveyardee1',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardse2': {
        'west': 'graveyardse1',
        'east': 'graveyardse3',
        'north': 'graveyardee2',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardse3': {
        'west': 'graveyardse2',
        'east': 'graveyardse4',
        'north': 'graveyardee3',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardse4': {
        'west': 'graveyardse3',
        'north': 'graveyardee4',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardnne1': {
        'east': 'graveyardnne2',
        'south': 'graveyardnorthe4',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardnne2_key': {
        'west': 'graveyardnne1',
        'east': 'graveyardnne3',
        'south': 'graveyardnorthe5',
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
    'graveyardnne3': {
        'west': 'graveyardnne2',
        'south': 'graveyardnorthe6',  
        'enemy': False,
        'mini boss': False,
        'boss': False,
        'secret boss': False,
    },
}

#time in death falls goes up by one everytime you go into a room after 12:00 lunch enemys get stronger each hour until midnight where they are at peak power and midnight lasts for a few room until after midnight they get weaker until 12:00 lunch where they are normal and 12:00 lunch lasts for a few rooms reward for surviving midnight.
knifes_edge_enemys = {
  '1': {
    #enemy
    'name': 'mugger',
    'health': 100,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'stab',
        'damage': 15,
        'max_damage': 15,
        'min_damge': 5,
        },
      '2': {
        #basic attack
        'name': 'kick',
        'damage': 10,
        'max_damage': 10,
        'min_damge': 5,
        },
      '3': {
        #basic attack
        'name': 'punch',
        'damage': 10,
        'max_damage': 10,
        'min_damge': 5,
        },
      '4': {
        #
        'name': 'super stab',
        'damage': 30,
        'max_damage': 30,
        'min_damge': 15,
        },
    },
 },
  '2': {
    #enemy
    'name': 'Thief',
    'health': 105,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'punch',
        'damage': 15,
        'max_damage': 15,
        'min_damge': 5,
        },
      '2': {
        #
        'name': 'crowbar bash',
        'damage': 30,
        'max_damage': 30,
        'min_damge': 10,
        },
    },
 },
  '3': {
    #mini boss
    'name': 'mafia boss',
    'health': 110,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'punch',
        'damage': 15,
        'max_damage': 15,
        'min_damge': 5,
        },
      '2': {
        #
        'name': 'gun',
        'damage': 50,
        'max_damage': 50,
        'min_damge': 0,
        },
      '3': {
        #chance to block
        'name': 'bullet proof vest',
        'damage': 0,
        'max_damage': 0,
        'min_damge': 0,
        },
    },
 },
  '4': {
    #enemy
    'name': 'dwarf',
    'health': 50,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'pickaxe',
        'damage': 25,
        'max_damage': 25,
        'min_damge': 10,
        },
      '2': {
        #normal sword slash
        'name': 'boulder throw',
        'damage': 50,
        'max_damage': 50,
        'min_damge': 30,
        },
      '3': {
        #summons lightning bolt
        'name': 'rock wall',
        'damage': 0,
        'max_damage': 0,
        'min_damge': 0,
        },
      '4': {
        #a lightning sword slash
        'name': 'super pickaxe',
        'damage': 55,
        'max_damage': 55,
        'min_damge': 24,
        },
    },
 },
  '5': {
    #mini boss1 with key
    'name': 'Earth bender',
    'health': 100,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'rock throw',
        'damage': 10,
        'max_damage': 10,
        'min_damge': 2,
        },
      '2': {
        #normal sword slash
        'name': 'lava bending',
        'damage': 32,
        'max_damage': 32,
        'min_damge': 7,
        },
      '3': {
        #summons lightning bolt
        'name': 'rock fist',
        'damage': 50,
        'max_damage': 50,
        'min_damge': 22,
        },
    },
 },
  '6': {
    #mini boss
    'name': 'dwarf king',
    'health': 145,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'ultimate pickaxe',
        'damage': 45,
        'max_damage': 45,
        'min_damge': 20,
        },
      '2': {
        #
        'name': 'Gem sword',
        'damage': 75,
        'max_damage': 75,
        'min_damge': 45,
        },
      '3': {
        #
        'name': 'gold pickaxe',
        'damage': 58,
        'max_damage': 58,
        'min_damge': 42,
        },
      '4': {
        #
        'name': 'dwarf cannon',
        'damage': 70,
        'max_damage': 70,
        'min_damge': 45,
        },
    },
 },
  '7': {
    #mini boss1 with key
    'name': 'fire bender',
    'health': 100,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'fire blast',
        'damage': 25,
        'max_damage': 25,
        'min_damge': 5,
        },
      '2': {
        #normal sword slash
        'name': 'flamethrower',
        'damage': 50,
        'max_damage': 50,
        'min_damge': 37,
        },
      '3': {
        #summons lightning bolt
        'name': 'lightning bolt',
        'damage': 75,
        'max_damage': 75,
        'min_damge': 45,
        },
      '4': {
        #a lightning sword slash
        'name': 'wave of fire',
        'damage': 102,
        'max_damage': 102,
        'min_damge': 50,
        },
    },
 },
  '8': {
    #boss
    'name': ' jaha the demi god of thiefs',
    'health': 250,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'toolnado',
        'damage': 75,
        'max_damage': 75,
        'min_damge': 25,
        },
      '2': {
        #
        'name': 'shadow knifes',
        'damage': 105,
        'max_damage': 105,
        'min_damge': 55,
        },
      '3': {
        #
        'name': 'shawdow thiefs',
        'damage': 50,
        'max_damage': 50,
        'min_damge': 15,
        },
      '4': {
        #a lightning sword slash
        'name': 'shadow army',
        'damage': 75,
        'max_damage': 75,
        'min_damge': 20,
        },
    },
 },
  '9': {
    #mini boss
    'name': 'The gold king',
    'health': 125,
    'movelist': {
      '1': {
        #all enemys have a basic attack
        'name': 'coin gun',
        'damage': 50,
        'max_damage': 50,
        'min_damge': 5,
        },
      '2': {
        #normal sword slash
        'name': 'coinnado',
        'damage': 75,
        'max_damage': 75,
        'min_damge': 20,
        },
      '3': {
        #summons lightning bolt
        'name': 'golden sword',
        'damage': 25,
        'max_damage': 25,
        'min_damge': 5,
        },
      '4': {
        #a lightning sword slash
        'name': 'gold fist',
        'damage': 15,
        'max_damage': 20,
        'min_damge': 5,
        },
    },
 },
}

#get from secret level black dragon boss
#god
#common from dragon boss from secret level
#can only be sold for 1 coin
#if you go to a level that you already beated it resets so you can farm

#1% chance to get
#GOD
sword_that_can_destroy_the_freaking_universe = {
    'name': 'stcdtfu version2.0',
    'damage': 999999,
    'special_ability': 'blank',
    'effect': 'blank',
    'ability_effect': 'blank'
}
player_health = 100
enemy_health = 100
gold_give1 = randint(1, 5)
gold = 0

#  'max_damage':1,
#  'min_damge': 1,
#Well_Spring
#super_rare
fist24315 = {
    'name':'fist',
    'damage': randint(1,5),
    'max_damage': 5,
    'min_damge': 1,
    'special_ability': 'blank',
    'effect': 'blank',
    'ability_effect': 'blank'
}
#common
sword = {
    'name':'wooden sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'blank',
    'effect': 'blank',
    'ability_effect': 'blank'
}
#common
staff = {
    'name':'wooden staff',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'Wall_of_water',
    'effect': 'blank',
    'ability_effect': 'weapon_block'
}
#common
bow1 = {
    'name':'wooden bow',
    'damage': randint(7, 12),
    'max_damage': 12,
    'min_damge': 7,
    'special_ability': 'blank',
    'effect': 'blank',
    'ability_effect': 'blank'
}

#Sky_Stead
#find a way to sort out damage in the game
#common
cloud_sword = {
    'name':'cloud sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'blank',
    'effect': 'blank',
    'ability_effect': 'blank'
}
#uncommon
rain_sword = {
    'name':'rain sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'lightning_bolt',
    'effect': 'blurred_vision',
    'ability_effect': 'electricute'
}
#rare
storm_sword = {
    'name':'storm sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'f1_tornado',
    'effect': 'burred_vision',
    'slippery'
    'ability_effect': 'whirlpool_of_air'
}
#damage not sorted out yet
#rare
storm_bow = {
    'name':'storm bow',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'Lightning_arrows',
    'effect': 'burred_vision',
    'slippery'
    'ability_effect': 'electricute',
}
#rare
storm_staff1 = {
    'name':'storm staff',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'master_of_storms',
    'effect': 'elements_of_a_storm',
    'ability_effect': '???'  #find out
}

#Knifes_Edge
#common
dagger = {
    'name':'dagger',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'blank',
    'effect': 'bleeding',
    'ability_effect': 'blank'
}
#uncommon
posin_dagger = {
    'name':'posin dagger',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'blank',
    'effect': 'bleeding'
    'posin',
    'ability_effect': 'blank'
}
#uncommon
posin_sword = {
    'name':'posin sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'blank',
    'effect': 'posin',
    'ability_effect': 'blank'
}
#rare
posin_staff2 = {
    'name':'posin staff',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'toxic_cloud',
    'effect': 'posin'
    'toxic_wood',  #toxic_wood damages player
    'ability_effect': 'posin'
}
#common
sword2 = {
    'name':'sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'blank',
    'effect': 'blank',
    'ability_effect': 'blank'
}
#common
bow2 = {
    'name':'bow',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'rain_of_arrow',
    'effect': 'blank',
    'ability_effect': 'blank'
}
#uncommon
posin_bow = {
    'name':'posin bow',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'rain_of_posin_arrows',
    'effect': 'posin',
    'ability_effect': 'peircing',
}

#Iron_forge
#uncommon
iron_fist = {
    'name':'iron fist',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'Earthquake',
    'effect': 'crushing',  #does not hurt player
    'ability_effect': 'uneven ground',
}
#rare
mechanical_staff3 = {
    'name':'mechanical staff',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'Robot_servents',
    'effect': 'blank',
    'ability_effect': 'peircing',
}
#epic
gatling_gun = {
    'name':'gatling gun',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'bullet_storm',
    'effect': 'fast_bullet'
    'unwelding',  #unwelding makes it hard to aim
    'ability_effect': 'peircing',
}
#common
iron_sword3 = {
    'name':'iron sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'blank',
    'effect': 'crushing',
    'ability_effect': 'blank'
}
#rare
mechanical_sword3 = {
    'name':'mechanical sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'Tri_Iron_Sword',
    'ability_effect': 'bleeding',
    'effect': 'blank',
}
#common
iron_bow3 = {
    'name':'iron bow',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'blank',
    'effect': 'crushing',
    'ability_effect': 'blank'
}
#uncommon
mechanical_bow = {
    'name':'mechanical bow',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'Automatic_arrows',
    'effect': 'blank',
    'ability_effect': 'bleeding'
}
#epic
laser_bow = {
    'name':'laser bow',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'super_charged_arrows',
    'ability_effect': 'exploding',
    'effect': 'burning'
}
#legendary
laser_eye = {
    'name':'laser eye',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'laser_beam',
    'effect': 'burning',
    'ability_effect': 'disinagration'
}
#ultimate
molten_sword_secret = {
    'name':'molten sword',
    'max_damage': 10,
    'min_damge': 5,
    'damage': randint(5, 10),
    'special_ability': 'nucls_implode',
    'effect': 'radation'
    'melt',
    'ability_effect': 'Super_radation'
    'disinagration'
    'burning'
    'explode'
}
#death falls
#epic
void_sword4 = {
    'name':'void sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability':
    'The_Endless_Void',  #instant kills enemys requires shard_of_the_void
    'effect':
    'void',  #hitting enemys give a a piece enough hits gives you the shard_of_the_void
    'ability_effect': 'erasing'
}
#epic
cursed_tree_sword = {
    'name':'cursed wood sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'vines_of_the_dead',
    'effect': 'strangling',
    'life_steal'
    'ability_effect': 'portal_to_the_dead_world'
    'life_steal'
}
#rare
arrows_of_death_bow4 = {
    'name':'arrows of death bow',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'storm_of_death',
    'effect': 'Lingring_death',
    'ability_effect': 'death'
}
#uncommon
shadow_sword4 = {
    'name':'shadow sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'Crit_2',
    'effect': 'double_crit',  #chance to crit
    'ability_effect': 'Shadow_crit'
}
#uncommon
shadow_bow4 = {
    'name':'shadow bow',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'Crit_arrow_2',
    'effect': 'double_crit',  #chance to crit
    'ability_effect': 'Shadow_arrow_crit'
}
#rare
skelaton_sword4 = {
    'name':'bone sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'max_sharpnel',
    'effect': 'sharpnel',  #more damage and chance to double damage
    'ability_effect': 'triple_damage_sharpnel'  #it's what it says
}
#rare
skelaton_bow4 = {
    'name':'bone bow',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'spike_storm',  #storm of sharpnel
    'effect': 'sharpnel',  #more damage and chance to double damage
    'ability_effect':
    'sharpnel_double_damage'  #same thing as the skelaton sword
}
#uncommon
necromancer_staff4 = {
    'name':'necromancer staff',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'Summon_the_dead',  #summons zombies and skelatons
    'effect': 'blank',
    'ability_effect': 'blank'
}
#uncommon
shadow_staff4 = {
    'name':'shadow staff',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'Crit_2',
    'effect': 'double_crit',  #chance to crit
    'ability_effect': 'Shadow_crit'
}
#epic
void_staff4 = {
    'name':'void staff',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'The_Voids_army',
    'effect':
    'void',  #hitting enemys give a a piece enough hits gives you the shard_of_the_void
    'ability_effect': 'sacrifice'
    'looting'
    'destruction'
    #an army of the void gives you loot and death lose 50hp requires shard_of_the_void
}
#rare
skelaton_staff4 = {
    'name':'skelaton staff',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'skelaton_army',
    'effect': 'sharpnel',
    'ability_effect': 'sacrifice'
    'sharpnel'
    #an army of skelatons lose 50hp
}
#can only get from black dragon boss
#legendary
dragon_staff = {
    'name':'dragon staff',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'dragon_army',
    'effect': 'burning',
    'ability_effect': 'burning'
    'crushing'
    'destruction'
    #an army of dragons
}
#found in secret level
#common
enchanted_sword5 = {
    'name':'enchanted sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'enchanted_rain_of_swords',
    'effect': 'blank',
    'ability_effect': 'blank'
}
#found in secret level
#uncommon
blank = {
    'name':'blank',
    'damage': randint(0, 0),
    'max_damage': 0,
    'min_damge': 0,
    'special_ability': 'nothing',  #long cooldown
    'effect': 'empty',  #no damage
    'ability_effect': 'triple_death'
    #does 300 damage times 3
}
#godly
creative_sword_secret = {
    'name':'creative sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'delete',
    'effect': 'blank',
    'ability_effect': 'erasing'
}
#creative_only
admin_sword = {
    'name':'admin sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'blank',
    'effect': 'blank',
    'ability_effect': 'blank'
}
#secret level black boss before black dragon
#common
ultimate_sword_secret = {
    'name':'ultimate sword',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'heal',
    'effect': 'blank',
    'ability_effect': 'healing'
}
#in secret level after you defeat the boss
#rare
ice_blade = {
    'name':'ice blade',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'frost',
    'effect': 'freezing',
    'ability_effect': 'freezing'
    'frostbite'
}
#rare
phase_saber = {
    'name':'phase saber',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'blank',
    'effect': 'blank',
    'ability_effect': 'melt'
    'disinagration'
}
#rare
fight = {
    'name':'fight',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'blank',
    'effect': 'confusion',
    'ability_effect': 'blank'
}
#epic
rpg = {
    'name':'rpg',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'code',  #gives you a lot of coins
    'effect': 'blank',
    'ability_effect': 'hundred_thousand_coins'
}
#ultimate_legendary
game = {
    'name':'game',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'blank',
    'effect': 'insta_kill',
    'ability_effect': 'blank'
}
zero_divided_by_zero = {
    'name':'0 / 0',
    'damage': randint(5, 10),
    'max_damage': 10,
    'min_damge': 5,
    'special_ability': 'blackhole',
    'effect': 'blank',
    'ability_effect': 'insta_kill'
}

insta_kill = {
    'damage': 1000000000000000,
}
hundred_thousand_coins = {
    'damage': 0,
}

effect_inventory = {
    'insta_kill': insta_kill,
    'hundred_thousand_coins': hundred_thousand_coins,
}

weapon_inventory = {
    'sword_that_can_destory_the_freaking_universe':
    sword_that_can_destroy_the_freaking_universe,
    'fist24315': fist24315,
    'sword': sword,
    'staff': staff,
    'cloud_sword': cloud_sword,
    'rain_sword': rain_sword,
    'storm_sword': storm_sword,
    'storm_bow': storm_bow,
    'bow1': bow1,
    'storm_staff1': storm_staff1,
    'dagger': dagger,
    'posin_dagger': posin_dagger,
    'posin_sword': posin_sword,
    'posin_staff2': posin_staff2,
    'sword2': sword2,
    'bow2': bow2,
    'posin_bow': posin_bow,
    'iron_fist': iron_fist,
    'mechanical_staff3': mechanical_staff3,
    'gatling_gun': gatling_gun,
    'iron_sword3': iron_sword3,
    'mechanical_sword3': mechanical_sword3,
    'iron_bow3': iron_bow3,
    'mechanical_bow': mechanical_bow,
    'laser_bow': laser_bow,
    'laser_eye': laser_eye,
    'molten_sword_secret': molten_sword_secret,
    'void_sword4': void_sword4,
    'cursed_tree_sword4': cursed_tree_sword,
    'arrows_of_death_bow4': arrows_of_death_bow4,
    'shadow_sword4': shadow_bow4,
    'shadow_bow4': shadow_bow4,
    'skelaton_sword4': skelaton_sword4,
    'skelaton_bow4': skelaton_bow4,
    'necromancer_staff4': necromancer_staff4,
    'shadow_staff4': shadow_staff4,
    'void_staff4': void_staff4,
    'skelaton_staff4': skelaton_staff4,
    'dragon_staff': dragon_staff,
    'enchanted_sword5': enchanted_sword5,
    'blank': blank,
    'creative_sword_secret': creative_sword_secret,
    'admin_sword': admin_sword,
    'ultimate_sword_secret': ultimate_sword_secret,
    'ice_blade': ice_blade,
    'phase_saber': phase_saber,
    'fight': fight,
    'rpg': rpg,
    'game': game,
    'zero_divided_by_zero': zero_divided_by_zero,
}

inventory = ['nothing']

player_weapon = sword_that_can_destroy_the_freaking_universe
enemy_weapon = fist24315


#https://projects.raspberrypi.org/en/projects

#raspberry pi as server

print('one of the items may have numbers but that is an error')
sleep(1)
system('cls')
"""
while True:
  test = randint(1,4)
  test2 = randint(1,4)
  if test == 1:
    enemy_health += 1
  elif test == 2:
    enemy_health -= 1
  elif test == 3:
    player_health -= 1
  elif test == 4:
    player_health += 1
  print('action:',test)
  print('enemy_hp:',enemy_health)
  print('player_hp:',player_health)
  sleep(0.5)
  system('cls')"""
potion = 0
ultimate_potion = 0
while True:
    if player_health <= 0:
      print ('You have died.')
      sleep(1.5)
      break
    loot_chance = 50
    dodge_chance = 5
    heal_chance1 = randint(1,10)
    heal_chance2 = randint(1,10)
    healing1 = randint(5,25)
    enemy_action = randint(1,2)
    healing1 = randint(5,25)
    #test2 = randint(1,4)
    print('HP:', player_health)
    print('enemy HP:', enemy_health)
    print('gold:',gold)
    print('doge chance:',dodge_chance,'%')
    print('Weapon:'+player_weapon['name'])
    test = input("""
  (1)fight
  (2)heal
  (3)explore
  (4)inventory
  (5)shop
  (6)End proccess
  (7)Secret codes
               
  input:""")
    sleep(2)
    system('cls')

    if test == '1':
      if enemy_action == 2:
        if heal_chance2 <= 5:
          enemy_health += healing1
          print('enemy healed ',healing1, 'hp')
          sleep(2)
          system('cls')

      p_damage = player_weapon['damage']
      e_damage = enemy_weapon['damage']
      enemy_health -= player_weapon['damage']
      if enemy_action == 1:
        dodge = randint(1,100)
        if dodge >= dodge_chance:
          player_health -= enemy_weapon['damage']
          print('enemy delt', e_damage ,'damage!')
        else:
          print ('You dodged the attack.')
      enemy_weapon['damage'] = randint(enemy_weapon['min_damge'],
                                      enemy_weapon['max_damage'])
            
      gold += gold_give1
      sleep(2)
      print('you delt', p_damage, 'damage!')
      sleep(1)
      sleep(1)
      print('You earned', gold_give1, 'gold')
      gold_give1 = randint(1, 5)
      sleep(1)
      system('cls')
      if enemy_health <= 0:
          gold += 50
          enemy_health = 100

    if test == '2':
      if enemy_action == 1:
        player_health -= enemy_weapon['damage']
        e_damage = enemy_weapon['damage']
        player_weapon['damage'] = randint(player_weapon['min_damge'],
                                          player_weapon['max_damage'])
        print ('enemy delt ',e_damage,'damage')
        sleep(2)
        system('cls')
      if enemy_action == 2:
        if heal_chance2 <= 5:
            enemy_health += healing1
            print('enemy healed ',healing1, 'hp')
            sleep(2)
            system('cls')
      if heal_chance1 <= 5:
        player_health += healing1
        print('You healed ',healing1, 'hp')
        sleep(2)
        system('cls')


    #different towns have different maps
    #https://projects.raspberrypi.org/en/projects/rpg/0
    elif test == '3':
      while True:
        if player_health <= 0:
          break
        towns = input("""
Please choose a town!

(1)Skystead *
(2)Knife's Edge **
(3)Iron Forge ***
(4)Death Fall ****
(5)Black Dragon *****
(7)leave
            
Input:""")
        sleep(1)
        system('cls')
        current_room = "spawn room"

        if towns == '1':
          current_town = Skystead
          
        

        elif towns == '2':
          current_town = Knifes_Edge
          

        elif towns == '3':
          current_town = Iron_Forge

        elif towns == '4':
          current_town = Death_fall
          

        elif towns == '7':
            break

        elif towns == '24315':
            pass

        else:
            pass
        while True:
          while True:
            spawn = False
            if current_town[current_room]['enemy']:
               enemy_type = 'enemy'
               spawn = True
               target = current_town['enemy'][str(randint(1,len(current_town['enemy'])))]
               t_name = target['name']
               t_health = target['health']
               t_moves = target['movelist']
               p_damage = player_weapon['damage']
               print('You have been stopped by a '+t_name)
               sleep(2)
               print('Prepare to battle')
               sleep(2)
               system('cls')
            if current_town[current_room]['mini boss']:
               enemy_type = 'mini boss'
               spawn = True
               target = current_town['mini boss'][str(randint(1,len(current_town['mini boss'])))]
               t_name = target['name']
               t_health = target['health']
               t_moves = target['movelist']
               p_damage = player_weapon['damage']
               print('You have been stopped by a '+t_name)
               sleep(2)
               print('Prepare to battle')
               sleep(2)
               system('cls')
            if current_town[current_room]['boss']:
               enemy_type = 'boss'
               spawn = True
               target = current_town['boss'][str(randint(1,len(current_town['boss'])))]
               t_name = target['name']
               t_health = target['health']
               t_moves = target['movelist']
               p_damage = player_weapon['damage']
               print('You have been stopped by '+t_name)
               sleep(2)
               print('Prepare to battle')
               sleep(2)
               system('cls')
            if spawn == True:
              while True:
                print('Your weapon:')#+player_weapon['name']
                print('Hp:',player_health)
                print('Enemy hp:'+str(t_health))
                battle=input("""
  (1)fight
  (2)heal
  
  input:""")
                sleep(2)
                system('cls')
                if battle == '1':
                 t_health -= player_weapon['damage']
                 gold += gold_give1
                 #print('You use '+player_weapon['name'])
                 sleep(1.5)
                 print('You delt', p_damage, 'damage!')
                 sleep(1.5)
                 print('You earned', gold_give1, 'gold')
                 sleep(1.5)
                 system('cls')
                elif battle == '2':
                  print('You tried healing yourself.')
                  sleep(1.5)
                  if heal_chance1 <= 5:
                    player_health += healing1
                    print('You healed ',healing1, 'hp')
                    sleep(1.5)
                    system('cls')
                  else:
                    print('You failed to heal yourself.')
                    sleep(1.5)
                    system('cls')
  
                   
                    
                else:
                  pass
                     
                if t_health <= 0:
                  if enemy_type == 'enemy':
                    print('You defeated the enemy.')
                    loot = randint(1,100)
                    if loot <= loot_chance:
                      player_weapon = cloud_sword
                      sleep(2)
                      print('The enemy dropped something.')
                    else:
                      print ('The enemy dropped nothing.')
                  
                  elif enemy_type == 'mini boss':
                    print('You defeated the mini boss.')
                  else:
                    print('You defeated the boss.')
                  sleep(1.5)
                  system('cls')
                  break
                     
                move_c = str(randint(1,len(t_moves)))
                t_move = t_moves[move_c]
                t_move_name = t_move['name']
                t_damage = t_move['damage']
                print('Enemy used '+t_move_name)
                sleep(1.5)
                print('The enemy delt '+str(t_damage))
                sleep(2)
                system('cls')
                player_health -= t_damage
                if player_health <= 0:
                  break
                     
              if player_health <= 0:
                break
            options = list(current_town[current_room].keys())
            print('possible moves')
            for dir in options:
              if dir != 'enemy' and dir != 'mini boss' and dir != 'boss' and dir != 'secret boss':
               print (dir)
            print("""
player_heath:""",player_health)
            print("gold:",gold)
            print('room:',current_room)
            move=input("""
(1)inventory
(2)shop
(3)explore
  
input:""")
            sleep(1)
            system('cls')
            
            
            
            if move == '1':
              while True:
               print ('Healing potions:',potion)
               print ('Ultimate potions:',ultimate_potion)
               inventory2=input("""
               (1)use potion
               (2)use ultimate potion
               (3)
               (4)leave
               input:""")
               sleep(2)
               system('cls')
                
               if inventory2 == '1':
                 if potion <= 0:
                   print('you don\'t have any potions')
                 elif potion >= 1:
                  potion -= 1
                  player_health += 25
      
               elif inventory2 == '2':
                if ultimate_potion <= 0:
                   print('you don\'t have any ultimate potions')
                elif ultimate_potion >= 1:
                  ultimate_potion -= 1
                  player_health += 100
        
               elif inventory2 == '3':
                 pass
        
               elif inventory2 == '4':
                break
            elif move == '2':
              while True:
                print('gold:',gold)
                m_shop=input("""
              SHOP
(1)Health Potion(+25 HP)(20$)
(2)ULTIMATE POTION(+100 HP)(150$)
(3)
(4)
(5)exit
  
input:""")
                sleep(2)
                system('cls')
                if m_shop == '1':
                  if gold <= 19:
                    print('You can\'t afford this.')
                    sleep(2)
                    system('cls')
                  else:
                    print('You purchased health potion.')
                    sleep(2)
                    system('cls')
                    gold -= 20
                    potion += 1
                elif m_shop == '2':
                  if gold <= 149:
                    print('You can\'t afford this.')
                    sleep(2)
                    system('cls')
                  else:
                    print ('you purchased ultimate potion.')
                    sleep(2)
                    system('cls')
                    gold -= 150
                    ultimate_potion += 1
                elif m_shop == '3':
                  if gold <= 19:
                    print('You can\'t afford this.')
                    sleep(2)
                    system('cls')
                  else:
                    pass
                elif m_shop == '4':
                  if gold <= 19:
                    print('You can\'t afford this.')
                    sleep(2)
                    system('cls')
                  else:
                   pass
                elif m_shop == '5':
                  break
                else:
                  pass
          
            elif move == '3':
              if not current_room == "spawn room":
                print ('You can\'t explore when not in the spawn room.')
              else:
                current_town = "wellspring"
                break
            else:
              for i in options:
                if move.casefold() == i.casefold():
                 current_room = current_town[current_room][i]
                 print('You are are in',current_room)
                 sleep(2)
                 system('cls')
          break
          
          
    elif test == '4':
        while True:
         print ('Healing potions:',potion)
         print ('Ultimate potions:',ultimate_potion)
         inventory2=input("""
         (1)use potion
         (2)use ultimate potion
         (3)
         (4)leave
         input:""")
         sleep(2)
         system('cls')
          
         if inventory2 == '1':
           if potion <= 0:
             print('you don\'t have any potions')
           elif potion >= 1:
            potion -= 1
            player_health += 25

         elif inventory2 == '2':
          if ultimate_potion <= 0:
             print('you don\'t have any ultimate potions')
          elif ultimate_potion >= 1:
            ultimate_potion -= 1
            player_health += 100
  
         elif inventory2 == '3':
           pass
  
         elif inventory2 == '4':
          break
        
            

            
    elif test == '5':
     while True:
      code_ticket = randint(1,100)
      print('gold:',gold)
      shop=input("""
        SHOP
(1)Health Potion(+25 HP)(20$)
(2)ULTIMATE POTION(+100 HP)(150$)
(3)Code Ticket(5% chance to get a secret code)(10$)
(4)Sand Bag(+5% dodge chance)(250$)

(5)Attack Prediction(+15% dodge chance)(1000$)
(6)Toxic Gas(free)
(7)ultimate sunscrean(defends you from the SUN)(10000$)
(8)exit


input:""")
      sleep(2)
      system('cls')

      if shop == '1':
        if gold <= 19:
         print ('you can\'t afford this.')
         sleep(2)
         system('cls')
        else:
          print ('you purchased the health potion.')
          sleep(2)
          system('cls')
          gold -= 20
          potion += 1
        
      elif shop == '2':
        if gold <= 149:
         print ('you can\'t afford this.')
         sleep(2)
         system('cls')
        else:
          print ('you purchased the ultimate potion.')
          sleep(2)
          system('cls')
          gold -= 150
          ultimate_potion += 1

      elif shop == '3':
        if gold <= 9:
         print ('you can\'t afford this.')
         sleep(2)
         system('cls')
        else:
          print ('you purchased the code ticket.')
          sleep(2)
          system('cls')
          gold -= 10
          if code_ticket <= 5:
            print ('THE SECRET CODE IS')
            sleep(2)
            print ('5k')
            sleep(4)
            system('cls')
          if code_ticket >= 6:
            print ('you got nothing.')
            sleep(2)
            system('cls')
          
      elif shop == '4':
        if gold <= 249:
         print ('you can\'t afford this.')
         sleep(2)
         system('cls')
        else:
          print ('you purchased a sand bag')
          sleep(2)
          print ('+5% dogde chance')
          system('cls')
          gold -= 250
          dodge_chance += 5
        
      elif shop == '5':
        if gold <= 999:
         print ('you can\'t afford this.')
         sleep(2)
         system('cls')
        else:
          print ('you purchased a attack prediction')
          sleep(2)
          print ('+15% dogde chance')
          system('cls')
          gold -= 1000
          dodge_chance += 15

      elif shop == '6':
        print ('you bought, toxic gass.')
        sleep(2)
        print ('you die.')
        sleep(2)
        system('cls')
        print ('you ALMOST die!')
        sleep(2)
        system('cls')
        print ('you are now VERY WEAK!')
        sleep(2)
        system('cls')
        player_health = 0.1

      elif shop == '7':
        if gold <= 9999:
         print ('you can\'t afford this.')
         sleep(2)
         system('cls')
        else:
          print ('You bought ULTIMATE SUNSCREEN!')
          sleep(2)
          print ('The sun bosses attacks are now weakened.')
          sleep(2)
          system('cls')
          gold -= 10000

      elif shop == '8':
        break
        
      else:
        pass
       


    elif test == '7':
      while True:
        s_code=input("""
      Type in a secret code!
      DO NOT USE THE CODES TO MUCH!
      (1)exit
      
      input:""")
        sleep(2)
        system('cls')

        if s_code == '5k':
          if cheat_system >= 2:
            print ("""
you have cheated to many times and I AM SICK AND TIRED of it! 
NOW FACE THE CONSEQUENCES OF YOUR ACTIONS!""")
            sleep(4)
            system('cls')
            player_health = 1
            enemy_health = 1000
            gold = -1000
          if cheat_system <= 1:
           print ('+5000 gold')
           sleep(2)
           system('cls')
           gold += 5000
           cheat_system += 1
        
        elif s_code == '1':
          break

        elif s_code == 'game rpg':
          if cheat_system >= 2:
            print ("""
you have cheated to many times and I AM SICK AND TIRED of it! 
NOW FACE THE CONSEQUENCES OF YOUR ACTIONS!""")
            sleep(4)
            system('cls')
            player_health = 1
            enemy_health = 1000
            gold = -1000
          if cheat_system <= 1:
           print ('+1000 health')
           sleep(2)
           system('cls')
           player_health += 1000
           cheat_system += 1
            
        elif s_code == 'alert':
          if cheat_system >= 2:
            print ("""
you have cheated to many times and I AM SICK AND TIRED of it! 
NOW FACE THE CONSEQUENCES OF YOUR ACTIONS!""")
            sleep(4)
            system('cls')
            player_health = 1
            enemy_health = 1000
            gold = -1000
          if cheat_system <= 1:
           print ('bad move')
           sleep(2)
           system('cls')
           cheat_system = 100
          
        else:
          pass

    elif test == '4028':
     print ("""
                     ___ ||
                     ||| ||
                     ||||||
                     ||| ||
    +--------------+ ||| ||
    |.------------.| |||
    || Code 4028  || |||
    ||  11:45 AM  || |||
    ||  1/7/2023  ||_|||_
    || The dragon-||/////
    ||-Diary      ||////
    || find it    ||///
    || IMMEDIATELY||//
    || before it  ||/
    ||!IS TO LATE!||
    |+------------+|
    +-..--------..-+
    .--------------.
   / /============\ \
  / /==============\ \
 /____________________\
 \____________________/

[The world is ENDING!!!!!!!]
""") 
     sleep(0.5)
     system('cls')
    else:
        pass

#inventory = [
#'sword_that_can_destory_the_freaking_universe',
#'fist',  'sword', 'staff',  'cloud_sword',  'rain_sword',  'storm_sword', 'storm_bow', 'bow1', 'storm_staff1',  'dagger',  'posin_dagger',  'posin_sword', 'posin_staff2', 'sword2','bow2','posin_bow','iron_fist','mechanical_staff3','gatling_gun','iron_sword3','mechanical_sword3','iron_bow3','mechanical_bow','laser_bow','laser_eye','void_sword4','cursed_tree_sword4','arrows_of_death_bow4','shadow_sword4','shadow_bow4','skelaton_sword4','skelaton_bow4','necromancer_staff4','shadow_staff4','void_staff4','skelaton_staff4','dragon_staff','enchanted_sword5','blank','creative_sword_secret','admin_sword','ultimate_sword_secret',    #'ice_blade','phase_saber','fight','RPG','GAME','0 divided by','','','','',
#]
# This is a change