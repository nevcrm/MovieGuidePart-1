#// Name: Marcus Bracken
#// Course: CIS261-Object-Oriented Computer Programming I
#// Lab: MovieGuidePart 1

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()

def get_movie_list():
    return ["Monty Python and the Holy Grail", "On the Waterfront", "Cat on a Hot Tin Roof"]

def list_movies(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
    else:
        for i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie}")
    print()


def add_movie(movie_list):
    movie = input("Name: ")
    movie_list.append(movie)
    print(f"{movie} was added.\n")

def delete_movie(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie} was deleted.\n")

def main():
    movie_list = get_movie_list()  # Prepopulate movie list
    display_menu()  # Show the menu options
    
    while True:
        command = input("Command: ").lower()
        
        if command == "list":
            list_movies(movie_list)
        elif command == "add":
            add_movie(movie_list)
        elif command == "del":
            delete_movie(movie_list)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
    main()
