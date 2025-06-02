import datetime

# print(dir(datetime.datetime))
# print(datetime.datetime.now())  2025-05-30 21:05:50.711650
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)

# print(datetime.datetime.today())
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  2025-05-30 21:07:12
# print(datetime.datetime.now().date())  # 2025-05-30
# print(datetime.datetime.now().time())  # 21:07:12.123456


print(datetime.datetime.max)
print(datetime.datetime.min)
print(datetime.datetime.now().time().strftime("%H:%M:%S"))  # 21:11:31
print(datetime.datetime.now().time().strftime(format="%H:%M"))  # 21:11:31
print(datetime.datetime.now().time().hour)  # 21
