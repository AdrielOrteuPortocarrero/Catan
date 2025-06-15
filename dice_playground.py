import random
import math
def roll_dice(faces_of_dice=6):
    die1 = random.randint(1, faces_of_dice)
    die2 = random.randint(1, faces_of_dice)
    return die1 + die2

def compute_rolls():
    results ={
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0,
        10:0,
        11:0,
        12:0,
        13:0,
        14:0,
        15:0,
        16:0,
        17:0,
        18:0,
        19:0,
        20:0,
        21:0,
        22:0,
        23:0,
        24:0,
        25:0,
        26:0,
        27:0,
        28:0,
        29:0,
        30:0,
        31:0,
        32:0,
        33:0,
        34:0,
        35:0,
        36:0,
        37:0,
        38:0,
        39:0,
        40:0,
    }

    for n in range(100000):
        results[roll_dice()] += 1
    return results

print (compute_rolls())


def predict_rolls(n=100, dice_num=15):
    predictions = {}
    denominator = n * n
    for x in range(2, 2*n+1):
        numerator = math.comb(x-1, dice_num-1)
        predictions[x] = (numerator/denominator)*100

    return predictions

print(predict_rolls())