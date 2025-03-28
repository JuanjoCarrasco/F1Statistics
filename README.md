# FORMULA 1 WORLD CHAMPIONSHIP STATISTICS
#### Author: Juan José Carrasco Fernández
#### Date: 28/03/2025
### Description:
#### Introduction:

This is the README file for the FORMULA 1 WORLD CHAMPIONSHIP STATISTICS, a Python program designed to display data and statistics about the F1 world champion of each season from 1950 to 2024.

#### Dataset:

The dataset used in this project consists of several .csv files containing information on Formula 1 races, drivers, constructors, qualifying, circuits, lap times, pit stops and championships from 1950 till the latest 2024 season. The F1 World Championship dataset can be downloaded from [kaggle](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020).

Additionally, an extra file, *scoring_systemsV3.csv*, was requiered. This file, which is self-made and not part of the official F1 database, contains information about the scoring system for each season.

#### Libraries:

The required libraries are listed in the *requirements.txt* file. 

#### Features

Upon running the program, the data is loaded, and the title screen and main menu are displayed. The main menu is as follows:

Select data to retrieve:
* Press 1 for World Drivers' Champions.
* Press 2 for World Constructors' Champions.
* Press 3 for data about drivers.
* Press 4 for data about constructors.
* Press 5 for data about a season.   
* Press 6 for info about F1 World Championship dataset.
* Press 'e' to exit.

Selecting World Drivers' Champions (**option 1**) will display a second menu that allows you to sort the results:

Select variable to sort results:
* Press 1 to sort by season.
* Press 2 to sort by wins.
* Press 3 to sort by win rate.
* Press 4 to sort by points.
* Press 5 to sort by points rate.
* Press 6 to sort by points difference with the second classified.
* Press 'r' to return.
* Press 'e' to exit.

After selecting the variable to sort, the results table will display the following information for each season:
* Season.
* Number of races in the season.
* Name and surname of the champion driver.
* Age.
* Team.
* Number of wins in the season.
* Ratio of wins over the total.
* Points earned.
* Ratio of points over the total.
* Difference in points with the second-placed driver.

By pressing any key, another table will appear showing the F1 World Drivers' Champions with the following variables:

* Forename.   
* Surname.    
* Code.   
* Number.   
* Date of birth.   
* Nationality.   
* Number of Races.
* Number of World Drivers' Championsips. 
* Number of Wins. 
* Number of Podiums. 
* Number of Poles. 
* Number of Points. 
* Number of Fastest laps (due to missing data, that information may be inaccurate).

Selecting **option 2** in the main menu will display statistics about F1 World Constructors' (this data can be sorted in a similar way as option 1) with the following variables for each season: 

* Season.
* Number of races in the season.
* Name of the winning team.
* Number of wins in the season.
* Ratio of wins over the total.
* Points earned.
* Ratio of points over the total.
* Difference in points with the second-placed team.

Again, pressing any key will display another table showing the F1 World Constructors' Champions with the following variables:

* Name of team.  
* Nationality.   
* Number of Races.
* Number of World Constructors' Championsips. 
* Number of World Drivers' Championsips. 
* Number of Wins.
* Number of Podiums. 
* Number of Poles. 
* Number of Points. 
* Number of Fastest laps (due to missing data, that information may be inaccurate).

Selecting **option 3** in the main menu allows you to retrieve information about drivers by entering the surname of one or more drivers, separated by commas. If only one surname is entered, the information will be displayed in text format, and if more than one surname is entered, the information will be displayed in table format. If multiple drivers share the same surname, a menu will appear to allow you to select the desired driver.

**Option 4** provides information about one or more teams, functioning similarly to option 3 in the menu.

**Option 5** allows you to obtain the results of a specific session. After entering the session year, a new menu appears where you can select a race from the chosen year. The following variables are displayed:

* Position of the driver. 
* Driver name and surname.          
* Team.        
* Completed laps. 
* Time.         
* Grid position at the start.
* Points earned.
* Points accumulated in the world championship up to that race.

Pressing "f" will display the final results of the session.

Finally, **option 6** provides information about the dataset.



