"""rse_string_tools_demo
This contains a demonstration that does the following:
- Converts a box name payload in its byte form to strings
- Converts a box name payload in its string form to bytes

This will print out the result in stdout."""

from rse_string_tools.constants import Version, Language
import rse_string_tools


def main():
    b_box_names = [
        bytearray([0xEC, 0xB5, 0xEE, 0xC8, 0x00, 0xA7, 0xC0, 0xC0, 0xFF]),
        bytearray([0xD2, 0x00, 0xD2, 0xEC, 0xB5, 0x00, 0x00, 0x00, 0xFF]),
        bytearray([0x00, 0x00, 0xA5, 0xBD, 0xCF, 0xE2, 0x00, 0x00, 0xFF]),
        bytearray([0x00, 0xB6, 0xA3, 0xCB, 0xE1, 0x00, 0x00, 0x00, 0xFF]),
        bytearray([0xB8, 0xA3, 0xCB, 0xE1, 0xBA, 0xA3, 0xCB, 0xE1, 0xFF]),
        bytearray([0x00, 0x00, 0x00, 0xBB, 0xA3, 0xEB, 0xE1, 0x00, 0xFF]),
        bytearray([0x00, 0x00, 0xBE, 0xC0, 0xEB, 0xE1, 0x00, 0x00, 0xFF]),
        bytearray([0x00, 0xEC, 0xCF, 0xB0, 0xE3, 0x00, 0x00, 0x00, 0xFF]),
        bytearray([0xDF, 0xC8, 0xAC, 0xE2, 0xEE, 0xC2, 0xAC, 0xE2, 0xFF]),
        bytearray([0x00, 0x00, 0x00, 0x00, 0xC0, 0xAB, 0xE5, 0x00, 0xFF]),
        bytearray([0x00, 0x00, 0xEE, 0xCA, 0xAE, 0xE2, 0x00, 0x00, 0xFF]),
        bytearray([0x00, 0xE4, 0xCB, 0xAC, 0xE2, 0x00, 0x00, 0x00, 0xFF]),
        bytearray([0xA2, 0xCC, 0xAC, 0xE2, 0xCE, 0x00, 0xAC, 0xE2, 0xFF]),
        bytearray([0x00, 0x00, 0x00, 0xC9, 0xFF, 0xB0, 0xE3, 0x00, 0xFF]),
    ]
    s_box_names = [
        "x♂zN 6FF\x00",
        "X Xx♂   \x00",
        "  4CUn  \x00",
        " ♀2Qm   \x00",
        ",2Qm/2Qm\x00",
        "   A2wm \x00",
        "  DFwm  \x00",
        " xU…o   \x00",
        "kN?nzH?n\x00",
        "    F!q \x00",
        "  zP-n  \x00",
        " pQ?n   \x00",
        "1R?nT ?n\x00",
        "   O\x00…o \x00"
    ]
    for i, b_box_name in enumerate(b_box_names, start=1):
        print(f"Box {i:>2d}: {
            rse_string_tools.get_rse_string(b_box_name, Version.EMERALD, Language.ENG)
              .split("\0")[0]
            }")
    print()
    for i, s_box_name in enumerate(s_box_names, start=1):
        out = rse_string_tools.get_rse_bytes(s_box_name, Version.EMERALD, Language.ENG)
        print(f"Box {i:>2d}: {" ".join(f"{x:02X}" for x in out)}")


if __name__ == "__main__":
    main()
