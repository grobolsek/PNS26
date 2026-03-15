"""lexer.

Provides the Lexer class for performing lexical analysis on source files.
This module breaks down raw source text into a stream of tokens.
"""

import re
from pathlib import Path
from typing import ClassVar

from common.report import Report
from common.token import Location, Token


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

    KEYWORDS: ClassVar[dict[str, Token.Symbol]] = {
        "if": Token.Symbol.IF,
        "for": Token.Symbol.FOR,
        "while": Token.Symbol.WHILE,
        "return": Token.Symbol.RETURN,
    }

    OPERATORS: ClassVar[dict[str, Token.Symbol]] = {
        "+": Token.Symbol.ADD,
        "-": Token.Symbol.SUB,
        "*": Token.Symbol.MUL,
        "/": Token.Symbol.DIV,
        "(": Token.Symbol.L_PRENTICES,
        ")": Token.Symbol.R_PRENTICES,
        "==": Token.Symbol.EQU,
        "=": Token.Symbol.ASSIGN,
    }

    def __init__(self, path: str | Path) -> None:
        """Initializes the Lexer with a file path and reads its content.

        Args:
            path: String or Path object pointing to the source file.
        """
        self.path = Path(path)
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

    def next_token(self) -> Token:  # noqa: C901, PLR0911, PLR0912
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
        text: str = ""

        # EOF
        if char == "":
            self.eof = True
            return Token(Token.Symbol.EOF, start_loc, "")

        # Digits
        if char.isdigit():
            # Okta and hex
            if char == "0":
                text += self._next_char()
                char = self._peek()

                # Hex
                if re.search(r"[xX]", char):
                    text += self._next_char()

                    while re.search(r"[0-9a-fA-F]", self._peek()):
                        text += self._next_char()

                    # 0x is not valid hex number
                    if len(text) <= 2:  # noqa: PLR2004
                        raise Report.CompilerSyntaxError(self.path, start_loc, text, "invalid hexadecimal int const")

                    end_loc = self._get_current_loc()
                    return Token(Token.Symbol.INT_CONST, Location.range(start_loc, end_loc), text)

                while re.search(r"[0-9]", self._peek()):
                    text += self._next_char()

                # 8 and 9 cant be in okta
                if re.search(r"[89]", text):
                    raise Report.CompilerSyntaxError(self.path, start_loc, text, "invalid okta int const")

                end_loc = self._get_current_loc()
                return Token(Token.Symbol.INT_CONST, Location.range(start_loc, end_loc), text)

            # Allows one dot for decimals
            pattern = r"[0-9.]"
            while re.search(pattern, self._peek()):
                text += self._next_char()

                # If dot is already present in text than do not count it anymore
                if "." in text:
                    pattern = r"[0-9]"

            end_loc = self._get_current_loc()
            return Token(Token.Symbol.INT_CONST, Location.range(start_loc, end_loc), text)

        # Check for identifiers, than check if it it a keyword
        if re.search(r"[a-zA-z_]", self._peek()):
            while re.search(r"[a-zA-z_0-9]", self._peek()):
                text += self._next_char()

            end_loc = self._get_current_loc()

            # Check for keywords
            symbol = self.KEYWORDS.get(text, Token.Symbol.IDENTIFIER)
            return Token(symbol, Location.range(start_loc, end_loc), text)

        # Operators
        if char in [op[0] for op in self.OPERATORS]:
            # Consume the first character
            text = self._next_char()

            # Peek at the next character to see if a 2-char operator exists
            potential_2char = text + self._peek()

            # Check if the 2-char is valid
            if potential_2char in self.OPERATORS:
                text = potential_2char
                self._next_char()
                return Token(self.OPERATORS[text], start_loc, text)

            # Check if the single char is valid
            if text in self.OPERATORS:
                return Token(self.OPERATORS[text], start_loc, text)

        raise Report.CompilerSyntaxError(self.path, start_loc, char, "Unknown character")


"""
lexer = Lexer("test.txt")
token = lexer.next_token()

while token.token is not Token.Symbol.EOF:
    print(token)
    token = lexer.next_token()
"""
