import typer

from src.todo_app.model import TodoList

app = typer.Typer()
todo = TodoList()


@app.command("add")
def add(title: str = typer.Argument(..., help="Title of the new task")):
    task = todo.add_task(title)
    typer.echo(f"Added: {task.title} (ID: {task.id})")


if __name__ == "__main__":
    app()
