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

from spasm68k.parsers import OperandSplitter


def test_that_it_WILL_separate_operands():
    source = "a,b,c,d"
    operands = OperandSplitter().split(source)

    assert len(operands) == 4
    assert source[operands[0].start : operands[0].end] == "a"
    assert source[operands[1].start : operands[1].end] == "b"
    assert source[operands[2].start : operands[2].end] == "c"
    assert source[operands[3].start : operands[3].end] == "d"


def test_that_it_WILL_ignore_commas_in_strings_double_quotes():
    source = '"a,b,"c,d'
    operands = OperandSplitter().split(source)

    assert len(operands) == 2
    assert source[operands[0].start : operands[0].end] == '"a,b,"c'
    assert source[operands[1].start : operands[1].end] == "d"


def test_that_it_WILL_ignore_commas_in_strings_single_quotes():
    source = "'a,b,'c,d"
    operands = OperandSplitter().split(source)

    assert len(operands) == 2
    assert source[operands[0].start : operands[0].end] == "'a,b,'c"
    assert source[operands[1].start : operands[1].end] == "d"


def test_that_it_WILL_ignore_commas_in_parenthesis():
    source = "(a,b,)c,d"
    operands = OperandSplitter().split(source)

    assert len(operands) == 2
    assert source[operands[0].start : operands[0].end] == "(a,b,)c"
    assert source[operands[1].start : operands[1].end] == "d"


def test_that_it_WILL_ignore_commas_in_nested_parenthesis():
    source = "((a,)b,)c,d"
    operands = OperandSplitter().split(source)

    assert len(operands) == 2
    assert source[operands[0].start : operands[0].end] == "((a,)b,)c"
    assert source[operands[1].start : operands[1].end] == "d"


def test_that_it_WILL_ignore_prioritize_strings_over_parenthesis():
    source = "'((a,)'b,)c,d"
    operands = OperandSplitter().split(source)

    assert len(operands) == 3
    assert source[operands[0].start : operands[0].end] == "'((a,)'b"
    assert source[operands[1].start : operands[1].end] == ")c"
    assert source[operands[2].start : operands[2].end] == "d"


def test_that_it_WILL_supports_strings_in_parenthesis():
    source = "(('a,')b,)c,d"
    operands = OperandSplitter().split(source)

    assert len(operands) == 2
    assert source[operands[0].start : operands[0].end] == "(('a,')b,)c"
    assert source[operands[1].start : operands[1].end] == "d"
