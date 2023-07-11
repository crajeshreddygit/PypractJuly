class Movie:
    """ This is movie class developed by Rajesh"""
    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine
    def info(self):
        print("Movie name :", self.title)
        print("Hero name :", self.hero)
        print("Heroine name :", self.heroine)

list_of_movies = []
while True:
    title = input("Enter Movie name")
    Hero = input("Enter Hero name")
    Heroin = input("Enter Heroine name")
    m = Movie(title,Hero,Heroin)
    list_of_movies.append(m)
    print("Movie added Successfully")
    option = input("Do you want to add more [Yes/No")
    if option.lower() == "no":
        break

print(" All Movies Information")
for m in list_of_movies:
    m.info()
    print("-----------")
