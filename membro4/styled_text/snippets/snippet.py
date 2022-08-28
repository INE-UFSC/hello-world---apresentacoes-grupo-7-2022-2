import re
from typing import Tuple
from ..terminal_style import TerminalStyle


class Snippet:
    """ Represents a text snippet of the original text. """

    def __init__(self, content: str = ""):
        self._content = re.sub(r"\s+", " ", content)

    def render(self, current_style: TerminalStyle, wanted_style: TerminalStyle) -> Tuple[str, TerminalStyle]:
        """
        Render the snippet.

        :param current_style: Current terminal style
        :param wanted_style: wanted style for render
        :return: rendered text and current terminal style
        """
        render = ''
        if current_style != wanted_style:
            render += wanted_style.render()
        render += self._content
        return render, wanted_style
