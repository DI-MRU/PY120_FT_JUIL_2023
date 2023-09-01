## Team TechTitans

Description: A todo list app  
Team members: Onyeka

### MVP

- View the todo list
- Add a new item
- Check/Uncheck/Delete the item
- Search the todo list
- User Authentication (without email features)
- Store the todo list in SQLite
- Compact view by default
- Expandablee item
  - Title
  - Description
  - Check/Uncheck (Complete/Incomplete)
  - Delete button (with confirmation)
- API to save/load state

### Optional Features

- Image/Logo field in the todo list item
- Edit list items
- Order list items

## Team Tamagotchia

Description: A tamagotchi like game  
Team members: Laëticia

### MVP

- The creature
  - Health: Is it gonna die soon? Sick?
  - Age: How many units of time it has lived
  - Hungry: How hungry it is, if at 0/max, it will die of starvation
  - Poop: How close to pooping it is
  - Happy: How happy it is
  - Store state in a database PostgreSQL/SQLite
  - Static image representation
- Feed
- Clean poop
- Play (non-interactive)
- API to save/load state

### Optional Features

- The creature
  - Cleanliness: How dirty it is
- Give a bath
- Hatch an egg if no current creature to obtain
  initial creature
  - Give it a name
- Show a gravestone when creature dies
- Play (interactive) using rock-paper-scissors
- Show creature state
  - Hungry: Drooling mouth?
  - Poopy: Large stomach?
  - Dirty: Smells?
  - Happy: Smile?
  - Sad: Cry?
  - Sleeping: zZz?
- Animated/Dynamic/Gif image

## Team FlappyFlappy

Description: Flappy bird like game
Team members: Anas

### Important note

- Take care of memory leaks
- Clean up past obstacles/characters/etc appropriately

### MVP

- Player character
- Obstacles
- Score
- Highscore
- Menu
  - Resume/Pause
  - Show highscore(s)
  - Exit
- Hotkeys
  - P for pause/resume
  - M for mute/unmute
  - Spacebar for flapping
- API
  - GET/POST highscore
- Store the highscore in a database PostgreSQL

### Optional Features

- Player character multiple lives
- The more score you have, the faster the game goes
  - `game_speed = current_score * 1.005`?
- API
  - GET/POST username

### Example attribution

Attribution: Sprite pack `Protagonist Character | Free Pixel Art Animated Character` from https://penzilla.itch.io/protagonist-character
