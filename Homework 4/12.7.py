#Dan Doan 1986920
#first def return the heart rate
def fat_burning_heart_rate(age):
    return (220-age)*.7
#2nd def ask for input, check if age is correct, if yes it continues to print and call the other
#function to get the answer, if not it raises the ValueError and prints
def get_age():
    age = int(input())
    if 18<=age<=75:
        print("Fat burning heart rate for a {} year-old: {} bpm".format(age, fat_burning_heart_rate(age)))
    else:
        print("Invalid age.")
        raise ValueError

#main tries to call the 2nd function, then if there is a ValueError, it will print could not be done
if __name__ == "__main__":
    try:
        get_age()
    except ValueError:
        print("Could not calculate heart rate info.")
        print()