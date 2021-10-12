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
    input: n
    out: boolean variable
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
            if palindrom == True:
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


'''
    functie ajutatoare ca sa verificam daca cifrele unui numar sun in ordine descrescatoare
    input n
    output boolean variable
    '''
def cifre_descrescatoare(n):
    '''
    functie ajutatoare care determina daca cifrele unui numar sunt in ordine descrescatoare
    '''
    if n<10:
        return False

    k = n % 10
    n = n // 10
    while n:

        if n%10 < k:
            return False

        k = n % 10
        n = n // 10

    return True



def test_cifre_descrescatoare():
    '''
    functie test pentru  cifre_descrescatoare
    '''
    assert cifre_descrescatoare(54321)==True
    assert cifre_descrescatoare(123)==False
    assert cifre_descrescatoare(1)==False
    assert cifre_descrescatoare(32)==True
    assert cifre_descrescatoare(531)==True
    assert cifre_descrescatoare(69)==True


def get_longest_digit_count_desc(lst: list[int]):
    '''
    Problema 18:
    Functia determina cea mai lunga subsecventa cu toate numerele care au cifrele in ordine descrescatoare
    Input: o liste cu numere intregi
    Output: cea mai lunga subsecventa de numere avand cifrele in ordine descrescatoare
    '''
    n = len(lst)
    res = []
    for s in range(n):
        for d in range(s, n):
            des = True
            for num in lst[s:d+1]:
                if cifre_descrescatoare(num) == False:
                    des = False
                    break
            if des:
                if d-s+1>len(res):
                    res=lst[s:d+1]

    return res



def test_get_longest_digit_count_desc():
    '''
    functia test pentru get_longest_digit_count_desc():
    '''
    assert get_longest_digit_count_desc([1, 2, 3, 543, 432, 321, 7, 123, 234, 543, 43])==[543, 432, 321]
    assert get_longest_digit_count_desc([1, 2, 3, 4,])==[]
    assert get_longest_digit_count_desc([1, 2, 3, 43])==[43]
    assert get_longest_digit_count_desc([54, 43, 1, 2, 54, 21])==[54, 43]
    assert get_longest_digit_count_desc([54, 43, 2, 3, 98, 76, 43])==[98, 76, 43]








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
            cif = get_longest_digit_count_desc(lst)
            print(cif)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')



    test_is_palindrom()
    test_get_longest_all_palindromes()
    test_cifre_descrescatoare()
    test_get_longest_digit_count_desc()
if __name__ == '__main__':
    main()
