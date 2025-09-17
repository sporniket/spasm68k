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

from spasm68k.models import Segment


def test_that_it_MUST_be_valid():
    assert not Segment(-6, -1)
    assert not Segment(-1, 6)
    assert not Segment(6, 1)
    assert not Segment(2, 2)
    assert Segment(1, 6)


def test_that_it_WILL_have_a_length():
    assert len(Segment(1, 6)) == 5


def test_that_it_WILL_have_a_zero_length_when_invalid():
    assert len(Segment(-6, -1)) == 0
    assert len(Segment(-1, 6)) == 0
    assert len(Segment(6, 1)) == 0
    assert len(Segment(2, 2)) == 0
