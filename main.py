def main():
    try:
        #initialize book list
        booksList = []

        infile = open("theBooksList.txt", "r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError :
        print("the <bookslist.txt> file not found")
        print("Starting new books list!")
        booksList = []

    option = 0

    while option != 4:
        print("*** Books Manager ***")
        print("1) Add book")
        print("2) Lookup book")
        print("3) Display books")
        print("4) Quit")
        option = int(input())

        if option == 1:
            print("adding a book...")
            nBook = input("Enter book name >>>")
            nAuthor = input("Enter author name >>>")
            nPages = input("Enter number of pages >>>")
            booksList.append([nBook, nAuthor, nPages])

        elif option == 2:
            print("Looking for book...")
            keyword = input("Enter search term: ")

            for book in booksList:
                if keyword in book:
                    print(book)

        elif option == 3:
            print("Displaying all books...")
            for i in range(len(booksList)):
                print(booksList[i])

        elif option == 4:
            print("Quitting program")

    print("Program closed!")

    #saving to txt file
    outfile = open("theBooksList.txt", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()


if __name__ == "__main__":
    main()