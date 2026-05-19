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
        print("the books list file not found")
        print("Starting new books list!")
        booksList = []

    option = 0

    while option != 4:
        print("*** Books Manager ***")
        print("1) Add book")
        print("2) Lookup book")
        print("3) Display books")
        print("4) Quit")

        try:
            option = int(input("Choose an option >>> "))
        except ValueError:
            print("Please enter a number from 1 to 4")
            continue

        if option == 1:
            print("adding a book...")
            nBook = input("Enter book name >>>")
            nAuthor = input("Enter author name >>>")

            while True:
                try:
                    nPages = int(input("Enter number of pages >>> "))
                    break

                except ValueError:
                    print("Please entere a valir number")
            

            booksList.append([nBook, nAuthor, nPages])

        elif option == 2:
            print("Looking for book...")
            keyword = input("Enter search term: ").lower()

            found = False

            for book in booksList:
                if keyword in book[0].lower() or keyword in book[1].lower():
                    print(book)
                    found = True
            
            if not found:
                print("No matching books found")

        elif option == 3:
            print("Displaying all books...")
            for i in range(len(booksList)):
                print(booksList[i])

        elif option == 4:
            print("Quitting program")

        else:
            print("Invalid option. Please choose from 1 to 4")

    print("Program closed!")

    #saving to txt file
    outfile = open("theBooksList.txt", "w")
    for book in booksList:
        outfile.write(",".join(map(str, book)) + "\n")
    outfile.close()


if __name__ == "__main__":
    main()