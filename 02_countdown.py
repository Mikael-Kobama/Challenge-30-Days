
import time

t = input("digite o tempo (em segundos): ")

if t.isdigit():
  t = int(t)
else:
  print("Entrada Errada")
  quit()

while t != 0:
  minutes, seconds = divmod(t, 60)
  timer = "{:02d}:{:02d}".format(minutes, seconds)
  print(timer, end = "\r")
  time.sleep(1)
  t = t-1

print("O tempo acabou!")