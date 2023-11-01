from datetime import datetime

dt=datetime.today()
print(dt)

print()
newd1=dt.strftime('%B,%d,%Y')
print(newd1)
newd2=dt.strftime('%I:%M:%S')
print(newd2)
newd3=dt.strftime('%c')
print(newd3)