"""Tests for party creation and validation.

These tests define the expected behavior but will FAIL until 
rpg/party.py is properly implemented.
"""

import pytest
from rpg.party import create_party


def test_single_hero_party_is_valid():
    """A party with a single hero should be valid."""
    party = create_party(["warrior"])
    assert party == ["warrior"]


def test_mixed_party_within_limits_is_valid():
    """A mixed party within size and type limits should be valid."""
    hero_types = ["warrior", "mage", "rogue", "warrior"]
    party = create_party(hero_types)
    assert party == hero_types


def test_party_too_small_raises():
    """An empty party should raise ValueError."""
    with pytest.raises(ValueError):
        create_party([])


def test_party_too_big_raises():
    """A party with more than MAX_PARTY_SIZE heroes should raise ValueError."""
    # 5 heroes exceeds MAX_PARTY_SIZE (4)
    hero_types = ["warrior", "mage", "rogue", "warrior", "mage"]
    with pytest.raises(ValueError):
        create_party(hero_types)


def test_unknown_hero_type_raises():
    """A party with an unknown hero type should raise ValueError."""
    with pytest.raises(ValueError):
        create_party(["warrior", "paladin"])


def test_too_many_same_type_raises():
    """A party with too many heroes of the same type should raise ValueError."""
    hero_types = ["warrior", "warrior", "warrior"]
    with pytest.raises(ValueError):
        create_party(hero_types)
