import re

ALLOWED_TAGS = ["a", "code", "i", "strong"]


def validate_html(text):
    unclosed_tags_stack = []
    cleaned_text = ""
    pos = 0

    for tag in re.compile(r"(<.*?>)").finditer(text):
        tag_name = re.match(r'<\s*/?\s*(\w+)', tag.group(0))
        start, end = tag.span()

        cleaned_text += text[pos:start]  # add text before tag

        if tag_name.group(1) in ALLOWED_TAGS:
            if tag_name.group(0).startswith("</"):
                if unclosed_tags_stack and unclosed_tags_stack[-1] == tag_name.group(1):
                    unclosed_tags_stack.pop()
                    cleaned_text += tag.group(0)
                else:  # if text don't have the same opened tag
                    raise ValueError()
            else:
                unclosed_tags_stack.append(tag_name.group(1))
                cleaned_text += tag.group(0)

        pos = end

    cleaned_text += text[pos:]  # add last text

    if unclosed_tags_stack:
        raise ValueError()

    return cleaned_text
