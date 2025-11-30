"""CLI entry point for the RPG game."""

from rpg.party import create_party, ALLOWED_HERO_TYPES


def get_hero_types_from_user():
    """
    Get hero types from user input.
    
    TODO: Implement interactive input logic.
          For now, returns a hardcoded example.
    """
    # Example party - student can make this interactive
    return ["warrior", "mage"]


def display_welcome():
    """Display welcome message and game info."""
    print("=" * 50)
    print("Welcome to CLI RPG!")
    print("=" * 50)
    print(f"\nAvailable hero types: {', '.join(ALLOWED_HERO_TYPES)}")
    print("\nYour quest begins...\n")


def main():
    """Run the game."""
    display_welcome()
    
    # Get hero types (currently hardcoded, student can expand)
    hero_types = get_hero_types_from_user()
    print(f"Selected heroes: {', '.join(hero_types)}")
    
    # Try to create party
    try:
        party = create_party(hero_types)
        print(f"\n✓ Party created successfully!")
        print(f"Your party: {party}")
    except NotImplementedError:
        print("\n⚠ Party creation not yet implemented.")
        print("TODO: Implement validate_party() and create_party() in rpg/party.py")
    except ValueError as e:
        print(f"\n✗ Invalid party: {e}")


if __name__ == "__main__":
    main()

