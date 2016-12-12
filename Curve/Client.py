#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
#
# **********************************************************************

import sys, traceback, Ice

Ice.loadSlice('Curve.ice')
import Demo

def menu():
    print("""
usage:
t: send greeting as twoway
o: send greeting as oneway
O: send greeting as batch oneway
d: send greeting as datagram
D: send greeting as batch datagram
f: flush all batch requests
T: set a timeout
P: set a server delay
S: switch secure mode on/off
s: shutdown server
x: exit
?: help
""")

class Client(Ice.Application):
    def run(self, args):
        if len(args) > 1:
            print(self.appName() + ": too many arguments")
            return 1

        twoway = Demo.CurvePrx.checkedCast(\
            self.communicator().propertyToProxy('Curve.Proxy').ice_twoway().ice_secure(False))
        if not twoway:
            print(args[0] + ": invalid proxy")
            return 1

        oneway = Demo.CurvePrx.uncheckedCast(twoway.ice_oneway())
        delay = 0

        menu()

        c = None
        while c != 'x':
            try:
                sys.stdout.write("==> ")
                sys.stdout.flush()
                c = sys.stdin.readline().strip()
                if c == 't':
                    twoway.sayCurve(delay)
                elif c == 'o':
                    oneway.sayCurve(delay)
                elif c== '1':
                    pillars=twoway.getPillars()

                    print pillars
                elif c== '2':
                    df=twoway.getDiscount(123)
                    print df
                elif c == 's':
                    twoway.shutdown()
                elif c == 'x':
                    pass # Nothing to do
                elif c == '?':
                    menu()
                else:
                    print("unknown command `" + c + "'")
                    menu()
            except KeyboardInterrupt:
                break
            except EOFError:
                break
            except Ice.Exception as ex:
                print(ex)

        return 0

app = Client()
sys.exit(app.main(sys.argv, "config.client"))
