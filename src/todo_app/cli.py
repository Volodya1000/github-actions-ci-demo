import typer

from src.todo_app.model import TodoList

app = typer.Typer()
todo = TodoList()


@app.command("add")
def add(title: str = typer.Argument(..., help="Title of the new task")):
    """Add a new task."""
    task = todo.add_task(title)
    typer.echo(f"Added: {task.title} (ID: {task.id})")


@app.command("list")
def list_tasks(
    include_completed: bool = typer.Option(False, "--all", "-a", help="Show all tasks including completed"
    ),
):
    """List all tasks."""
    tasks = todo.list_tasks(include_completed=include_completed)
    if not tasks:
        typer.echo("No tasks found")
        return

    typer.echo("Tasks:")
    for task in tasks:
        status = "✓" if task.completed else "○"
        typer.echo(f"  {status} {task.id}: {task.title}")


@app.command("complete")
def complete(task_id: int = typer.Argument(..., help="ID of the task to complete")):
    """Mark a task as completed."""
    task = todo.complete_task(task_id)
    if task:
        typer.echo(f"Completed: {task.title} (ID:  {task.id})")
    else:
        typer.echo(f"Error: Task with ID {task_id} not found.", err=True)
        raise typer.Exit(code=1)


@app.command("delete")
def delete(task_id: int = typer.Argument(..., help="ID of the task to delete")):
    """Delete a task."""
    task = todo.delete_task(task_id)
    if task:
        typer.echo(f"Deleted: {task.title} (ID: {task.id})")
    else:
        typer.echo(f"Error: Task with ID {task_id} not found.", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
