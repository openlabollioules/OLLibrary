"""
This module provides multiple functions to work with String data.
"""
import re

def remove_tags_no_keep(text : str, start : str, end : str) -> str:
    """
    Remove all text between two tags (`start` and `end`), tags included.

    Parameters
    ----------
    text : str
        text to remove tags from
    start : str
        starting tag
    end : str
        ending tag

    Returns
    -------
    str
        Text with tags removed
    """
    return re.sub(r'{}.*?{}'.format(start, end), '', text, flags=re.DOTALL).strip()

def remove_tags_keep(text: str, start: str, end: str) -> str:
    """
    Remove the tags and keep the text between them.

    Parameters
    ----------
    text : str
        Text to remove tags from.
    start : str
        Starting tag.
    end : str
        Ending tag.

    Returns
    -------
    str
        Text with tags removed.
    """
    return re.sub(r'{}(.*?){}'.format(start, end), r'\1', text, flags=re.DOTALL).strip()
