import random
import math


def roll_dice(faces_of_dice=6, num_dice=2):
    dice_sum = 0
    for i in range(num_dice):
        dice_sum += random.randint(1, faces_of_dice)
    return dice_sum


def compute_rolls(num_rolls=100000):
    results = {
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
        21: 0,
        22: 0,
        23: 0,
        24: 0,
        25: 0,
        26: 0,
        27: 0,
        28: 0,
        29: 0,
        30: 0,
        31: 0,
        32: 0,
        33: 0,
        34: 0,
        35: 0,
        36: 0,
        37: 0,
        38: 0,
        39: 0,
        40: 0,
    }
    for n in range(num_rolls):
        results[roll_dice()] += 1
    for key in results:
        results[key] = results[key]/(num_rolls/100)
    return results


print(compute_rolls(10000000))


def predict_rolls(faces=6, dice_num=2):
    predictions = {}
    denominator = faces ** dice_num # exponentiation
    for x in range(2, 2 * faces + 1):
        numerator = math.comb(x-1, dice_num-1)
        predictions[x] = math.trunc((numerator/denominator)*100000)/1000 # sets format
    return predictions


print(predict_rolls())
