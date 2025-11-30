# Copilot Instructions for CLI RPG Learning Project

## Project Context

This is an **educational Python project** for learning software engineering practices through building a small CLI-based RPG game. The focus is on learning process, not just the final product.

## Core Philosophy: Learning-First Development

- **Incremental growth**: Features are built step-by-step, not all at once
- **Understanding over speed**: Code should be clear and educational, not clever
- **One concept at a time**: Each PR teaches a specific lesson (modules, testing, data structures, etc.)
- **Mistakes are learning opportunities**: Expect and welcome imperfect solutions that can be improved

## Project Structure (Target)

The project will evolve to this structure as students progress:

```
rpg/
  __init__.py
  cli.py           # Entry point - python -m rpg.cli
  player.py        # Player character and stats
  enemy.py         # Enemy types and AI
  world.py         # Game locations and navigation
  io.py            # Save/load game state
  combat.py        # Battle mechanics
tests/
  test_player.py
  test_combat.py
  ...
```

**Key convention**: Use `python -m rpg.cli` to run the game (not `python rpg/cli.py`)

## Branch & Commit Workflow

### Branch Naming (Strictly Enforced)

- Features: `feature/<short-desc>` (e.g., `feature/add-player-module`)
- Bugfixes: `bugfix/<issue-desc>` (e.g., `bugfix/fix-heal-hp`)
- Chores: `chore/<desc>` (e.g., `chore/reorganize-tests`)

### Commit Message Format

```
<verb>: <description>
```

Examples:
- `add: basic player factory`
- `fix: enemy damage calculation`
- `refactor: move save/load to io module`
- `test: add tests for world module`

**Important**: One logical change per commit. No "mixed bag" commits.

## Testing Conventions

Run tests with: `pytest -v`

- All new features require corresponding tests
- Test files mirror source structure: `rpg/player.py` → `tests/test_player.py`
- Focus on testing behavior, not implementation details
- Keep tests simple and readable for learning

## Code Style for This Project

Since this is a learning project, prioritize:

1. **Clarity over cleverness** - Avoid advanced Python features that obscure intent
2. **Explicit over implicit** - Be verbose if it aids understanding
3. **Simple data structures first** - Start with dicts/lists before custom classes
4. **Docstrings on functions** - Help students understand purpose
5. **Type hints encouraged** - But not required for early stages

Example of appropriate complexity:

```python
# Good for learning - clear and explicit
def create_player(name: str) -> dict:
    """Create a new player with starting stats."""
    return {
        "name": name,
        "hp": 100,
        "max_hp": 100,
        "level": 1
    }

# Too advanced for early stages
class Player(BaseCharacter, Observable):
    def __init__(self, name: str, **kwargs):
        super().__init__(**kwargs)
        self._state = PlayerState(name)
```

## PR & Code Review Guidelines

- **Educational feedback**: Explain *why*, not just *what* to change
- **Suggest alternatives**: Offer 2-3 approaches with tradeoffs
- **Ask guiding questions**: Help students discover solutions
- **Be constructive**: Frame criticism as learning opportunities
- **Reference resources**: Link to docs/examples when introducing new concepts

## What NOT to Do

- ❌ Don't create all features at once - this is incremental learning
- ❌ Don't over-engineer - keep solutions appropriate to learning stage
- ❌ Don't skip tests - testing is a core learning objective
- ❌ Don't commit directly to `main` - always use branches and PRs
- ❌ Don't use advanced patterns (metaclasses, decorators, async) until later lessons

## When Helping Students

1. Check which features already exist before suggesting new patterns
2. Match complexity to current project stage (check recent commits)
3. If suggesting refactoring, explain the pedagogical benefit
4. Provide working examples, not just descriptions
5. Remember: the goal is learning Python fundamentals, not building a production game
