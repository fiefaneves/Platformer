from scripts.utils import load_images, load_image, Animation, load_sound, load_music

assets = {
    'decor': load_images('tiles/decor'),
    'grass': load_images('tiles/grass'),
    'large_decor': load_images('tiles/large_decor'),
    'snow': load_images('tiles/snow'),
    'cloud_plataform' : load_images('tiles/cloud_plataform'),
    'scaffolding': load_images('tiles/scaffolding'),
    'boxes': load_images('tiles/boxes'),
    'coin': (Animation(load_images('tiles/coin'), img_dur=15)),
    'diamond': (Animation(load_images('tiles/diamond'), img_dur=15)),
    'crates': load_images('tiles/crates'),
    'key_door': load_images('tiles/key_door'),
    'door': load_images('tiles/door'),
    'fence': load_images('tiles/fence'),
    'flag': (Animation(load_images('tiles/flag'), img_dur=35)),
    'flag_pole': load_images('tiles/flag_pole'),
    'blue_flag': (Animation(load_images('tiles/blue_flag'), img_dur=35)),
    'blue_flag_pole': load_images('tiles/blue_flag_pole'),
    'ice1': load_images('tiles/ice1'),
    'ice2': load_images('tiles/ice2'),
    'tree': load_images('tiles/tree'),
    'leaves': load_images('tiles/leaves'),
    'lever': load_images('tiles/lever'),
    'mushroom': load_images('tiles/mushroom'),
    'path': load_images('tiles/path'),
    'pipe': load_images('tiles/pipe'),
    'ropes': load_images('tiles/ropes'),
    'signs': load_images('tiles/signs'),
    'stairs': load_images('tiles/stairs'),
    'water': (Animation(load_images('tiles/water'), img_dur=30)),
    'water_surface': (Animation(load_images('tiles/water_surface'), img_dur=30)),
    'key': (Animation(load_images('tiles/key'), img_dur=15)),
    'spike': load_images('tiles/spike'),
    'snowman': load_images('tiles/snowman'),
    'beams': load_images('tiles/beams'),
    'box_industrial': load_images('tiles/box_industrial'),
    'chests': load_images('tiles/chests'),
    'gears': load_images('tiles/gears'),
    'grass_industrial': load_images('tiles/grass_industrial'),
    'hoists': load_images('tiles/hoists'),
    'light_signals': load_images('tiles/light_signals'),
    'obstacles': load_images('tiles/obstacles'),
    'pipes': load_images('tiles/pipes'),
    'platform': load_images('tiles/platform'),
    'rails': load_images('tiles/rails'),
    'signals': load_images('tiles/signals'),
    'stairs_industrial': load_images('tiles/stairs_industrial'),
    'triangles': load_images('tiles/triangles'),
    'wheels': load_images('tiles/wheels'),
    'dye_point': load_images('tiles/dye_point'),
    'enemy': load_images('tiles/enemy'),
    'spawn_point': load_images('tiles/spawn_point'),
}

sounds = {
    'jump': load_sound('jump.wav') , 
    'next_level': load_sound('next_level.wav'),
    'damage': load_sound('damage.wav'),
    'walk': load_sound('walk.wav'),
    'collectible': load_sound('collectible.wav'),
    'open_crate': load_sound('open_crate.wav'),
    'ambience': load_sound('ambience.wav'),
    'music': load_sound('music.wav'),
    'checkpoint': load_sound('checkpoint.wav'),
    'kill': load_sound('kill.wav')
}
