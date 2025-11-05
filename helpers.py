"""
Self-implemented helper classes, variables and functions
"""

class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self._id = id
        self._description = description
        self._status = status
        self._createdAt = createdAt
        self._updatedAt = updatedAt

    def add(self):
        ...

    def update(self):
        ...

    def delete(self):
        ...

    def mark_in_progress(self):
        ...

    def mark_done(self):
        ...

    def list_all(self):
        ...

    def list_done(self):
        ...

    def list_todo(self):
        ...

    def list_in_progress(self):
        ...


class Command:
    def __init__(self, name, arg_desc, arg_count):
        self.name = name
        self.arg_desc = arg_desc
        self.arg_count = arg_count


commands = [
    Command("add", "[Task description]", 1),
    Command("update", "[Task number] [Task description]", 2),
    Command("delete", "[Task number]", 1),
    Command("mark-in-progress", "[Task number]", 1),
    Command("mark-done", "[Task number]", 1),
    Command("list", "[done / todo / in-progress] or leave blank to show all tasks", 0),
]


def helper():
    """Shows file documentation"""
    ...


if __name__ == "__main__":
    helper()