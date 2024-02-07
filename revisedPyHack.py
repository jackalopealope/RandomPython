import os, platform, keyboard, time

# This is made to make it easier to run a command in the host's command interpreter. The main ones being: 
# (I will not count virtualizing these shells to make an operating system compatible with these shells, that would make this list pointless.
# (i.e. Wine, WSL, etc.)
# [Bash - GNU/Linux + MacOS Mojave and earlier]
# [Powershell - Windows Xp and later + Optional to download on most decently modern linux distros]
# [Zsh - MacOS Catilina and earlier]

def command(c):
    os.system(c)

# This moves into the root directory and sets the color to hollywood hacker green! (idk how to change shell color in bash and the like, see comment below.) >:D  
def setup():
    # This is a long command that runs in the default command interpreter (see above) but is specifically designed to be run in bash-based shells. 
    # This is first set as a variable to avoid quote/escape character hell. 
    # I can't dive into the specifics of how this works because I stole it from some stack overflow thread,
    # (https://stackoverflow.com/questions/2444402/how-do-i-display-a-tree-of-things-in-bash) 
    # but it basically does the same thing as the tree command in windows command prompt.
    aliasstring = "alias tree=\"ls -R | grep ':$' | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /\ -e 's/-/|/'\""
    command("cd /")
    runningOS = platform.system()
    if runningOS == "Linux":
        command(aliasstring)
    # This is a Windows only thing, if you know how, feel free to push an update that does this for bash based shells.
    if runningOS == "Windows":
        command("color 0a")
     
 
    # This is where the magic happens, it is what you will see when you run this program.
def Hack():
    Level = 7
    runningOS = platform.system()
    if runningOS == "Windows":
        command("start /MAX cmd /k \"color 0a && cd \ && tree && dir && tree && dir && tree && dir && tree && dir && tree && dir && tree && dir && tree && dir\"")
        for i in range(Level):
            command("start cmd /c \"color 0a && cd \ && tree && dir && tree && dir && tree && dir && tree && dir && tree && dir && tree && dir && tree && dir\"")
            i = i+1
    elif runningOS == "Linux":
        command("")
    
    while True:
            # This is the command that is not installed by default I did that unreadable aliasing up above.
            command("tree")
            runningOS = platform.system()
            if runningOS == "Windows":
                command("Dir -r")
            
        

# Main loop runs "Hack()" until connection is lost.     
def main():
    try:
        Hack()
    except KeyboardInterrupt:
        print("\n" * 10000)
        print("Acess Granted...")
        input("Press any key to exit")
        exit()

setup()
main()

