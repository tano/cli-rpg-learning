# CLI RPG — Learning Project

This repository is part of an educational program for learning Python through building a small CLI-based RPG game.  
The project focuses on clean structure, modules, packages, testing, and good engineering practices.

---

## 📚 Goals of the project

- Learn how Python modules and packages work  
- Practice clean project organization  
- Learn to write small, meaningful commits  
- Practice testing with pytest  
- Learn to work with branches and pull requests  
- Build a tiny text-based RPG step by step  

---

## 🧭 Workflow

We follow a simple and clear development process:

1. Every change is done in a separate branch  
2. Each branch solves **one small, clear task** (Single Responsibility Principle — SRP)  
3. Each task is submitted as a Pull Request  
4. Pull Request goes through code review  
5. After approval, the branch is merged into `main`  

❗ **No direct commits to `main`.**

---

## 🌿 Branch naming conventions

Use short and descriptive branch names.

### Feature branches

```
feature/<short-description>
```

Examples:

```
feature/add-player-module
feature/world-locations
feature/cli-menu
```

---

### Bugfix branches

```
bugfix/<issue-description>
```

Examples:

```
bugfix/fix-heal-hp
bugfix/slime-damage
```

---

### Chore / maintenance branches

```
chore/<description>
```

Examples:

```
chore/refactor-io
chore/reorganize-tests
chore/update-readme
```

---

## ✳️ Commit message rules

We use small, clear commits.  
Each commit should cover **one logical change**.

### Format

```
<verb in present tense>: <short description>
```

### Examples

```
add: basic player factory
fix: enemy damage calculation
refactor: move save/load to io module
test: add tests for world module
docs: update setup instructions
```

### Guidelines (SRP)

- One change = one commit  
- Do not mix unrelated changes  
- Commit early, commit often  
- Message should describe **what was changed**, not “why”  

---

## 🛠️ Setup

### 1. Create virtual environment

```bash
python3 -m venv venv
```

### 2. Activate virtual environment

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🎯 Current Feature: Party Creation

The current task is to implement **party creation and validation** logic.

### Party Rules

- **Allowed hero types**: `warrior`, `mage`, `rogue`
- **Party size**: 1-4 heroes
- **Type limit**: Maximum 2 heroes of the same type

### Implementation Task

The module `rpg/party.py` contains:
- Constants: `ALLOWED_HERO_TYPES`, `MIN_PARTY_SIZE`, `MAX_PARTY_SIZE`, `MAX_PER_TYPE`
- Function stubs: `validate_party()` and `create_party()`

**Your task**: Implement these functions to make all tests in `tests/test_party.py` pass.

### Test-Driven Development

Run the tests to see what needs to be implemented:

```bash
pytest tests/test_party.py -v
```

All tests will **fail** initially because the functions raise `NotImplementedError`. Your goal is to implement the logic so all tests pass.

---

## 📁 Project structure

```
cli-rpg-learning/
├── rpg/
│   ├── __init__.py
│   ├── cli.py         # Entry point
│   └── party.py       # Party creation and validation
└── tests/
    └── test_party.py
```

**Note**: Additional modules (player, enemy, world, combat, io) will be added in future iterations.

---

## 🧪 Testing

Run tests:

```bash
pytest -v
```

---

## 🚀 Running the game

Launch the game:

```bash
python -m rpg.cli
```

---

## 🤝 Code review rules

- Be polite, constructive, and precise  
- Suggest improvements, not just point out problems  
- Ask clarifying questions  
- The goal is learning, not perfection  

---

## 🎓 Learning philosophy

We improve the project gradually:

- simple → clear → stable → extendable  
- step by step  
- with understanding, not memorization  

Mistakes are normal — clarity and iteration matter most.
