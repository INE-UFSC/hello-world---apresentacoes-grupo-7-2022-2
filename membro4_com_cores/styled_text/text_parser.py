import re

from .snippet_factory import SnippetFactory


class TextParser:
    def __init__(self, snippet_factory: SnippetFactory):
        self._snippet_factory = snippet_factory
        pass

    def _parser(self, content, root=True):
        # split text into snippets
        text_snippets = re.finditer(r"(?<!\\)<[^>]*>|(\\<|\\>|[^<>])*", content)
        content_parsed = []
        min_index = 0
        for snippet_match in text_snippets:
            snippet = snippet_match.group()
            current_position = snippet_match.end()

            if snippet_match.start() < min_index:
                continue

            if len(snippet) == 0:
                continue

            if snippet.startswith("</"):
                if not root:
                    return content_parsed, snippet_match.end()
                else:
                    raise SyntaxError("Unbalanced tags")
            # snippet is a tag
            if snippet.startswith("<"):
                # this tag is a self-closing tag
                if snippet.endswith("/>"):
                    parsed_tag = self._snippet_factory.create_tag(snippet, [])
                    content_parsed.append(parsed_tag)
                else:
                    # this tag is a tag with content
                    content_remming = content[current_position:]

                    parsed_tag_content, tag_position_end = self._parser(content_remming, False)
                    parsed_tag = self._snippet_factory.create_tag(snippet, parsed_tag_content)
                    content_parsed.append(parsed_tag)

                    min_index = current_position + tag_position_end
            else:
                content_parsed.append(self._snippet_factory.create_snippet(snippet))
        if not root:
            raise SyntaxError("Unbalanced tags")
        return content_parsed, len(content)

