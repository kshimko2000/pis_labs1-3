groupmates = [
    {
        "name": "Кирилл",
        "surname": "Шимко",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5],
    },
    {
        "name": "Петр",
        "surname": "Сорокин",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4],
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5],
    },
    {
        "name": "Евгений",
        "surname": "Воробьев",
        "exams": ["Математика", "ИС", "КТП"],
        "marks": [3, 3, 3],
    },
    {
        "name": "Иван",
        "surname": "Марков",
        "exams": ["Информатика", "ЭЭиС", "Информатика"],
        "marks": [5, 3, 5],
    },{
        "name": "Сергей",
        "surname": "Иванов",
        "exams": ["Статистика", "ИС", "Web"],
        "marks": [5, 3, 4],
    },
]

def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(15), "Экзамены".ljust(35), "Оценки".ljust(20), "Средний".ljust(10))
    for st in students:
        avg = sum(st["marks"]) / len(st["marks"]) if st["marks"] else 0
        print(
            st["name"].ljust(15),
            st["surname"].ljust(15),
            str(st["exams"]).ljust(35),
            str(st["marks"]).ljust(20),
            f"{avg:.2f}".ljust(10)
        )


def filter_students_by_avg(students, min_avg):
    res = []
    for st in students:
        if not st["marks"]:
            continue
        avg = sum(st["marks"]) / len(st["marks"])
        if avg > min_avg:
            res.append(st)
    return res


if __name__ == "__main__":
    try:
        min_avg = float(input("Введите средний балл для фильтрации: ").replace(",", "."))
    except ValueError:
        print("Ошибка: нужно число.")
        raise SystemExit(1)

    filtered = filter_students_by_avg(groupmates, min_avg)
    print_students(filtered)