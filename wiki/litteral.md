# Litteral value

## Integer value

_The provided regular expressions are crafted so that the group capturing the prefix the group capturing the value have the same parent_

### Binary notation

A prefix among `[%,0b]` (case insensitive) followed by any number of binary digits (`0` to `1`), with optional visual separation using `_` in the middle (the first and last position MUST be digits, e.g. `0b1111_1100`)

**Regular expression :** `(([%])|(0b))([01]+(_[01]+)*)` (case insensitive)

### Octal notation

* A prefix among `[0,0o]` (case insensitive) followed by any number of octal digits (`0` to `7`), with optional visual separation using `_` in the middle (the first and last position MUST be digits, e.g. `0o123_4567`)

**Regular expression :** `((0)|(0o))([0-7]+(_[0-7]+)*)` (case insensitive)

### Decimal notation

* A prefix `[0d]` (case insensitive) followed by any number of decimal digits (`0` to `9`), with optional visual separation using `_` in the middle (the first and last position MUST be digits, e.g. `0d12_345_678`) ; _this form of decimal litteral allows to write 0-padded values, e.g `0d0001`)
* A non-zero digit (`1` to `9`) followed by any number of decimal digits (`0` to `9`), with optional visual separation using `_` in the middle (the first and last position MUST be digits, e.g. `12_345_678`)

**Regular expression :** `((0d)([0-9]+(_[0-9]+)*))|([1-9][0-9]*(_[0-9]+)*)` (case insensitive)

### Hexadecimal notation
* A prefix among `[$,0x]` (case insensitive) followed by any number of hexadecimal digits (`0` to `9`, `a` to `f` case insensitive), with optional visual separation using `_` in the middle (the first and last position MUST be digits, e.g. `0xff_32_ab`)

**Regular expression :** `(([$])|(0x))([0-9a-f]+(_[0-9a-f]+)*)` (case insensitive)
