TODO_SCHEMA = {
    'type': 'object',
    'properties': {
        'description': {'title': 'Description', 'type': 'string'},
        'task_lists': {
            'title': 'Task lists',
            'type': 'array',
            'uniqueItems': True,
            'items': {'$ref': '#/definitions/TaskList'},
        },
    },
    'required': ['description', 'task_lists'],
    'definitions': {
        'Task': {
            'title': 'Task',
            'type': 'object',
            'properties': {
                'name': {'title': 'Name', 'type': 'string'},
                'task_type': {'type': 'string', 'enum': []},
            },
            'required': ['name'],
        },
        'TaskList': {
            'title': 'Task lists',
            'type': 'object',
            'properties': {
                'name': {'title': 'Name', 'type': 'string'},
                'tasks': {
                    'title': 'Tasks',
                    'type': 'array',
                    'items': {'$ref': '#/definitions/Task'},
                },
            },
            'required': ['name', 'tasks'],
        },
    },
}


TODO_UI_SCHEMA = {
    'ui:title': 'Todo lists',
    'description': {
        'ui:autofocus': True,
        'ui:emptyValue': '',
        'ui:help': 'A summary of all the tasks lists',
        'ui:widget': 'textarea',
    },
    'task_lists': {
        'items': {
            'classNames': 'dynamic-task-list',
            'name': {'ui:help': 'A descriptive name for the task list'},
            'tasks': {
                'items': {
                    'classNames': 'dynamic-task-item',
                    'name': {'ui:help': 'A descriptive name for the task'},
                    'task_type': {
                        'classNames': 'dynamic-task-field',
                        'ui:help': 'The task type',
                        'ui:widget': 'select',
                    },
                }
            },
        },
    },
}


def set_task_types(schema, ui_schema):
    from todos.models import TaskType

    task_types = list(TaskType.objects.all().values_list('name', flat=True))
    schema['definitions']['Task']['properties']['task_type']['enum'] = task_types
    ui_schema['task_lists']['items']['tasks']['items']['task_type'][
        'ui:help'
    ] = f'Select 1 of {len(task_types)} task types'
