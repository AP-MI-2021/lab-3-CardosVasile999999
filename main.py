def read_list():
    lst = []
    lst_str = input('Dați numerele separate prin spațiu: ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst









def main():
    lst = []
    while True:
        print('1. Citire lista: ')
        print('2. Optiunea 2')
        print('3. Optiunea 3')
        print('x. Exit')
        optiune = input('Optiunea: ')
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            pass
        elif optiune == '3':
            pass
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')




    if __name__ == '__main__':
        main()
