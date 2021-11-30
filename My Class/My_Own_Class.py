#Zane Burklin, Assignment 10.1 Your Own Class
#This program is designed to create my own class based on a real object, and make functions and subclasses for it.
#Thanks to professor Hari for teaching me about classes and thanks to my roommate for helping me think things through.



#This code creates my parent Class.
class Bread:
    def __init__(self, name, days_old):
        self.name = ""
        self.name = name
        self.days_old = ""
        self.days_old = days_old
    def get_days(self):
        print (f"This {self.name} is {self.days_old} days old.")
    def set_self(self, cost):
        self.cost = ""
        self.cost = cost
    def determine_expensive(self):
        if float(self.cost) > 5.00:
            print (f"Dang! This {self.name} is expensive!")
        else:
            print (f"Nice! This {self.name} isn't too expensive.")
    def buy_or_nah(self):
        if float(self.cost) <= 5.00 and float(self.days_old) <= 1:
            print (f"Yo... Five dollars or less AND it's baked fresh???? Yeah, this {self.name} is a cop.")
        elif float(self.cost) <= 5.00 and float(self.days_old) > 1:
            print (f"Well, this {self.name} isn't baked fresh, but it is cheap. Probably a good buy.")
        elif float(self.cost) > 5.00 and float(self.days_old) <= 1:
            print (f"Well, this {self.name} is baked fresh, but it'll cost you... Probably a good buy, if you're willing to spend.")
        elif float(self.cost) > 10.00 or float(self.days_old) > 7:
            print (f"Yikes, I don't know if I'd buy this {self.name}...")



#This code creates a main function, and tests the code I've created.
def main():
    x = Bread("Wheat Bread", "1")
    x.set_self(4.99)
    x.get_days()
    x.determine_expensive()
    x.buy_or_nah()



if __name__ == "__main__":
    main()