"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    rating = score_calc(score)
    print(rating)




def score_calc(score):
    if (score < 0) or (score > 100):
        rating = str("Invalid score")
        return rating
    elif score < 50:
        rating = str("Bad")
        return rating
    elif score < 90:
        rating = str("Passable")
        return rating
    else:
        rating = str("Excellent!")
        return rating


main()