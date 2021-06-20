# dice-maiden-ui
Python app which provides a more automated way of generating roll commands for Dice Maiden dicsord app

# Configuration

1) Create a JSON document which outlines the commands you'd like this program to generate a GUI for. Please see the [config doc](documentation/json_config.md) for more info.
2) Run the app (TODO)

# Running the app

- TODO

# Expected Roadmap

### Version 0.1.0

- Need a GUI
- Needs to open predefined JSON document
- Creates buttons for document
- Button doesnt do anything
- On open, it always finds a specific file

### Version 0.2.0

- Create initial code to translate `commands` into dice maiden valid commands
- Have buttons copy those commands to clipboard

### Version 0.3.0

- Can open document via find file browser
- Upon re-open, it tries to load the previously opened file

### Version 0.4.0

- Add advantage / disadvantage modification to dice maiden code
- Add toggle for functionality in GUI

### Version 0.5.0 or 1.0.0 release

- Allow commands to be grouped by some sort of `category
- General refactoring of how the GUI looks as im sure it'll look 💩 by now

### Potential Future Version Ideas

- Multiple JSON document support
- Add modifier override code (e.g say you do more damage sometimes due to teammate buff)
- Gui to generate the JSON file for the user