Sure! Here is the code for a run.bat file that will help the user run the main.py program locally on their PC:

```batch
@echo off
pip install -r requirements.txt
python main.py
```

Please make sure to save this code in a file named "run.bat" in the same directory as your main.py and requirements.txt files. When the user runs the run.bat file, it will first install the required packages specified in the requirements.txt file using pip, and then execute the main.py program.

Note: The user will need to have Python and pip already installed on their PC for this to work.