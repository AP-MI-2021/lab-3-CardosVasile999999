def function(rf):
    if rf % 2 == 0:
        return 1
    else:
        return 0


def main():
    t = int(input('numarul este'))
    s = function(t)
    print(f'NUMARUL ESTE {s}')
    if __name__ == '__main__':
        main()
