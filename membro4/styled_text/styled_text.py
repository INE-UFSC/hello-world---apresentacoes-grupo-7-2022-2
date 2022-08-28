from .snippet_factory import SnippetFactory
from .snippets import (BackgroundColorTag, BaseTag, BoldTag, BrTag,
                       RemoveIndent, TextTag)
from .terminal_style import TerminalStyle
from .text_parser import TextParser


class StyledText:
    def __init__(self,
                 snippet_factory: SnippetFactory = None,
                 text_parser: TextParser = None,
                 initial_style: TerminalStyle = None):

        if snippet_factory is None:
            self._snippet_factory = SnippetFactory()
            tags = [BrTag, TextTag, BackgroundColorTag, BoldTag, RemoveIndent]
            for tag in tags:
                self._snippet_factory.register_tag(tag)
        else:
            self._snippet_factory = snippet_factory

        if initial_style is None:
            self._initial_style = TerminalStyle(background_color="black", foreground_color="white")
        else:
            self._initial_style = initial_style

        if text_parser is None:
            self._text_parser = TextParser(self._snippet_factory)
        else:
            self._text_parser = text_parser

    def render(self, content):
        content_parsed, end_position = self._text_parser._parser(content)
        tree = BaseTag('root', content_parsed)
        text_rendered, end_style = tree.render(self._initial_style, self._initial_style)
        return self._initial_style.render() + text_rendered
