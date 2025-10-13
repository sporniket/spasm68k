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
from spasm68k.models.operands import (
    Operand,
    OperandDirectRegisterData,
    OperandDirectRegisterAddress,
    OperandIndirectRegisterAddress,
)
from .base import MatcherUsingPattern

ALIAS_STACK_POINTER = "sp"


class MatcherOfDirectRegisterData(MatcherUsingPattern):
    __matcher = re.compile("d([0-7])", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 2 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandDirectRegisterData(origin, int(match.group(1)))


class MatcherOfDirectStackPointer(MatcherUsingPattern):
    __matcher = re.compile("sp", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 2 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandDirectRegisterAddress(origin, 7, ALIAS_STACK_POINTER)


class MatcherOfDirectRegisterAddress(MatcherUsingPattern):
    __matcher = re.compile("a([0-7])", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 2 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandDirectRegisterAddress(origin, int(match.group(1)))


class MatcherOfIndirectRegisterAddress(MatcherUsingPattern):
    __matcher = re.compile("[(]a([0-7])[)]", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 4 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddress(origin, int(match.group(1)))


class MatcherOfIndirectStackPointer(MatcherUsingPattern):
    __matcher = re.compile("[(]sp[)]", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 4 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddress(origin, 7, ALIAS_STACK_POINTER)
