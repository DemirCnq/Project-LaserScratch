from Utility.ByteStream import Reader


class AccountSwitchedMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.SwitchedToAccountId = self.readLong()
        self.readByte()
        self.readString()


    def process(self):
        pass