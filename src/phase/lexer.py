"""lexer.

Provides the Lexer class for performing lexical analysis on source files.
This module breaks down raw source text into a stream of tokens.
"""

from pathlib import Path
from typing import ClassVar

from common import Location, Report, Symbol, Token


class Lexer:
    """A lexical analyzer that scans source code and produces tokens.

    The Lexer maintains a pointer to the current position in the source file
    and tracks line and column numbers.

    Attributes:
        path (Path): The path to the source file being analyzed.
        source (str): The full content of the source file.
        offset (int): The current character index in the source string.
        line (int): The current line number (1-indexed).
        column (int): The current column number (1-indexed).
    """

    KEYWORDS: ClassVar[dict[str, Symbol]] = {}

    OPERATORS: ClassVar[dict[str, Symbol]] = {
        "+": Symbol.ADD,
        "-": Symbol.SUB,
        "*": Symbol.MUL,
        "/": Symbol.DIV,
        "(": Symbol.L_PAREN,
        ")": Symbol.R_PAREN,
    }

    def __init__(self, file: str | Path) -> None:
        """Initializes the Lexer with a file path and reads its content.

        Args:
            file: String or Path object pointing to the source file.
        """
        self.path = Path(file)
        self.source = self.path.read_text()
        self.offset = 0

        # Track the current state
        self.line = 1
        self.column = 1

    def _get_current_loc(self) -> Location:
        """Returns a snapshot of the current line and column.

        Returns:
            Location: An object representing the current point in the source.
        """
        return Location.point(self.line, self.column)

    def _peek(self) -> str:
        """Looks at the current character without advancing the offset.

        Returns:
            str: The character at the current offset, or an empty string if EOF.
        """
        return self.source[self.offset] if self.offset < len(self.source) else ""

    def _next_char(self) -> str:
        """Consumes and returns the current character, advancing the internal state.

        Updates the line and column counters based on the character consumed.

        Returns:
            str: The character that was consumed.
        """
        char = self._peek()
        self.offset += 1

        if char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        return char

    def next_token(self) -> Token:
        """Scans the source and returns the next valid Token.

        Returns:
            Token: The next token found in the source.

        Raises:
            Report.SyntaxError: If an invalid character sequence or constant is found.
        """
        # Skip whitespaces
        while self._peek().isspace():
            self._next_char()

        # set starting location
        start_loc = self._get_current_loc()

        char = self._peek()
        buffer: str = ""

        # EOF
        if char == "":
            self.eof = True
            return Token(Symbol.EOF, start_loc, "")

        # Digits
        if char.isdigit():
            while self._peek().isdigit():
                buffer += self._next_char()

            location = Location.range(start_loc, self._get_current_loc())
            return Token(Symbol.INT_CONST, location, buffer)

        # Check for identifiers
        if char.isalpha() or char == "_":
            while self._peek().isalnum() or self._peek() == "_":
                buffer += self._next_char()

            location = Location.range(start_loc, self._get_current_loc())
            return Token(Symbol.IDENTIFIER, location, buffer)

        # Operators
        if char in [op[0] for op in self.OPERATORS]:
            # Consume the first character
            buffer = self._next_char()

            # Check if the single char is valid
            if buffer in self.OPERATORS:
                return Token(self.OPERATORS[buffer], start_loc, buffer)

        raise Report.CompilerSyntaxError(self.path, Token(Symbol.UNKNOWN, start_loc, buffer), "Unknown character")
