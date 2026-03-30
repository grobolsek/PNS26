from collections.abc import Callable  # noqa: D100

from common import NonTerminal as NT  # noqa: N817
from common import Symbol


class Table:
    """Table for LR1."""

    def __init__(  # noqa: D107
        self,
        shift: Callable[[int], None],
        reduce: Callable[[NT, list[NT | Symbol]], None],
        accept: Callable,
    ) -> None:
        self.action: dict[tuple[int, Symbol], Callable] = {
            # State 0
            (0, Symbol.L_PAREN): lambda: shift(4),
            (0, Symbol.INT_CONST): lambda: shift(5),
            (0, Symbol.IDENTIFIER): lambda: shift(6),
            # State 1
            (1, Symbol.ADD): lambda: shift(7),
            (1, Symbol.SUB): lambda: shift(8),
            (1, Symbol.EOF): accept,
            # State 2
            (2, Symbol.ADD): lambda: reduce(NT.E, [NT.T]),
            (2, Symbol.SUB): lambda: reduce(NT.E, [NT.T]),
            (2, Symbol.MUL): lambda: shift(9),
            (2, Symbol.DIV): lambda: shift(10),
            (2, Symbol.EOF): lambda: reduce(NT.E, [NT.T]),
            # State 3
            (3, Symbol.ADD): lambda: reduce(NT.T, [NT.F]),
            (3, Symbol.SUB): lambda: reduce(NT.T, [NT.F]),
            (3, Symbol.MUL): lambda: reduce(NT.T, [NT.F]),
            (3, Symbol.DIV): lambda: reduce(NT.T, [NT.F]),
            (3, Symbol.EOF): lambda: reduce(NT.T, [NT.F]),
            # State 4
            (4, Symbol.L_PAREN): lambda: shift(14),
            (4, Symbol.INT_CONST): lambda: shift(15),
            (4, Symbol.IDENTIFIER): lambda: shift(16),
            # State 5
            (5, Symbol.ADD): lambda: reduce(NT.F, [Symbol.INT_CONST]),
            (5, Symbol.SUB): lambda: reduce(NT.F, [Symbol.INT_CONST]),
            (5, Symbol.MUL): lambda: reduce(NT.F, [Symbol.INT_CONST]),
            (5, Symbol.DIV): lambda: reduce(NT.F, [Symbol.INT_CONST]),
            (5, Symbol.EOF): lambda: reduce(NT.F, [Symbol.INT_CONST]),
            # State 6
            (6, Symbol.ADD): lambda: reduce(NT.F, [Symbol.IDENTIFIER]),
            (6, Symbol.SUB): lambda: reduce(NT.F, [Symbol.IDENTIFIER]),
            (6, Symbol.MUL): lambda: reduce(NT.F, [Symbol.IDENTIFIER]),
            (6, Symbol.DIV): lambda: reduce(NT.F, [Symbol.IDENTIFIER]),
            (6, Symbol.EOF): lambda: reduce(NT.F, [Symbol.IDENTIFIER]),
            # State 7
            (7, Symbol.L_PAREN): lambda: shift(4),
            (7, Symbol.INT_CONST): lambda: shift(5),
            (7, Symbol.IDENTIFIER): lambda: shift(6),
            # State 8
            (8, Symbol.L_PAREN): lambda: shift(4),
            (8, Symbol.INT_CONST): lambda: shift(5),
            (8, Symbol.IDENTIFIER): lambda: shift(6),
            # State 9
            (9, Symbol.L_PAREN): lambda: shift(4),
            (9, Symbol.INT_CONST): lambda: shift(5),
            (9, Symbol.IDENTIFIER): lambda: shift(6),
            # State 10
            (10, Symbol.L_PAREN): lambda: shift(4),
            (10, Symbol.INT_CONST): lambda: shift(5),
            (10, Symbol.IDENTIFIER): lambda: shift(6),
            # State 11
            (11, Symbol.ADD): lambda: shift(22),
            (11, Symbol.SUB): lambda: shift(23),
            (11, Symbol.R_PAREN): lambda: shift(21),
            # State 12
            (12, Symbol.ADD): lambda: reduce(NT.E, [NT.T]),
            (12, Symbol.SUB): lambda: reduce(NT.E, [NT.T]),
            (12, Symbol.MUL): lambda: shift(24),
            (12, Symbol.DIV): lambda: shift(25),
            (12, Symbol.R_PAREN): lambda: reduce(NT.E, [NT.T]),
            # State 13
            (13, Symbol.ADD): lambda: reduce(NT.T, [NT.F]),
            (13, Symbol.SUB): lambda: reduce(NT.T, [NT.F]),
            (13, Symbol.MUL): lambda: reduce(NT.T, [NT.F]),
            (13, Symbol.DIV): lambda: reduce(NT.T, [NT.F]),
            (13, Symbol.R_PAREN): lambda: reduce(NT.T, [NT.F]),
            # State 14
            (14, Symbol.L_PAREN): lambda: shift(14),
            (14, Symbol.INT_CONST): lambda: shift(15),
            (14, Symbol.IDENTIFIER): lambda: shift(16),
            # State 15
            (15, Symbol.ADD): lambda: reduce(NT.F, [Symbol.INT_CONST]),
            (15, Symbol.SUB): lambda: reduce(NT.F, [Symbol.INT_CONST]),
            (15, Symbol.MUL): lambda: reduce(NT.F, [Symbol.INT_CONST]),
            (15, Symbol.DIV): lambda: reduce(NT.F, [Symbol.INT_CONST]),
            (15, Symbol.R_PAREN): lambda: reduce(NT.F, [Symbol.INT_CONST]),
            # State 16
            (16, Symbol.ADD): lambda: reduce(NT.F, [Symbol.IDENTIFIER]),
            (16, Symbol.SUB): lambda: reduce(NT.F, [Symbol.IDENTIFIER]),
            (16, Symbol.MUL): lambda: reduce(NT.F, [Symbol.IDENTIFIER]),
            (16, Symbol.DIV): lambda: reduce(NT.F, [Symbol.IDENTIFIER]),
            (16, Symbol.R_PAREN): lambda: reduce(NT.F, [Symbol.IDENTIFIER]),
            # State 17
            (17, Symbol.ADD): lambda: reduce(NT.E, [NT.E, Symbol.ADD, NT.T]),
            (17, Symbol.SUB): lambda: reduce(NT.E, [NT.E, Symbol.ADD, NT.T]),
            (17, Symbol.MUL): lambda: shift(9),
            (17, Symbol.DIV): lambda: shift(10),
            (17, Symbol.EOF): lambda: reduce(NT.E, [NT.E, Symbol.ADD, NT.T]),
            # State 18
            (18, Symbol.ADD): lambda: reduce(NT.E, [NT.E, Symbol.SUB, NT.T]),
            (18, Symbol.SUB): lambda: reduce(NT.E, [NT.E, Symbol.SUB, NT.T]),
            (18, Symbol.MUL): lambda: shift(9),
            (18, Symbol.DIV): lambda: shift(10),
            (18, Symbol.EOF): lambda: reduce(NT.E, [NT.E, Symbol.SUB, NT.T]),
            # State 19
            (19, Symbol.ADD): lambda: reduce(NT.T, [NT.T, Symbol.MUL, NT.F]),
            (19, Symbol.SUB): lambda: reduce(NT.T, [NT.T, Symbol.MUL, NT.F]),
            (19, Symbol.MUL): lambda: reduce(NT.T, [NT.T, Symbol.MUL, NT.F]),
            (19, Symbol.DIV): lambda: reduce(NT.T, [NT.T, Symbol.MUL, NT.F]),
            (19, Symbol.EOF): lambda: reduce(NT.T, [NT.T, Symbol.MUL, NT.F]),
            # State 20
            (20, Symbol.ADD): lambda: reduce(NT.T, [NT.T, Symbol.DIV, NT.F]),
            (20, Symbol.SUB): lambda: reduce(NT.T, [NT.T, Symbol.DIV, NT.F]),
            (20, Symbol.MUL): lambda: reduce(NT.T, [NT.T, Symbol.DIV, NT.F]),
            (20, Symbol.DIV): lambda: reduce(NT.T, [NT.T, Symbol.DIV, NT.F]),
            (20, Symbol.EOF): lambda: reduce(NT.T, [NT.T, Symbol.DIV, NT.F]),
            # State 21
            (21, Symbol.ADD): lambda: reduce(NT.F, [Symbol.L_PAREN, NT.E, Symbol.R_PAREN]),
            (21, Symbol.SUB): lambda: reduce(NT.F, [Symbol.L_PAREN, NT.E, Symbol.R_PAREN]),
            (21, Symbol.MUL): lambda: reduce(NT.F, [Symbol.L_PAREN, NT.E, Symbol.R_PAREN]),
            (21, Symbol.DIV): lambda: reduce(NT.F, [Symbol.L_PAREN, NT.E, Symbol.R_PAREN]),
            (21, Symbol.EOF): lambda: reduce(NT.F, [Symbol.L_PAREN, NT.E, Symbol.R_PAREN]),
            # State 22
            (22, Symbol.L_PAREN): lambda: shift(14),
            (22, Symbol.INT_CONST): lambda: shift(15),
            (22, Symbol.IDENTIFIER): lambda: shift(16),
            # State 23
            (23, Symbol.L_PAREN): lambda: shift(14),
            (23, Symbol.INT_CONST): lambda: shift(15),
            (23, Symbol.IDENTIFIER): lambda: shift(16),
            # State 24
            (24, Symbol.L_PAREN): lambda: shift(14),
            (24, Symbol.INT_CONST): lambda: shift(15),
            (24, Symbol.IDENTIFIER): lambda: shift(16),
            # State 25
            (25, Symbol.L_PAREN): lambda: shift(14),
            (25, Symbol.INT_CONST): lambda: shift(15),
            (25, Symbol.IDENTIFIER): lambda: shift(16),
            # State 26
            (26, Symbol.ADD): lambda: shift(22),
            (26, Symbol.SUB): lambda: shift(23),
            (26, Symbol.R_PAREN): lambda: shift(31),
            # State 27
            (27, Symbol.ADD): lambda: reduce(NT.E, [NT.E, Symbol.ADD, NT.T]),
            (27, Symbol.SUB): lambda: reduce(NT.E, [NT.E, Symbol.ADD, NT.T]),
            (27, Symbol.MUL): lambda: shift(24),
            (27, Symbol.DIV): lambda: shift(25),
            (27, Symbol.R_PAREN): lambda: reduce(NT.E, [NT.E, Symbol.ADD, NT.T]),
            # State 28
            (28, Symbol.ADD): lambda: reduce(NT.E, [NT.E, Symbol.SUB, NT.T]),
            (28, Symbol.SUB): lambda: reduce(NT.E, [NT.E, Symbol.SUB, NT.T]),
            (28, Symbol.MUL): lambda: shift(24),
            (28, Symbol.DIV): lambda: shift(25),
            (28, Symbol.R_PAREN): lambda: reduce(NT.E, [NT.E, Symbol.SUB, NT.T]),
            # State 29
            (29, Symbol.ADD): lambda: reduce(NT.T, [NT.T, Symbol.MUL, NT.F]),
            (29, Symbol.SUB): lambda: reduce(NT.T, [NT.T, Symbol.MUL, NT.F]),
            (29, Symbol.MUL): lambda: reduce(NT.T, [NT.T, Symbol.MUL, NT.F]),
            (29, Symbol.DIV): lambda: reduce(NT.T, [NT.T, Symbol.MUL, NT.F]),
            (29, Symbol.R_PAREN): lambda: reduce(NT.T, [NT.T, Symbol.MUL, NT.F]),
            # State 30
            (30, Symbol.ADD): lambda: reduce(NT.T, [NT.T, Symbol.DIV, NT.F]),
            (30, Symbol.SUB): lambda: reduce(NT.T, [NT.T, Symbol.DIV, NT.F]),
            (30, Symbol.MUL): lambda: reduce(NT.T, [NT.T, Symbol.DIV, NT.F]),
            (30, Symbol.DIV): lambda: reduce(NT.T, [NT.T, Symbol.DIV, NT.F]),
            (30, Symbol.R_PAREN): lambda: reduce(NT.T, [NT.T, Symbol.DIV, NT.F]),
            # State 31
            (31, Symbol.ADD): lambda: reduce(NT.F, [Symbol.L_PAREN, NT.E, Symbol.R_PAREN]),
            (31, Symbol.SUB): lambda: reduce(NT.F, [Symbol.L_PAREN, NT.E, Symbol.R_PAREN]),
            (31, Symbol.MUL): lambda: reduce(NT.F, [Symbol.L_PAREN, NT.E, Symbol.R_PAREN]),
            (31, Symbol.DIV): lambda: reduce(NT.F, [Symbol.L_PAREN, NT.E, Symbol.R_PAREN]),
            (31, Symbol.R_PAREN): lambda: reduce(NT.F, [Symbol.L_PAREN, NT.E, Symbol.R_PAREN]),
        }

        self.goto: dict[tuple[int, NT], int] = {
            # State 0
            (0, NT.E): 1,
            (0, NT.T): 2,
            (0, NT.F): 3,
            # State 4
            (4, NT.E): 11,
            (4, NT.T): 12,
            (4, NT.F): 13,
            # State 7
            (7, NT.T): 17,
            (7, NT.F): 3,
            # State 8
            (8, NT.T): 18,
            (8, NT.F): 3,
            # State 9
            (9, NT.F): 19,
            # State 10
            (10, NT.F): 20,
            # State 14
            (14, NT.E): 26,
            (14, NT.T): 12,
            (14, NT.F): 13,
            # State 22
            (22, NT.T): 27,
            (22, NT.F): 13,
            # State 23
            (23, NT.T): 28,
            (23, NT.F): 13,
            # State 24
            (24, NT.F): 29,
            # State 25
            (25, NT.F): 30,
        }
