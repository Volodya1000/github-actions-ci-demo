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


def test_delete_task():
    todo = TodoList()
    t1 = todo.add_task("Task 1")
    _ = todo.add_task("Task 2")

    deleted = todo.delete_task(t1.id)
    assert deleted == t1
    assert len(todo.list_tasks(include_completed=True)) == 1
    assert todo.delete_task(999) is None


def test_delete_task_removes_correct_task():
    """Удаляет именно ту задачу, которую нужно."""
    todo = TodoList()
    _ = todo.add_task("Task  1")
    t2 = todo.add_task("Task  2")
    _ = todo.add_task("Task  3")

    todo.delete_task(t2.id)
    tasks = todo.list_tasks(include_completed=True)

    assert len(tasks) == 2
    assert tasks[0].id == 1
    assert tasks[1].id == 3
    assert all(t.title != "Task 2" for t in tasks)
