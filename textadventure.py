location = (0,0,0)
alive = True
commandList = ['north', 'east', 'west', 'look']
description = "You're standing in a field surrounded my mountains."

def printCommands():
    commands = ""
    for c in commandList:
        commands += f"[{c}] "
    print(commands)

def Command(cmd):
    global location
    global alive
    global commandList
    global description

    if cmd not in commandList:
        print("\nNope. Nope. To the Nope. Try again.\n")
        return
    else:
        if cmd == 'look':
            print("\nYou see a cave.\n")
            if 'enter' not in commandList:
                commandList.append('enter')
        if cmd == 'enter':
            commandList = ['exit']
            description = ""
            location = (0,0,1)
            print("\nYou enter the cave.\n")
            print("It's dangerous to go alone. Take this.")
            print("You are now equipped with a stick.")
        elif cmd in {'north', 'west', 'east'}:
            print("\nYou fell into a pit and died.")
            print("\nGAME OVER\n")
            alive = False
        elif cmd == 'exit':
            description = "You're standing in a field surrounded my mountains."
            location = (0,0,0)
            commandList = ['north', 'east', 'west', 'look', 'enter']
            print("\nYou exited the cave\n")

while alive:
    print(description)
    printCommands()
    x  = input()
    Command(x)