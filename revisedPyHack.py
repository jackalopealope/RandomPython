import os
import subprocess

# Define internet connection check (This is an artificial requirement, it is possible to run this script without an internet connection, I just did this for kicks and giggles.)
def internet_on_firstboot():
    print("connecting...")
    try:
        subprocess.check_output(["ping", "-c", "1", "google.com"], stderr=subprocess.STDOUT, timeout=5)
        print("Connected")
        return True
    except subprocess.CalledProcessError:
        print("Error. No internet connection present")
        return False
    except subprocess.TimeoutExpired:
        print("Error. Ping timed out.")
        return False

# This is the same thing as "internet_on_firstboot()" except it is deverbosified so it can check every cycle in the main loop without ruining the illusion by printing to the screen your connection status
def internet_on_silent():
    try:
        subprocess.check_output(["ping", "-c", "1", "google.com"], stderr=subprocess.STDOUT, timeout=5)
        return True
    except subprocess.CalledProcessError:
        return False
    except subprocess.TimeoutExpired:
        print("Error. Ping timed out.")
        return False

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
    command(aliasstring)
    # This is a Windows only thing, if you know how, feel free to push an update that does this for bash based shells.
    command("color 0a")   
 
    # This is where the magic happens, it is what you will see when you run this program.
def Hack():
    # Variable is set again inside the function.
    IsConnected = internet_on_silent()
    
    # Tests connection before next cycle
    while IsConnected:
        IsConnected = internet_on_silent()
        # This is why I did that unreadable aliasing up above.
        command("tree")
        # Extra stuff to list stuff in a different way
        command("Dir -r")
        return True
    else:
        print("Disconnected...")

# Main loop runs "Hack()" until connection is lost.     
def main():
    Hack()
    input("Press any key to exit")
    exit()

main()
