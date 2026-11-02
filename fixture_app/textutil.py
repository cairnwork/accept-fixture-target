"""Small text helpers (synthetic fixture code; each has one known bug, see Issues 1-5)."""
import re


def slugify(text):
    """Lowercase, replace whitespace with '-', strip leading/trailing '-'."""
    s = text.strip().lower()
    s = re.sub(r"\s", "-", s)  # BUG (issue 1): each whitespace char becomes its own '-'
    return s.strip("-")


def chunk(items, n):
    """Split a list into consecutive chunks of size n."""
    if n <= 0:
        raise ValueError("n must be positive")
    out = []
    for i in range(0, len(items) - n + 1, n):  # BUG (issue 2): drops the last partial chunk
        out.append(items[i:i + n])
    return out


def parse_bool(value):
    """'true'/'yes'/'1' -> True, 'false'/'no'/'0' -> False, anything else -> ValueError."""
    if value in ("true", "yes", "1"):  # BUG (issue 3): case and surrounding spaces not handled
        return True
    if value in ("false", "no", "0"):
        return False
    raise ValueError("not a boolean: %r" % (value,))


def median(values):
    """Median of a non-empty list of numbers; empty -> ValueError."""
    if not values:
        raise ValueError("empty")
    s = sorted(values)
    return s[len(s) // 2]  # BUG (issue 4): even length returns the upper middle, not the mean


def truncate(text, n):
    """Cut text to at most n characters, ending with '...' when cut. Short text unchanged."""
    if len(text) <= n:
        return text
    return text[:n] + "..."  # BUG (issue 5): result is n+3 characters, should be n
