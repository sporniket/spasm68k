"""
---
(c) 2025 David SPORN
---
This is part of SPASM68K -- Sporniket's toolbox for assembly language targeting 
the MC68000 instruction set architecture.

SPASM68K is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

SPASM68K is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.

See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with SPASM.
If not, see <https://www.gnu.org/licenses/>. 
---
"""

import random

from spasm68k.models import LineOfCode, Segment
from spasm68k.models.operands import (
    OperandDirectRegisterData,
    OperandDirectRegisterAddress,
    OperandIndirectRegisterAddress,
    OperandIndirectRegisterAddressWithPostIncrement,
    OperandIndirectRegisterAddressWithPreDecrement,
    OperandIndirectRegisterAddressWithDisplacement,
    OperandUnsupported,
)

from spasm68k.parsers import OperandParser

parser = OperandParser()


def setupOperandToParse(operand: str) -> tuple[LineOfCode, Segment]:
    _operand = operand.strip()
    line = LineOfCode(
        "whatever", int(random.random() * 75000), f"  opcode {_operand} some comments"
    )
    segment = Segment(9, 9 + len(_operand))
    return (line, segment)


def test_setupOperandToParse():
    line, segment = setupOperandToParse("  my operand    ")
    assert segment.start == 9
    assert segment.end == 19
    assert line.content == "  opcode my operand some comments"


def test_that_it_WILL_returns_an_unsupported_operand_when_it_cannot_recognize_anything():
    for op in ["whatever", "d8"]:
        source, oseg = setupOperandToParse(op)
        operand = parser.parse(oseg, source)
        assert isinstance(operand, OperandUnsupported)
        assert operand.origin.segment == oseg
        assert operand.origin.lineOfCode == source


def test_that_it_WILL_parse_direct_register_data_operand():
    for d in ["d", "D"]:
        for n in range(8):
            source, oseg = setupOperandToParse(f"{d}{n}")
            operand = parser.parse(oseg, source)
            assert isinstance(operand, OperandDirectRegisterData)
            assert operand.value == n
            assert operand.origin.segment == oseg
            assert operand.origin.lineOfCode == source


def test_that_it_WILL_parse_direct_register_address_operand():
    for d in ["a", "A"]:
        for n in range(8):
            source, oseg = setupOperandToParse(f"{d}{n}")
            operand = parser.parse(oseg, source)
            assert isinstance(operand, OperandDirectRegisterAddress)
            assert operand.value == n
            assert operand.alias == None
            assert operand.origin.segment == oseg
            assert operand.origin.lineOfCode == source


def test_that_it_WILL_parse_direct_register_address_sp_operand():
    for s in ["s", "S"]:
        for p in ["p", "P"]:
            source, oseg = setupOperandToParse(f"{s}{p}")
            operand = parser.parse(oseg, source)
            assert isinstance(operand, OperandDirectRegisterAddress)
            assert operand.value == 7
            assert operand.alias == "sp"
            assert operand.origin.segment == oseg
            assert operand.origin.lineOfCode == source


def test_that_it_WILL_parse_indirect_register_address_operand():
    for d in ["a", "A"]:
        for n in range(8):
            source, oseg = setupOperandToParse(f"({d}{n})")
            operand = parser.parse(oseg, source)
            assert isinstance(operand, OperandIndirectRegisterAddress)
            assert operand.value == n
            assert operand.alias == None
            assert operand.origin.segment == oseg
            assert operand.origin.lineOfCode == source


def test_that_it_WILL_parse_indirect_register_address_sp_operand():
    for s in ["s", "S"]:
        for p in ["p", "P"]:
            source, oseg = setupOperandToParse(f"({s}{p})")
            operand = parser.parse(oseg, source)
            assert isinstance(operand, OperandIndirectRegisterAddress)
            assert operand.value == 7
            assert operand.alias == "sp"
            assert operand.origin.segment == oseg
            assert operand.origin.lineOfCode == source


def test_that_it_WILL_parse_indirect_register_address_with_postincrement_operand():
    for d in ["a", "A"]:
        for n in range(8):
            source, oseg = setupOperandToParse(f"({d}{n})+")
            operand = parser.parse(oseg, source)
            assert isinstance(operand, OperandIndirectRegisterAddressWithPostIncrement)
            assert operand.value == n
            assert operand.alias == None
            assert operand.origin.segment == oseg
            assert operand.origin.lineOfCode == source


def test_that_it_WILL_parse_indirect_register_address_sp_with_postincrement_operand():
    for s in ["s", "S"]:
        for p in ["p", "P"]:
            source, oseg = setupOperandToParse(f"({s}{p})+")
            operand = parser.parse(oseg, source)
            assert isinstance(operand, OperandIndirectRegisterAddressWithPostIncrement)
            assert operand.value == 7
            assert operand.alias == "sp"
            assert operand.origin.segment == oseg
            assert operand.origin.lineOfCode == source


def test_that_it_WILL_parse_indirect_register_address_with_predecrement_operand():
    for d in ["a", "A"]:
        for n in range(8):
            source, oseg = setupOperandToParse(f"-({d}{n})")
            operand = parser.parse(oseg, source)
            assert isinstance(operand, OperandIndirectRegisterAddressWithPreDecrement)
            assert operand.value == n
            assert operand.alias == None
            assert operand.origin.segment == oseg
            assert operand.origin.lineOfCode == source


def test_that_it_WILL_parse_indirect_register_address_sp_with_predecrement_operand():
    for s in ["s", "S"]:
        for p in ["p", "P"]:
            source, oseg = setupOperandToParse(f"-({s}{p})")
            operand = parser.parse(oseg, source)
            assert isinstance(operand, OperandIndirectRegisterAddressWithPreDecrement)
            assert operand.value == 7
            assert operand.alias == "sp"
            assert operand.origin.segment == oseg
            assert operand.origin.lineOfCode == source


# generate displacement
def generateDisplacementStrings_generic(
    span: int, numberFormat: str, prefixes: list[str]
) -> list[str]:
    baseValue = format(int(random.random() * span), numberFormat)
    values = [baseValue, baseValue + "_" + baseValue]
    result = []
    for v in values:
        result += [p + v for p in prefixes]
    return result


def generateDisplacementStrings_binaryValues() -> list[str]:
    return generateDisplacementStrings_generic(65536, "b", ["%", "0b"])


def generateDisplacementStrings_octalValues() -> list[str]:
    return generateDisplacementStrings_generic(65536, "o", ["0", "0o"])


def generateDisplacementStrings_decimalValues() -> list[str]:
    return generateDisplacementStrings_generic(65536, "d", ["", "0d", "0d0"])


def generateDisplacementStrings_hexadecimalValues() -> list[str]:
    return generateDisplacementStrings_generic(65536, "x", ["$", "0x"])


def generateDisplacementStrings_validSymbols() -> list[str]:
    return ["simple", "with_underscores", "a1pha_num3r1c"]


def generateDisplacementStrings() -> list[str]:
    result = []
    for g in [
        generateDisplacementStrings_binaryValues,
        generateDisplacementStrings_octalValues,
        generateDisplacementStrings_decimalValues,
        generateDisplacementStrings_hexadecimalValues,
        generateDisplacementStrings_validSymbols,
    ]:
        result += g()
    return result


def test_that_it_WILL_parse_indirect_register_address_with_displacement():
    for displ in generateDisplacementStrings():
        for d in ["a", "A"]:
            for n in range(8):
                for variant in [f"{displ}({d}{n})", f"({displ},{d}{n})"]:
                    source, oseg = setupOperandToParse(variant)
                    operand = parser.parse(oseg, source)
                    assert isinstance(
                        operand, OperandIndirectRegisterAddressWithDisplacement
                    )
                    assert operand.value == n
                    assert operand.alias == None
                    assert operand.origin.segment == oseg
                    assert operand.origin.lineOfCode == source
                    assert isinstance(operand.displacement, Segment)
                    if variant[0] == "(":
                        assert operand.displacement.start == 1
                        assert operand.displacement.end == 1 + len(displ)
                    else:
                        assert operand.displacement.start == 0
                        assert operand.displacement.end == len(displ)


def test_that_it_WILL_parse_indirect_register_address_sp_with_displacement():
    for displ in generateDisplacementStrings():
        for s in ["s", "S"]:
            for p in ["p", "P"]:
                for variant in [f"{displ}({s}{p})", f"({displ},{s}{p})"]:
                    source, oseg = setupOperandToParse(variant)
                    operand = parser.parse(oseg, source)
                    assert isinstance(
                        operand, OperandIndirectRegisterAddressWithDisplacement
                    )
                    assert operand.value == 7
                    assert operand.alias == "sp"
                    assert operand.origin.segment == oseg
                    assert operand.origin.lineOfCode == source
                    if variant[0] == "(":
                        assert operand.displacement.start == 1
                        assert operand.displacement.end == 1 + len(displ)
                    else:
                        assert operand.displacement.start == 0
                        assert operand.displacement.end == len(displ)
