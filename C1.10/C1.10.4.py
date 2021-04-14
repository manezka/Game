class Guests:

    def __init__(self, name, town, status):
        self.name = name
        self.town = town
        self.status = status

class Man(Guests):
    def get_volunteer(self):
        return print(str(self.name) + ', ' + 'г. ' + str(self.town) + ', ' + 'статус ' + '"' + str(self.status) + '"')

Vol_1 = Man('Иван Петров', 'Москва', 'Наставник')
Vol_2 = Man('Анна Иванова', 'СПБ', 'Ветеринар')
Vol_3 = Man('Евгений Олегов', 'Казань', 'Писатель')
volunteer = [Vol_1, Vol_2, Vol_3]
for i in volunteer:
    print(i.get_volunteer())