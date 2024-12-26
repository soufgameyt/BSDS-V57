# This is a fork from original BSDS by [Crazor](https://github.com/CrazorTheCat)  with a lot less features, it is meant for developement, do not use for production and hosting for others.

Discord link : https://discord.gg/mt4dUxXryh


## How to play BSDS: ##

### Server ###
1: Download the server and extract it.

2: Open terminal on your computer and go to BSDS directory.

3: Type python Core.py and it's done, follow client instructions.

### iOS client ###
1: Download the client and extract it. : prob never unless someone give me one

2: go to Payload/Brawl Stars.app/ in your file manager and start a new tab and go to this location in your terminal.

3: In your file manager, you will see ipPatcher.py, open it in any text editor and locate in the first line of the script the patched_ip variable with a string.

4: Change the string to be your ipv4 address of your device you execute the server from.

5: After the ip changed is saved, in your terminal with the client location, execute this following command : python ipPatcher.py

6: Save and compile back to ipa format.

7: Install the client using your favorite app installer and enjoy BSDS.

### Android client ###
1: Download the apk here: find on telegram (lazy uploading on mediafire)

2: Download an apk editor of your choice

3: Decompile the apk with mt manager and go to lib/armeabi-v7a/libBSD.s.so and open the file with a text editor.

4: Go in the script and search for the part where there a ip and remplace with yours

5: How to find ipv4 address?, if your running the server on your phone, you can change that "192.168.18.102" to "127.0.0.1", otherwise if your running the server on pc, open command prompt and type ipconfig and you'll see your ipv4 address down below which will start like "192.168.xx.xx"

6: Compile the apk with the changes and install it, and enjoy playing bsds brawl!

![Sceenshot of the menu](https://github.com/user-attachments/assets/22c744e1-791b-4ea5-87db-84c44a65b48c)
## credits ##
gene brawl : for the promon bypassed client
[Risporce](https://github.com/Risporce) for his readme
