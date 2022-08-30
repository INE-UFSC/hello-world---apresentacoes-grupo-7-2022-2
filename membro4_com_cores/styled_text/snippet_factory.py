import re

from .snippets import Snippet, BaseTag


class SnippetFactory():
    """ Factory for creating tags. """

    def __init__(self):
        self.tags = {}

    def register_tag(self, tag):
        self.tags[tag.name] = tag

    def create_tag(self, tag: str, content: list[Snippet]) -> BaseTag:
        tag_match = re.search(r"(\w|-)+", tag)
        tag_name = ''
        if not tag_match is None:
            tag_name = tag_match.group()

        if tag_name in self.tags:
            return self.tags[tag_name](tag, content)
        else:
            raise ValueError(f"Invalid tag name, '{tag_name}' is not a valid tag name.")

    def create_snippet(self, content: str) -> Snippet:
        return Snippet(content)
