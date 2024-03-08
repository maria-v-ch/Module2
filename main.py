from typing import List


class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description


class TaskManager:
    def __init__(self):
        self.__tasks = []

    @property
    def get_tasks(self) -> List[Task]:
        return self.__tasks

    def add_task(self, task):
        self.__tasks.append(task)


if __name__ == '__main__':
    task_manager = TaskManager()
    task_manager.add_task(Task('Первое', 'Сделать то-то'))
    task_manager.add_task(Task('А еще', 'Сделать это'))
    task_manager.add_task(Task('И наконец', 'Вот это вот'))
    tasks = task_manager.get_tasks
    for idx, task in enumerate(tasks, start=1):
        print(f'Задача {idx}: {task.title} - {task.description}')
