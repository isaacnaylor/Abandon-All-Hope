# Abandon-All-Hope
Abandon All Hope Is A Minecraft Plugin
How to install Spigot and the Python plugin
===
1. Download all 5 files:
  * paper-204.jar
  * PythonPlugins-1.0-SNAPSHOT.jar
  * example_plugin.py
  * cat_snowballs.py
  * iron_man_suit.py
2. Create a directory for your test server and create plugin directories:
  # example for Ubuntu on Windows:
  # - first, start Ubuntu, then in the shell, enter the following commands:
  $ mkdir testserver
  $ mkdir testserver/plugins
  $ mkdir testserver/superpowers
3. Copy the files from Windows download into your test server directory
  # example for Ubuntu on Windows:
  # - first, start Ubuntu, then in the shell, enter the following commands: (NOTE: you have to substitue your windows username into the commands)
  # - if you don't know your windows username, you can try the following:
  $ ls /mnt/c/Users   # then look for the users that are listed and pick the one you are logged in as
  $ MAC: cp ~/Downloads/paper-204.jar testserver
  $ cp /mnt/c/Users/[your windows username here]/Downloads/paper-204.jar testserver
  $ cp /mnt/c/Users/[your windows username here]/Downloads/PythonPlugins-1.0-SNAPSHOT.jar testserver/plugins
  $ cp /mnt/c/Users/[your windows username here]/Downloads/example_plugin.py testserver/superpowers
  $ cp /mnt/c/Users/[your windows username here]/Downloads/cat_snowballs.py testserver/superpowers
  $ cp /mnt/c/Users/[your windows username here]/Downloads/iron_man_suit.py testserver/superpowers
4. Accept the minecraft EULA:
  $ echo eula=true > testserver/eula.txt
5. Start up the server once to get it installed:
  $ cd testserver
  $ java -jar paper-204.jar nogui
6. Attach to your local server:
  # start minecraft 1.16.3
  # pick Multiplayer
  # pick Local Server
7. Try throwing a snowball and seeing if it spawns a cat with thunder
8. Try putting on an iron helmet in survival mode and see if you hear thunder and can fly in survival

To see the code for the cat snowballs superpower, look at the contents of the `cat_snowballs.py` file
To see the code for the iron man suit superpower, look at the contents of the `iron_man_suit.py` file
