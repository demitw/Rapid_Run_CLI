import random

# Global variables
horses = []
race_started = False
winners = []
deleted_horses = []




def count_horses_in_group(group):
    return sum(1 for horse in horses if horse['group'] == group)


def add_horse_details():
    global horses
    global race_started

    if not race_started:
        while True:
            try:
                horse_id = int(input("Enter Horse ID: "))
                # Check if the horse ID already exists
                if not any(horse['id'] == horse_id for horse in horses):
                    # If the ID is unique, proceed
                    break
                else:
                    print("Error: Duplicate horse ID. Please enter a unique ID.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

        horse_name = input("Enter Horse Name: ")
        jockey_name = input("Enter Jockey Name: ")
        while True:
            try:
                age = int(input("Enter Age: "))
                break  # Break out of the loop if the input is a valid integer
            except ValueError:
                print("Invalid input. Please enter a valid integer for Age.")
                continue

        while True:
            breed = input("Enter Breed: ")
            # Check if the breed contains only alphabetical characters
            if breed.isalpha():
                break
            else:
                print("Error: Breed should contain only alphabetical characters.")

        while True:
            try:
                num_races = int(input("Enter Number of Races: "))
                num_wins = int(input("Enter Number of Wins: "))
                # Check if the number of wins is less than or equal to the number of races
                if 0 <= num_wins <= num_races:
                    break
                else:
                    print("Error: Number of wins should be less than or equal to the number of races.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue
        while True:
            group = input("Enter Group (A, B, C, or D): ").upper()  # Convert to uppercase for uniformity
            # Check if the group is one of the valid options
            if group in {'A', 'B', 'C', 'D'}:
                # Check if the group has reached its limit of five horses
                if count_horses_in_group(group) < 5:
                    break
                else:
                    print(f"Error: Group {group} has reached its limit of five horses. Choose a different group.")
            else:
                print("Error: Invalid group. Please enter A, B, C, or D.")

        horse_details = {'id': horse_id, 'name': horse_name, 'jockey': jockey_name,
                         'age': age, 'breed': breed, 'num_races': num_races, 'num_wins': num_wins, 'group': group}

        horses.append(horse_details)
        print("Horse details added successfully.")
    else:
        print("Race has already started. Cannot add horse details.")


def delete_horse_details():
    global horses
    global race_started
    global deleted_horses

    if not race_started:
        while True:
            try:
                horse_id_to_delete = int(input("Enter Horse ID to delete: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for Horse ID.")
                continue

        deleted_horse = next((horse for horse in horses if horse['id'] == horse_id_to_delete), None)
        if deleted_horse:
            horses.remove(deleted_horse)  # Remove the horse from the list
            deleted_horses.append(deleted_horse)  # Add the horse to the deleted list
            print(f"Horse with ID {horse_id_to_delete} deleted successfully.")
        else:
            print(f"Error: Horse with ID {horse_id_to_delete} not found.")
    else:
        print("Race has already started. Cannot delete horse details.")


def update_horse_details():
    global horses
    global race_started

    if not race_started:
        while True:
            try:
                horse_id = int(input("Enter Horse ID to update details: "))
                # Check if the horse ID exists
                index = next((i for i, horse in enumerate(horses) if horse['id'] == horse_id), None)
                if index is not None:
                    break  # Horse ID found, proceed with the update
                else:
                    print("Error: Horse ID not found. Please enter a valid ID.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

        # Allow the user to update specific details of the horse
        horse = horses[index]
        print(f"Current details for Horse ID {horse_id}: {horse}")
        horse_name = input("Enter updated Horse Name (press Enter to keep current): ")
        jockey_name = input("Enter updated Jockey Name (press Enter to keep current): ")

        # Update age with validation
        while True:
            try:
                age = int(input("Enter updated Age (press Enter to keep current): "))
                break  # Break out of the loop if the input is a valid integer
            except ValueError:
                print("Invalid input. Please enter a valid integer for Age.")
                continue

        # Update breed with validation
        while True:
            breed = input("Enter updated Breed (press Enter to keep current): ")
            # Check if the breed contains only alphabetical characters
            if breed.isalpha() or breed == "":
                break
            else:
                print("Error: Breed should contain only alphabetical characters.")

        # Update num_races and num_wins with validation
        while True:
            try:
                num_races = int(input("Enter updated Number of Races (press Enter to keep current): "))
                num_wins = int(input("Enter updated Number of Wins (press Enter to keep current): "))
                # Check if the number of wins is less than or equal to the number of races
                if 0 <= num_wins <= num_races:
                    break
                else:
                    print("Error: Number of wins should be less than or equal to the number of races.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

        # Update group with validation
        while True:
            group = input("Enter updated Group (A, B, C, or D): ").upper()  # Convert to uppercase for uniformity
            # Check if the group is one of the valid options
            if group in {'A', 'B', 'C', 'D'}:
                # Check if the group has reached its limit of five horses
                if count_horses_in_group(group) < 5:
                    break
                else:
                    print(f"Error: Group {group} has reached its limit of five horses. Choose a different group.")
            else:
                print("Error: Invalid group. Please enter A, B, C, or D.")

        # Update the horse details in the list
        horse.update({'name': horse_name or horse['name'],
                      'jockey': jockey_name or horse['jockey'],
                      'age': age or horse['age'],
                      'breed': breed or horse['breed'],
                      'num_races': num_races or horse['num_races'],
                      'num_wins': num_wins or horse['num_wins'],
                      'group': group or horse['group']})

        print(f"Horse details for Horse ID {horse_id} updated successfully.")
    else:
        print("Race has already started. Cannot update horse details.")


def bubble_sort():
    global horses
    n = len(horses)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if horses[j]['id'] > horses[j + 1]['id']:
                # Swap the horses if they are in the wrong order
                horses[j], horses[j + 1] = horses[j + 1], horses[j]


def view_horses_details_sorted_by_id():
    global horses
    global deleted_horses

    if horses:
        # Sort the horses using bubble sort
        bubble_sort()

        # Display the sorted horse details
        print("Horse details sorted by Horse ID:")
        for horse in horses:
            if horse not in deleted_horses:  # Check if the horse is not in the deleted list
                print(horse)
    else:
        print("No horses to display.")


def save_to_file():
    global horses
    filename = "horse_details.txt"

    with open(filename, "w") as file:
        for horse in horses:
            # Write horse details to the file, categorizing them according to the group
            file.write(f"Group {horse['group']}:\n")
            file.write(f"ID: {horse['id']}\n")
            file.write(f"Name: {horse['name']}\n")
            file.write(f"Jockey: {horse['jockey']}\n")
            file.write(f"Age: {horse['age']}\n")
            file.write(f"Breed: {horse['breed']}\n")
            file.write(f"Number of Races: {horse['num_races']}\n")
            file.write(f"Number of Wins: {horse['num_wins']}\n")
            file.write("\n")

    print(f"Horse details saved to '{filename}' successfully.")

def random_draw():
    global race_started
    global winners

    if not race_started:
        groups = ['A', 'B', 'C', 'D']
        for group in groups:
            group_horses = [horse for horse in horses if horse['group'] == group]
            if len(group_horses) >= 4:
                selected_horse = random.choice(group_horses)
                winners.append(selected_horse)
                print(f" selected horse from Group {group}: {selected_horse}")
            else:
                print(f"Not enough horses in Group {group} to perform a random draw.")

        race_started = True
    else:
        print("Race has already started. Cannot perform a random draw.")

def bubble_sort_winners():
    global winners
    n = len(winners)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if winners[j]['time'] > winners[j + 1]['time']:
                # Swap the winners if they are in the wrong order
                winners[j], winners[j + 1] = winners[j + 1], winners[j]

def display_winners():
    global race_started
    global winners

    if race_started:
        # Assign a random time for each winner (if not assigned already)
        for winner in winners:
            if 'time' not in winner:
                winner['time'] = random.randint(0, 90)

        # Sort the winners based on the assigned time
        bubble_sort_winners()

        print("Winning horses' details:")
        for i, winner in enumerate(winners, start=1):
            print(f"{i}. {winner['name']} - Time: {winner['time']}s")
    else:
        print("Race has not started yet. Call SDD to perform a random draw first.")


def start_race():
    global race_started

    if race_started:
        print("Race is already in progress.")
    else:
        print("Race has not started yet. Call SDD to perform a random draw first.")


def visualize_winning_time():
    global race_started
    global winners

    if not race_started:
        print("Race has not started yet. Call SDD to perform a random draw first.")
        return

    print("Visualizing the time of the winning horses:")
    for i, winner in enumerate(winners, start=1):
        time_spent = winner.get('time', 0)  # Use the assigned time
        stars = '*' * (time_spent // 10)
        place = ordinal(i)
        print(f"{winner['name']}: {stars} {time_spent}s ({place} Place)")


def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"


def exit_program():
    print("Exiting the program.")
    # Add any cleanup code here if needed
    quit()


def show_menu():
    menu = """
    Menu:
    - Type AHD for adding horse details.
    - Type UHD for updating horse details.
    - Type DHD for deleting horse details.
    - Type VHD for viewing the registered horses’ details table (sorted by Horse ID).
    - Type SHD for saving the horse details to the text file.
    - Type SDD for selecting four horses randomly for the major round.
    - Type WHD for displaying the Winning horses’ details.
    - Type VWH for visualizing the time of the winning horses.
    - Type ESC to exit the program.
    """

    print(menu)


def run():
    global race_started

    while True:
        show_menu()
        choice = input("Enter your choice: ").upper()

        if choice == "AHD":
            if not race_started:
                add_horse_details()
            else:
                print("Race has already started. Cannot add horse details.")
        elif choice == "UHD":
            update_horse_details()
        elif choice == "DHD":
            delete_horse_details()
        elif choice == "VHD":
            view_horses_details_sorted_by_id()
        elif choice == "SHD":
            save_to_file()
        elif choice == "SDD":
            random_draw()
        elif choice == "WHD":
            display_winners()
        elif choice == "VWH":
            visualize_winning_time()
        elif choice == "START":
            if race_started:
                start_race()
            else:
                print("Race has not started yet. Call SDD to perform a random draw first.")
        elif choice == "ESC":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    run()
