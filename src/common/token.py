"""token.

Defines the data structures used to represent lexical units (Tokens)
and their physical positions within a source file (Location).
"""

from dataclasses import dataclass
from enum import Enum
from typing import Self


class Symbol(Enum):
    """The type of the token."""

    INT_CONST = "int"
    STR_CONST = "str"
    IDENTIFIER = "id"
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    L_PAREN = "("
    R_PAREN = ")"
    EOF = "$"
    UNKNOWN = "?"

    def __str__(self) -> str:  # noqa: D105
        return self.value


class NonTerminal(Enum):
    """The type of the non terminal."""

    E = "E"
    T = "T"
    F = "F"

    def __str__(self) -> str:  # noqa: D105
        return self.value


@dataclass(frozen=True)
class Token:
    """Represents a single lexical token."""

    @dataclass(frozen=True)
    class Location:
        """Represents a range of positions within a source file."""

        beg_line: int
        beg_column: int
        end_line: int
        end_column: int

        @classmethod
        def point(cls, line: int, col: int) -> Self:
            """Creates a location representing a single character position."""
            return cls(line, col, line, col)

        @classmethod
        def range(cls, start: "Token.Location", end: "Token.Location") -> Self:
            """Creates a location spanning from the start of one to the end of another."""
            return cls(start.beg_line, start.beg_column, end.end_line, end.end_column)

        def __str__(self) -> str:
            """Returns representation of the line/column range."""
            if self.beg_line == self.end_line and self.beg_column == self.end_column:
                return f"{self.beg_line}:{self.beg_column}"
            return f"{self.beg_line}:{self.beg_column}-{self.end_line}:{self.end_column}"

    symbol: Symbol
    location: "Location"
    lexeme: str

    def __str__(self) -> str:
        """Returns a string representation of the token."""
        return f'({self.symbol.name}, {self.location}, "{self.lexeme}")'
