# GovNaB Voice Typing
You probably have used _Google's Voice Typing_ feature where you don't have to type anything, everything will be done by the system, it's just you have to say and the system will automatically converts it into string and tyoe it onto the place where you are planning on typing. Well that same feature is applied here with the help of **Python**.

## Working
1. The UI of this project was made with **TKinter Module**.
2. The _Voice Type_ button will trigger the voice typing by calling the **writeOnScreen()** function.
3. This function will invoke **speechToText()**, an another function.
4. The second function will take voice input from user and returns it by converting it into text.
5. At last the first function will write this received string on the _Text Area_ created with the help of **PyAutoGUI Module**.

## Opening
1. To install all the required libraries, type<br>`pip install -r requirements.txt`<br>in command prompt.
2. All the required libraries will download automatically. Now run `voice_typing.py` file with<br>`python voice_type.py` command<br>and use it.