import re


import re

from .base_tag import BaseTag
from ..terminal_style import TerminalStyle


class BackgroundColorTag(BaseTag):
    """ Change the background color. """

    name = "background-color"

    def tag_style(self, current_style: TerminalStyle) -> TerminalStyle:
        new_style = super().tag_style(current_style)
        color = self._tag_attribute.strip()
        new_style.background_color = color
        return new_style
