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

from dataclasses import dataclass


@dataclass
class LineOfCode:
    sourceFile: (
        str  # the path of the source file, usually relative to the working directory
    )
    lineNumber: int  # 0-based
    content: str  # the actual content, no stripping of leading/trailing whitespaces


class LineOfCodeLoader:
    def read(self, filename: str) -> list[LineOfCode]:
        with open(filename) as src:
            lines = src.readlines()
            return list(
                map(lambda e: LineOfCode(filename, e[0], e[1]), enumerate(lines))
            )
        return []
