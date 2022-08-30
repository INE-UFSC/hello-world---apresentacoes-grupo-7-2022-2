import re
from typing import Tuple, Union

from ..terminal_style import TerminalStyle
from .snippet import Snippet
from copy import copy


class BaseTag(Snippet):
    """ Abstract class for tags. """

    name: str = None

    def __init__(self,  tag_value: str, children: list[Union[Snippet, 'BaseTag']]):
        super().__init__()
        self._children = children
        self._tag_value = tag_value

    def tag_style(self, current_style: TerminalStyle) -> TerminalStyle:
        """ Return the style for the tag. """
        return copy(current_style)

    @property
    def _tag_attribute(self):
        """ 
            Returns the 'attribute' part of the tag.
            E.g. '<tag_name red> return 'red'.
        """
        return re.sub(r">$", "", re.sub(r"^<(\w|-)+ ", "", self._tag_value))

    def render(self, current_style: TerminalStyle, wanted_style: TerminalStyle) -> Tuple[str, TerminalStyle]:
        rendered_text = ''

        tag_style = self.tag_style(wanted_style)

        for child in self._children:
            rendered_content, current_style = child.render(current_style, tag_style)
            rendered_text += rendered_content
        return (rendered_text, current_style)
