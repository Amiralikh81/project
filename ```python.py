cclass Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def bet(self, amount):
        if amount > self.money:
            print(f"{self.name} does not have enough money to bet {amount}.")
        else:
            self.money -= amount
            print(f"{self.name} bet {amount}. Remaining money: {self.money}")


def main():
    num_players = int(input("Enter the number of players: "))
    players = []

    for i in range(num_players):
        name = input(f"Enter player {i+1}'s name: ")
        money = int(input(f"Enter {name}'s initial money: "))
        players.append(Player(name, money))

    while True:
        for player in players:
            bet_amount = int(input(f"{player.name}'s turn to bet. Enter bet amount: "))
            player.bet(bet_amount)

        play_again = input("Do you want to play another round? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

