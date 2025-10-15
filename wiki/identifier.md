# Identifier

_Identifiers are case sensitive, **no exception**._

## Valid identifier for referencing a value

An identifier is the label in a line holding an _equate_ statement.

```asm
my_value: equ 0d0001
```

An identifier starts with a letter (`a` to `z`, lower or upper case), followed by any char among letters (`a` to `z`, lower or upper case), digits (`0` to `9`) and `_`. E.g. `what`, `iAmIn2_Places`, `I_believe_I_can_fly`.

**Regular expression :** `[A-Za-z][_0-9A-Za-z]*`