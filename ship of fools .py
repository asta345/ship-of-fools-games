from random import randint
class Die():
    def __init__(avi):
        avi._value=1
        avi.roll()

    def roll(avi):
        avi._value= randint(1,6)

    def get_value(avi):
        return avi._value

    def print_dice(avi):
        print(" ___ ")
        if avi._value == 1:
            print("|   |")
            print("| 0 |")
            print("|   |")
        elif avi._value == 2:
            print("|   |")
            print("|0 0|")
            print("|   |")
        elif avi._value == 3:
            print("|   |")
            print("|000|")
            print("|   |")
        elif avi._value == 4:
            print("|0 0|")
            print("|   |")
            print("|0 0|")
        elif avi._value == 5:
            print("|0 0|")
            print("| 0 |")
            print("|0 0|")
        elif avi._value == 6:
            print("|0 0|")
            print("|0 0|")
            print("|0 0|")
        print(" --- ")

       
class DiceCup():
    def __init__(avi,no=5):
        avi.no=no
        die1=Die()
        die2=Die()
        die3=Die()
        die4=Die()
        die5=Die()
        avi._dice=[die1,die2,die3,die4,die5]
        avi.dice_banked=[False,False,False,False,False]

    def roll(avi):
        dice_index = 1
        for each_die in avi._dice:
            index_value=avi._dice.index(each_die)
            if not avi.dice_banked[index_value]:
                each_die.roll()
            print("Dice {000}".format(dice_index))
            each_die.print_dice()
            dice_index +=1

    def value(avi,index):
        return avi._dice[index].get_value()

    def bank(avi,index):
        avi.dice_banked[index]=True    

    def is_banked(avi,index):
        return avi.dice_banked[index]

    def release(avi,index):
        avi.dice_banked[index]=False

    def release_all(avi):
        for i in range(len(avi.dice_banked)):
            avi.dice_banked[i]=False


class ShipOfFoolsGame():
    def __init__(self,winning_score):
        self._cup=DiceCup()
        self._winning_score=winning_score

    def round(self):
        has_ship=False
        has_captain=False
        has_crew=False
       
        crew=0
        for i in range(3):
            continue_round = True
            if(crew > 0):
                while not True:
                    decision = input("NEXT ROUND (YES or NO)?: ")
                    if decision == "NO":
                        continue_round = False
                        break
                    elif decision == "YES":
                        break
                    else:
                        print("Enter a valid choice!")
            else:
                input("Press any key to play the round\n")
            if continue_round:
                self._cup.roll()
                rolled_values = []
                for j in range(5):
                    rolled_values.append(self._cup.value(j))
                if not has_ship and 6 in rolled_values:
                    self._cup.bank(rolled_values.index(6))
                    has_ship=True
                if has_ship and not has_captain and 5 in rolled_values:
                    self._cup.bank(rolled_values.index(5))
                    has_captain=True
                if has_ship and has_captain and not has_crew and 4 in rolled_values:
                    self._cup.bank(rolled_values.index(4))
                    has_crew=True
                if has_ship and has_captain and has_crew:
                    self._cup.bank(rolled_values.index(6))
                    self._cup.bank(rolled_values.index(5))
                    self._cup.bank(rolled_values.index(4))
                    crew = sum(rolled_values) - 15
                print("Round {0} score: {1}\n\n".format(i+1,crew))
            else:
                break
        self._cup.release_all()
        return crew
   
       

class PlayRoom():

    def __init__(self):
        self._game=None
        self._players=[]
   
    def set_game(self,ShipOfFoolsGame):
        self._game=ShipOfFoolsGame

    def add_player(self,player):
        self._players.append(player)
   
    def reset_scores(self):
        for player in self._players:
            player.reset_score()

    def play_round(self):
        i = 1
        for player in self._players:
            print("\nPlayer{0}: {1}\n".format(i,player._name))
            player.play_round(self._game)
            i = i+1

    def game_finished(self):
        for player in self._players:
        	if player._score >= self._game._winning_score:
        		return True
        return False

    def print_scores(self):
        for player in self._players:
            print(player._name,player.current_score(),end=" ")
        print("\n\n")

    def print_winner(self):
        max_score=0
        winner=None
        draw = False
        for player in self._players:
            if player.current_score() == max_score:
                draw = True
            if player.current_score() > max_score:
                winner = player
                max_score = player.current_score()
                draw = False
        if winner != None and not draw:
            print("Winner is {0} with score {1}".format(winner._name,winner._score))
        else:
            print("!!!!!!!IT'S tie!!!!!!!")
        print("\n")



class Player():
    def __init__(self):
        self._name=None
        self._score=0
    def set_name(self,name):
        self._name = name
    def current_score(self):
        return self._score
    def reset_score(self):
        self._score = 0
    def play_round(self,ShipOfFools):
        self._score += ShipOfFools.round()
   
       
   
       
if __name__ == "__main__":
    winning_score = int(input("Enter winning score: "))

    game = ShipOfFoolsGame(winning_score)

    gameRoom = PlayRoom()
    gameRoom.set_game(game)

    player1 = Player()
    player1.set_name(input("Enter player1's name: "))
    gameRoom.add_player(player1)

    player2 = Player()
    player2.set_name(input("Enter player2's name: "))
    gameRoom.add_player(player2)

    gameRoom.reset_scores()

    while not gameRoom.game_finished():
    	gameRoom.play_round()
    	gameRoom.print_scores()
    gameRoom.print_winner()