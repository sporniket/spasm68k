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

from class_collector import itemsOf
from spasm68k.models import LineOfCode, Segment, Origin
from spasm68k.models.operands import (
    Operand,
    OperandUnsupported,
)

from .operand_matchers import (
    MatcherOfDirectRegisterAddress,
    MatcherOfDirectRegisterData,
    MatcherOfDirectStackPointer,
    MatcherOfIndirectRegisterAddress,
    MatcherOfIndirectStackPointer,
)


class OperandParser:
    __matchers = itemsOf("spasm68k.parsers.operand_matchers").values()

    def parse(self, segment: Segment, lineOfCode: LineOfCode) -> Operand:
        origin = Origin(segment, lineOfCode)
        for m in self.__matchers:
            if m.isMatchable(origin) and (op := m.matches(origin)):
                return op
        return OperandUnsupported(origin)
