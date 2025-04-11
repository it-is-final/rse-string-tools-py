from typing import Iterable
from rse_string_tools.constants import Version, Language


def build_character_map(
        version: Version,
        langauge: Language
        ) -> dict[int, str]:
    """Builds a decoding map based on the given game version and language.
    
    Arguments:
        version -- Target game version
        language -- Target game language
    """
    base_jpn_map = {
        0x0: '　', 
        0x1: 'あ', 0x2: 'い', 0x3: 'う', 0x4: 'え', 0x5: 'お', 
        0x6: 'か', 0x7: 'き', 0x8: 'く', 0x9: 'け', 0xa: 'こ', 
        0xb: 'さ', 0xc: 'し', 0xd: 'す', 0xe: 'せ', 0xf: 'そ', 
        0x10: 'た', 0x11: 'ち', 0x12: 'つ', 0x13: 'て', 0x14: 'と', 
        0x15: 'な', 0x16: 'に', 0x17: 'ぬ', 0x18: 'ね', 0x19: 'の', 
        0x1a: 'は', 0x1b: 'ひ', 0x1c: 'ふ', 0x1d: 'へ', 0x1e: 'ほ', 
        0x1f: 'ま', 0x20: 'み', 0x21: 'む', 0x22: 'め', 0x23: 'も', 
        0x24: 'や', 0x25: 'ゆ', 0x26: 'よ', 
        0x27: 'ら', 0x28: 'り', 0x29: 'る', 0x2a: 'れ', 0x2b: 'ろ', 
        0x2c: 'わ', 0x2d: 'を', 0x2e: 'ん', 
        0x2f: 'ぁ', 0x30: 'ぃ', 0x31: 'ぅ', 0x32: 'ぇ', 0x33: 'ぉ', 
        0x34: 'ゃ', 0x35: 'ゅ', 0x36: 'ょ',
        0x37: 'が', 0x38: 'ぎ', 0x39: 'ぐ', 0x3a: 'げ', 0x3b: 'ご',
        0x3c: 'ざ', 0x3d: 'じ', 0x3e: 'ず', 0x3f: 'ぜ', 0x40: 'ぞ',
        0x41: 'だ', 0x42: 'ぢ', 0x43: 'づ', 0x44: 'で', 0x45: 'ど',
        0x46: 'ば', 0x47: 'び', 0x48: 'ぶ', 0x49: 'べ', 0x4a: 'ぼ',
        0x4b: 'ぱ', 0x4c: 'ぴ', 0x4d: 'ぷ', 0x4e: 'ぺ', 0x4f: 'ぽ',
        0x50: 'っ',
        0x51: 'ア', 0x52: 'イ', 0x53: 'ウ', 0x54: 'エ', 0x55: 'オ',
        0x56: 'カ', 0x57: 'キ', 0x58: 'ク', 0x59: 'ケ', 0x5a: 'コ',
        0x5b: 'サ', 0x5c: 'シ', 0x5d: 'ス', 0x5e: 'セ', 0x5f: 'ソ',
        0x60: 'タ', 0x61: 'チ', 0x62: 'ツ', 0x63: 'テ', 0x64: 'ト',
        0x65: 'ナ', 0x66: 'ニ', 0x67: 'ヌ', 0x68: 'ネ', 0x69: 'ノ',
        0x6a: 'ハ', 0x6b: 'ヒ', 0x6c: 'フ', 0x6d: 'ヘ', 0x6e: 'ホ',
        0x6f: 'マ', 0x70: 'ミ', 0x71: 'ム', 0x72: 'メ', 0x73: 'モ',
        0x74: 'ヤ', 0x75: 'ユ', 0x76: 'ヨ',
        0x77: 'ラ', 0x78: 'リ', 0x79: 'ル', 0x7a: 'レ', 0x7b: 'ロ',
        0x7c: 'ワ', 0x7d: 'ヲ', 0x7e: 'ン',
        0x7f: 'ァ', 0x80: 'ィ', 0x81: 'ゥ', 0x82: 'ェ', 0x83: 'ォ',
        0x84: 'ャ', 0x85: 'ュ', 0x86: 'ョ',
        0x87: 'ガ', 0x88: 'ギ', 0x89: 'グ', 0x8a: 'ゲ', 0x8b: 'ゴ',
        0x8c: 'ザ', 0x8d: 'ジ', 0x8e: 'ズ', 0x8f: 'ゼ', 0x90: 'ゾ',
        0x91: 'ダ', 0x92: 'ヂ', 0x93: 'ヅ', 0x94: 'デ', 0x95: 'ド',
        0x96: 'バ', 0x97: 'ビ', 0x98: 'ブ', 0x99: 'ベ', 0x9a: 'ボ',
        0x9b: 'パ', 0x9c: 'ピ', 0x9d: 'プ', 0x9e: 'ペ', 0x9f: 'ポ',
        0xa0: 'ッ',
        0xa1: '０',
        0xa2: '１', 0xa3: '２', 0xa4: '３',
        0xa5: '４', 0xa6: '５', 0xa7: '６',
        0xa8: '７', 0xa9: '８', 0xaa: '９',
        0xab: '！', 0xac: '？',
        0xad: '。', 0xae: 'ー', 0xaf: '・', 0xb0: '‥',
        0xb1: '『', 0xb2: '』', 0xb3: '「', 0xb4: '」',
        0xb5: '♂', 0xb6: '♀',
        0xb7: '円', 0xb8: '．', 0xb9: '×',
        0xba: '／',
        0xbb: 'Ａ', 0xbc: 'Ｂ', 0xbd: 'Ｃ', 0xbe: 'Ｄ', 0xbf: 'Ｅ',
        0xc0: 'Ｆ', 0xc1: 'Ｇ', 0xc2: 'Ｈ', 0xc3: 'Ｉ', 0xc4: 'Ｊ',
        0xc5: 'Ｋ', 0xc6: 'Ｌ', 0xc7: 'Ｍ', 0xc8: 'Ｎ', 0xc9: 'Ｏ',
        0xca: 'Ｐ', 0xcb: 'Ｑ', 0xcc: 'Ｒ', 0xcd: 'Ｓ', 0xce: 'Ｔ',
        0xcf: 'Ｕ', 0xd0: 'Ｖ', 0xd1: 'Ｗ', 0xd2: 'Ｘ', 0xd3: 'Ｙ',
        0xd4: 'Ｚ',
        0xd5: 'ａ', 0xd6: 'ｂ', 0xd7: 'ｃ', 0xd8: 'ｄ', 0xd9: 'ｅ',
        0xda: 'ｆ', 0xdb: 'ｇ', 0xdc: 'ｈ', 0xdd: 'ｉ', 0xde: 'ｊ',
        0xdf: 'ｋ', 0xe0: 'ｌ', 0xe1: 'ｍ', 0xe2: 'ｎ', 0xe3: 'ｏ',
        0xe4: 'ｐ', 0xe5: 'ｑ', 0xe6: 'ｒ', 0xe7: 'ｓ', 0xe8: 'ｔ',
        0xe9: 'ｕ', 0xea: 'ｖ', 0xeb: 'ｗ', 0xec: 'ｘ', 0xed: 'ｙ',
        0xee: 'ｚ',
        0xef: '►', 0xf0: '：',
        0xf1: 'Ä', 0xf2: 'Ö', 0xf3: 'Ü',
        0xf4: 'ä', 0xf5: 'ö', 0xf6: 'ü',
        0xf7: '\x00', 0xf8: '\x00', 0xf9: '\x00',
        0xfa: '\x00', 0xfb: '\x00', 0xfc: '\x00', 0xfd: '\x00', 0xfe: '\n',
        0xff: '\x00'
    }
    base_non_jpn_map = {
        # Due to limitations of Unicode certain custom
        # characters cannot be represented, they will be represented
        # as spaces.
        0x0: ' ', 0x1: 'À', 0x2: 'Á', 0x3: 'Â', 0x4: 'Ç',
        0x5: 'È', 0x6: 'É', 0x7: 'Ê', 0x8: 'Ë', 0x9: 'Ì',
        0xb: 'Î', 0xc: 'Ï', 0xd: 'Ò', 0xe: 'Ó', 0xf: 'Ô',
        0x10: 'Œ', 0x11: 'Ù', 0x12: 'Ú', 0x13: 'Û', 0x14: 'Ñ',
        0x15: 'ß', 0x16: 'à', 0x17: 'á', 0x19: 'ç', 0x1a: 'è',
        0x1b: 'é', 0x1c: 'ê', 0x1d: 'ë', 0x1e: 'ì', 0x20: 'î',
        0x21: 'ï', 0x22: 'ò', 0x23: 'ó', 0x24: 'ô', 0x25: 'œ',
        0x26: 'ù', 0x27: 'ú', 0x28: 'û', 0x29: 'ñ', 0x2a: 'º',
        0x2b: 'ª', 0x2c: ' ', 0x2d: '&', 0x2e: '+',
        0x34: ' ', 0x35: '=', 0x36: ';',
        0x50: '▯', 0x51: '¿', 0x52: '¡', 0x53: ' ', 0x54: ' ',
        0x55: ' ', 0x56: ' ', 0x57: ' ', 0x58: ' ', 0x59: ' ',
        0x5a: 'Í', 0x5b: '%', 0x5c: '(', 0x5d: ')',
        0x68: 'â', 0x6f: 'í', 0x79: '↑',
        0x7a: '↓', 0x7b: '←', 0x7c: '→', 0x7d: ' ', 0x7e: ' ',
        0x7f: ' ', 0x80: ' ', 0x81: ' ', 0x82: ' ', 0x83: ' ',
        0x84: 'ᵉ', 0x85: '<', 0x86: '>',
        0xa0: ' ', 0xa1: '0', 0xa2: '1', 0xa3: '2', 0xa4: '3',
        0xa5: '4', 0xa6: '5', 0xa7: '6', 0xa8: '7', 0xa9: '8',
        0xaa: '9', 0xab: '!', 0xac: '?', 0xad: '.', 0xae: '-',
        0xaf: '·', 0xb0: '…', 0xb1: '“', 0xb2: '”', 0xb3: '‘',
        0xb4: '’', 0xb5: '♂', 0xb6: '♀', 0xb7: '$', 0xb8: ',',
        0xb9: '×', 0xba: '/', 0xbb: 'A', 0xbc: 'B', 0xbd: 'C',
        0xbe: 'D', 0xbf: 'E', 0xc0: 'F', 0xc1: 'G', 0xc2: 'H',
        0xc3: 'I', 0xc4: 'J', 0xc5: 'K', 0xc6: 'L', 0xc7: 'M',
        0xc8: 'N', 0xc9: 'O', 0xca: 'P', 0xcb: 'Q', 0xcc: 'R',
        0xcd: 'S', 0xce: 'T', 0xcf: 'U', 0xd0: 'V', 0xd1: 'W',
        0xd2: 'X', 0xd3: 'Y', 0xd4: 'Z', 0xd5: 'a', 0xd6: 'b',
        0xd7: 'c', 0xd8: 'd', 0xd9: 'e', 0xda: 'f', 0xdb: 'g',
        0xdc: 'h', 0xdd: 'i', 0xde: 'j', 0xdf: 'k', 0xe0: 'l',
        0xe1: 'm', 0xe2: 'n', 0xe3: 'o', 0xe4: 'p', 0xe5: 'q',
        0xe6: 'r', 0xe7: 's', 0xe8: 't', 0xe9: 'u', 0xea: 'v',
        0xeb: 'w', 0xec: 'x', 0xed: 'y', 0xee: 'z', 0xef: '►',
        0xf0: ':', 0xf1: 'Ä', 0xf2: 'Ö', 0xf3: 'Ü', 0xf4: 'ä',
        0xf5: 'ö', 0xf6: 'ü', 0xf7: '\x00', 0xf8: '\x00', 0xf9: '\x00',
        0xfa: '\x00', 0xfb: '\x00', 0xfc: '\x00', 0xfd: '\x00', 0xfe: '\n',
        0xff: '\x00'
    }
    character_map = (base_jpn_map.copy()
                     if langauge is Language.JPN
                     else base_non_jpn_map.copy())
    if (version is Version.RUBY
        or version is Version.SAPPHIRE):
        # 0xF7-0xF9 are not control characters in Ruby/Sapphire.
        # In these games, they will always print as arrows.
        character_map[0xF7] = '↑'
        character_map[0xF8] = '↓'
        character_map[0xF9] = '←'
        # All game languages uses a two-dot elipsis
        character_map[0xB0] = '‥'
    if (langauge is Language.JPN
        and (version is Version.FIRERED
             or version is Version.LEAFGREEN)
        ):
        # Japanese FireRed/LeafGreen uses a three-dot elipsis
        # while all other game versions (JPN) uses a two-dot elipsis
        character_map[0xB0] = '…'
    if langauge is not Language.JPN and version is not Version.EMERALD:
        # These codepoints are not used in versions other than Emerald
        character_map.pop(0x50)
        character_map.pop(0x7D)
        character_map.pop(0x7E)
        character_map.pop(0x7F)
        character_map.pop(0x80)
        character_map.pop(0x81)
        character_map.pop(0x82)
        character_map.pop(0x83)
    if langauge is Language.FRA:
        character_map[0xB1] = '«'
        character_map[0xB2] = '»'
        if version is Version.EMERALD:
            character_map[0x64] = ' '
    if langauge is Language.GER:
        character_map[0xB1] = '„'
        character_map[0xB2] = '“'
    if langauge is Language.ITA:
        # Italian language uses 0x5E-0x63 for rendering the name for PokéBlocks
        character_map[0x57] = ' '
        character_map[0x58] = ' '
        character_map[0x59] = ' '
        character_map[0x5E] = ' '
        character_map[0x5F] = ' '
        character_map[0x60] = ' '
        character_map[0x61] = ' '
        character_map[0x62] = ' '
        character_map[0x63] = ' '
    if (langauge is not Language.JPN
        and (version is Version.RUBY
             or version is Version.SAPPHIRE)
        ):
        for k, v in base_jpn_map.items():
            character_map.setdefault(k, v)
    return character_map


CHARACTER_MAPS = {
    Version.RUBY: {
        Language.JPN: build_character_map(Version.RUBY, Language.JPN),
        Language.ENG: build_character_map(Version.RUBY, Language.ENG),
        Language.FRA: build_character_map(Version.RUBY, Language.FRA),
        Language.ITA: build_character_map(Version.RUBY, Language.ITA),
        Language.GER: build_character_map(Version.RUBY, Language.GER),
        Language.SPA: build_character_map(Version.RUBY, Language.SPA),
    },
    Version.SAPPHIRE: {
        Language.JPN: build_character_map(Version.SAPPHIRE, Language.JPN),
        Language.ENG: build_character_map(Version.SAPPHIRE, Language.ENG),
        Language.FRA: build_character_map(Version.SAPPHIRE, Language.FRA),
        Language.ITA: build_character_map(Version.SAPPHIRE, Language.ITA),
        Language.GER: build_character_map(Version.SAPPHIRE, Language.GER),
        Language.SPA: build_character_map(Version.SAPPHIRE, Language.SPA),
    },
    Version.FIRERED: {
        Language.JPN: build_character_map(Version.FIRERED, Language.JPN),
        Language.ENG: build_character_map(Version.FIRERED, Language.ENG),
        Language.FRA: build_character_map(Version.FIRERED, Language.FRA),
        Language.ITA: build_character_map(Version.FIRERED, Language.ITA),
        Language.GER: build_character_map(Version.FIRERED, Language.GER),
        Language.SPA: build_character_map(Version.FIRERED, Language.SPA),
    },
    Version.LEAFGREEN: {
        Language.JPN: build_character_map(Version.LEAFGREEN, Language.JPN),
        Language.ENG: build_character_map(Version.LEAFGREEN, Language.ENG),
        Language.FRA: build_character_map(Version.LEAFGREEN, Language.FRA),
        Language.ITA: build_character_map(Version.LEAFGREEN, Language.ITA),
        Language.GER: build_character_map(Version.LEAFGREEN, Language.GER),
        Language.SPA: build_character_map(Version.LEAFGREEN, Language.SPA),
    },
    Version.EMERALD: {
        Language.JPN: build_character_map(Version.EMERALD, Language.JPN),
        Language.ENG: build_character_map(Version.EMERALD, Language.ENG),
        Language.FRA: build_character_map(Version.EMERALD, Language.FRA),
        Language.ITA: build_character_map(Version.EMERALD, Language.ITA),
        Language.GER: build_character_map(Version.EMERALD, Language.GER),
        Language.SPA: build_character_map(Version.EMERALD, Language.SPA),
    },
}


def build_character_map_r(
        version: Version,
        langauge: Language
        ) -> dict[str, int]:
    """Builds a encoding map based on the given game version and game language.

    Arguments:
        version -- Target game version
        language -- Target game language
    """
    reference_map = CHARACTER_MAPS[version][langauge]
    character_map = {
        '\n': 0xfe, '\x00': 0xff
        }
    for k, v in reference_map.items():
        character_map.setdefault(v, k)
    jpn_extension = {
        '‥': 0xb0,
        '：': 0xf0, '＿': 0x00,
        ' ': 0x0,
        '0': 0xA1, '1': 0xA2, '2': 0xA3, '3': 0xA4, '4': 0xA5,
        '5': 0xA6, '6': 0xA7, '7': 0xA8, '8': 0xA9, '9': 0xAA,
        '!': 0xAB, '?': 0xAC, '¥': 0xB7, '·': 0xAF, '･': 0xAF,
        '-': 0xAE, '–': 0xAE, '…': 0xB0, '.': 0xB8, '/': 0xba,
        'A': 0xBB, 'B': 0xBC, 'C': 0xBD, 'D': 0xBE, 'E': 0xBF,
        'F': 0xC0, 'G': 0xC1, 'H': 0xC2, 'I': 0xC3, 'J': 0xC4,
        'K': 0xC5, 'L': 0xC6, 'M': 0xC7, 'N': 0xC8, 'O': 0xC9,
        'P': 0xCA, 'Q': 0xCB, 'R': 0xCC, 'S': 0xCD, 'T': 0xCE,
        'U': 0xCF, 'V': 0xD0, 'W': 0xD1, 'X': 0xD2, 'Y': 0xD3,
        'Z': 0xD4, 
        'a': 0xD5, 'b': 0xD6, 'c': 0xD7, 'd': 0xD8, 'e': 0xD9,
        'f': 0xDA, 'g': 0xDB, 'h': 0xDC, 'i': 0xDD, 'j': 0xDE,
        'k': 0xDF, 'l': 0xE0, 'm': 0xE1, 'n': 0xE2, 'o': 0xE3,
        'p': 0xE4, 'q': 0xE5, 'r': 0xE6, 's': 0xE7, 't': 0xE8,
        'u': 0xE9, 'v': 0xEA, 'w': 0xEB, 'x': 0xEC, 'y': 0xED,
        'z': 0xEE, ':': 0xF0, '_': 0x00, '␣': 0x00,
    }
    non_jpn_extension = {
        '…': 0xB0,
        '‥': 0xB0, '–': 0xAE, '･': 0xAF, '・': 0xAF,
        '_': 0x00, '␣': 0x00,
    }
    if langauge is Language.JPN:
        character_map.update(jpn_extension)
    else:
        character_map.update(non_jpn_extension)
    return character_map


CHARACTER_MAPS_R = {
    Version.RUBY: {
        Language.JPN: build_character_map_r(Version.RUBY, Language.JPN),
        Language.ENG: build_character_map_r(Version.RUBY, Language.ENG),
        Language.FRA: build_character_map_r(Version.RUBY, Language.FRA),
        Language.ITA: build_character_map_r(Version.RUBY, Language.ITA),
        Language.GER: build_character_map_r(Version.RUBY, Language.GER),
        Language.SPA: build_character_map_r(Version.RUBY, Language.SPA),
    },
    Version.SAPPHIRE: {
        Language.JPN: build_character_map_r(Version.SAPPHIRE, Language.JPN),
        Language.ENG: build_character_map_r(Version.SAPPHIRE, Language.ENG),
        Language.FRA: build_character_map_r(Version.SAPPHIRE, Language.FRA),
        Language.ITA: build_character_map_r(Version.SAPPHIRE, Language.ITA),
        Language.GER: build_character_map_r(Version.SAPPHIRE, Language.GER),
        Language.SPA: build_character_map_r(Version.SAPPHIRE, Language.SPA),
    },
    Version.FIRERED: {
        Language.JPN: build_character_map_r(Version.FIRERED, Language.JPN),
        Language.ENG: build_character_map_r(Version.FIRERED, Language.ENG),
        Language.FRA: build_character_map_r(Version.FIRERED, Language.FRA),
        Language.ITA: build_character_map_r(Version.FIRERED, Language.ITA),
        Language.GER: build_character_map_r(Version.FIRERED, Language.GER),
        Language.SPA: build_character_map_r(Version.FIRERED, Language.SPA),
    },
    Version.LEAFGREEN: {
        Language.JPN: build_character_map_r(Version.LEAFGREEN, Language.JPN),
        Language.ENG: build_character_map_r(Version.LEAFGREEN, Language.ENG),
        Language.FRA: build_character_map_r(Version.LEAFGREEN, Language.FRA),
        Language.ITA: build_character_map_r(Version.LEAFGREEN, Language.ITA),
        Language.GER: build_character_map_r(Version.LEAFGREEN, Language.GER),
        Language.SPA: build_character_map_r(Version.LEAFGREEN, Language.SPA),
    },
    Version.EMERALD: {
        Language.JPN: build_character_map_r(Version.EMERALD, Language.JPN),
        Language.ENG: build_character_map_r(Version.EMERALD, Language.ENG),
        Language.FRA: build_character_map_r(Version.EMERALD, Language.FRA),
        Language.ITA: build_character_map_r(Version.EMERALD, Language.ITA),
        Language.GER: build_character_map_r(Version.EMERALD, Language.GER),
        Language.SPA: build_character_map_r(Version.EMERALD, Language.SPA),
    }
}


def get_rse_string(data: Iterable[int], version: Version, language: Language):
    """Returns a string from decoding a bytearray
    
    Arguments:
        data -- Input bytearray
        version -- Target game version
        language -- Target game language
    """
    character_map = CHARACTER_MAPS[version][language]
    placeholder = character_map[0]
    return ''.join(character_map.get(b, placeholder) for b in data)


def get_rse_bytes(data: str, version: Version, language: Language):
    """Returns the resulting bytearray from encoding the string
    
    Arguments:
        data -- Input string
        version -- Target game version for character map
        language -- Target game language for character map
    """
    character_map = CHARACTER_MAPS_R[version][language]
    return bytes(character_map[c] for c in data.replace('�', ' '))
