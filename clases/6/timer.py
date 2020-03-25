
import time

#print("This is printed immediately.")
#time.sleep(2.4)
#print("This is printed after 2.4 seconds.")

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result, end="", flush=True)
  print("\r", end="", flush=True)
  time.sleep(1)