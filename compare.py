a = 'a.txt'
b = 'b.txt'
c = 'output.txt'


with open(a, 'r') as fa, open(b, 'r') as fb, open(c, 'w') as fc:
    sa = set(fa.readlines())
    sb = set(fb.readlines())
    sc = ()

    out = sa - sb

    fc.writelines(sorted(out))