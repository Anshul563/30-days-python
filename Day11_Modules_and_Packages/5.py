import datetime

# Get current date and time
now = datetime.datetime.now()
print(now) 
# Output: 2023-10-27 15:45:12.123456 (format varies)

# Get just the current date (no time)
today = datetime.date.today()
print(today) 
# Output: 2023-10-27