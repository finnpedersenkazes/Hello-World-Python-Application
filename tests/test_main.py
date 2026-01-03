"""Tests for the main module."""

import pytest
from src.main import greet


class TestGreet:
    """Tests for the greet function."""
    
    def test_greet_default(self):
        """Test greet with default parameter."""
        assert greet() == "Hello, World!"
    
    def test_greet_with_name(self):
        """Test greet with a custom name."""
        assert greet("Alice") == "Hello, Alice!"
    
    def test_greet_with_empty_string(self):
        """Test greet with an empty string."""
        assert greet("") == "Hello, !"
    
    def test_greet_returns_string(self):
        """Test that greet returns a string."""
        result = greet()
        assert isinstance(result, str)
