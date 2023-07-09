#!/usr/bin/env python3
# The types of the elements of the input are not know
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Return duck-typed Annotation"""
    if lst:
        return lst[0]
    else:
        return None
