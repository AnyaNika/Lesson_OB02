# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников
# на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять
# пользователя из системы.

# Требования:
#
# 1.Класс `User': Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа
# ('user' для обычных сотрудников).

class User:
    def __init__(self, ID, name, access_level = "user"):
        self.__ID = ID
        self.__name = name
        self.__access_level = access_level

    # 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь
    # доступ к необходимым атрибутам через методы (например, get и set методы).
    
    def get_id(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_access_level(self):
        return self.__access_level

    def set_access_level(self, access_level):
        self.__access_level = access_level

# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin').

class Admin(User):
    def __init__(self, ID, name):
        super().__init__(ID, name, access_level = "admin")
        self.users = []  # список для хранения пользователей

# Класс должен также содержать методы add_user и remove_user, которые
# позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
    def add_user(self, user):

        if isinstance(user, User):
            self.users.append(user)
            print(f"Сотрудник {user.get_name()} добавлен в список")
        else:
            print("Ошибка: добавляемый объект не является сотрудником")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"Сотрудник {user.get_name()} удален из списка")
        else:
            print(f"Сотрудник {user.get_name()} не найден в списке")

# Пример использования:
admin = Admin(1, "Леша")
user1 = User(2, "Петя")
user2 = User(3, "Таня")

admin.add_user(user1)
admin.add_user(user2)
admin.remove_user(user1)

