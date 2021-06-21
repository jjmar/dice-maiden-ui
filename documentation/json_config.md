# JSON Config

In order to run the program, you'll need to generate a JSON file which outlines the commands you'd like to automate. This document
outlines the required format of the JSON file.

## Top Level Format

It should contain 2 parent levels key called `character_name` and `actions`.

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
  "num_dice_sides": "5",
  "modifier": "+5"
}
```

- This would be translated into the dice maiden command `!roll 1d5 +5 ! Attack with dagger`.
- If advantage is specified, it would be `!roll 2d20 + 5 d1 ! Attack with dagger`
- If disadvantage is specified, it would be `!roll 2d20 + 5 kl1 ! Attack with dagger`

## Fields 
#### name (String)

Name of your character

#### num_dice (Integer)

Number of dice to be rolled

#### num_dice_sides (integer)

Number from 1 to 100.

#### Modifier (string)

The amount to add or remove from the dice roll. The following are examples of accepted values

- `+5`
- `+0`
- `-5`

Notice that the sign is required.

# Example Configuration File

```json
{
  "character_name": "Kalius the Great",
  "commands": [
    {
      "name": "Attack with Javelin",
      "num_dice": 1,
      "num_dice_sides": 6,
      "modifier": "+3"
    },
    {
      "name": "Spell Damage: Heat Metal",
      "num_dice": 2,
      "num_dice_sides": 8,
      "modifier": "+0"
    }
    {
      "name": "Skill Check: Intimidation",
      "num_dice": 1,
      "num_dice_sides": 20,
      "modifier": "+10"
    },
    {
      "name": "Saving Thow: Intelligence",
      "num_dice": 1,
      "num_dice_sides": 20,
      "modifier": "-1"
    },
    
  ]
}
```