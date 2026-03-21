"""report.

Provides error reporting mechanisms for the compiler.
"""

import linecache
from pathlib import Path

# Fix: Import Token directly from the sibling module to avoid the circular loop
from .token import Token


class Report:
    """A container for compiler error reporting and diagnostics."""

    class CompilerSyntaxError(Exception):
        """Raised when the Lexer or Parser encounters invalid syntax."""

        # Use Token.Location for the type hint
        def __init__(self, file: Path, token: Token, message: str) -> None:
            """Initializes the syntax error with contextual file and position data.

            Args:
                file: Path to the source file where the error occurred.
                token: Token where error occurred.
                message: A descriptive explanation of what went wrong.
            """
            source_line = linecache.getline(str(file), token.location.beg_line).rstrip()

            # Formatting the error message
            formatted_msg = f"File {file}, at: {token.location}\n\t{source_line}\n\t{(token.location.beg_column - 1) * ' '}^\n{message}"
            super().__init__(formatted_msg)
