from behave import then, when

from tests.untils.group import is_sorted, group, group_identical

@then('Группируем лист')
def group_list(context):
    context.group_events = group(context.list_events)

@when('Группировка отработала успешно')
def check_sorted(context):
    is_sorted(context.group_events)

@when('Значения множества и ключи словаря совпадают')
def check_identical(context):
    group_identical(context.list_events, context.group_events)