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

collectionsOfItems = {}
collectionsOfFactories = {}


def itemsOf(name: str) -> dict:
    return collectionsOfItems[name] if name in collectionsOfItems else {}


def factoriesOf(name: str) -> dict:
    return collectionsOfFactories[name] if name in collectionsOfFactories else {}


def itemOf(name: str):
    def _actual_itemOf(clazz: any):
        if name not in collectionsOfItems:
            collectionsOfItems[name] = {}
        collectionsOfItems[name][clazz.__qualname__] = clazz()
        return clazz

    return _actual_itemOf


def factoryOf(name: str):
    def _actual_factoryOf(clazz):
        if name not in collectionsOfFactories:
            collectionsOfFactories[name] = {}
        collectionsOfFactories[name][clazz.__qualname__] = clazz
        return clazz

    return _actual_factoryOf
