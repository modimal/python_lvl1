# coding: utf-8


class School:
    def __init__(self, number):
        self.number = number
        self._all_classes = set()

    def add_class(self, class_room):
        self._all_classes.add(class_room)

    @property
    def all_classes(self):
        return ', '.join([c.class_id for c in self._all_classes])

    def teachers_in_class(self, class_id):
        for c in self._all_classes:
            if c.class_id == class_id:
                return c.format_teachers()

    def _search_certain_student(self, stud_id):
        cur_class, student = None, None
        for c in self._all_classes:
            for s in c.students:
                if s.stud_id == stud_id:
                    cur_class, student = c, s
                    break

        if student is None:
            raise ValueError('Студента с id {} в классе {} не существует.'
                             .format(stud_id, cur_class.class_id))
        return cur_class, student

    def student_subjects(self, stud_id):
        cur_class, student = self._search_certain_student(stud_id)

        return '\nВсе предметы ученика {} из класса {}:\n{}'\
            .format(student.fullname, cur_class.class_id,
                    ', '.join([t.subject.name for t in cur_class.teachers]))

    def student_parents(self, stud_id):
        cur_class, student = self._search_certain_student(stud_id)

        return '\nФ.И.О. родителей ученика {} из класса {}:\nМама: {}\nПапа: {}'\
            .format(student.fullname, cur_class.class_id, student.mom.fullname, student.dad.fullname)

    def __str__(self):
        return '\nВсе классы школы №{}:\n{}'.format(self.number, self.all_classes)


class Subject:
    def __init__(self, name):
        self.name = name


class Human:
    def __init__(self, firstname, lastname, patronymic):
        self.firstname = firstname
        self.lastname = lastname
        self.patronymic = patronymic

    @property
    def fullname(self):
        return self.firstname + ' ' + self.lastname + ' ' + self.patronymic


class Teacher(Human):
    def __init__(self, firstname, lastname, patronymic, subject):
        super().__init__(firstname, lastname, patronymic)
        self.subject = subject  # Экземпляр класса Subject


class Class:
    def __init__(self, school, class_id):
        self.class_id = class_id
        self._teachers = set()  # Множество экземпляров класса Teacher
        self._students = set()  # Множество экземпляров класса Student
        school.add_class(self)  # При создании нового класса, добавляем его в школу

    @property
    def students(self):
        return self._students

    def format_students(self):
        return '\nВсе ученики класса {}:\n{}'\
            .format(self.class_id, '\n'.join([s.fullname for s in self.students]))

    def add_student(self, student):
        self._students.add(student)

    @property
    def teachers(self):
        return self._teachers

    def format_teachers(self):
        return '\nВсе учителя класса {}:\n{}' \
            .format(self.class_id, '\n'.join([t.fullname for t in self.teachers]))

    def add_teacher(self, student):
        self._teachers.add(student)


class Parent(Human):
    def __init__(self, firstname, lastname, patronymic):
        super().__init__(firstname, lastname, patronymic)


class Student(Human):
    def __init__(self, stud_id, firstname, lastname, patronymic, mom, dad):
        super().__init__(firstname, lastname, patronymic)
        self.stud_id = stud_id
        self.mom = mom  # Экземпляр класса Parent
        self.dad = dad  # Экземпляр класса Parent
        self._subjects = set()  # Множество экземпляров класса Subject


school173 = School('173')

class_7A = Class(school173, '7A')
class_8B = Class(school173, '8B')
class_9C = Class(school173, '9C')

print(school173)

# Добавление учителей в класс 8B

class_8B.add_teacher(
    Teacher(
        'Сергей', 'Громов', 'Синькеевич',
        Subject('Математика')
    )
)
class_8B.add_teacher(
    Teacher(
        'Анатолий', 'Гроцков', 'Викторович',
        Subject('География')
    )
)
class_8B.add_teacher(
    Teacher(
        'Дмитрий', 'Смирнов', 'Васильевич',
        Subject('Программирование')
    )
)

# Добавление учителей в класс 7A

class_7A.add_teacher(
    Teacher(
        'Сергей', 'Громов', 'Синькеевич',
        Subject('Биология')
    )
)
class_7A.add_teacher(
    Teacher(
        'Анатолий', 'Гроцков', 'Викторович',
        Subject('Русский язык')
    )
)
class_7A.add_teacher(
    Teacher(
        'Дмитрий', 'Смирнов', 'Васильевич',
        Subject('История России')
    )
)

# Добавление учителей в класс 9С

class_9C.add_teacher(
    Teacher(
        'Сергей', 'Громов', 'Синькеевич',
        Subject('История Мира')
    )
)
class_9C.add_teacher(
    Teacher(
        'Анатолий', 'Гроцков', 'Викторович',
        Subject('Физика')
    )
)
class_9C.add_teacher(
    Teacher(
        'Дмитрий', 'Смирнов', 'Васильевич',
        Subject('Черчение')
    )
)

# Добавление студентов

class_8B.add_student(
    Student(
        '002',
        'Иван', 'Петров', 'Сергеевич',
        Parent('Наталья', 'Петрова', 'Сергеевна'),
        Parent('Сергей', 'Петров', 'Дмитриевич'),
    )
)
class_8B.add_student(
    Student(
        '003',
        'Иван', 'Сергеев', 'Дмитриевич',
        Parent('Анна', 'Сергеева', 'Ивановна'),
        Parent('Дмитрий', 'Петров', 'Алексеевич'),
    )
)
class_8B.add_student(
    Student(
        '004',
        'Алексей', 'Скворцов', 'Анатольевич',
        Parent('Лариса', 'Скворцова', 'Петровна'),
        Parent('Анатолий', 'Скворцов', 'Александрович'),
    )
)

class_7A.add_student(
    Student(
        '001',
        'Алексей', 'Петров', 'Сергеевич',
        Parent('Наталья', 'Петрова', 'Сергеевна'),
        Parent('Сергей', 'Петров', 'Дмитриевич'),
    )
)
class_9C.add_student(
    Student(
        '005',
        'Дмитрий', 'Сергеев', 'Дмитриевич',
        Parent('Анна', 'Сергеева', 'Ивановна'),
        Parent('Дмитрий', 'Петров', 'Алексеевич'),
    )
)

print(class_8B.format_students())
print(school173.student_subjects('005'))
print(school173.student_parents('004'))
print(school173.teachers_in_class('8B'))
