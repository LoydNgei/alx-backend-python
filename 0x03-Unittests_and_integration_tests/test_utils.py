#!/usr/bin/env python3
"""Generic utilities for github org client."""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test that the method returns what it is supposed to"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """Test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)

        ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        """Test that a KeyError is raised for the following inputs"""
        with self.assertRaises(expected_output):
            access_nested_map(nested_map, path)
