#!/usr/bin/env python2
# code from tesla_tester.py + pandad.py

import time
from selfdrive.swaglog import cloudlog
from panda import Panda
from common.params import Params
params = Params()


def panda_comm():
  panda = None

  cloudlog.info("Connecting to panda")

  # connect to panda
  while True:
    # break on normal mode Panda
    panda_list = Panda.list()
    if len(panda_list) > 0:
      cloudlog.info("Panda found, connecting")
      panda = Panda(panda_list[0])
      panda.set_safety_mode(Panda.SAFETY_ALLOUTPUT)
      break

    print "waiting for board..."
    time.sleep(1)

  # send commands to panda
  while True:
    command = params.get("DragonToyotaCommand")
    if not command == "":
      addr, vl, bus = command.split(',')
      panda.can_send(addr, vl, bus)
      print("sending command: panda.can_send(%s, %s, %s)" % (addr, vl, bus))
      params.put("DragonToyotaCommand", "")
    time.sleep(1)



def main(gctx=None):
  panda_comm()

if __name__ == "__main__":
  main()
