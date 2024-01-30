def fun(a):
    a("Untold mystery")
fun(print)


def d(f):
    def execute():
        print("Executing")
        f()
        print("Deaded")
    return execute
@d
def s():
    print("Untold mystery_sri")
#s1=d(s)
s()