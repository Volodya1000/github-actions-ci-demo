from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False


class TodoList:
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str) -> Task:
        if not title:
            raise ValueError("Title cannot be empty")
        task = Task(id=self._next_id, title=title)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def complete_task(self, task_id: int) -> Optional[Task]:
        for task in self._tasks:
            if task.id == task_id:
                task.completed = True
                return task
        return None

    def list_tasks(self, include_completed: bool = False) -> List[Task]:
        if include_completed:
            return self._tasks
        return [t for t in self._tasks if not t.completed]

    def delete_task(self, task_id: int) -> Optional[Task]:
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                return self._tasks.pop(i)
        return None

