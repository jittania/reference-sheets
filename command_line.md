Command | Action | Notes
--- | --- | ---
`q` or `q!` | quit or force quit |
`exit(), quit(), ctrl c` | other ways to exit |
`pwd` | Print the path of the current working directory | Use this command when you're lost in the terminal or need to confirm where you are; you can read this path to understand the pathway to get to the current working directory from root.
`ls` |	List the visible files and folders that are inside of the current directory	| This command does not list hidden files or folders; there is a separate argument for that
`ls -A` | List all the files and folders inside of the current directory | The -A is an argument to the ls command - note that it could be path, such as 
`cd ..` | Change the working directory to the given path... And .. is a nickname for "the parent folder of the current directory." | Use this command to go "up" one folder level
`cd ~` | Change the working directory to the home directory |
`cd /` | Change the working directory to the root directory | 
`mkdir new-folder-name` |
Creates a new folder with the given path and folder name. By default, this will create a new folder as a sub-folder in the current working directory |	In this example, `mkdir new-folder-name` makes a new folder named `new-folder-name` inside the current directory.
`touch new_file.py`	| Creates a new file with the given path and file name. By default, this creates a new file inside the current working dierctory | Can include a relative path if you want to store the file somewhere else, such as `touch app/models/book.py`
`rm file.py`	| Deletes the file |
`man` | Displays manual pages for any command | Ex: `man cd`
`rm -rf` | | `rm -rf myproject`
`mv` | move file to new directory | `mv olddirectory newdirectory`
`cat` | used to concatenate and display files | syntax `cat filename` or `cat > filename` or `cat [options] filename`
`echo` | writes an argument to the Terminal’s standard output| syntax is `echo some_argument`
`grep` | searches plain text | super powerful and complex search tool