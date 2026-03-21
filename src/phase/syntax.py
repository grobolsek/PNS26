from pathlib import Path  # noqa: D100

from common import Report, Symbol, Token
from phase.lexer import Lexer

"""syntax.

Provides a recursive LL(1) parser and generating syntax error reports.
"""


class Syntax:
    """A recursive LL(1) parser.

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

    def parse(self) -> None:
        """Starts the parsing process from the entry point (Expression).

        Raises:
            CompilerSyntaxError: If the input does not conform to the grammar or
                                 if there is trailing junk after a valid expression.
        """
        self._parse_e()

        # Check for trailing tokens after the expression finishes
        if self._peek() != Symbol.EOF:
            raise self._error()

    def _parse_e(self) -> None:
        match self._peek():
            case Symbol.INT_CONST | Symbol.IDENTIFIER | Symbol.L_PRENTICES:
                self._parse_t()
                self._parse_e2()
            case _:
                self._error()

    def _parse_e2(self) -> None:
        match self._peek():
            case Symbol.ADD | Symbol.SUB:
                self._take(self._peek())
                self._parse_t()
                self._parse_e2()
            case _:
                return  # Epsilon

    def _parse_t(self) -> None:
        match self._peek():
            case Symbol.INT_CONST | Symbol.IDENTIFIER | Symbol.L_PRENTICES:
                self._parse_f()
                self._parse_t2()
            case _:
                raise self._error()

    def _parse_t2(self) -> None:
        match self._peek():
            case Symbol.MUL | Symbol.DIV:
                self._take(self._peek())
                self._parse_f()
                self._parse_t2()
            case _:
                return  # Epsilon

    def _parse_f(self) -> None:
        match self._peek():
            case Symbol.INT_CONST | Symbol.IDENTIFIER:
                self._take(self._peek())
            case Symbol.L_PRENTICES:
                self._take(Symbol.L_PRENTICES)
                self._parse_e()
                self._take(Symbol.R_PRENTICES)
            case _:
                raise self._error()

    def _peek(self) -> Symbol:
        return self.current_token.symbol

    def _take(self, symbol: Symbol) -> None:
        if self._peek() == symbol:
            self.current_token = self.lexer.next_token()
            return
        raise self._error()

    def _error(self) -> Report.CompilerSyntaxError:
        return Report.CompilerSyntaxError(self.file, self.current_token, "Invalid operation")
