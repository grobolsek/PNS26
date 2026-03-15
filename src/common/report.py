"""report.

Provides error reporting mechanisms for the compiler.
"""

from pathlib import Path

from common.token import Location


class Report:
    """A container for compiler error reporting and diagnostics."""

    class CompilerSyntaxError(Exception):
        """Raised when the Lexer or Parser encounters invalid syntax."""

        def __init__(self, file: Path | str, location: Location, text: str, message: str) -> None:
            """Initializes the syntax error with contextual file and position data.

            Args:
                file: Path to the source file where the error occurred.
                location: The Location object (point or range) of the error.
                text: The specific text snippet that caused the error.
                message: A descriptive explanation of what went wrong.
            """
            formatted_msg = f"File {file}, at: {location}\n\t{text}\n{message}"
            super().__init__(formatted_msg)
