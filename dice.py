class Dice:
    layers = [
        "+---------+",
        "|         |",
        [
            "|         |",
            "|     o   |",
            "|     o   |",
            "|  o   o  |",
            "|  o   o  |",
            "|  o   o  |"
        ],
        [
            "|    o    |",
            "|         |",
            "|    o    |",
            "|         |",
            "|    o    |",
            "|  o   o  |",
        ],
        [
            "|         |",
            "|   o     |",
            "|   o     |",
            "|  o   o  |",
            "|  o   o  |",
            "|  o   o  |",
        ],
        "|         |",
        "+---------+"
    ]

    def __init__(self, n):
        self.n = n

    def layer(self, n_layer):
        return self.layers[n_layer] if type(self.layers[n_layer]) == str else self.layers[n_layer][self.n - 1]


