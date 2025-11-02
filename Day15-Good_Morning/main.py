import time

hour = int(time.strftime('%H'))
if 4 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 16:
    print("Good Afternoon!")
elif 16 <= hour < 18:
    print("Good Evening!")
else:
    print("Good Night!")
# https://docs.python.org/3/library/time.html#time.strftime