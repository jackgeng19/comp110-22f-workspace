"""Example implementing a list utility function."""

# Function name: contains
# We will have two parameters: needle: str, haystack: list[str]

def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if we find it."""
    i: int = 0
    found: bool = False
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False