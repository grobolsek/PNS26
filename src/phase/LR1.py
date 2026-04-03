"""syntax.

Provides a RL(1) parser and generating syntax error reports.
"""  # noqa: N999

from pathlib import Path

from common import NonTerminal as NT  # noqa: N817
from common import Report, Terminal, Token
from common.lr1_table import Table
from phase.lexer import Lexer


class Syntax:
    """A RL(1) parser.

    This class orchestrates the Lexer to consume tokens and validates them against
    the language rules for expressions, terms, and factors.
    """

    def __init__(self, file: str | Path) -> None:
        """Initializes the parser with a source file and primes the first token.

        Args:
            file: The path to the source file to be parsed.
        """
        self.file = Path(file)
        self.lexer = Lexer(file)
        self.current_token: Token = self.lexer.next_token()
        self.stack: list[int] = [0]
        self.table = Table(self._shift, self._reduce, self._accept)

    def parse(self) -> None:
        """Starts the parsing process from the entry point (Expression).

        Raises:
            CompilerSyntaxError: If the input does not conform to the grammar or
                                 if there is trailing junk after a valid expression.
        """
        try:
            while True:
                state = self.stack[-1]
                symbol = self.current_token.symbol
                action = self.table.action.get((state, symbol))
                if action is None:
                    raise self._error() from None
                action()
        except StopIteration:
            pass
        except Report.CompilerSyntaxError as e:
            print(f"\033[1;31m{e}\033[0m")  # noqa: T201

    def _shift(self, state: int) -> None:
        self.stack.append(state)
        self.current_token = self.lexer.next_token()

    def _reduce(self, lhs: NT, rhs: list[NT | Terminal]) -> None:
        print(f"{lhs} -> {' '.join(str(s) for s in rhs)}")  # noqa: T201

        for _ in range(len(rhs)):
            self.stack.pop()

        exposed_state = self.stack[-1]
        next_state = self.table.goto.get((exposed_state, lhs))
        if next_state is None:
            raise self._error() from None

        self.stack.append(next_state)

    def _accept(self) -> None:
        raise StopIteration

    def _error(self) -> Report.CompilerSyntaxError:
        return Report.CompilerSyntaxError(self.file, self.current_token, "Invalid operation")


syntax = Syntax("a.txt")
syntax.parse()
