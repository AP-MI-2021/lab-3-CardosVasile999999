def read_list():
    lst = []
    lst_str = input('Dați numerele separate prin spațiu: ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst


def is_palindrom(n):
    aux=n
    inv=0
    if n >= 10:
        while n:
            inv=inv*10+n%10
            n=n//10
    else:
        return False

    if aux == inv:
        return True
    else:
        return False


def get_longest_all_palindromes(lst: list[int]):
    n = len(lst)
    res = []
    for s in range(n):
        for d in range(s, n):
            palindrom = True
            for num in lst[s:d+1]:
                if is_palindrom(num) == False:
                    palindrom = False
                    break
            if palindrom:
                if d-s+1>len(res):
                    res=lst[s:d+1]

    return res









def main():
    lst = []
    while True:
        print('1. Citire lista: ')
        print('2. Cea mai lunga subsecventa de palindroame')
        print('3. Optiunea 3')
        print('x. Exit')
        optiune = input('Optiunea: ')
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            palindrom = get_longest_all_palindromes(lst)
            print(palindrom)
        elif optiune == '3':
            pass
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')


if __name__ == '__main__':
    main()
