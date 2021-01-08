
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

from test_scripts.test_class import Test

```

    The autoreload extension is already loaded. To reload it, use:
      %reload_ext autoreload


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
print(trip1_scan)
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
# Replace None with the appropriate code
answer_sentence = None

### BEGIN SOLUTION
answer_sentence = sentence_beginning + trip1_scan + colon_and_space + community_area_15_name + sentence_end_punctuation
### END SOLUTION
print(answer_sentence)
```

    Trip 1 started in Community Area 15: Portage Park.



```python
### BEGIN HIDDEN TESTS

assert answer_sentence == 'Trip 1 started in Community Area 15: Portage Park.'


### END HIDDEN TESTS
```



## Task 2: Integers and Floats
Two string variables are defined below named `trip1_dist` and `trip1_time`. 


```python
trip1_dist, trip1_time = load_start_time_and_distance()
```


```python
# The units of distance is meters.
print(f"Trip 1 covered {trip1_dist} meters.")
```

    Trip 1 covered 3793 meters.



```python
# Time is measured in seconds
print(f"Trip 1 took {trip1_time} seconds")
```

    Trip 1 took 1152 seconds


**Task 2a**: 
 > convert both of these strings to integers using a `built in method`.


```python
# Replace None with the appropriate code
trip_dist_int = None
trip_time_int = None

### BEGIN SOLUTION

trip1_dist_int = int(trip1_dist)
trip1_time_int = int(trip1_time)

### END SOLUTION
```


```python
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

### BEGIN HIDDEN TESTS

assert trip1_dist_int == 3793
assert trip1_time_int == 1152

### END HIDDEN TESTS
```

**Task 2b**: 
 > create a new variable, `trip_distance_miles`, which represents the length of the trip in miles.  
  > **hint** 1 mile is roughly equal to 1,609 meters.


```python
# REplace None with the appropriate code
trip_distance_miles = None

### BEGIN SOLUTION

trip_distance_miles = int(trip1_dist)/1609

test = Test()


test.save(trip_distance_miles, 'trip_distance_miles')


### END SOLUTION
```


```python
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

### BEGIN HIDDEN TESTS

Test().run_test(trip_distance_miles,'trip_distance_miles')


### END HIDDEN TESTS
```

# List Manipulation

## Task 3

Below, you are provided with a list containing all the trip distances in the original data set.  


```python
trip_distances = load_trip_distance()
```

**Task 3a**: 
 > Determine how many rides are in the dataset, and assign that integer to the `number_of_rides` variable.


```python
# Replace None with the appropriate code
number_of_rides = None

### BEGIN SOLUTION

number_of_rides = len(trip_distances)

### END SOLUTION
```


```python
assert type(number_of_rides) == int

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

### BEGIN HIDDEN TESTS

assert number_of_rides == 943

### END HIDDEN TESTS
```

Although you cannot tell from the list by itself, the rides are ordered by start_community_area_number.  
The first 7 rides correspond to rides that started in community area 15.  

**Task 3b:**
  > Create a new variable, `trips_start_15` which contains a slice of the list corresponding to the first 7 rides.  


```python
# Replace None with the appropriate code

trips_start_15 = None

### BEGIN SOLUTION


from test_scripts.test_class import Test
test = Test()

trips_start_15 = trip_distances[:7]

test.save(trips_start_15, 'trips_start_15')



### END SOLUTION
```


```python
assert type(trips_start_15) == list

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

### BEGIN HIDDEN TESTS

test = Test()

test.run_test(trips_start_15, 'trips_start_15')


### END HIDDEN TESTS
```

**Task 3c:**

  > Add a new element - `the integer 1500` - to the end of the trip_distances list.


```python
# Your code here

### BEGIN SOLUTION

trip_distances.append(1500)

### END SOLUTION
```


```python
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

### BEGIN HIDDEN TESTS

assert trip_distances[-1] == 1500

### END HIDDEN TESTS
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

### BEGIN SOLUTION

trip_1['trip_distance'] = 3793

### END SOLUTION
```


```python
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

### BEGIN HIDDEN TESTS

assert trip_1['trip_distance'] == 3793


### END HIDDEN TESTS
```

**Task 4b**:
  > create a new key value pair within `trip_1` representing the name of the start area community name: `Portage Park` .  Use `start_area_community_name` as the key.


```python
# Your code here

### BEGIN SOLUTION

trip_1['start_area_community_name'] = 'Portage Park'

### END SOLUTION
```


```python
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

### BEGIN HIDDEN TESTS

assert trip_1['start_area_community_name'] == 'Portage Park'

### END HIDDEN TESTS
```

# Task 5: For-Loops and if/else statements

Let's return to the trip_distances list, reloaded below for your convenience:


```python
trip_distances = load_trip_distance()

```

**Task 5a:**
 > Using a **for-loop** and **if/else** statements, create a new list called `short_rides` which holds all rides less than or equal to 700 meters.   



```python
# Replace None with the appropriate code, as well as add the for look code below.
short_rides = None

### BEGIN SOLUTION

test = Test()

short_rides = []

for trip in trip_distances:
    
    if trip  <= 700:
        short_rides.append(trip)
        
test.save(short_rides, 'short_rides_list')



### END SOLUTION
```


```python
assert type(short_rides) == list
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

### BEGIN HIDDEN TESTS

test = Test()

test.run_test(short_rides, 'short_rides_list')


### END HIDDEN TESTS
```

**Task 5b**:
    
  > Add another conditional statement to the for loop above to create two lists simultaneously: `short_rides` and `long_rides`.   
  >> `short_rides` should consist of rides less than or equal to 700 meters.  
  >> `long_rides` should consist of rides greater than or equal to 5,000 meters.
    


```python
# Replace None with the appropriate code, as well as add the for look code below.
short_rides = None
long_rides  = None

### BEGIN SOLUTION


from test_scripts.test_class import Test
test = Test()


short_rides = []
long_rides = []

for trip in trip_distances:
    
    if trip  <= 700:
        short_rides.append(trip)
    
    elif trip >= 5000:
        long_rides.append(trip)

test.save(long_rides, 'long_rides_list')



### END SOLUTION
```


```python
assert type(short_rides) == list
assert type(long_rides) == list

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

### BEGIN HIDDEN TESTS

test = Test()

test.run_test(short_rides, 'short_rides_list')
test.run_test(long_rides, 'long_rides_list')


### END HIDDEN TESTS
```

## Task 6: Functions

> Create a simple function named `longest_ride` which takes the a list of integers as a **parameter** and **returns** the largest integer.

> Passing `trip_distances` as an argument to the function should result in the function returning the distance of the longest ride in meters.


```python
# Fill in the missing parts of the function below
def longest_ride():
    '''A function that takes a list of trip distances and 
    returns the distance of the longest trip in the original units: meters'''
    
    
### BEGIN SOLUTION
def longest_ride(trip_distance_list):
    '''A function that takes a list of trip distances and 
    returns the distance of the longest trip in the original units: meters'''
    
    return max(trip_distances)
        
### END SOLUTION
```


```python
assert type(longest_ride(trip_distances)) == int

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

### BEGIN HIDDEN TESTS

assert longest_ride(trip_distances) == 15658


### END HIDDEN TESTS
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


### BEGIN SOLUTION

test = Test()

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
    
    for ride in trips_list:
        if ride['start_community_area_number'] == start_area:
            community_area_rides.append(ride)
    
    return community_area_rides

test.save(get_start_area_rides('15', trips_list), 'start_comm_area_15_rides')


### END SOLUTION
```


```python
assert type(get_start_area_rides('15', trips_list)) == list

# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

### BEGIN HIDDEN TESTS

test = Test()

test.run_test(get_start_area_rides('15', trips_list), 'start_comm_area_15_rides')


### END HIDDEN TESTS
```
