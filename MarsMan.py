#Lucy Kull
#CS 101, Professor Hare
#Program 1 Part 1

print("Welcome to Mars!")

# Ask how many rations Mark has?
Rations = input("How many ration packs do you have? ")
print('')

# Ask how many calories per day he eats?
Calories = input("How many calories a day do you consume? ")
print('')

# Ask how many square meters of he will devote to growing crops
SqMeters = input("How many square meters will you be using to grow crops? ")
print('')

Rations = float(Rations)
Calories = float(Calories)
SqMeters = float(SqMeters)

# Firgure out how long he can last on his rations
RationCalories = Rations * 2000
RationDays = RationCalories / Calories
print("If you only ate ration packs, you would have", RationDays, "days to live.")
print('')
print("Your potatoes are growing, please wait")
print('')

# How much soil he will need
Soil = SqMeters / 10

# How much water he will need
# DONT FORGET UNITS!
Water = SqMeters * 40

# How many kg of potatoes he can grow
Potatoes = RationDays * SqMeters * 0.006

# How long that will last him
PotatoCalories = Potatoes * 700
PotatoDays = PotatoCalories / Calories
print("Your potatoes have gained you", PotatoDays, "extra days of life")
print('')
MarsDays = PotatoDays + RationDays
print("With this food, you have survived", MarsDays, "days on Mars!")
print('')
if MarsDays >= 260:
    print("Congratulations! ")
    print("You survived long enough for someone on Earth to save you!")
if MarsDays < 260:
    print("Sadly, you did not survive long enough for someone on Earth could pick you up.")
