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

from spasm68k.parsers import (
    MnemonicParser,
    MnemonicParserConfiguration,
    RegistryOfMacros,
)
from spasm68k.models.mnemonics import DirectiveInvocation, InstructionInvocation

DIRECTIVES = ["albus", "severus"]
INSTRUCTIONS = ["harry", "hermione", "ron"]


def makeConfiguration():
    return MnemonicParserConfiguration(DIRECTIVES, INSTRUCTIONS, RegistryOfMacros())


def test_that__MnemonicParser_parse__recognizes_directives():
    # prepare and execute
    mnemonic = MnemonicParser(makeConfiguration()).parse("albus.dumbledor")

    # verify
    assert type(mnemonic) is DirectiveInvocation
    assert mnemonic.name == "albus"
    assert mnemonic.suffix == "dumbledor"
    assert mnemonic.mnemonicField == "albus.dumbledor"


def test_that__MnemonicParser_parse__recognizes_directives_without_suffixes():
    # prepare and execute
    mnemonic = MnemonicParser(makeConfiguration()).parse("albus")

    # verify
    assert type(mnemonic) is DirectiveInvocation
    assert mnemonic.name == "albus"
    assert mnemonic.suffix == ""
    assert mnemonic.mnemonicField == "albus"


def test_that__MnemonicParser_parse__recognizes_directives_case_insensitive():
    # prepare and execute
    mnemonic = MnemonicParser(makeConfiguration()).parse("aLbUs.DuMbLeDoR")

    # verify
    assert type(mnemonic) is DirectiveInvocation
    assert mnemonic.name == "albus"
    assert mnemonic.suffix == "dumbledor"
    assert mnemonic.mnemonicField == "albus.dumbledor"


def test_that__MnemonicParser_parse__recognizes_instructions():
    # prepare and execute
    mnemonic = MnemonicParser(makeConfiguration()).parse("harry.potter")

    # verify
    assert type(mnemonic) is InstructionInvocation
    assert mnemonic.name == "harry"
    assert mnemonic.suffix == "potter"
    assert mnemonic.mnemonicField == "harry.potter"


def test_that__MnemonicParser_parse__recognizes_instructions_without_suffixes():
    # prepare and execute
    mnemonic = MnemonicParser(makeConfiguration()).parse("harry")

    # verify
    assert type(mnemonic) is InstructionInvocation
    assert mnemonic.name == "harry"
    assert mnemonic.suffix == ""
    assert mnemonic.mnemonicField == "harry"


def test_that__MnemonicParser_parse__recognizes_instructions_case_insensitive():
    # prepare and execute
    mnemonic = MnemonicParser(makeConfiguration()).parse("HarrY.PotteR")

    # verify
    assert type(mnemonic) is InstructionInvocation
    assert mnemonic.name == "harry"
    assert mnemonic.suffix == "potter"
    assert mnemonic.mnemonicField == "harry.potter"
