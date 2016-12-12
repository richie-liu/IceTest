#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
#
# **********************************************************************
from random import random

import sys, traceback, time, Ice

Ice.loadSlice('Curve.ice')
Ice.updateModules()
import Demo


class CurveI(Demo.Curve):
    def sayCurve(self, delay, current=None):
        if delay != 0:
            time.sleep(delay / 1000.0)
        print("Curve World!")

    def shutdown(self, current=None):
        current.adapter.getCommunicator().shutdown()

    def getDiscount(self, date,current=None):
        return random()

    def getPillars(self,current=None):
        return ['ON','1M','2M']


class Server(Ice.Application):
    def run(self, args):
        if len(args) > 1:
            print(self.appName() + ": too many arguments")
            return 1

        adapter = self.communicator().createObjectAdapter("Curve")
        adapter.add(CurveI(), self.communicator().stringToIdentity("Curve"))
        adapter.activate()
        self.communicator().waitForShutdown()
        return 0

sys.stdout.flush()
app = Server()
sys.exit(app.main(sys.argv, "config.server"))
