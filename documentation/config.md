# JSON Config

In order to run the program, you'll need to generate a JSON file which outlines the commands you'd like to automate. This document
outlines the required format of the JSON file.

## Top Level Format

It should contain 2 parent levels key called `character_name` and `commands`.

```json
{
  "character_name": "Kalius The Bard",
  "commands": [
    <list-of-command-objects>
  ]
}
```

## Fields

#### character_name (String)

The name of your character

#### commands

A list of command objects. See below for format.

## Command Object

A command object is a JSON object which specifies the details of the command to be automated. It has the following format:

```json
{
  "name": "Attack with dagger",
  "num_dice": 1,
  "num_dice_sides": 20,
  "modifier": 5
}
```

- This would be translated into the dice maiden command `!roll 1d5 +5`.
- If advantage is specified, it would be `!roll 2d20 + 5 d1`
- If disadvantage is specified, it would be `!roll 2d20 + 5 kl1`

## Fields 
#### name (String)

Name of your character

#### num_dice (Integer)

Number of dice to be rolled

#### num_dice_sides (integer)

Number from 1 to 100.

#### Modifier (Integer)

The amount to add or remove from the dice roll. The following are examples of accepted values

- `5`
- `0`
- `-5`

Notice that the sign is required if value is negative.

# Example Configuration File

[Sample Config](config_example.json)