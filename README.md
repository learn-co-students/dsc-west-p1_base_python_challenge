
# Base Python Week 1 Code Exercise

The present code challenge will test your skills in base Python.    
You will be asked to show your knowledge of:
 
 - basic Python types - strings, floats/integers, lists, and dictionaries.
 - for-loops and if/else statements
 - functions
 

You are presented with a data set describing scooter rides.  Chicago rolled out a pilot program for rentable scooters in 2019.

<a href='https://data.cityofchicago.org/Transportation/E-Scooter-Trips-2019-Pilot/2kfw-zvte'> <img src='./img/scooter_pilot.png'  height='500' width='500'></a>


```python
# Run cell with no changes

import sys

sys.path.append('src')

%load_ext autoreload
%autoreload 2

from data_import import load_scooter, load_start_end_numbers, load_start_time_and_distance, load_trip_distance, load_start_community_area, load_trip_dictionary
```

# Task 1: Strings

The data set defines where each trip starts, and where each trip ends by`'start_community_area_number'` and `'end_community_area_number'`.  

In the cell below, you are presented with two variables containing start and end community area information for the first trip: `trip1_scan` and `trip1_ecan` respectively.


```python
trip1_scan, trip1_ecan = load_start_end_numbers()
```


```python
print(trip1_scan)
```

    15



```python
print(trip1_ecan)
```

    15


As you can see from the cell output above, the 1st trip started and ended in Community Area 15. Community Area 15 is named Portage Park.


```python
community_area_15_name = 'Portage Park'
```

Just like numbers, strings can be joined using the `+` operator. 


With the variables defined above - `trip1_scan`, `community_area_15_name`- and the additional variables below, construct the following sentence:
   > "Trip 1 started in Community Area 15: Portage Park."

Combine the strings using the `+` operator.


```python
sentence_beginning = 'Trip 1 started in Community Area '
colon_and_space = ': '
sentence_end_punctuation = '.'
```


```python
# Your code here
answer_sentence = None
```



## Task 2: Integers and Floats
Two string variables are defined below named `trip1_dist` and `trip1_time`. 


```python
trip1_dist, trip1_time = load_start_time_and_distance()
```

The units of distance is meters.


```python
print(f"Trip 1 covered {trip1_dist} meters.")
```

    Trip 1 covered 3793 meters.


Time is measured in seconds


```python
print(f"Trip 1 took {trip1_time} seconds")
```

    Trip 1 took 1152 seconds


**Task 2a**: 
 > convert both of these strings to integers using a `built in method`.


```python
trip1_dist_int = None
```


```python
trip1_time_int = None
```

**Task 2b**: 
 > create a new variable, `trip_distance_miles`, which represents the length of the trip in miles.  
  > **hint** 1 mile is roughly equal to 1,609 meters.


```python
# Your code here

trip_distance_miles = None
```

# List Manipulation

## Task 3

Below, you are provided with a list containing all the trip distances in the original data set.  


```python
trip_distances = load_trip_distance()
```

**Task 3a**: 
 > Determine how many rides are in the dataset, and assign that number to the `number_of_rides` variable.


```python
# Your code here
number_of_rides = None
```

Although you cannot tell from the list by itself, the rides are ordered by start_community_area_number.  
The first 7 rides correspond to rides that started in community area 15.  

**Task 3b:**
  > Create a new variable, `trips_start_15` which contains a slice of the list corresponding to the first 7 rides.  


```python
trips_start_15 = None
```

**Task 3c:**

  > Add a new element - `the integer 1500` - to the end of the trip_distances list.


```python
# your code here
```

## Task 4:  Basic Dictionary Manipulation

The original data comes in the form of dictionaries.  The data for each trip is stored as is shown below for the first trip.



```python
trip_1 = {'trip_id': '33b50938-5626-4124-ba57-cc0a3dd058aa',
  'trip_distance': '3793',
  'trip_duration': '1152',
  'start_community_area_number': '15',
  'end_community_area_number': '15'}

```

**Task 4a**: 
  > As you can see in the cell above, trip distance is defined as a `string`.
  > Using key value pairs, reassign the `trip_distance` value to the `integer 3793`.


```python
# Your code here
```

**Task 4b**:
  > create a new key value pair within `trip_1` representing the name of the start area community name: `Portage Park` .  Use `start_area_community_name` as the key.


```python
# Your code here
```

# Task 5: For-Loops and if/else statements

Let's return to the trip_distances list, reloaded below for your convenience:



```python
trip_distances = load_trip_distance()
```

**Task 5a:**
 > Using a **for-loop** and **if/else** statements, create a new list called `short_rides` which holds all rides less than or equal to 700 meters.   



```python
# Your code here
short_rides = None
```

**Task 5b**:
    
  > Add another conditional statement to the for loop above to create two lists simultaneously: `short_rides` and `long_rides`.   
  >> `short_rides` should consist of rides less than or equal to 700 meters.  
  >> `long_rides` should consist of rides greater than or equal to 5,000 meters.
    


```python
# Your code here
short_rides = None
long_rides = None

```

## Task 6: Functions

> Create a simple function named `longest_ride` which takes the a list of integers as a **parameter** and **returns** the largest integer.

> Passing `trip_distances` as an argument to the function should result in the function returning the distance of the longest ride in meters.


```python
# Your code here
def longest_ride():
    pass
```

# Bonus task

The original data comes from an API query that returns a json object.  We will cover json's soon.  Below, this json object is converted to a list of dictionaries.  


```python
trips_list = load_scooter()
```

We see the first trip once again as accessed using the first index in the trips_dictionary.


```python
trips_list[0]
```




    {'trip_id': '33b50938-5626-4124-ba57-cc0a3dd058aa',
     'trip_distance': '3793',
     'trip_duration': '1152',
     'start_community_area_number': '15',
     'end_community_area_number': '15'}



Create a function called `get_start_area_rides`, which takes two **parameters**:

    `start_area`: a string representing the community number of a trip's start community area number.
    `trips_list`: the full **list** of rides imported above as `trips_list`
    
The function should loop through the rides and select only those which start in the community area fed to it as an argument.

It should **return** a list of rides, each of which is the full dictionary describing the data of the ride.



```python
# Your code here

def get_start_area_rides():
    pass
```
