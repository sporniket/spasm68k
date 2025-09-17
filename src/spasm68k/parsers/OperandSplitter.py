from spasm68k.models import Segment

PARENTHESIS = {"(": ")"}
QUOTES = ["'", '"']


class OperandSplitter:

    def split(self, operandsField: str) -> list[Segment]:
        operands = []
        start = 0
        accumulator = start
        quote = ""
        waitParenthesis = []
        for i, c in enumerate(operandsField):
            # Being in quote is primary
            if len(quote):
                accumulator += 1
                if c == quote:
                    quote = ""
            elif c in QUOTES:
                accumulator += 1
                quote = c

            # Not being in quote, be aware of parenthesis - with nesting
            elif c in PARENTHESIS:
                accumulator += 1
                waitParenthesis += [PARENTHESIS[c]]
            elif len(waitParenthesis):
                accumulator += 1
                if c == waitParenthesis[-1]:
                    del waitParenthesis[-1]

            # No special context
            elif c == ",":
                operands += [Segment(start, i)]
                start = i + 1
            else:
                accumulator += 1

        if start < len(operandsField):
            operands += [Segment(start, len(operandsField))]
        return operands
