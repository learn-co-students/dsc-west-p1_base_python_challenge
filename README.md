
# Base Python Week 1 Code Exercise

The present code challenge will test your skills in base Python.    
You will be asked to show your knowledge of:
 
 - basic Python types - strings, floats/integers, lists, and dictionaries.
 - for-loops and if/else statements
 - functions
 

You are presented with a data set describing scooter rides.  Chicago rolled out a pilot program for rentable scooters in 2019.

<img src='./img/scooter_pilot.png' height='500' width='500'>

# Task 1: Strings

The data set defines where each trip starts, and where each trip ends by`'start_community_area_number'` and `'end_community_area_number'`.  

In the cell below, you are presented with two variables containing start and end community area information for the first trip: `trip1_scan` and `trip1_ecan` respectively.

As you can see from the cell output above, the 1st trip started and ended in community area 15.


 > Create a new variable, `trip1_st_end_cn` that combines the start community area and the end community area with an underscore for the 1st trip only.  



```python
trip1_st_end_cn = trip1_scan + '_' + trip1_ecan
trip1_st_end_cn
```




    '15_15'





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
 > create a new variable, `trip_mph`, which represents the average speed of the trip in miles per hour.  
  > **hint** 1 mile is roughly equal to 1,609 meters.


```python

trip_mph = (int(trip1_dist)/1609)/(int(trip1_time)/(60*60))
trip_mph
```




    7.366765071472965



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
  > Create a new variable, `trips_start_15`, which holds all trip distances that start in area 15. Slice the list using indices.



```python
trips_start_15 = trip_distances[:7]
```

The last 30 records are rides starting in community area 31.  

**Task 3c:**
  > Create a new list called `trips_area_31` that consists of only rides that start in area 31.


```python

trips_area_31 = data[-30:]
```

**Task 3d:**

  > Add a new element to the end of the trip_distances list with the integer 1500.


```python
trip_distances.append(1500)
```

## Task 4:  Basic Dictionary Manipulation

The original data comes in the form of dictionaries.  The data for each trip is stored as is shown below for the first trip.


**Task 4a**: 
  > Using key value pairs, reassign the `trip_distance` value to the integer 3793.


```python
trip_1['trip_distance'] = 3793
```

**Task 4b**:
  > create a new key value pair within `trip_1` representing average speed of of trip in miles per hour.  Use `mph` as the key, and make sure the value associated with the key is a float.


```python
trip_1['mph'] = (trip_1['trip_distance']/1609)/(int(trip_1['trip_duration'])/(60*60))
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

> Create a simple function named `longest_ride` which takes the a **list of integers as an argument** and **returns the value of the longest ride distance.**


```python
def longest_ride(trip_distances):
    
    return max(trip_distances)
    
    
```

# Bonus task

The original data comes from an API query that return a json object.  We will cover json's soon.  Below, this json object is converted to a list of dictionaries.  

Create a function called `start_area_durations`, which takes two **parameters**:

    `start_area`: a string representing the community number of a trip's start community area number.
    `trips_list`: the full **list** of rides imported above.
    
The function should loop through the rides and select only those which start in the community area fed to it as an argument.

It should **return** a list of rides, each of which is the full dictionary describing the data of the ride.



```python
def start_area_durations(start_area, trips_list):
    '''
    Return all rides in a given start area.
    
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
