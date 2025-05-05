age = int(input('what\'s your age ? ').strip())

month = age * 12
weeks = month * 4
days = age * 365

hours = days * 24
minuts = hours * 60
seconds = minuts * 60

print(f"You lives for : \
    \n{month} Month, \
    \n{weeks:,} Weeks, \
    \n{days:,} Days, \
        \n{hours:,} Hours, \
            \n{minuts:,} Minuts, \
                \n{seconds:,} Seconds, \
        ")
