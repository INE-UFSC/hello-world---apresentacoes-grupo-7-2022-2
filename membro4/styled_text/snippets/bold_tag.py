from ..terminal_style import TerminalStyle
from .base_tag import BaseTag


class BoldTag(BaseTag):
    """ Apply bold to the text. """
    name = "bold"

    def tag_style(self, current_style: TerminalStyle) -> TerminalStyle:
        new_style = super().tag_style(current_style)
        new_style.bold = True
        return new_style
