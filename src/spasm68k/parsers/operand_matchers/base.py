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

import re

from spasm68k.models import Origin
from spasm68k.models.operands import Operand


class MatcherOfOperand:
    """
    Base class of any matcher of operand
    ---

    Defines the template methods to perform the matching, allows to implement a Strategy pattern.
    """

    def isMatchable(self, origin: Origin) -> bool:
        """
        # A quick assesment of whether the given origin could match or not

        * No more than 2 tests
        * Testing a length (either equal, minimal or maximal)
        * Testing either the first char or the last char

        @param origin: a segment + a line of code to parse.

        ## Returns

        **True** when an operand COULD be found with this matcher.
        """
        return False

    def matches(self, origin: Origin) -> Operand | None:
        """
        # Try to match an operand from the given origin.

        @param origin: a segment + a line of code to parse.

        ## Returns

        The operand found, or nothing.
        """
        if match := self._fullmatch(origin):
            return self._buildOperand(match, origin)
        return None

    def _fullmatch(self, origin: Origin) -> any:
        return None

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return None


class MatcherUsingPattern(MatcherOfOperand):

    @property
    def pattern(self) -> re.Pattern:
        pass

    def _fullmatch(self, origin: Origin) -> any:
        segment, lineOfCode = origin.segment, origin.lineOfCode
        return self.pattern.fullmatch(lineOfCode.content[segment.start : segment.end])
