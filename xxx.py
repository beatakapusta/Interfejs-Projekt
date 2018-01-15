def __init__(self):
    self.players = 2
    self.colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indygo', 'purple']
    self.numbers = [1, 2, 3, 4, 5, 6, 7]
    self.cards = []
    self.user = []
    self.hand = {}
    self.palette = {}
    self.background = {}
    self.pile = None
    self.active_rule = 'red'
    self.chosen_action = None
    self.turn = 1
    self.win = False
    self.loose = False
    self.secondmove = False
    self.start_move = 0


def start(self):
    self.generate_cards()
    self.hand[1] = Hand(self.generate_hand())
    self.hand[2] = Hand(self.generate_hand())
    self.palette[1] = Palette(self.generate_palette())
    self.palette[2] = Palette(self.generate_palette())
    self.pile = self.generate_pile()
    card = Card('red', 0)
    self.background = Background({0: card})
    self.who_starts()


def show_table(self):
    return self.hand[1], self.hand[2], self.palette[1], self.palette[2], self.pile, self.background


def generate_cards(self):
    # Funkcja generuje karty
    for c in self.colors:
        for n in self.numbers:
            self.cards.append(Card(c, n))
    return self.cards


def generate_hand(self):
    # Funkcja losuje 7 dla gracza
    cards_in_hand = {}
    counter = 7
    i = 0
    for counter in range(0, 7):
        li = len(self.cards)
        li -= 1
        rnumber = (randint(0, li))
        card = self.cards[rnumber]
        cards_in_hand.update({i: card})
        self.cards.pop(rnumber)
        counter -= 1
        i += 1
    return cards_in_hand


def generate_palette(self):
    # Funkcja generuje paletÄ™
    card_in_palette = {}
    li = len(self.cards)
    li -= 1
    rnumber = (randint(0, li))
    card = self.cards[rnumber]
    card_in_palette.update({0: card})
    self.cards.pop(rnumber)
    return card_in_palette


def generate_pile(self):
    shuffle(self.cards)
    self.pile = Pile(self.cards)
    return self.pile


def who_starts(self):
    prompt = Prompt()
    who = self.check_if_win()
    print("who_start")
    print(who)
    if who == True:
        self.start_move = 2
        self.turn = 2
    else:
        self.start_move = 1
        self.turn = 1


def whose_trun(self):
    prompt = Prompt()
    if self.turn == 1:
        return prompt.your_turn
    else:
        return prompt.his_turn


def what_rule(self):
    prompt = Prompt()
    active_rule = self.background.rule()
    if active_rule == 'red':
        return prompt.red
    elif active_rule == 'orange':
        return prompt.orange
    elif active_rule == 'yellow':
        return prompt.yellow
    elif active_rule == 'green':
        return prompt.green
    elif active_rule == 'blue':
        return prompt.blue
    elif active_rule == 'indygo':
        return prompt.indygo
    elif active_rule == 'purple':
        return prompt.purple


def computer_move(self):
    print("computer moves")
    possible_moves = {}
    self.start_move = 3
    if self.turn == 2:
        print("computer move")
        print(self.hand[self.turn])
        for c in self.hand[self.turn].hand.items():
            print(c)
            # palette
            test_hand = copy.deepcopy(self.hand[self.turn])
            test_palette = copy.deepcopy(self.palette[self.turn])
            test_background = copy.deepcopy(self.background)
            print("paleta")
            active_card = test_hand.put_card(id_card=c[0])
            test_palette.add_card(active_card)
            # checking
            active_rule = self.background.rule()
            if self.turn == 1:
                other_turn = 2
            else:
                other_turn = 1
            power_one = self.count_power(active_palette=test_palette, rule=active_rule)
            power_two = self.count_power(active_palette=self.palette[other_turn], rule=active_rule)
            result = self.compare_power(power_one=power_one, power_two=power_two, active_rule=active_rule)
            print("czy mozemy dodaÄ‡ do palety")
            print(result)
            if result != False:
                li = len(possible_moves)
                possible_moves[li] = ("palette", c)
                print('czy dodano possible moeve??')
                print(possible_moves)

            # background
            print(c)
            test_hand = copy.deepcopy(self.hand[self.turn])
            test_palette = copy.deepcopy(self.palette[self.turn])
            test_background = copy.deepcopy(self.background)

            print("tlo")
            active_card = test_hand.put_card(id_card=c[0])
            print(active_card)
            test_background.add_card(active_card)
            # checking
            active_rule = test_background.rule()
            print(test_background)
            print(active_rule)
            if self.turn == 1:
                other_turn = 2
            else:
                other_turn = 1
            power_one = self.count_power(active_palette=test_palette, rule=active_rule)
            power_two = self.count_power(active_palette=self.palette[other_turn], rule=active_rule)
            result = self.compare_power(power_one=power_one, power_two=power_two, active_rule=active_rule)
            if result != False:
                li = len(possible_moves)
                possible_moves.update({li: ("background", c)})
            else:
                print("jeĹ›l tĹ‚o ma reslut flase")
                print(test_hand)
                for b in test_hand.hand.items():
                    print(b)
                    new_test_hand = copy.deepcopy(test_hand)
                    new_test_palette = copy.deepcopy(test_palette)
                    new_test_background = copy.deepcopy(test_background)
                    new_active_card = new_test_hand.put_card(id_card=b[0])
                    new_test_palette.add_card(new_active_card)
                    if self.turn == 1:
                        other_turn = 2
                    else:
                        other_turn = 1
                    new_power_one = self.count_power(active_palette=new_test_palette, rule=active_rule)
                    new_power_two = self.count_power(active_palette=self.palette[other_turn], rule=active_rule)
                    new_result = self.compare_power(power_one=new_power_one, power_two=new_power_two,
                                                    active_rule=active_rule)
                    print("nowy result ==")
                    print(new_result)
                    if new_result != False:
                        li = len(possible_moves)
                        print("new background-palette")
                        possible_moves.update({li: ("background-palette", c, b)})

        print("possible moves")
        print(possible_moves)
        if len(possible_moves) == 0:
            self.win = True
            self.turn = 1
        else:
            shuffle(possible_moves)
            print(possible_moves)
            chosen_move = possible_moves.get(0)
            print("pshuffle ones")
            print(chosen_move)
            print(chosen_move[0])
            print(chosen_move[1][0])
            print(chosen_move[1][1])
            if chosen_move[0] == "background-palette":
                c_move = self.make_move(move_type=chosen_move[0], card_one=chosen_move[1][0],
                                        card_two=chosen_move[2][0])
            else:
                c_move = self.make_move(move_type=chosen_move[0], card_one=chosen_move[1][0])
            self.turn = 1
            return c_move


def make_move(self, move_type, card_one=None, card_two=None, active_pile=True):
    if move_type == "pass":
        print('Sorry looser')
        self.loose = True
        return self.loose
    else:
        if move_type == "palette":
            active_card = self.hand[self.turn].put_card(id_card=card_one)
            self.palette[self.turn].add_card(active_card)
        elif move_type == "background":
            active_card = self.hand[self.turn].put_card(id_card=card_one)
            self.background.add_card(active_card)
            if active_pile == True:
                li = len(self.background.background)
                li -= 1
                rule_number = self.background.get_number()
                if rule_number > len(self.hand[self.turn].hand):
                    from_pile = self.pile.take_one()
                    self.hand[self.turn].add_card(from_pile)

        elif move_type == "background-palette":
            active_card = self.hand[self.turn].put_card(id_card=card_one)
            self.background.add_card(active_card)
            if active_pile == True:
                second_active_card = self.hand[self.turn].put_card(id_card=card_two)
                self.palette[self.turn].add_card(second_active_card)
                li = len(self.background.background)
                li -= 1
                rule_number = self.background.get_number()
                if rule_number > len(self.hand[self.turn].hand):
                    from_pile = self.pile.take_one()
                    self.hand[self.turn].add_card(from_pile)

        result = self.check_if_win()
        prompt = Prompt()
        if result == True:
            if self.secondmove == True:
                self.secondmove = False
            if move_type == "background" or move_type == "palette":
                if self.turn == 1:
                    self.turn = 2
                else:
                    self.turn = 1
            return True
            # return prompt.you_win
        else:
            if move_type == "background":
                self.loose = True
            elif move_type == "palette":
                self.secondmove = True


def check_if_win(self):
    active_rule = self.background.rule()
    print('aaactive rule::')
    print(active_rule)
    if self.turn == 1:
        other_turn = 2
    else:
        other_turn = 1

    print(self.palette[self.turn])
    print(self.palette[other_turn])

    power_one = self.count_power(active_palette=self.palette[self.turn], rule=active_rule)
    print('aaaa')
    print(power_one)
    power_two = self.count_power(active_palette=self.palette[other_turn], rule=active_rule)
    print('aaaa')
    print(power_two)

    result = self.compare_power(power_one=power_one, power_two=power_two, active_rule=active_rule)
    return result


def compare_power(self, power_one, power_two, active_rule):
    if self.turn == 1:
        other_turn = 2
    else:
        other_turn = 1
    print("compare power %d vs %d" % (power_one, power_two))
    if power_one > power_two:
        return True
    elif power_one == power_two:
        power_one_card = self.count_power(active_palette=self.palette[self.turn], rule=active_rule, extra=True)
        power_two_card = self.count_power(active_palette=self.palette[other_turn], rule=active_rule, extra=True)
        print('*power*')
        print("active rule %s" % active_rule)
        print(power_one_card)
        print(power_two_card)
        if power_one_card == None and power_two_card == None:
            return False
        elif power_one_card == None and power_two_card != None:
            return False
        elif power_one_card != None and power_two_card == None:
            return True
        else:
            if power_one_card.number > power_two_card.number:
                return True
            elif power_one_card.number == power_two_card.number:
                power_one_color = self.colors.index(power_one_card.color)
                print('**indexy')
                power_two_color = self.colors.index(power_two_card.color)
                print(power_one_color)
                print(power_two_color)
                if power_one_color < power_two_color:
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False


def count_power(self, active_palette, rule, extra=False):
    card = 0
    if rule == 'red':
        sorted_palette = sorted(active_palette.palette.items(), key=lambda x: x[1].number, reverse=True)
        b = Test()
        high = 0
        for c in sorted_palette:
            if len(b.hand) == 0:
                b.add_card(c[1])
                high = c[1].number
            else:
                if c[1].number == high:
                    b.add_card(c[1])
        if extra == False:
            return b.hand.get(0).number
        else:
            find_best = self.sort_by_colors(test_palette=b.hand.items())
            print("RED -  karta do porĂłwnaina")
            print(find_best[0])
            return find_best[0]
    elif rule == 'orange':
        # wygrywa najwiÄ™cej kart z tymi samymi liczbami
        # sort po 1. argumencie
        print("we are in ORANGE")
        sorted_palette = sorted(active_palette.palette.items(), key=lambda x: x[1].number)
        print(sorted_palette)
        b = Test()
        last = 0
        best = Test()
        for c in sorted_palette:
            if last == 0:
                last = c[1].number
                b.add_card(c[1])
            elif c[1].number == last:
                b.add_card(c[1])
            else:
                if last != 0:
                    if len(best.hand) < len(b.hand):
                        best = b
                last = c[1].number
                print("last ==")
                print(last)
                b.hand.clear()
                b.add_card(c[1])
        print(b.hand)
        print("wynik orange")
        if len(best.hand) < len(b.hand):
            if extra == False:
                # print (len(b.hand))
                return len(b.hand)
            else:
                find_best = self.sort_by_colors(test_palette=b.hand.items())
                print("orange -  karta do porĂłwnaina 1")
                print(find_best[0])
                return find_best[0]
        else:
            if extra == False:
                print(len(best.hand))
                return len(best.hand)
            else:
                find_best = self.sort_by_colors(test_palette=best.hand.items())
                print("orange -  karta do porĂłwnaina 2")
                print(find_best[0])
                return find_best[0]
    elif rule == 'yellow':
        # wygrywa najwiÄ™cej kart tego samego koloru
        # sort po 2. argumencie
        sorted_palette = self.sort_by_colors(test_palette=active_palette.palette.items())
        print("posortowana paeta kolory")
        print(sorted_palette)
        b = Test()
        last = 0
        best = Test()
        color_name = 0
        for c in sorted_palette.items():
            print("element in sorted palette")
            print(c)
            if color_name == 0:
                color_name = c[1].color
                b.add_card(c[1])
            elif c[1].color == color_name:
                b.add_card(c[1])
            else:
                if last != 0:
                    if len(best.hand) < len(b.hand):
                        best = copy.deepcopy(b)
                color_name = c[1].color
                print(best)
                b.hand.clear()
                print("is it really clean ..")
                print(b)
                b.add_card(c[1])

        print(best.hand)
        print(b.hand)
        print("wynik yellow")
        if len(best.hand) < len(b.hand):
            if extra == False:
                # print (len(b.hand))
                return len(b.hand)
            else:
                find_best = sorted(b.hand.items(), key=lambda x: x[1].number, reverse=True)
                print("orange -  karta do porĂłwnaina1")
                print(find_best[0][1])
                return find_best[0][1]
        elif len(best.hand) == 1 and len(best.hand) == 1:
            if extra == True:
                find_best = sorted(active_palette.palette.items(), key=lambda x: x[1].number, reverse=True)
                print("orange -  karta do porĂłwnaina2")
                print(find_best[0][1])
                return find_best[0][1]
        elif len(best.hand) < len(b.hand) and extra == True:
            for c in best.hand.items():
                b.add_card(c[1])
            find_best = sorted(b.hand.items(), key=lambda x: x[1].number, reverse=True)
            print("orange -  karta do porĂłwnaina3")
            print(find_best[0][1])
            return find_best[0][1]
        else:
            if extra == False:
                print(len(best.hand))
                return len(best.hand)
            else:
                find_best = sorted(best.hand.items(), key=lambda x: x[1].number, reverse=True)
                print("orange -  karta do porĂłwnaina")
                print(find_best[0][1])
                return find_best[0][1]
    elif rule == 'green':
        # wygrywa najwiÄ™cej kart tego parzystych
        sorted_palette = sorted(active_palette.palette.items(), key=lambda x: x[1].number, reverse=True)
        b = Test()
        for c in sorted_palette:
            if c[1].number % 2 == 0:
                b.add_card(c[1])
        print(b.hand)
        if extra == False:
            return len(b.hand)
        else:
            return b.hand.get(0)
    elif rule == 'blue':
        # wygrywa najwiÄ™cej kart w rĂłĹĽnych kolorach
        sorted_palette = sorted(active_palette.palette.items(), key=lambda x: x[1].number, reverse=True)
        colors = []
        b = Test()
        for c in sorted_palette:
            if c[1].color not in colors:
                colors.append(c[1].color)
                b.add_card(c[1])
        if extra == False:
            return len(b.hand)
        else:
            return b.hand.get(0)
    elif rule == 'indygo':
        # wygrywa najwiÄ™cej kart z kolejnymi liczbami
        print('INDYGO RULE')
        sorted_palette = sorted(active_palette.palette.items(), key=lambda x: x[1].number)
        b = Test()
        n = 0
        count = 0
        best = Test()
        for c in sorted_palette:
            if c[1].number == (n + 1):
                n += 1
                b.add_card(c[1])
            elif c[1].number > (n + 1):
                n = c[1].number
                if len(best.hand) < len(b.hand):
                    best = b
                b.hand.clear()
                b.add_card(c[1])

        if len(best.hand) < len(b.hand):
            if extra == False:
                # print (len(b.hand))
                return len(b.hand)
            else:
                find_best = sorted(b.hand.items(), key=lambda x: x[1].number, reverse=True)
                print("purple -  karta do porĂłwnaina")
                print(find_best[0][1])
                return find_best[0][1]
        else:
            if extra == False:
                print(len(best.hand))
                return len(best.hand)
            else:
                find_best = sorted(best.hand.items(), key=lambda x: x[1].number, reverse=True)
                print("purple -  karta do porĂłwnaina")
                print(find_best[0][1])
                return find_best[0][1]
    elif rule == 'purple':
        # wygrywa najwiÄ™cej kart z cyframi poniĹĽej 4
        sorted_palette = sorted(active_palette.palette.items(), key=lambda x: x[1].number, reverse=True)
        b = Test()
        for c in sorted_palette:
            if c[1].number < 4:
                b.add_card(c[1])
        print(b.hand)
        if extra == False:
            return len(b.hand)
        else:
            return b.hand.get(0)


def sort_by_colors(self, test_palette):
    new_palette = Test()
    for c in self.colors:
        for a in test_palette:
            # print("wesz to wyprintuj")
            # print(a)
            if a[1].color == c:
                new_palette.add_card(a[1])
    return new_palette.hand


#######################################################################################################

# OTHER CLASSES

class Card():
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __repr__(self):
        return '%s %d' % (self.color, self.number)


class Test():
    def __init__(self):
        self.hand = {}

    def __repr__(self):
        return str(self.hand)

    def lenght(self):
        li = len(self.hand)
        return li

    def add_card(self, card):
        li = len(self.hand)
        self.hand.update({li: card})
        return self.hand

    def put_card(self, id_card):
        card = self.hand.get(int(id_card))
        self.hand.pop(int(id_card), None)
        return card


class Hand():
    def __init__(self, hand):
        self.hand = hand

    def __repr__(self):
        return str(self.hand)

    def lenght(self):
        li = len(self.hand)
        return li

    def add_card(self, card):
        li = len(self.hand)
        self.hand.update({li: card})
        return self.hand

    def put_card(self, id_card):
        card = self.hand.get(int(id_card))
        self.hand.pop(int(id_card), None)
        return card


class Palette():
    def __init__(self, palette):
        self.palette = palette

    def __repr__(self):
        return str(self.palette)

    def add_card(self, card):
        li = len(self.palette)
        self.palette.update({li: card})
        return self.palette

    def put_card(self, id_card):
        card = self.palette.get(int(id_card))
        self.palette.pop(int(id_card), None)
        return card


class Pile():
    def __init__(self, pile):
        self.pile = pile

    def __repr__(self):
        return str(self.pile)

    def take_one(self):
        lenght = len(self.pile)
        return self.pile.pop(lenght - 1)


class Background():
    def __init__(self, background):
        self.background = background

    def __repr__(self):
        li = len(self.background)
        li -= 1
        last_card = self.background[li]
        return str(self.background)

    def get_last(self):
        li = len(self.background)
        li -= 1
        last_card = self.background[li]
        return last_card

    def add_card(self, card):
        li = len(self.background)
        self.background.update({li: card})
        return self.background

    def put_card(self, id_card):
        card = self.background.get(int(id_card))
        self.background.pop(int(id_card), None)
        return card

    def rule(self):
        li = len(self.background)
        li -= 1
        last_card = self.background[li]
        rule = last_card.color
        return rule

    def get_number(self):
        li = len(self.background)
        li -= 1
        last_card = self.background[li]
        return last_card.number
