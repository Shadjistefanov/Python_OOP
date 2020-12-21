# section_code:

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'
    def complete_task(self, task_name: str):
        task_lists = list(filter(lambda t: t.name == task_name, self.tasks))
        if task_lists:
            task = task_lists[0]
            task.completed = True
            return f'Completed task{task.name}'

        return f'Could not find task with the name {task_name}'


    def clean_section(self):
        completed_tasks = list(filter(lambda t: t.completed, self.tasks))
        for tsk in completed_tasks:
            self.tasks.remove(tsk)
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        result = f'Section {self.name}:\n'
        for task in self.tasks:
            result += task.details() + '\n'

        return result



