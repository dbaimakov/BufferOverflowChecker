# BufferOverflowChecker

Copy and paste the script into Notepad++, then save it as a .py file.

Press the Windows key and search for "Command Prompt", or press Windows + R, type in cmd, and hit Enter.

To install PyPDF2, type pip install PyPDF2 in the command prompt and hit Enter.

To avoid potential issues, update pip by typing the following into the command prompt:
"C:\Program Files\Python311\python.exe" -m pip install --upgrade pip

Open Command Prompt and navigate to the directory where the script is saved using the cd (change directory) command.

After navigating to the correct directory, run the saved python script from that directory. The command to run would look like this:
"C:\Program Files\Python311\python.exe" check_for_null_and_long_strings.py

If your command prompt is not already in the script's directory, you would need to input the full path to the script. In that case, the command would look like this:
"C:\Program Files\Python311\python.exe" "C:\Users\BaimakovD\Desktop\Scripts\check_for_null_and_long_strings.py"

After running the command, the script will inform you if your PDF contains NULL or excessively long strings.
