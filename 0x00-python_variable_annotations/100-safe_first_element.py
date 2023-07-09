#!/usr/bin/env python3
import typing 


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
        """Return duck-typed Annotation"""
        if lst:
            return lst[0]
        else:
            return None