# Author: Kael
# Date: 02/13/2026
# Title: Movie Tickets Program

total_tickets = 0

num_movies = int(input("How many movies would you like to enter? "))

for i in range(num_movies):
    movie_name = input(f"Enter the name of movie #{i+1}: ")
    tickets = int(input(f"How many tickets for '{movie_name}'? "))
    total_tickets += tickets

print(f"\nTotal tickets desired: {total_tickets}")
