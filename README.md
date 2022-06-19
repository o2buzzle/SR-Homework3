# JARVIS (Just a Rather Very Intelligent System)

## Built with

<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>


## Features

#### For a cool demo of this project watch this [YouTube video](https://www.youtube.com)

It can do a lot of cool things, some of them being:

- Greet user
- Can search anything on Google 
- Can play any song/video on YouTube
- Tell current time and date
- Tells about weather of any city
- Look up for a word through a dictionary
- Shutdown or reboot this device
- Can take screenshot and save it
- Has a cool Graphical User Interface

  
## Installation

- First clone the repo
- Make a new python environment
    If you are using anaconda just type ```conda create -n jarvis python==3.8.5``` in anaconda prompt
- To activate the environment ```conda activate jarvis```
- Navigate to the directory of your project
- Install all the requirements by just hitting ```pip install -r requirements.txt```
- Install PyAudio from wheel file by following instructions given [here](https://stackoverflow.com/a/55630212)
- Run the program by ```python src/sr_main.py```
- Enjoy !!!!

## Code Structure

    ├── src                              # main folder for source codes 
    │   ├── core_interaction             # Contains all secret API Keys
    │   │   ├── __init__.py              # classify the preprocessed sentence into 4 categories
    │   │   ├── browser_interface.py     # browse google or youtube for anything
    │   │   ├── info_interface.py        # get info about time, date, weather, or look up any word
    │   │   ├── media_interface.py       # search any thing on youtube
    │   │   └── system_interface.py      # to shutdown, reboot, or take a screenshot
    │   ├── GUI                          # for graphical user interface
    │   ├── speech_to_text               # model that converts input speech to text
    │   ├── text_to_speech               # model that converts text to speech (then speak it out)
    │   ├── interpreter.py               # processing an input sentence after preprocessing it
    │   ├── preprocess.py                # format an input sentence to make it more explicit for the model
    │   └── sr_main.py                   # main driver program of Jarvis
    └── requirements.txt                 # all dependencies of the program
