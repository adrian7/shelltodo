#ShellTODO#

***A simple TODO List manager directly from shell***

##Installing:##
First make sure you have Python installed, version 2.2.6 or newer. Then make sure you have a python interpreter in your PATH. You can check that with `ls -l /usr/bin | grep python` , and if you see a symlink called "python" it means it's ok. 
On most  *nix machines python and a suitable ENV would be available by default.

Download the file shelltodo.py and save it on your computer. Then make it executable: `$ chmod +x shelltodo.py`
Then you should be able to run it: `$ ./shelltodo.py -h` . You should see the help screen.

##Advanced install (like a pro!)##
You can also add shelltodo.py to your PATH using  `.bashrc` and thus making it available from erywhere. 

- Make a directory (preferably in your home directory) called myscripts and copy in it the file shelltodo.py;
- Rename shelltodo.py to simply `todo`
- Make sure it's an executable `$ chmod +x todo`
- Add the following lines to your `.bashrc` file:
` PATH=$PATH:/home/username/myscripts
    export PATH`

Course you'll have to replace *username* in the above path with your linux user.
Test it: `$ todo -h`

##Usage##
Examples of commands

+ `$ todo -s ` : shows the todolist 
+ `$ todo -a "Write a letter to Santa "` : add a new item to list
+ `$ todo -m 4 ` : mark item #4 as completed
+ `$ todo -d 2` : delete item 2 from list
+ `$ todo -x ` : delete the entire list (clear)

Combining commands
`$ todo -s -m 2 -a "A new item"` : shows the current list, marks item 2 as completed, and adds "A new item" to the list
`$ todo -s -d 10 ` : shows the todolist then deletes item #10

###Settings###
If you open the file shelltodo.py, you'll notice at the beginning of it the settings:

+ AUTOSAVE : tells the script to save any modifications to file - `True` or `False`;
+ AUTOLOAD: tells the script to load the todo list file before any action - `True` or `False`;
+ SHELLONLY: disables the interactive mode, and makes the script to go back to shell once the command(s) have been executed. When `False`, any call of the script from shell whithout the -q (quit) command will drop the user to interactive mode. Possible value `True` or `False`
+ HOMEDIR: the base directory to keep the todo.list file. You can set here an custom path, and thus have all users using the same todo list. Defaults  to the user's home directory.
+ OUTFILE: The script's output file. Replacing it with an absolute path will have the same effect, will overwrite the option above, and have the same result.


