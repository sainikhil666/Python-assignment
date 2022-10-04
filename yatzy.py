import random
import math
from collections import namedtuple

play = namedtuple('play', ['name', 'score_pad', 'dice'])
print("---------------------Welcome to the yazty game---------------------")
current_selections = 0

score_pad = {"ones": 0, "twos": 0, "threes": 0, "fours": 0, "fives": 0, "sixes": 0, "pair": 0, "two_pair": 0,
             "three_of_kind": 0, "four_of_kind": 0, "small_strght": 0, "large_strght": 0, "full_house": 0, "chance": 0,
             "yatzy": 0}


def instructions():
    print("------------------------Choose ones------------------------")
    yield 0
    print("------------------------Choose twos------------------------")
    yield 1
    print("------------------------Choose threes------------------------")
    yield 2
    print("------------------------Choose fours------------------------")
    yield 3
    print("------------------------Choose fives------------------------")
    yield 4
    print("------------------------Choose sixes------------------------")
    yield 5
    print("------------------------Choose pair------------------------")
    yield 6
    print("------------------------Choose two pairs------------------------")
    yield 7
    print("------------------------Choose three of kind------------------------")
    yield 8
    print("------------------------Choose four of kind------------------------")
    yield 9
    print("------------------------Choose small straight------------------------")
    yield 10
    print("------------------------Choose large straight------------------------")
    yield 11
    print("------------------------Choose full house------------------------")
    yield 12
    print("------------------------Choose chance------------------------")
    yield 13
    print("------------------------Choose yazty------------------------")
    yield 14


def dice_roll(chance_no):
    dice_list1 = []
    dice_list2 = []
    dice_list3 = []
    keep_lst = []
    for chance in range(1, 4):
        if chance == 1:
            # Trail 1
            for i in range(0, 5):
                dice_list1.append(random.randint(1, 6))
            print("The dice values for the first trail are:", dice_list1)
            print('Enter the no. of dices you want to keep: ')
            diceskept = int(input())  # diceskept is used to know how many dices player is keeping
            for j in range(0, diceskept):
                print('Enter the index value of dices you want to keep:')
                temp = int(input())
                keep_lst.append(dice_list1[temp])
            yield keep_lst
        if diceskept < 5:
            if chance == 2:
                # Trail 2
                for i in range(0, 5 - diceskept):
                    dice_list2.append(random.randint(1, 6))
                print("The dice values for the second trail are:", dice_list2)
                print('Enter the no. of dices you want to keep: ')
                diceskept2 = int(input())
                diceskept = diceskept + diceskept2
                for j in range(0, diceskept2):
                    print('Enter the index value of dices you want to keep:')
                    temp = int(input())
                    keep_lst.append(dice_list2[temp])
                print(keep_lst)
                dices_removed = int(input("Enter the number of kept dices you want to reroll (Remaining dices will reroll by default):"))
                while dices_removed > diceskept:
                    dices_removed = int(input("You have asked to reroll the dices than you've kept. Please enter appropriate value: "))
                    
                if diceskept == 0:
                    print("You haven't kept any dices")
                    yield keep_lst
                diceskept = diceskept - dices_removed
                for i in range(dices_removed):
                    print("Selected list: ", keep_lst)
                    temp4 = int(input("Enter the index value of dice you want to remove from selected list:"))
                    print("Dice removed: ", keep_lst.pop(temp4))
                yield keep_lst
            if chance == 3:
                # Trail 3
                for i in range(0, 5 - diceskept):
                    dice_list3.append(random.randint(1, 6))
                print("The dice values for the last trail are: ", dice_list3)
                for i in range(0, len(dice_list3)):
                    keep_lst.append(dice_list3[i])
                yield keep_lst
        else:
            yield keep_lst


def counter(dies, k):
    count = 0
    for i in range(0, len(dies)):
        if dies[i] == k:
            count += 1
    return count


def one(dies):
    return counter(dies, 1)


def two(dies):
    return 2 * counter(dies, 2)


def three(dies):
    return 3 * counter(dies, 3)


def four(dies):
    return 4 * counter(dies, 4)


def five(dies):
    return 5 * counter(dies, 5)


def six(dies):
    return 6 * counter(dies, 6)


def pair(dies):
    pairs = [0]
    for i in range(1, 7):
        if counter(dies, i) == 2:
            pairs.append(i)

    return 2 * max(pairs)


def two_pairs(dies):
    pairs = [0]
    for i in range(1, 7):
        if counter(dies, i) == 2:
            pairs.append(i)
    if len(pairs) == 3:
        return 2 * (sum(pairs))
    else:
        return 0


def three_of_kind(dies):
    for i in range(1, 7):
        if counter(dies, i) >= 3:
            return 3 * i
    return 0


def four_of_kind(dies):
    for i in range(1, 7):
        if counter(dies, i) >= 4:
            return 4 * i
    return 0


def small_strght(dies):
    cnt = 0
    for i in range(1, 6):
        if counter(dies, i) == 1:
            cnt += 1
    if cnt == 5:
        return 15
    else:
        return 0


def large_strght(dies):
    cnt = 0
    for i in range(2, 7):
        if counter(dies, i) == 1:
            cnt += 1
    if cnt == 5:
        return 20
    else:
        return 0


def full_house(dies):
    a = three_of_kind(dies)
    b = pair(dies)
    if a != 0 and b != 0:
        return (a + b)
    else:
        return 0


def chance(dies):
    return sum(dies)


def yatzy(dies):
    for i in range(1, 7):
        if counter(dies, i) == 5:
            return 50
    return 0


i = 1
j = 1
dices = []
players = []
players1 = []
print("Enter player names. Type 'start' to start the game. Minimum two players are required.")
while (j == 1):
    ch = input("Enter player " + str(i) + " name:")

    if ch == "start":
        if i >= 2:
            break
        else:
            print("Atleast two players are required.")
    p_name = str(ch)
    tmp = (p_name, score_pad, dices)
    players.append(tmp)
    players1.append(play(p_name, score_pad, dices))
    i += 1

random.shuffle(players)
play.name = players
print(players1)
print(play)
for i in range(0, len(play.name)):
    print("Player", i + 1, ":", play.name[i][0])
tt = {}
for items in instructions():
    j = items
    for r in range(0, len(play.name)):
        # current_selections = 0
        print("Turn for player " + str(r + 1) + " ", play.name[r][0], ":\n")
        print("*************************Rolling the dice*************************\n")
        t = 0
        dice = []
        dicee = {}
        for i in range(0,len(play.name)):
            dicee[i] = {

            }
        for item in dice_roll(j):
            selected_dice = item

        players1[r][2].append(selected_dice)

        if j == 0:
            score = one(selected_dice)
            players1[r][1]["ones"] = score
            players[r][1]["ones"] = score
            play.score_pad = players
            dicee[r]["ones"] = selected_dice
            play.dice = dicee

            tt[r] = score
        if j == 1:
            score = two(selected_dice)
            players1[r][1]["twos"] = score
            players[r][1]["twos"] = score
            play.score_pad = players
            dicee[r]["twos"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
        if j == 2:
            score = three(selected_dice)
            players1[r][1]["threes"] = score
            players[r][1]["threes"] = score
            play.score_pad = players
            dicee[r]["threes"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
        if j == 3:
            score = four(selected_dice)
            players1[r][1]["fours"] = score
            players[r][1]["fours"] = score
            play.score_pad = players
            dicee[r]["fours"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
        if j == 4:
            score = five(selected_dice)
            players1[r][1]["fives"] = score
            players[r][1]["fives"] = score
            play.score_pad = players
            dicee[r]["fives"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
        if j == 5:
            score = six(selected_dice)
            players1[r][1]["sixes"] = score
            players[r][1]["sixes"] = score
            play.score_pad = players
            dicee[r]["sixes"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
        if j == 6:
            score = pair(selected_dice)
            if score == 0:
                if three_of_kind(selected_dice) != 0:
                    score = (three_of_kind(selected_dice) / 3) * 2
            players1[r][1]["pair"] = score
            players[r][1]["pair"] = score
            play.score_pad = players
            dicee[r]["pair"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
        if j == 7:
            score = two_pairs(selected_dice)
            players[r][1]["two_pair"] = score
            players1[r][1]["two_pair"] = score
            play.score_pad = players
            dicee[r]["two_pair"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
        if j == 8:
            score = three_of_kind(selected_dice)
            players[r][1]["three_of_kind"] = score
            players1[r][1]["three_of_kind"] = score
            play.score_pad = players
            dicee[r]["three_of_kind"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
        if j == 9:
            score = four_of_kind(selected_dice)
            players[r][1]["four_of_kind"] = score
            players1[r][1]["four_of_kind"] = score
            play.score_pad = players
            dicee[r]["four_of_kind"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
        if j == 10:
            score = small_strght(selected_dice)
            players[r][1]["small_strght"] = score
            players1[r][1]["small_strght"] = score
            play.score_pad = players
            dicee[r]["small_strght"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
        if j == 11:
            score = large_strght(selected_dice)
            players[r][1]["large_strght"] = score
            players1[r][1]["large_strght"] = score
            play.score_pad = players
            dicee[r]["large_strght"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
        if j == 12:
            score = full_house(selected_dice)
            players[r][1]["full_house"] = score
            players1[r][1]["full_house"] = score
            play.score_pad = players
            dicee[r]["full_house"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
        if j == 13:
            score = chance(selected_dice)
            players[r][1]["chance"] = score
            players1[r][1]["chance"] = score
            play.score_pad = players
            dicee[r]["chance"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
        if j == 14:
            score = yatzy(selected_dice)
            players[r][1]["yatzy"] = score
            players1[r][1]["yatzy"] = score
            play.score_pad = players
            dicee[r]["yatzy"] = selected_dice
            play.dice = dicee
            tt[r] = tt[r] + score
            players[r][2].append(selected_dice)
        print("Score of player " + str(players[r][0]) + " is: ", score)
        print("The final dice numbers for the above round are", selected_dice)
        print("\n")
    j += 1
totalscore = {}
for r in range(0, len(play.name)):
    totalscore[players[r][0]] = tt[r]
print(players1)
print("--------------------------- FINAL SCORES ---------------------------")
tt1 = [ k for k in tt ]
tt2 = [ k for k in tt.values() ]
while len(tt1) != 0:
    for i in range(0, len(tt1)):
        if max(tt2) == tt2[i]:
            print("\t", players[int(tt1[i])][0], tt2[i])
            del tt1[i]
            del tt2[i]
            break
