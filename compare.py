a = 'a.txt'
b = 'b.txt'
c = 'output.txt'


with open(a, 'r') as fa, open(b, 'r') as fb, open(c, 'w') as fc:
    sa = set(x.strip() for x in fa.readlines())
    sb = set(x.strip() for x in fb.readlines())
    sc = ()
 
    out = sa - sb
 
    fc.writelines(x + '\n' for x in sorted(out))