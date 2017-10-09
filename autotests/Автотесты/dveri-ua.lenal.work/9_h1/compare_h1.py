
def main():
    with open('h1.txt', 'r', encoding='utf-8') as h1_file, open('origin_h1.txt', 'r', encoding='utf-8-sig') as origin_h1:




        list = []
        for line1 in h1_file.readlines():

            list.append(line1)
        list2 = []
        for line2 in origin_h1.readlines():
            list2.append(line2)


        print(set(list)^set(list2))














if __name__ == '__main__':
    main()