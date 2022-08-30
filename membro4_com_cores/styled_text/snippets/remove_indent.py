import re
from typing import Tuple
from ..terminal_style import TerminalStyle
from .base_tag import BaseTag


class RemoveIndent(BaseTag):
    """ Remove the indentation from the text. """
    
    name = "remove-indent"

    def render(self, current_style: TerminalStyle, wanted_style: TerminalStyle) -> Tuple[str, TerminalStyle]:
        tag_style = self.tag_style(wanted_style)
        rendered_children = []
        rendered_children: list[str] = []
        for snippet in self._children:
            rendered_child, current_style = snippet.render(current_style, tag_style)

            if len(rendered_children) > 0:
                last_child = rendered_children[-1]
                if not last_child.endswith("\n"):
                    rendered_children.append(rendered_child)
                    continue

            child_without_indent = re.sub(r"^( |\t)+", "", rendered_child)
            initial_style_with_space = re.search(r"^\x1b\[([0-9]|;)*?m(\t| )+", child_without_indent)
            if initial_style_with_space != None:
                style = re.search(f"\x1b\[([0-9]|;)*?m", child_without_indent)[0]
                child_without_indent = re.sub(r"^\x1b\[([0-9]|;)*?m(\t| )+", style, child_without_indent)

            rendered_children.append(child_without_indent)

        return ''.join(rendered_children), current_style
