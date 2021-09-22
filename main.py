#!/usr/bin/env python


import json
import os
import typer

from datetime import datetime
from enum import Enum
from error import InvalidArgument
from shutil import copyfile
from typing import Dict

app = typer.Typer()

TODO_FILE = 'todo.txt'
WIP_FILE = 'wip.txt'
DONE_FILE = 'done.txt'
TMP_FILE = 'tmp.txt'

class ActionType(str, Enum):
    todo = "todo"
    wip = "wip"
    done = "done"


@app.command()
def new(name: str):
    """add new item to todo list"""
    last_id = None
    try:
        with open(TODO_FILE, "r") as f:
            for line in f:
                pass
        last_data = json.loads(line)
        last_id = last_data['id']
    except FileNotFoundError:
        pass

    data = dict()
    a_id = last_id + 1 if last_id else 1
    f = open(TODO_FILE, "a")
    data['id'] = a_id
    data['name'] = name
    data['mtime'] = f'{datetime.now()}'
    data_json = json.dumps(data)
    f.write(f'{data_json}\n')
    f.close()

@app.command()
def move(id: int, to: str, type_: ActionType):
    """update by moving items from a file to another file"""
    types = ['wip', 'done']
    if type_ not in types:
        raise InvalidArgument

    if type_ == ActionType.wip:
        check_file = TODO_FILE
        append_file = WIP_FILE
    elif type_ == ActionType.done:
        check_file = WIP_FILE
        append_file = DONE_FILE

    with open(check_file, "r") as f:
        for line in f:
            data: Dict = json.loads(line)
            if data['id'] == id:
                with open(append_file, "a") as ff:
                    data.update({"mtime": f'{datetime.now()}'})
                    ff.write(f'{json.dumps(data)}\n')
            else:
                with open(TMP_FILE, "a") as tf:
                    tf.write(line)         

    copyfile(TMP_FILE, check_file)

    if os.path.exists(TMP_FILE):
        os.remove(TMP_FILE)


@app.command()
def todo():
    query(ActionType.todo)

@app.command()
def wip():
    query(ActionType.wip)

@app.command()
def done():
    query(ActionType.done)

def query(type_: ActionType):
    target_file = None
    if type_ == ActionType.todo:
        target_file = TODO_FILE
    elif type_ == ActionType.wip:
        target_file = WIP_FILE
    elif type_ == ActionType.done:
        target_file = DONE_FILE

    with open(target_file, 'r') as f:
        for line in f:
            print(line.rstrip())


if __name__ == '__main__':
    app()