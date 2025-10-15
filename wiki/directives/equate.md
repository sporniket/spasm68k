# Equate

**Requires** a label that is a valid [identifier](../identifier.md).

An equate directive instructs the compiler to map the label to the given litteral value.

Then, whenever the label is found in an operand, it is substituted with the value mapped to it.

**Regular form** : `equ`

**Variants** : `=`

## Examples

```asm
** with 'equ'
BIT_AND equ 0
BIT_OR  equ 1
BIT_NOT equ 2

** with '='
MAX_CHAR = 255
```