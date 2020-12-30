
# Base Python Week 1 Code Challenge

The present code challenge will test your skills in base Python.    
You will be asked to show your knowledge of:
 
 - basic Python types - strings, floats/integers, lists, and dictionaries.
 - for-loops and if/else statements
 - functions
 

You are presented with a data set describing scooter rides.  Chicago rolled out a pilot program for rentable scooters in 2019.

<img src='./img/scooter_pilot.png' height='500' width='500'>

As you see in the output from the cell above, each ride data point contains information about distance, time, and the start and end locations of the trips. 

# Strings

Each trip in the Scooter data consists of a `'start_community_area_number'` and an `'end_community_area_number'`.  

The start and end community area number are assigned to two variables below: `trip1_scan` and `trip1_ecan` respectively.

## Task 1:
Create a new variable, `trip1_st_end_cn` that combines the start community area and the end community area with an underscore. 



```python
trip1_st_end_cn = trip1_scan + '_' + trip1_ecan
trip1_st_end_cn
```




    '15_15'



# Ints and Floats

## Task 2:
Two string variables are defined below named `trip1_dist` and `trip1_time`. 


  - First: convert these strings to integers or floats. 
  - Second: the original units are in meters and seconds. Make a new variable, `trip_mph` which represents speed in mph.  
  
> Hint: to convert meters to miles, divide by 1609.



```python

trip_mph = (int(trip1_dist)/1609)/(int(trip1_time)/(60*60))
trip_mph
```




    2.237414543194531



# Basic List Manipulation

## Task 3

The data list is comprised of 943 scooter rides.

They are ordered by start_community_area_number.  The last 30 records are rides starting in community area 31.  
Create a new list called `trips_area_31` that consists of only rides that start in area 31.


```python

trips_area_31 = data[-30:]
len(trips_area_31)
```




    30



## Task 4

Below, information associated with a new trip is defined.  Add this trip to the end of the trips_area_31 list.


```python
trips_area_31.append(new_trip)
```

`trips_area_31` should now have 31 rides in it.

# Basic Dictionary Manipulation

Below is a dictionary which contains data related to a second new trip.

Notice that the trip distance and trip duration are represented by strings with commas in them.  Such a format can result in errors during data procesing.

## Task 5

Add new_trip_2 to the `trip_areas_31` list, but before doing so, reassign the value of trip distance and trip duration to values without commas: i.e. 4400 and 2000.   
The final types should still be strings.
You do not have to do fancy string manipulation, but you do have to assign values using **key/value** pairs.  
Do not just fix the strings in the code block above. 




```python
new_trip_2['trip_distance'] = '4400'
new_trip_2['trip_duration'] = '2000'
```


```python
trips_area_31.append(new_trip_2)
```

# For-Loops and if/else statements

The `trip_distance` variable below is **list** of all of the rides' trip distances in their original unit (meters) and type (string).  


The distances correspond to the same data in the list of dictionaries above, but the trip distances have been isolated from the other data.

## Task 6

Using a **for-loop** and **if/else** statements, create a new list called `short_rides` which holds all rides less than or equal to 1 mile.   
To do so, you will once again have to convert to miles by dividing by 1609.


```python
short_rides = []

for trip in trip_distances:
    
    trip_in_miles = int(trip)/1609
    
    if trip_in_miles <= 1:
        short_rides.append(trip_in_miles)
        
short_rides[:5]
```




    [1.0,
     0.4934742075823493,
     0.5699192044748291,
     0.8999378495960224,
     0.5823492852703542]



## Task 7

What percentage of the total rides are less than or equal to 1 mile?


```python
len(short_rides)/len(trip_distances) * 100
```




    52.70413573700954



# Processing Two Lists at Once

The variable `start_community_areas` holds a list of community area numbers where each trip started.   

The `start_community_areas` list and the `trip_distance` list are the same length, and are both ordered in the same way.  
In other words, the 1st element of `start_community_areas` and the 1st element of `trip_distance` refer to the same trip.  

The built in [zip](https://docs.python.org/3/library/functions.html#zip) function allows you to iterate through multiple iterables at the same time.  
Each trip through the for-loop processes elements with matching indices from the iterables passed as arguments.

## Task 8

Using a **for-loop** and the **zip** function, create a list called `short_rides_22` which stores all trip_distances (in miles) less than or equal to 1 mile which originated in community area 22.


```python

short_rides_22 = []

for distance, comm_num in zip(trip_distances, start_community_areas):
    
    dist_in_miles = int(distance)/1609
    
    if dist_in_miles <= 1 and comm_num == '22':
        short_rides_22.append(dist_in_miles)
        
short_rides_22[:5]
```




    [0.9297700435052828,
     0.9527656929770043,
     0.23927905531385954,
     0.45245494095711625,
     0.5835922933499068]



## Task 9

Next, create a similar for loop, but this time create two lists simultaneously:
 -  the list `short_rides_24` stores all trip_distances (in miles) less than or equal to 1 mile which originated in community area 24.
 -  the list `short_rides_28` stores all trip_distances (in miles) less than or equal to 1 mile which originated in community area 28.




```python

short_rides_24 = []
short_rides_28 = []

for distance, comm_num in zip(trip_distances, start_community_areas):
    dist_in_miles = int(distance)/1609
    
    if dist_in_miles <= 1 and comm_num == '24':
        short_rides_24.append(dist_in_miles)
    
    elif dist_in_miles <= 1 and comm_num == '28':
        short_rides_28.append(dist_in_miles)
        
    else:
        pass
print(short_rides_24[:5])
print(short_rides_28[:5])
```

    [0.07955251709136109, 0.814791796146675, 0.0, 0.7501553760099441, 0.7806090739589807]
    [0.6668738346799254, 0.8458669981354879, 0.6830329397141082, 0.0, 0.6395276569297701]


# Nested Dictionaries

You are now presented with the rides data in a slightly different form. Instead of a list of rides, it is a dictionary.

Each element in the `trips_dictionary` variable below uses the trip_id as a dictionary key, and stores the trip data associated with each key as a second dictionary.

This nested, second dictionary has keys representing all the data you have come to know: trip_distance, trip_duration, start_community_area_number, and end_community_area_number.

## Task 10

Now, loop through this new dictionary and find all rides **over 20 minutes**. 

Store these rides in a dictionary called `long_rides` with trip_id's as keys and ride time in minutes as the value.

Again, you will have to convert the ride durations to integers, as well as convert seconds to minutes.


```python
long_rides = {}
for ride in trips_dictionary:

    ride_in_minutes = int(trips_dictionary[ride]['trip_duration'])/60
    
    if ride_in_minutes > 20:
        long_rides[ride] = ride_in_minutes

```

# Functions 

## Task 11

Next, create a function called `start_area_durations`, which takes two parameters:

    `start_area`: a string representing the community number of a trip's start community area number.

and either:

    `data`: the full **list** of rides imported above.
    or
    `trips_dictionary`: the dictionary of rides which uses ride_id as keys.
    
The function should loop through the rides and select only those which start in the community area fed to it as an argument.

It should **return** a list of rides, each of which is the full dictionary describing the data of the ride.

> **Note** Whether you use the data variable or the trips_dictionary variable, you should get almost identical output.  
However, using the trips_dictionary may return a list of rides which do not have ride ids.  That is acceptible. Everything else will be the same.



```python
def start_area_durations(start_area, data):
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


```python


def start_area_durations_with_dict(start_area, trips_dictionary):
    '''
    Return all rides in a given start area.
    
    Params
    trips_dictionary: a dictionary of rides which uses ride_id as the key
    start_area: a string representing a community start area
    ----
    returns
    community_area_rides: a list of all rides in a given community area without ride_ids.
    '''
    community_area_rides = []
    for ride in trips_dictionary:
        if trips_dictionary[ride]['start_community_area_number'] == start_area:
            community_area_rides.append(trips_dictionary[ride])
    
    return community_area_rides
```

## Task 12

Finally, build a second function `start_area_longest_ride` which **returns the distance in miles** of the longest ride for a given start area community number.  
Ideally, this function will act on  the output of the function coded above.

Whether you used the data list or trips_dictionary, the output should be the same.
