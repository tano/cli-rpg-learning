"""Party creation and validation for RPG heroes."""

# Hero types available for party composition.
# Each type represents a class with unique abilities in the RPG (e.g., "warrior" is strong in melee combat, "mage" uses magic, "rogue" excels at stealth).
ALLOWED_HERO_TYPES = ("warrior", "mage", "rogue")

# Party size constraints
MIN_PARTY_SIZE = 1
MAX_PARTY_SIZE = 4

# Per-type limit
MAX_PER_TYPE = 2


def validate_party(hero_types):
    """
    Validate a party composition.

    Args:
        hero_types: list of strings, each string is a hero type, 
                   e.g. "warrior", "mage", "rogue".

    Rules:
        - Only allowed hero types are accepted.
        - Party must contain at least MIN_PARTY_SIZE heroes.
        - Party must contain at most MAX_PARTY_SIZE heroes.
        - Each hero type may appear at most MAX_PER_TYPE times.

    Raises:
        ValueError: If any validation rule is violated with a 
                   human-readable message.

    TODO: Implement validation logic.
    """
    raise NotImplementedError("validate_party() is not yet implemented")


def create_party(hero_types):
    """
    Create a party from a list of hero types.

    Args:
        hero_types: list of strings representing hero types.

    Returns:
        A party representation (for now, returns the list as-is).

    Raises:
        ValueError: If party composition is invalid 
                   (via validate_party()).

    TODO: Implement party creation logic.
          Should call validate_party() first, then return the party.
    """
    raise NotImplementedError("create_party() is not yet implemented")
