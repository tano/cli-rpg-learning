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

## 🧪 Testing

Run tests:

```
pytest -v
```

---

## 🚀 Running the game

Launch the game:

```
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
