#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jforeman
#
# Created:     14/11/2015
# Copyright:   (c) jforeman 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, traceback

#-------------------------------------------------------------------------------
def fizzbuzz(x=None,
             y=None,
             n=None):
    try:
        i = 1
        list1 = []
        while i <= n:
            if i%x == 0 and i%y == 0:
                list1.append('FB')

            elif i%x == 0:
                list1.append('F')

            elif i%y == 0:
                list1.append('B')

            else:
                list1.append(str(i))
            i += 1
        print ' '.join(list1)
    except:
        traceback.print_exc(file=sys.stdout)

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:
        list1 = [ str(x) for x in test.split(' ') ]
        list2 = map(lambda s: s.strip(), list1)
        x = int(list2[0])
        y = int(list2[1])
        n = int(list2[2])
        fizzbuzz(x,y,n)

    test_cases.close()
    sys.exit(0)
