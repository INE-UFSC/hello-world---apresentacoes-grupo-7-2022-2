import re

from .base_tag import BaseTag
from ..terminal_style import TerminalStyle


class TextTag(BaseTag):
    """ Change the foreground color. """
    name = "text"

    def tag_style(self, current_style: TerminalStyle) -> TerminalStyle:
        new_style = super().tag_style(current_style)
        color = self._tag_attribute.strip()
        new_style.foreground_color = color
        return new_style
