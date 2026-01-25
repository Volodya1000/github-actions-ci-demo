import pytest

from todo_app.model import TodoList


def test_add_task():
    todo = TodoList()
    t = todo.add_task("Test CI")
    assert t.id == 1
    assert t.title == "Test CI"


def test_add_empty_raises():
    todo = TodoList()
    with pytest.raises(ValueError):
        todo.add_task("")


def test_complete_task():
    todo = TodoList()
    todo.add_task("Job")
    res = todo.complete_task(1)
    assert res.completed is True


def test_complete_missing():
    todo = TodoList()
    assert todo.complete_task(999) is None


def test_list_tasks():
    todo = TodoList()
    todo.add_task("A")
    t2 = todo.add_task("B")
    todo.complete_task(t2.id)

    # Только активные
    assert len(todo.list_tasks()) == 1
    # Все
    assert len(todo.list_tasks(include_completed=True)) == 2
