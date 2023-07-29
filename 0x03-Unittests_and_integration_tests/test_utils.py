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


class TestGetJson(unittest.TestCase):
    """class that tests the get_json method"""
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url, test_payload):
        """Use Mocks to test that get_json returns the expected result"""
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json(test_url), test_payload)
            mock.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """class that tests the memoize method"""

    def test_memoize(self):
        """Method with a class TestClass and a method a_method"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

            with patch.object(TestClass, "a_method", return_value=42) as mock:
                test = TestClass()
                self.assertEqual(test.a_property, mock.return_value)
                self.assertEqual(test.a_property, mock.return_value)
                mock.assert_called_once()
