# 1.Define a function, 
# which will be given an hour (always in the range of 1 to 12, inclusive),
# a minute (always in the range of 0 to 59, inclusive), 
# and a period (either "am" or "pm") as input.
# 2.Return a four-digit string that encodes that time in 24-hour time.


def convert(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    return f"{hour:02d}{minute:02d}"

hour = int(input('Enter hour: '))
minute = int(input('Enter minute: '))
period = input('Enter period: ')
time = convert(hour, minute, period)
print(time)



