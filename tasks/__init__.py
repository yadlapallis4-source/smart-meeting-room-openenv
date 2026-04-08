from .task_easy import get_task as get_easy
from .task_medium import get_task as get_medium
from .task_hard import get_task as get_hard

TASKS = [get_easy(), get_medium(), get_hard()]
