class Client:
    def __init__(self, client, balance):
        self.client = client
        self.balance = balance

    def get_client(self):
        return self.client

    def get_balance(self):
        return self.balance

    def get_wallet(self):
        return print('Клиент ' + '"' + str(self.client) + '"' + '. ' + "Баланс: " + str(self.balance) + ' Руб.')


Client_1 = Client("Иван Петров", 50)
Client_1.get_wallet()