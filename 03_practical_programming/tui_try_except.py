import os

def clear():
    if os.name == 'nt':
        # windows
        os.system('cls')
    else:
        # linux, macOS, BSD
        print(f'Non-windows ({os.name})')
        os.system('clear')

todo_list_items = [
    {'name': 'Take out the trash', 'priority': 1},
    {'name': 'Fix the hall light fixture', 'priority': 12},
]

def view_todo_list():
    print('Your To Do List:')
    print(f"{'Task':<30}{'Priority':>10}")
    print('-' * 40)
    for item in todo_list_items:
        print(f"{item['name']:<30}{item['priority']:>10}")
    print('-' * 40)

def add_todo_list_item():
    new_item = {}
    new_item['name'] = input('Task: ')
    new_item['priority'] = input('Priority: ')
    todo_list_items.append(new_item)

def show_menu():
    # clear()
    print('1 - view todo list')
    print('2 - add a new todo list item')
    print('3 - quit')

def get_user_choice(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            integer_choice = int(raw)
            return integer_choice
        except ValueError:
            print('Error, please enter an integer (1-3)')

if __name__ == '__main__':
    keep_going = True
    while keep_going:
        show_menu()
        user_choice = get_user_choice('Choice: ')

        if user_choice == 1:
            view_todo_list()
        elif user_choice == 2:
            add_todo_list_item()
        else:
            keep_going = False