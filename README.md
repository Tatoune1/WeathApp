# WeathApp

A simple weather app using the OpenWeatherMap API, created mostly for my portfolio and to learn PySide.

## Features

* **Weather Display**: Display the current weather in a chosen city.
* **Favorites Cities**: Users can quickly access to a list of city put in favorites.
* **Weather Forcast**: Users can see the weather they are going to deal with.
* **Searchable city List**: User can check the weather on any city.
* **Custom UI**: Frameless and styled windows with drag support.

## Installation

### 1. Clone the repository:

```bash
git clone <your-repository-url>
cd <repository-folder>
```

### 2. Create a virtual environment (recommended):

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the application:

```bash
python main.py
```


## API Key

To make it work, you’ll need an API key from the official [OpenWeatherMap website](https://home.openweathermap.org/users/sign_up)
. Replace the `API_KEY` in the get_openweather_data() function in the weather_API.py with your own. I haven’t really received any spam, and API keys can probably be found anywhere anyway (it’s just OpenWeatherMap, after all).



## Why is there a weather_API.py file here?

Yeah, I know, it’s not pretty. I originally tested OpenWeatherMap in another project (which might end up on GitHub as `ARVAC`), and since `Ctrl+C` and `Ctrl+V` were already more effort than I wanted to put in, I just dragged the whole file into this project.

I’ll eventually move it somewhere else or clean things up. If you’re reading this and thinking “why is he talking about a file that doesn’t even exist?” please let me know so I can update (or delete) this section of the README.
