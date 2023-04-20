from AAkinter.view.base.constants import (
    W, E, N, S, BOTH, BOTTOM, RIGHT, LEFT, X, Y
)


PACK_EXPANDY = {"expand": True, "fill": Y}
PACK_EXPANDX = {"expand": True, "fill": X}
PACK_EXPAND = {"expand": True, "fill": BOTH}

COMBOBOX = {"fill": X, "expand": True, 'pady': 10, 'padx': 10}
SCROLLBAR_PACK = {"side": RIGHT, "fill": Y}

LEFT_PACK_EXPAND = {"side": LEFT, "fill": BOTH}
RIGHT_PACK_EXPAND = {"side": RIGHT, "fill": BOTH}

CONTAINER_GRID = {'padx': 15, 'pady': 5, "sticky": W+E+N+S}

PACK_EXPAND_15x_5y = {"expand": True, "fill": BOTH, "fill": BOTH, 'padx': 15, 'pady': 5}  # noqa

LEFT_PACK_EXP_PAD5_15 = {"expand": 1, "side": LEFT, "fill": BOTH, 'padx': 15, 'pady': 5}  # noqa

RIGHT_PACK_EXP_PAD5_15 = {"expand": 1, "side": RIGHT, "fill": BOTH, 'padx': 15, 'pady': 5}  # noqa

CENTER_PACK_EXP_PAD5_15 = {"expand": 1, "side": LEFT, "fill": BOTH, 'padx': 15, 'pady': 5}  # noqa
