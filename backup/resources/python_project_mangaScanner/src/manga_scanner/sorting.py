"""Sorting helpers for manga page filenames."""
import re

def natural_sort_key(value: str) -> tuple[object, ...]:
    """Return a key that sorts embedded numbers numerically."""

    parts = re.split(r'(\d+)', value)

    key = []
    for part in parts:
        if part.isdigit():
            # Convert number parts to int
            key.append(int(part))
        else:
            # Lowercase text parts for case-insensitive sorting
            key.append(part.lower())

    return tuple(key)
