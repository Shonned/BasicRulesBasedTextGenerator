class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.advisors = []
        self.clients = []

    def new_arrival(self, client):
        print("Welcome " + client.get_name() + " to Bank of Aberdeen, an advisor should arrive")

    def add_advisor(self, advisor):
        self.advisors.append(advisor)

    def add_client(self, client):
        self.clients.append(client)

    def get_advisors(self):
        return self.advisors

    def get_clients(self):
        return self.clients

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address
