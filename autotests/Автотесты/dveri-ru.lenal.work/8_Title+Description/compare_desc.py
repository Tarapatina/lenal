
def main():
    with open('description.txt', 'r', encoding='utf-8') as desc_file, open('origin.txt', 'r', encoding='utf-8-sig') as origin_desc:

        list = []
        for line1 in desc_file.readlines():
            list.append(line1)

        list2 = []
        for line2 in origin_desc.readlines():
            list2.append(line2)

        print(set(list)^set(list2))














if __name__ == '__main__':
    main()