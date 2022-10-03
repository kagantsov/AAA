import csv

def open_menu():
    """Открыть меню действий"""
    print('Меню:')
    print('1. Вывести департаменты и входящие в них отделы.')
    print('2. Вывести сводный отчет по департаментам.')
    print('3. Сохранить отчет из пункта 2 в csv-файл.')

def user_input_and_check():
    """Принять команду от пользователя и перепроверить ее"""
    user_input = input('Пожалуйста, выберите пункт из меню:')
    if user_input.isdigit() and int(user_input) in {1, 2, 3}:
        return int(user_input)
    else:
        print('Вы выбрали несуществующую опцию. Попробуйте снова.')
        return user_input_and_check()

def read_csv_file() -> list[dict]:
    """Чтение файла в формате csv"""
    with open('Corp_Summary.csv', 'r', encoding='utf8') as file:
        lines = file.readlines()
        data = list(map(lambda r: r.strip().split(';'), lines))[1:]
    return data

def get_department_hierarchy() -> dict:
    """Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него"""
    data = read_csv_file()
    departments = {row[1]: [] for row in data}

    for department in departments:
        for row in data:
            if row[1] == department:
                team = row[2]
                if team not in departments[department]:
                    departments[department].append(row[2])
    print()
    for department, team in departments.items():
        print(f'{department} : {",".join(team)}')

def department_consolidated_report() -> list[dict]:
    """Создание сводного отчета по департаменту"""
    data = read_csv_file()
    department_data = {row[1]: [0, list().copy()] for row in data}

    for department in department_data:
        for row in data:
            if row[1] == department:
                department_data[department][0] += 1
                if row[-1].isdigit():
                    department_data[department][1].append(int(row[-1]))
    result = []
    for department, salary in department_data.items():
        row = [department, str(salary[0]), str(min(salary[1])),
               str(max(salary[1])), str(round(sum(salary[1])/len(salary[1]), 2))]
        result.append(row)
    return result

def demonstrate_department_consolidated_report():
    """Вывод сводного отчета по департаменту"""
    data_consolidated_report = department_consolidated_report()
    columns = ['Департамент', 'Численность сотрудников', 'Минимальная зарплата', 'Максимальная зарплата', 'Средняя зарплата']
    print(*columns)
    for department in data_consolidated_report:
        print(*department)

def department_consolidated_report_to_csv():
    """Сохранение сводного отчета по департаменту в формате CSV"""
    data_consolidated_report = department_consolidated_report()
    columns = ['Департамент', 'Численность сотрудников', 'Минимальная зарплата', 'Максимальная зарплата', 'Средняя зарплата']
    with open('Department_consolidated_report.csv', 'w', encoding='utf8') as output_file:
        output_file.write(",".join(columns) + '\n')
        for row in data_consolidated_report:
            output_file.write(",".join(row) + '\n')
    print('Файл успешно сохранен!')

def main():
    """Общая функция для задания"""
    open_menu()
    user_input = user_input_and_check()

    if user_input == 1:
        get_department_hierarchy()
        return main()
    elif user_input == 2:
        demonstrate_department_consolidated_report()
        return main()
    elif user_input == 3:
        department_consolidated_report_to_csv()
        return main()
    else:
        print('Неправильный ввод!')

if __name__ == '__main__':
    main()