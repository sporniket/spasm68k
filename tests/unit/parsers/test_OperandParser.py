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


def test_OperandParser_can_parse_direct_register_data_operand():
    for d in ["d", "D"]:
        for n in range(8):
            source, oseg = setupOperandToParse(f"{d}{n}")
            operand = parser.parse(oseg, source)
            assert isinstance(operand, OperandDirectRegisterData)
            assert operand.value == n
            assert operand.origin.segment == oseg
            assert operand.origin.lineOfCode == source


def test_OperandParser_can_parse_direct_register_address_operand():
    for d in ["a", "A"]:
        for n in range(8):
            source, oseg = setupOperandToParse(f"{d}{n}")
            operand = parser.parse(oseg, source)
            assert isinstance(operand, OperandDirectRegisterAddress)
            assert operand.value == n
            assert operand.alias == None
            assert operand.origin.segment == oseg
            assert operand.origin.lineOfCode == source

    # match alias "sp"
    source, oseg = setupOperandToParse("sp")
    operand = parser.parse(oseg, source)
    assert isinstance(operand, OperandDirectRegisterAddress)
    assert operand.value == n
    assert operand.alias == "sp"
    assert operand.origin.segment == oseg
    assert operand.origin.lineOfCode == source


def test_OperandParser_can_parse_indirect_register_address_operand():
    for d in ["a", "A"]:
        for n in range(8):
            source, oseg = setupOperandToParse(f"({d}{n})")
            operand = parser.parse(oseg, source)
            assert isinstance(operand, OperandIndirectRegisterAddress)
            assert operand.value == n
            assert operand.alias == None
            assert operand.origin.segment == oseg
            assert operand.origin.lineOfCode == source

    # match alias "sp"
    source, oseg = setupOperandToParse("(sp)")
    operand = parser.parse(oseg, source)
    assert isinstance(operand, OperandIndirectRegisterAddress)
    assert operand.value == n
    assert operand.alias == "sp"
    assert operand.origin.segment == oseg
    assert operand.origin.lineOfCode == source


def test_OperandParser_returns_an_unsupported_operand_when_it_cannot_recognize_anything():
    for op in ["whatever", "d8"]:
        source, oseg = setupOperandToParse(op)
        operand = parser.parse(oseg, source)
        assert isinstance(operand, OperandUnsupported)
        assert operand.origin.segment == oseg
        assert operand.origin.lineOfCode == source
