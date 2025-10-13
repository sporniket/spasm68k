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

import pytest

from spasm68k.models import Origin, Segment, LineOfCode
from spasm68k.parsers.operand_matchers.base import MatcherOfOperand, MatcherUsingPattern


def test_MatcherOfOperand_default_behaviors():
    matcher = MatcherOfOperand()
    origin = Origin(Segment(1, 2), LineOfCode("never", 0, "mind"))
    assert matcher.isMatchable(origin) is False
    assert matcher.matches(origin) is None
    assert matcher._fullmatch(origin) is None
    assert matcher._buildOperand("whatever", origin) is None


def test_MatcherUsingPattern_default_behaviors():
    matcher = MatcherUsingPattern()
    origin = Origin(Segment(1, 2), LineOfCode("never", 0, "mind"))
    assert matcher.isMatchable(origin) is False
    assert matcher.pattern is None
    with pytest.raises(AttributeError) as error:
        matcher.matches(origin)
    assert "'NoneType' object has no attribute 'fullmatch'" in str(error.value)
