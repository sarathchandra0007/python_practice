from nose.tools import assert_equal

def solution_add(a1,a2):
    return a1+a2

class checkadd(object):
    def check(solution_add):
        assert_equal(solution_add(2,2),4)
        assert_equal(solution_add(3,3),6)

        print ("both are equal")

c=checkadd()
c.check(solution_add)

