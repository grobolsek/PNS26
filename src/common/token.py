"""token.

Defines the data structures used to represent lexical units (Tokens)
and their physical positions within a source file (Location).
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Self


@dataclass(frozen=True)
class Token:
    """Represents a single lexical token."""

    class Symbol(Enum):
        """The type of the token."""

        INT_CONST = auto()
        STR_CONST = auto()

        IDENTIFIER = auto()

        ADD = auto()
        SUB = auto()
        MUL = auto()
        DIV = auto()

        EQU = auto()
        ASSIGN = auto()

        L_PRENTICES = auto()
        R_PRENTICES = auto()
        L_C_PRENTICES = auto()
        R_C_PRENTICES = auto()
        SEMICOLON = auto()

        IF = auto()
        FOR = auto()
        WHILE = auto()
        RETURN = auto()

        EOF = auto()

    token: Symbol
    location: "Location"
    actual: str

    def __str__(self) -> str:
        """Returns a string representation of the token."""
        return f'({self.token.name}, {self.location}, "{self.actual}")'


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
    def range(cls, start: "Location", end: "Location") -> Self:
        """Creates a location spanning from the start of one to the end of another."""
        return cls(start.beg_line, start.beg_column, end.end_line, end.end_column)

    def __str__(self) -> str:
        """Returns representation of the line/column range."""
        if self.beg_line == self.end_line and self.beg_column == self.end_column:
            return f"{self.beg_line}:{self.beg_column}"
        return f"{self.beg_line}:{self.beg_column}-{self.end_line}:{self.end_column}"
