class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address      # Тип данных Address
        self.from_address = from_address  # Тип данных Address
        self.cost = cost
        self.track = track
