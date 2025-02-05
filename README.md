# Script for getting the weather

[wttr.in](https://wttr.in/) is a web service for getting weather information. This script sends GET requests to wttr.in with preset parameters to get formatted weather data for a predefined list of locations.

## Installation

1. Make sure that Python is installed on your computer. You can download it from python.org.

2. Install the requests library, if it is not already installed:
```
bash
pip install requests
```
## Usage

1. Define a list of places in the `cities` variable. By default, the list includes:

* Cherepovets
* London
* SVO

2. Run the script:
```
bash
python main.py
```
3. The script will receive and display weather information for each location in Russian.

## Additional information

1. Make sure that you have an active internet connection when running the script.

2. The script uses the `response.raise_for_status()` method to handle HTTP errors.

3. You can customize the list of locations and parameters according to your needs.

## The purpose of the project

This project was developed for educational purposes as part of an online course for web developers on the platform [dvmn.org](https://dvmn.org/). He demonstrates API skills, data processing, and creating a tool for comparing information from different sources.
