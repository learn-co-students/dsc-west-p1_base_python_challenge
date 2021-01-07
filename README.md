
# Base Python Week 1 Code Exercise

The present code challenge will test your skills in base Python.    
You will be asked to show your knowledge of:
 
 - basic Python types - strings, floats/integers, lists, and dictionaries.
 - for-loops and if/else statements
 - functions
 

You are presented with a data set describing scooter rides.  Chicago rolled out a pilot program for rentable scooters in 2019.

<a href='https://data.cityofchicago.org/Transportation/E-Scooter-Trips-2019-Pilot/2kfw-zvte'> <img src='./img/scooter_pilot.png'  height='500' width='500'></a>

# Task 1: Strings

The data set defines where each trip starts, and where each trip ends by`'start_community_area_number'` and `'end_community_area_number'`.  

In the cell below, you are presented with two variables containing start and end community area information for the first trip: `trip1_scan` and `trip1_ecan` respectively.

As you can see from the cell output above, the 1st trip started and ended in Community Area 15. Community Area 15 is named Portage Park.

Just like numbers, strings can be joined using the `+` operator. 


With the variables defined above - `trip1_scan`, `community_area_15_name`- and the additional variables below, construct the following sentence:
   > "Trip 1 started in Community Area 15: Portage Park."

Combine the strings using the `+` operator.


```python
answer_sentence = sentence_beginning + trip1_scan + colon_and_space + community_area_15_name + sentence_end_punctuation
```



## Task 2: Integers and Floats
Two string variables are defined below named `trip1_dist` and `trip1_time`. 

The units of distance is meters.

Time is measured in seconds

**Task 2a**: 
 > convert both of these strings to integers using a `built in method`.


```python
trip1_dist_int = int(trip1_dist)
```


```python
trip1_time_int = int(trip1_time)
```

**Task 2b**: 
 > create a new variable, `trip_distance_miles`, which represents the length of the trip in miles.  
  > **hint** 1 mile is roughly equal to 1,609 meters.


```python

trip_distance_miles = int(trip1_dist)/1609
trip_distance_miles
```




    2.357364822871349



# List Manipulation

## Task 3

Below, you are provided with a list containing all the trip distances in the original data set.  

**Task 3a**: 
 > Determine how many rides are in the dataset, and assign that number to the `number_of_rides` variable.


```python
number_of_rides = len(trip_distances)
```

Although you cannot tell from the list by itself, the rides are ordered by start_community_area_number.  
The first 7 rides correspond to rides that started in community area 15.  

**Task 3b:**
  > Create a new variable, `trips_start_15` which contains a slice of the list corresponding to the first 7 rides.  


```python
trips_start_15 = trip_distances[:7]
```

**Task 3c:**

  > Add a new element - `the integer 1500` - to the end of the trip_distances list.


```python
trip_distances.append(1500)
```

## Task 4:  Basic Dictionary Manipulation

The original data comes in the form of dictionaries.  The data for each trip is stored as is shown below for the first trip.


**Task 4a**: 
  > As you can see in the cell above, trip distance is defined as a `string`.
  > Using key value pairs, reassign the `trip_distance` value to the `integer 3793`.


```python
trip_1['trip_distance'] = 3793
```

**Task 4b**:
  > create a new key value pair within `trip_1` representing the name of the start area community name: `Portage Park` .  Use `start_area_community_name` as the key.


```python
trip_1['start_area_community_name'] = 'Portage Park'
```

# Task 5: For-Loops and if/else statements

Let's return to the trip_distances list, reloaded below for your convenience:


**Task 5a:**
 > Using a **for-loop** and **if/else** statements, create a new list called `short_rides` which holds all rides less than or equal to 700 meters.   



```python
short_rides = []

for trip in trip_distances:
    
    if trip  <= 700:
        short_rides.append(trip)
        

```

**Task 5b**:
    
  > Add another conditional statement to the for loop above to create two lists simultaneously: `short_rides` and `long_rides`.   
  >> `short_rides` should consist of rides less than or equal to 700 meters.  
  >> `long_rides` should consist of rides greater than or equal to 5,000 meters.
    


```python

short_rides = []
long_rides = []

for trip in trip_distances:
    
    if trip  <= 700:
        short_rides.append(trip)
    
    elif trip >= 5000:
        long_rides.append(trip)
        

```

## Task 6: Functions

> Create a simple function named `longest_ride` which takes the a list of integers as a **parameter** and **returns** the largest integer.

> Passing `trip_distances` as an argument to the function should result in the function returning the distance of the longest ride in meters.


```python
def longest_ride(trip_distances):
    
    return max(trip_distances)
    
    
```

# Bonus task

The original data comes from an API query that returns a json object.  We will cover json's soon.  Below, this json object is converted to a list of dictionaries.  

We see the first trip once again as accessed using the first index in the trips_dictionary.

Create a function called `get_start_area_rides`, which takes two **parameters**:

    `start_area`: a string representing the community number of a trip's start community area number.
    `trips_list`: the full **list** of rides imported above as `trips_list`
    
The function should loop through the rides and select only those which start in the community area fed to it as an argument.

It should **return** a list of rides, each of which is the full dictionary describing the data of the ride.



```python
def get_start_area_rides(start_area, trips_list):
    
    '''
    Return a list of all rides for a given start area.
    
    Params
    data: a list of rides, each of which is a dictionary of data.
    start_area: a string representing a community start area
    ----
    returns
    community_area_rides: a list of all rides in a given community area
    '''
    
    community_area_rides = []
    
    for ride in data:
        if ride['start_community_area_number'] == start_area:
            community_area_rides.append(ride)
    
    return community_area_rides
```
