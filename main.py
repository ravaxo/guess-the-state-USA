from turtle import Turtle, Screen
import pandas

# Create a turtle object to write state names on the map
rom = Turtle()
rom.penup()
rom.hideturtle()

# Set up the game screen
SCREEN = Screen()
SCREEN.setup(width=725, height=491)
SCREEN.title("USA States Guessing Game")
SCREEN.bgpic("blank_states_img.gif")  # Set background image of the US map

# Load the list of states and their coordinates from CSV
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()  # List of all state names
guessed_states: list = []          # List to store correctly guessed states

# Game loop: keep asking for guesses until all 50 states are guessed
while len(guessed_states) < 50:

    # Ask the user to guess a state name
    answer = (SCREEN.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? or type 'exit'") or "").title()

    # If user types 'Exit', save the missing states to a CSV file and end the game
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states to learn.csv")
        break

    # If the guess is correct, write the state name on the map
    if answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        state_data = data[data.state == answer]
        rom.goto(state_data.x.item(), state_data.y.item())
        rom.write(answer)