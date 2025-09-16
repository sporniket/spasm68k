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
from spasm68k.models.mnemonics import (
    DirectiveInvocation,
    InstructionInvocation,
    MacroInvocation,
    UnknownInvocation,
)


class RegistryOfMacros:
    def __init__(self):
        self._registered = []

    def register(self, name: str):
        if name not in self._registered:
            self._registered.append(name)
        pass

    def isRegistered(self, name: str) -> bool:
        return name in self._registered


@dataclass
class MnemonicParserConfiguration:
    directives: list[str]
    instructions: list[str]
    macroRegistry: RegistryOfMacros


class MnemonicParser:
    def __init__(self, configuration: MnemonicParserConfiguration):
        self._configuration = (
            configuration
            if configuration is not None
            else MnemonicParserConfiguration([], [], RegistryOfMacros())
        )

    def parse(self, mnemonicField: str):
        parts = mnemonicField.lower().split(".", 1)
        if len(parts) < 2:
            parts += [""]
        if self.isDirective(parts):
            return DirectiveInvocation(*parts)
        elif self.isInstruction(parts):
            return InstructionInvocation(*parts)
        elif self.isRegisteredMacro(mnemonicField):
            return MacroInvocation(mnemonicField)
        else:
            return UnknownInvocation(mnemonicField)

    def isRegisteredMacro(self, mnemonicField):
        return self._configuration.macroRegistry.isRegistered(mnemonicField)

    def isInstruction(self, parts):
        return parts[0] in self._configuration.instructions

    def isDirective(self, parts):
        return parts[0] in self._configuration.directives
