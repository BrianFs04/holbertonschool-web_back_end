#!/usr/bin/env python3
"""
test_utils module
"""
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import *
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """TestAcccessNestedMap Class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Tests that KeyError is raised for the parameterized test"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(cm.exception))


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Mock HTTP class"""
        mock = Mock()
        mock.json = Mock(return_value=test_payload)
        with patch('utils.requests.get', return_value=mock) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""

    def test_memoize(self):
        """Test that when calling a_property twice,
        the correct result is returned"""
        class TestClass:
            """TestClass class"""

            def a_method(self):
                """a method"""
                return 42

            @memoize
            def a_property(self):
                """a property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_method.assert_called_once()
