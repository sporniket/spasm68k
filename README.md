# spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA

![PyPI - Version](https://img.shields.io/pypi/v/spasm68k-by-sporniket)
![PyPI - License](https://img.shields.io/pypi/l/spasm68k-by-sporniket)


> [WARNING] Please read carefully this note before using this project. It contains important facts.

Content

1. What is **spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA**, and when to use it ?
2. What should you know before using **spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA** ?
3. How to use **spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA** ?
4. Known issues
5. Miscellanous

## 1. What is **spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA**, and when to use it ?

**spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA** is a collection of tools for assembly language, targeting the 'Motorola 68000' Instruction Set Architecture (ISA).

This Instruction Set Architecture was designed by a manufacturer that was known as
'Motorola' in the 1980~2000 period. At the time of writing (2025-09-13), this
manufacturer is now known as 'NXP'.

### Licence
 **spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA** is free software: you can redistribute it and/or modify it under the terms of the
 GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your
 option) any later version.

 **spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA** is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
 more details.

 You should have received a copy of the GNU General Public License along with **spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA**.
 If not, see http://www.gnu.org/licenses/ .


## 2. What should you know before using **spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA** ?

> **SECURITY WARNING** : **spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA** is a set of tools for manipulating files, and thus WILL allows attacks on the files systems. Do not install this project on servers.

**spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA** is written in [Python](http://python.org) language, version 3.10 or above.

> Do not use **spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA** if this project is not suitable for your project

## 3. How to use **spasm68k -- SPorniket's tools for ASseMbly targeting m68k ISA** ?

### Requirements

Python 3.8 or later versions, `pip3` and `pdm` are required.

### From source

To get the latest available code, one must clone the git repository, build and install to the maven local repository.

	git clone https://github.com/sporniket/spasm68k.git
	cd spasm68k
	pdm build
    sudo pip3 install dist/spasm68k_by_sporniket-<version>-py3-none-any.whl

### From Pypi
Add any of the following dependencies that are appropriate to your project.

```
sudo pip3 install spasm68k_by_sporniket
```

## 4. Known issues
See the [project issues](https://github.com/sporniket/spasm68k/issues) page.

## 5. Miscellanous

### Report issues
Use the [project issues](https://github.com/sporniket/spasm68k/issues) page.
