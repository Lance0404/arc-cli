## Arc-cli
* typer is the main purpose for this trial
* typer, a brilliant work by tiangolo, is like a wrapper of click

### Requirements
```sh
live coding assessment from Arc & Codementor

Please build a CLI version kanban.
user can add a new task to kanban

user can see todo list in chronological order

user can move a todo item to WIP

user can see WIP list in chronological order

user can move a WIP item to Done

user can see Done list in chronological order
# create a item to todo list
$ kanban new "I want to drink water"
# C

---
# move item with id 1 to wip list
$ kanban move 1 to wip

# move item with id 1 to done list
$ kanban move 1 to done
# U

--- 
# display all items in todo list
$ kanban todo

# display all items in wip list
$ kanban wip

# display all items in done list
$ kanban done
# R
```

### How to implement
1. UI 
2. state file (todo, wip, done)
3. CRU (no D required)

### How to use
1. poetry install
1. poetry shell
1. python main.py --help

* `python main.py new 'love'` to add new item to todo list
* `python main.py move 11 to wip` to move item id 11 from todo to wip list
* `python main.py move 11 to done` to move item id 11 from wip to done list
* `python main.py todo` to list todo items
* `python main.py wip` to list wip items
* `python main.py done` to list done items

### Ref
1. [Typer](https://typer.tiangolo.com/tutorial/parameter-types/enum/)
