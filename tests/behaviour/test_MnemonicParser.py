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

from spasm68k.parsers import MnemonicParser
from spasm68k.models.mnemonics import DirectiveInvocation


def test_that__MnemonicParser_parse__recognizes_directives():
    mnemonic = MnemonicParser().parse("albus.dumbledor")

    assert type(mnemonic) is DirectiveInvocation
    assert mnemonic.name == "albus"
    assert mnemonic.suffix == "dumbledor"
    assert mnemonic.mnemonicField == "albus.dumbledor"


def test_that__MnemonicParser_parse__recognizes_directives_without_suffixes():
    mnemonic = MnemonicParser().parse("albus")

    assert type(mnemonic) is DirectiveInvocation
    assert mnemonic.name == "albus"
    assert mnemonic.suffix == ""
    assert mnemonic.mnemonicField == "albus"


def test_that__MnemonicParser_parse__recognizes_directives_case_insensitive():
    mnemonic = MnemonicParser().parse("aLbUs.DuMbLeDoR")

    assert type(mnemonic) is DirectiveInvocation
    assert mnemonic.name == "albus"
    assert mnemonic.suffix == "dumbledor"
    assert mnemonic.mnemonicField == "albus.dumbledor"
