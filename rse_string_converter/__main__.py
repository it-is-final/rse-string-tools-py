from rse_string_converter.enums import Version, Language
from rse_string_converter.string_encoder import encode_bytes
from rse_string_converter.string_decoder import decode_string


def main():
    a = encode_bytes(
        [0x10, 0xFF, 0x2F, 0xE1],
        Version.EMERALD,
        Language.JPN
    )
    print(a.replace("\0", "␃"))
    try:
        b = decode_string(a, Version.EMERALD, Language.JPN)
        print(b)
    except KeyError as e:
        e.add_note("is not a valid character")
        print(e)


if __name__ == "__main__":
    main()
