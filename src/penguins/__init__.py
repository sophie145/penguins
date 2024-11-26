"""
Penguins: A great package that analyses penguin populations.
"""

from __future__ import annotations

from importlib.metadata import version

__all__ = ("__version__",)
__version__ = version(__name__)


from penguins.functions import p_value_to_words