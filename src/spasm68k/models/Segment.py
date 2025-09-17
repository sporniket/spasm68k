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
class Segment:
    start: int  # starting position (included) >= 0
    end: int  # ending position (excluded) > start

    @property
    def valid(self) -> bool:
        return self.start > 0 and self.end > self.start

    def __bool__(self) -> bool:
        return self.valid

    def __len__(self) -> int:
        return self.end - self.start if self.valid else 0
