# Vector_The_Lost_Treasure 👾

--> A Raspberry Pi's SenseHat LED-based game for all ages. Enjoy! :D <--

# Installing steps

## 1. Install python3

### Windows

Go to the python.org website. Link -> https://www.python.org/downloads/

### MacOS and Linux-based systems

Type this is Terminal application:
```
sudo apt install python3
``` 

## 2. Download the game

![Suggesting image](https://github.com/DavidGhergut/Vector_The_Lost_Treasure/blob/master/Download_the_ZIP_file.png)

Or clone the repository from Terminal / Powershell:

```
git clone https://github.com/DavidGhergut/Vector_The_Lost_Treasure
```

## 3. Install the essential modules

Open the Powershell application (Windows) or Terminal and type this command:

```
pip install -r requirements.txt
```
## ⚠️ For M1 Macs, pygame currently does not have all the features fixed, thus in order to make pygame work properly, you need run the following command in the Terminal ⚠️

```
pip install git+https://github.com/Muxelmann/pygame.git@patch-1
```
### 📚 For more detailes check this out -> https://github.com/pygame/pygame/pull/2636!

## 4. Run the game

### Windows

Go to the local folder and press ```Shift + Right Click```

![Opening local Powershell](https://github.com/DavidGhergut/Vector_The_Lost_Treasure/blob/master/Opening_Powershell.jpg)

Type this command in the Powershell application:
```
python.exe .\MAINMENU.py
```

### MacOS and Linux-based systems

Type these commands in the Terminal

```
python3 MAINMENU.py
```

You will see popping up a pygame window and in order to enter the game ```Left Click + Space``` and then you will be able to move around.

### Basic Controls -> Navigation

Select -> ```Space```

Move around -> ```Keyboard arrows (Up, Down, Left, Right)```

We suggest you playing the game like this:

![Playing suggestion](https://github.com/DavidGhergut/Vector_The_Lost_Treasure/blob/master/Playing_suggestion.png)

So that it is easier to follow the instructions and indications on the Powershell / Terminal.

Beware that by default, the game is in Romanian, but if you want to use the English version, go through each file and you will see blocks of code like this:

![Romanian to English conversion](https://github.com/DavidGhergut/Vector_The_Lost_Treasure/blob/master/Romanian_To_English_Conversion.png)

Uncomment the English part and comment the Romanian part for a more general experience!

### Very important!! We also recommend using headphones or speakers for an even more enhanced experience!

### P.S. If you want to use a physical SenseHat, please enter the following command on the Powershell / Terminal!!

```
git apply sensehat.diff
```

# This is it! You are done installing *Vector. The Lost Treasure.* Thank you so much and happy gaming! 💪
