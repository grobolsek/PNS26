from collections.abc import Callable  # noqa: D100

from common import NonTerminal as NT  # noqa: N817
from common import Terminal


class Table:
    """Table for LR1."""

    def __init__(  # noqa: D107
        self,
        shift: Callable[[int], None],
        reduce: Callable[[NT, list[NT | Terminal]], None],
        accept: Callable,
    ) -> None:
        self.action: dict[tuple[int, Terminal], Callable] = {
            # State 0
            (0, Terminal.L_PAREN): lambda: shift(4),
            (0, Terminal.INT_CONST): lambda: shift(5),
            (0, Terminal.IDENTIFIER): lambda: shift(6),
            # State 1
            (1, Terminal.ADD): lambda: shift(7),
            (1, Terminal.SUB): lambda: shift(8),
            (1, Terminal.EOF): accept,
            # State 2
            (2, Terminal.ADD): lambda: reduce(NT.E, [NT.T]),
            (2, Terminal.SUB): lambda: reduce(NT.E, [NT.T]),
            (2, Terminal.MUL): lambda: shift(9),
            (2, Terminal.DIV): lambda: shift(10),
            (2, Terminal.EOF): lambda: reduce(NT.E, [NT.T]),
            # State 3
            (3, Terminal.ADD): lambda: reduce(NT.T, [NT.F]),
            (3, Terminal.SUB): lambda: reduce(NT.T, [NT.F]),
            (3, Terminal.MUL): lambda: reduce(NT.T, [NT.F]),
            (3, Terminal.DIV): lambda: reduce(NT.T, [NT.F]),
            (3, Terminal.EOF): lambda: reduce(NT.T, [NT.F]),
            # State 4
            (4, Terminal.L_PAREN): lambda: shift(14),
            (4, Terminal.INT_CONST): lambda: shift(15),
            (4, Terminal.IDENTIFIER): lambda: shift(16),
            # State 5
            (5, Terminal.ADD): lambda: reduce(NT.F, [Terminal.INT_CONST]),
            (5, Terminal.SUB): lambda: reduce(NT.F, [Terminal.INT_CONST]),
            (5, Terminal.MUL): lambda: reduce(NT.F, [Terminal.INT_CONST]),
            (5, Terminal.DIV): lambda: reduce(NT.F, [Terminal.INT_CONST]),
            (5, Terminal.EOF): lambda: reduce(NT.F, [Terminal.INT_CONST]),
            # State 6
            (6, Terminal.ADD): lambda: reduce(NT.F, [Terminal.IDENTIFIER]),
            (6, Terminal.SUB): lambda: reduce(NT.F, [Terminal.IDENTIFIER]),
            (6, Terminal.MUL): lambda: reduce(NT.F, [Terminal.IDENTIFIER]),
            (6, Terminal.DIV): lambda: reduce(NT.F, [Terminal.IDENTIFIER]),
            (6, Terminal.EOF): lambda: reduce(NT.F, [Terminal.IDENTIFIER]),
            # State 7
            (7, Terminal.L_PAREN): lambda: shift(4),
            (7, Terminal.INT_CONST): lambda: shift(5),
            (7, Terminal.IDENTIFIER): lambda: shift(6),
            # State 8
            (8, Terminal.L_PAREN): lambda: shift(4),
            (8, Terminal.INT_CONST): lambda: shift(5),
            (8, Terminal.IDENTIFIER): lambda: shift(6),
            # State 9
            (9, Terminal.L_PAREN): lambda: shift(4),
            (9, Terminal.INT_CONST): lambda: shift(5),
            (9, Terminal.IDENTIFIER): lambda: shift(6),
            # State 10
            (10, Terminal.L_PAREN): lambda: shift(4),
            (10, Terminal.INT_CONST): lambda: shift(5),
            (10, Terminal.IDENTIFIER): lambda: shift(6),
            # State 11
            (11, Terminal.ADD): lambda: shift(22),
            (11, Terminal.SUB): lambda: shift(23),
            (11, Terminal.R_PAREN): lambda: shift(21),
            # State 12
            (12, Terminal.ADD): lambda: reduce(NT.E, [NT.T]),
            (12, Terminal.SUB): lambda: reduce(NT.E, [NT.T]),
            (12, Terminal.MUL): lambda: shift(24),
            (12, Terminal.DIV): lambda: shift(25),
            (12, Terminal.R_PAREN): lambda: reduce(NT.E, [NT.T]),
            # State 13
            (13, Terminal.ADD): lambda: reduce(NT.T, [NT.F]),
            (13, Terminal.SUB): lambda: reduce(NT.T, [NT.F]),
            (13, Terminal.MUL): lambda: reduce(NT.T, [NT.F]),
            (13, Terminal.DIV): lambda: reduce(NT.T, [NT.F]),
            (13, Terminal.R_PAREN): lambda: reduce(NT.T, [NT.F]),
            # State 14
            (14, Terminal.L_PAREN): lambda: shift(14),
            (14, Terminal.INT_CONST): lambda: shift(15),
            (14, Terminal.IDENTIFIER): lambda: shift(16),
            # State 15
            (15, Terminal.ADD): lambda: reduce(NT.F, [Terminal.INT_CONST]),
            (15, Terminal.SUB): lambda: reduce(NT.F, [Terminal.INT_CONST]),
            (15, Terminal.MUL): lambda: reduce(NT.F, [Terminal.INT_CONST]),
            (15, Terminal.DIV): lambda: reduce(NT.F, [Terminal.INT_CONST]),
            (15, Terminal.R_PAREN): lambda: reduce(NT.F, [Terminal.INT_CONST]),
            # State 16
            (16, Terminal.ADD): lambda: reduce(NT.F, [Terminal.IDENTIFIER]),
            (16, Terminal.SUB): lambda: reduce(NT.F, [Terminal.IDENTIFIER]),
            (16, Terminal.MUL): lambda: reduce(NT.F, [Terminal.IDENTIFIER]),
            (16, Terminal.DIV): lambda: reduce(NT.F, [Terminal.IDENTIFIER]),
            (16, Terminal.R_PAREN): lambda: reduce(NT.F, [Terminal.IDENTIFIER]),
            # State 17
            (17, Terminal.ADD): lambda: reduce(NT.E, [NT.E, Terminal.ADD, NT.T]),
            (17, Terminal.SUB): lambda: reduce(NT.E, [NT.E, Terminal.ADD, NT.T]),
            (17, Terminal.MUL): lambda: shift(9),
            (17, Terminal.DIV): lambda: shift(10),
            (17, Terminal.EOF): lambda: reduce(NT.E, [NT.E, Terminal.ADD, NT.T]),
            # State 18
            (18, Terminal.ADD): lambda: reduce(NT.E, [NT.E, Terminal.SUB, NT.T]),
            (18, Terminal.SUB): lambda: reduce(NT.E, [NT.E, Terminal.SUB, NT.T]),
            (18, Terminal.MUL): lambda: shift(9),
            (18, Terminal.DIV): lambda: shift(10),
            (18, Terminal.EOF): lambda: reduce(NT.E, [NT.E, Terminal.SUB, NT.T]),
            # State 19
            (19, Terminal.ADD): lambda: reduce(NT.T, [NT.T, Terminal.MUL, NT.F]),
            (19, Terminal.SUB): lambda: reduce(NT.T, [NT.T, Terminal.MUL, NT.F]),
            (19, Terminal.MUL): lambda: reduce(NT.T, [NT.T, Terminal.MUL, NT.F]),
            (19, Terminal.DIV): lambda: reduce(NT.T, [NT.T, Terminal.MUL, NT.F]),
            (19, Terminal.EOF): lambda: reduce(NT.T, [NT.T, Terminal.MUL, NT.F]),
            # State 20
            (20, Terminal.ADD): lambda: reduce(NT.T, [NT.T, Terminal.DIV, NT.F]),
            (20, Terminal.SUB): lambda: reduce(NT.T, [NT.T, Terminal.DIV, NT.F]),
            (20, Terminal.MUL): lambda: reduce(NT.T, [NT.T, Terminal.DIV, NT.F]),
            (20, Terminal.DIV): lambda: reduce(NT.T, [NT.T, Terminal.DIV, NT.F]),
            (20, Terminal.EOF): lambda: reduce(NT.T, [NT.T, Terminal.DIV, NT.F]),
            # State 21
            (21, Terminal.ADD): lambda: reduce(NT.F, [Terminal.L_PAREN, NT.E, Terminal.R_PAREN]),
            (21, Terminal.SUB): lambda: reduce(NT.F, [Terminal.L_PAREN, NT.E, Terminal.R_PAREN]),
            (21, Terminal.MUL): lambda: reduce(NT.F, [Terminal.L_PAREN, NT.E, Terminal.R_PAREN]),
            (21, Terminal.DIV): lambda: reduce(NT.F, [Terminal.L_PAREN, NT.E, Terminal.R_PAREN]),
            (21, Terminal.EOF): lambda: reduce(NT.F, [Terminal.L_PAREN, NT.E, Terminal.R_PAREN]),
            # State 22
            (22, Terminal.L_PAREN): lambda: shift(14),
            (22, Terminal.INT_CONST): lambda: shift(15),
            (22, Terminal.IDENTIFIER): lambda: shift(16),
            # State 23
            (23, Terminal.L_PAREN): lambda: shift(14),
            (23, Terminal.INT_CONST): lambda: shift(15),
            (23, Terminal.IDENTIFIER): lambda: shift(16),
            # State 24
            (24, Terminal.L_PAREN): lambda: shift(14),
            (24, Terminal.INT_CONST): lambda: shift(15),
            (24, Terminal.IDENTIFIER): lambda: shift(16),
            # State 25
            (25, Terminal.L_PAREN): lambda: shift(14),
            (25, Terminal.INT_CONST): lambda: shift(15),
            (25, Terminal.IDENTIFIER): lambda: shift(16),
            # State 26
            (26, Terminal.ADD): lambda: shift(22),
            (26, Terminal.SUB): lambda: shift(23),
            (26, Terminal.R_PAREN): lambda: shift(31),
            # State 27
            (27, Terminal.ADD): lambda: reduce(NT.E, [NT.E, Terminal.ADD, NT.T]),
            (27, Terminal.SUB): lambda: reduce(NT.E, [NT.E, Terminal.ADD, NT.T]),
            (27, Terminal.MUL): lambda: shift(24),
            (27, Terminal.DIV): lambda: shift(25),
            (27, Terminal.R_PAREN): lambda: reduce(NT.E, [NT.E, Terminal.ADD, NT.T]),
            # State 28
            (28, Terminal.ADD): lambda: reduce(NT.E, [NT.E, Terminal.SUB, NT.T]),
            (28, Terminal.SUB): lambda: reduce(NT.E, [NT.E, Terminal.SUB, NT.T]),
            (28, Terminal.MUL): lambda: shift(24),
            (28, Terminal.DIV): lambda: shift(25),
            (28, Terminal.R_PAREN): lambda: reduce(NT.E, [NT.E, Terminal.SUB, NT.T]),
            # State 29
            (29, Terminal.ADD): lambda: reduce(NT.T, [NT.T, Terminal.MUL, NT.F]),
            (29, Terminal.SUB): lambda: reduce(NT.T, [NT.T, Terminal.MUL, NT.F]),
            (29, Terminal.MUL): lambda: reduce(NT.T, [NT.T, Terminal.MUL, NT.F]),
            (29, Terminal.DIV): lambda: reduce(NT.T, [NT.T, Terminal.MUL, NT.F]),
            (29, Terminal.R_PAREN): lambda: reduce(NT.T, [NT.T, Terminal.MUL, NT.F]),
            # State 30
            (30, Terminal.ADD): lambda: reduce(NT.T, [NT.T, Terminal.DIV, NT.F]),
            (30, Terminal.SUB): lambda: reduce(NT.T, [NT.T, Terminal.DIV, NT.F]),
            (30, Terminal.MUL): lambda: reduce(NT.T, [NT.T, Terminal.DIV, NT.F]),
            (30, Terminal.DIV): lambda: reduce(NT.T, [NT.T, Terminal.DIV, NT.F]),
            (30, Terminal.R_PAREN): lambda: reduce(NT.T, [NT.T, Terminal.DIV, NT.F]),
            # State 31
            (31, Terminal.ADD): lambda: reduce(NT.F, [Terminal.L_PAREN, NT.E, Terminal.R_PAREN]),
            (31, Terminal.SUB): lambda: reduce(NT.F, [Terminal.L_PAREN, NT.E, Terminal.R_PAREN]),
            (31, Terminal.MUL): lambda: reduce(NT.F, [Terminal.L_PAREN, NT.E, Terminal.R_PAREN]),
            (31, Terminal.DIV): lambda: reduce(NT.F, [Terminal.L_PAREN, NT.E, Terminal.R_PAREN]),
            (31, Terminal.R_PAREN): lambda: reduce(NT.F, [Terminal.L_PAREN, NT.E, Terminal.R_PAREN]),
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
