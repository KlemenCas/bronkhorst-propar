import propar
import time

dut = propar.instrument('com5')

dut.master.dump(1)

while True:
  time.sleep(1)
  v = dut.readParameter(11)
  #print(v)