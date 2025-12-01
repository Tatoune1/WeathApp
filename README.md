# WeathApp

A simple weather app using the OpenWeatherMap API, created mostly for my portfolio and to learn PySide. It runs in a custom, separate environment and was built using PySide6, PySide tools, and—more specifically—PySide’s Designer, which can probably still be found in the environment folder if I was too lazy to delete it.
I used PySide6 mainly for two reasons:
**1** It includes a GUI framework that makes it much more fun to create UIs, and
**2** I already have friends who tested it.


## API Key

To make it work, you’ll need an API key from the official [OpenWeatherMap website](https://home.openweathermap.org/users/sign_up)
. Replace the `API_KEY` in the get_openweather_data() function in the weather_API.py with your own. I haven’t really received any spam, and API keys can probably be found anywhere anyway (it’s just OpenWeatherMap, after all).

Because I am not the smartest man alive, I may accidentally left my key somewhere in the folder. Please don’t use it (you probably will anyway, but please don’t), and if you do, don’t send more than 1 request per second.  


## Why is there a weather_API.py file here?

Yeah, I know, it’s not pretty. I originally tested OpenWeatherMap in another project (which might end up on GitHub as `ARVAC`), and since `Ctrl+C` and `Ctrl+V` were already more effort than I wanted to put in, I just dragged the whole file into this project.

I’ll eventually move it somewhere else or clean things up. If you’re reading this and thinking “why is he talking about a file that doesn’t even exist?” please let me know so I can update (or delete) this section of the README.

# How to make it work
In order to make the program run without installing all required library, you can use the env folder, by running `myenv\Scripts\activate` in the console. If it dont work, use pip to install PySide6 and requests
