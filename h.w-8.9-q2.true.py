
# MAKE ALL OF THIS CONDITION TRUE

a = 0
b = 0
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 1
b = 2
c = 3
d = 4
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 3
b = 1
c = 4
d = 2
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 0
c = 0
d = 0
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 10
b = 10
c = 5
d = 8
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 2
c = 3
d = 4
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 0
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 5
b = 4
c = 3
if a != b and a <= c or a <= b or True:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 5
b = 8
c = 10
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 0.5
b = 0.5
c = 1.5
d = 1.5
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

#לגבי התשובה האחרונה, לדעתי תמיד יצא שקר