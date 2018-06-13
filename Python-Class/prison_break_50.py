#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      qwang12
#
# Created:     05/06/2018
# Copyright:   (c) qwang12 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
"""


gate_closed = False
gate_open = True



def print_prison(prison):
    print "print prison cells"
    _str = ""
    for i in range(1, len(prison)):
        if prison[i] == gate_closed:
            _str = "closed"
        else:
            _str = "open"
        print "Cell No. %d is %s" %(i, _str)


def print_open_door(prison):
    print "Only print the open door"

    door_no = 1
    for p in prison[1:]:
        if p is gate_open:
            print "Door %d is Open" %door_no

        door_no += 1

    return


def main():

    prison = []

    #For normal math style, array start at 1 and stop at N.
    # So use "50 + 1"
    for i in range(50 + 1):
        prison.append(gate_closed)

    print_prison(prison)

    for guard in range(1, 51):
        turnk = 50 / guard
        print "turnk is %d" %turnk
        for _turnk in range(1, turnk + 1):
            #Guard turn the key.
            prison[_turnk * guard] = not prison[_turnk * guard]
            #print "guard %d _turnk %d" %(guard, _turnk*guard)


    print_prison(prison)

    print_open_door(prison)

    return

if __name__ == '__main__':
    main()
