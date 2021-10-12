def read_list():
    '''
    Functie pentru citirea listei
    :return: lista citita
    '''
    lst = []
    lst_str = input('Dați numerele separate prin spațiu: ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst


def is_palindrom(n):
    '''
    functia determina daca un numar este palindrom sau nu
    si returneaza True daca este iar in caz contrar False
    Are ca parametru un numar intreg
    '''
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


def test_is_palindrom(n):
    '''
    Functie de test pentru functia _is_palindrom
    '''
    assert is_palindrom(232) == True
    assert is_palindrom(12) == False
    assert is_palindrom(2) == False
    assert is_palindrom(7777) == True
    assert is_palindrom(123) == False
    assert is_palindrom(24342) == True
    assert is_palindrom(1234322) == False



def get_longest_all_palindromes(lst: list[int]):
    '''
    Problema 5:
    Functia determina cea mai lunga subsecventa cu toate numerele palindroame dintr-o lista
    Input: o liste cu numere intregi
    Output: cea mai lunga subsecventa de numere palindroame
    '''
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


def test_get_longest_all_palindromes(lst: list[int]):
    '''
        Functie de test pentru functia _get_longest_all_palindromes
    '''
    assert get_longest_all_palindromes([1, 2, 5, 7, 43, 12]) == []
    assert get_longest_all_palindromes([2, 33, 44, 656, 12, 434, 565]) == [33, 44, 656]
    assert get_longest_all_palindromes([434, 12, 54, 23 ,765, 3225, 54])== [434]
    assert get_longest_all_palindromes([23, 543, 541, 23432, 57575, 121, 686, 90, 242, 373, 1221])==[23432, 57575, 121, 686]
    assert get_longest_all_palindromes([123, 123, 5432, 5432,]) == []




def numar_biti_unu(n):
    '''
        Functie ajutatoare care determina cati biti de unu are un numar
        Input: un numar natural
        Output: numarul de biti egali cu 1 al numarului respectiv
    '''
    k=0
    while n:
        if n%2==1:
            k=k+1
    n=n//2
    return k



def test_numar_biti_unu():
    '''
    functie test pentru numar_biti_unu
    '''
    assert numar_biti_unu(19)==3
    assert numar_biti_unu(23)==4
    assert numar_biti_unu(2)==1
    assert numar_biti_unu(10110)==10
    assert numar_biti_unu(200)==3






def get_longest_same_bit_counts(lst: list[int]):
    '''
    Problema 11. Determinarea celei mai lungi subsecvente de termeni care au acelasi numar de biti 1
    Input: O lista de intregi
    Output: cea mai lunga subsecventa de de termeni care au acelasi numar de biti 1
    '''
    n = len(lst)
    res = []
    for s in range(n):
        for d in range(s, n):
            bit = True
            for num in lst[s:d+1]:
                if is_palindrom(num) == False:
                    bit = False
                    break
            if bit:
                if d-s+1>len(res):
                    res=lst[s:d+1]

    return res








def main():
    lst = []
    while True:
        print('1. Citire lista: ')
        print('2. Cea mai lunga subsecventa de palindroame')
        print('3. Cea mai lunga subsecventa cu termeni ce au acelasi numar de biti de 1')
        print('x. Exit')
        optiune = input('Optiunea: ')
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            palindrom = get_longest_all_palindromes(lst)
            print(palindrom)
        elif optiune == '3':
            bit = get_longest_same_bit_counts(lst)
            print(bit)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')


    test_numar_biti_unu()
    test_is_palindrom()
    test_get_longest_all_palindromes()

if __name__ == '__main__':
    main()
