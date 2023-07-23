def strcounter(s): #решение за N*N
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
        print(sym, counter)
strcounter('aba')


def strcounter(s): #решение за N*M
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
        print(sym, counter)
strcounter('aba')

def strcounter(s): #решение за N + M
    symb_counter = {}
    for sym in s:
        symb_counter[sym] = symb_counter.get(sym, 0) + 1
    for sym, counter in symb_counter.items():
        print(sym, counter)
strcounter('aba')

#подается строка, нужно посчитать и вывести количество каждого уникального символа
# aba, то вывод будет
# а 2
# b 1
