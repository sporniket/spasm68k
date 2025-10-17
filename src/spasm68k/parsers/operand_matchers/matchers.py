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

from class_collector import itemOf
from spasm68k.models import Origin, Segment
from spasm68k.models.operands import (
    Operand,
    OperandDirectRegisterData,
    OperandDirectRegisterAddress,
    OperandIndirectRegisterAddress,
    OperandIndirectRegisterAddressWithPostIncrement,
    OperandIndirectRegisterAddressWithPreDecrement,
    OperandIndirectRegisterAddressWithDisplacement,
)
from .base import MatcherUsingPattern

ALIAS_STACK_POINTER = "sp"


PATTERNS = {
    "litteral_binary": "(([%])|(0b))([01]+(_[01]+)*)",
    "litteral_octal": "((0)|(0o))([0-7]+(_[0-7]+)*)",
    "litteral_decimal": "((0d)([0-9]+(_[0-9]+)*))|([1-9][0-9]*(_[0-9]+)*)",
    "litteral_hexadecimal": "(([$])|(0x))([0-9a-f]+(_[0-9a-f]+)*)",
    "identifier_value": "[A-Za-z][_0-9A-Za-z]*",
}
"""Common patterns to match some parts of interest
---

Patterns for _litterals_ are **case insensitive**.

Patterns for _identifiers_ are **case sensitive**.
"""


def makeCombinedPatterns(keys: list[str] = []):
    return "|".join([PATTERNS[k] for k in keys])


PATTERNS_ANY_LITTERAL_NUMBER = makeCombinedPatterns(
    [f"litteral_{i}" for i in ["binary", "octal", "decimal", "hexadecimal"]]
)


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfDirectRegisterData(MatcherUsingPattern):
    __matcher = re.compile("d([0-7])", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 2 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandDirectRegisterData(origin, int(match.group(1)))


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfDirectStackPointer(MatcherUsingPattern):
    __matcher = re.compile("sp", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 2 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandDirectRegisterAddress(origin, 7, ALIAS_STACK_POINTER)


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfDirectRegisterAddress(MatcherUsingPattern):
    __matcher = re.compile("a([0-7])", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 2 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandDirectRegisterAddress(origin, int(match.group(1)))


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectRegisterAddress(MatcherUsingPattern):
    __matcher = re.compile("[(]a([0-7])[)]", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 4 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddress(origin, int(match.group(1)))


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectStackPointer(MatcherUsingPattern):
    __matcher = re.compile("[(]sp[)]", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 4 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddress(origin, 7, ALIAS_STACK_POINTER)


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectRegisterAddressWithPostIncrement(MatcherUsingPattern):
    __matcher = re.compile("[(]a([0-7])[)][+]", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 5 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddressWithPostIncrement(
            origin, int(match.group(1))
        )


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectStackPointerWithPostIncrement(MatcherUsingPattern):
    __matcher = re.compile("[(]sp[)][+]", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 5 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddressWithPostIncrement(
            origin, 7, ALIAS_STACK_POINTER
        )


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectRegisterAddressWithPredecrement(MatcherUsingPattern):
    __matcher = re.compile("[-][(]a([0-7])[)]", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 5 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddressWithPreDecrement(
            origin, int(match.group(1))
        )


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectStackPointerWithPrederement(MatcherUsingPattern):
    __matcher = re.compile("[-][(]sp[)]", re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) == 5 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddressWithPreDecrement(
            origin, 7, ALIAS_STACK_POINTER
        )


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectRegisterAddressWithDisplacement_Litteral(MatcherUsingPattern):
    __matcher = re.compile(
        "[(](?P<displacement>" + PATTERNS_ANY_LITTERAL_NUMBER + "),a(?P<a>[0-7])[)]",
        re.IGNORECASE,
    )

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) >= 6 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddressWithDisplacement(
            origin,
            int(match["a"]),
            displacement=Segment(
                match.start("displacement"), match.end("displacement")
            ),
        )


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectRegisterAddressWithDisplacement_Litteral_AltSyntax(
    MatcherUsingPattern
):
    __matcher = re.compile(
        "(?P<displacement>" + PATTERNS_ANY_LITTERAL_NUMBER + ")[(]a(?P<a>[0-7])[)]",
        re.IGNORECASE,
    )

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) >= 5 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddressWithDisplacement(
            origin,
            int(match["a"]),
            displacement=Segment(
                match.start("displacement"), match.end("displacement")
            ),
        )


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectRegisterAddressWithDisplacement_Identifier(MatcherUsingPattern):
    __matcher = re.compile(
        "[(](?P<displacement>" + PATTERNS["identifier_value"] + "),[aA](?P<a>[0-7])[)]",
    )

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) >= 6 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddressWithDisplacement(
            origin,
            int(match["a"]),
            displacement=Segment(
                match.start("displacement"), match.end("displacement")
            ),
        )


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectRegisterAddressWithDisplacement_Identifier_AltSyntax(
    MatcherUsingPattern
):
    __matcher = re.compile(
        "(?P<displacement>" + PATTERNS["identifier_value"] + ")[(][aA](?P<a>[0-7])[)]",
    )

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) >= 5 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddressWithDisplacement(
            origin,
            int(match["a"]),
            displacement=Segment(
                match.start("displacement"), match.end("displacement")
            ),
        )


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectStackPointerWithDisplacement_Litteral(MatcherUsingPattern):
    __matcher = re.compile(
        "[(](?P<displacement>" + PATTERNS_ANY_LITTERAL_NUMBER + "),sp[)]",
        re.IGNORECASE,
    )

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) >= 6 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddressWithDisplacement(
            origin,
            7,
            alias=ALIAS_STACK_POINTER,
            displacement=Segment(
                match.start("displacement"), match.end("displacement")
            ),
        )


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectStackPointeWithDisplacement_Litteral_AltSyntax(
    MatcherUsingPattern
):
    __matcher = re.compile(
        "(?P<displacement>" + PATTERNS_ANY_LITTERAL_NUMBER + ")[(]sp[)]",
        re.IGNORECASE,
    )

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) >= 5 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddressWithDisplacement(
            origin,
            7,
            alias=ALIAS_STACK_POINTER,
            displacement=Segment(
                match.start("displacement"), match.end("displacement")
            ),
        )


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectStackPointeWithDisplacement_Identifier(MatcherUsingPattern):
    __matcher = re.compile(
        "[(](?P<displacement>" + PATTERNS["identifier_value"] + "),[sS][pP][)]",
    )

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) >= 6 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddressWithDisplacement(
            origin,
            7,
            alias=ALIAS_STACK_POINTER,
            displacement=Segment(
                match.start("displacement"), match.end("displacement")
            ),
        )


@itemOf("spasm68k.parsers.operand_matchers")
class MatcherOfIndirectStackPointeWithDisplacement_Identifier_AltSyntax(
    MatcherUsingPattern
):
    __matcher = re.compile(
        "(?P<displacement>" + PATTERNS["identifier_value"] + ")[(][sS][pP][)]",
    )

    @property
    def pattern(self) -> re.Pattern:
        return self.__matcher

    def isMatchable(self, origin: Origin) -> bool:
        return True if len(origin.segment) >= 5 else False

    def _buildOperand(self, match: any, origin: Origin) -> Operand:
        return OperandIndirectRegisterAddressWithDisplacement(
            origin,
            7,
            alias=ALIAS_STACK_POINTER,
            displacement=Segment(
                match.start("displacement"), match.end("displacement")
            ),
        )
