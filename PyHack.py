#import dependencies
import os, urllib3

#Define internet connection check (This is an artifical requirement, it is possible to run this script without an internet connection, I just did this for kicks and giggles.)
def internet_on_firstboot():
    print("connecting...")
    try:
    #Tries opening a connection to google, It could be any website but I decided to use google because it is almost never down, if it can't reach it, you are probably not connected to the internet.
        urllib3.urlopen("https://www.google.com")
        print("Connected")
        #This is how I determine the value of a variable while having it acessible outside of the function, the value that is returned is later set as the variable "IsConnected"
        return True
        
    except:
        #If it can not reach it, like I said, you are most likely not connected to the internet
        print("Error. No internet connection present")
        #This is how I determine the value of a variable while having it acessible outside of the function, the value that is returned is later set as the variable "IsConnected"
        return False




#This is the same thing as "internet_on_firstboot()" except it is deverbosified so it can check every cycle in the main loop without ruining the illusion by printing to the screen your connection status
def internet_on_silent():
    
    try:
    
        urllib3.urlopen("https://www.google.com")
        return True
        
    except:
        
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
    #This is a long command that runs in the default command interperiter (see above) but is spesifically designed to be run is bash based shells. 
    # This is first set as a variable to avoid quote/escape character hell. 
    # I can't dive into the spesifics of how this works because I stole it from some stack overflow thread,
    # (https://stackoverflow.com/questions/2444402/how-do-i-display-a-tree-of-things-in-bash) 
    # but it basically does the some thing as the tree command in windows command prompt.
    aliasstring = "alias tree=\"ls -R | grep ':$' | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /\ -e 's/-/|/'\""
    command("cd /")
    command(aliasstring)
    #This is a windows only thing, if you know how, feel free to push an update that does this for bash based shells.
    command("color 0a")   
 
    #This is where the magic happens, it is what you will see when you run this program.
def Hack():

    #Variable is set again inside the function.
    IsConnected = internet_on_silent()
    
    #Tests connection before next cycle
    while IsConnected == True:
        IsConnected = internet_on_silent()
        #This is why I did that unreadable aliasing up above.
        command("tree")
        #Extra stuff to list stuff in a differnt way
        command("Dir -r")
        return True
    if IsConnected == False:
        print("Disconnected...")
# Main loop runs "Hack()" until connection is lost.     
def main():
    
    Hack()
    input("Press any key to exit")
    exit()

main()
    

    