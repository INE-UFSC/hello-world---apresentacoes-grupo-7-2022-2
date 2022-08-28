from typing import Tuple
from .base_tag import BaseTag
from ..terminal_style import TerminalStyle


class BrTag(BaseTag):
    """ Insert a newline. """
    name = "br"

    def render(self, current_style: TerminalStyle, wanted_style: TerminalStyle) -> Tuple[str, TerminalStyle]:
        if len(self._children) > 0:
            raise ValueError("Br tag cannot have content.")

        render = ''
        if current_style != wanted_style:
            render += wanted_style.render()
        render += "\n"
        return render, wanted_style
