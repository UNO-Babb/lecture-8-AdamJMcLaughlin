def main():
    with open("qbdata.txt", 'r') as myFile:
        for line in myFile:
            info = line.strip().split()
            if len(info) > 12:
                td = info[12]
                name = info[0]
                last = info[1]
                rating = info[9]
                print(f"{name} {last} had a rating of {rating} and threw {td} touchdowns.")
            

if __name__ == '__main__':
    main()
