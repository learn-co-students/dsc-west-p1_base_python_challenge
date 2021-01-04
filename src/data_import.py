import json 
import sys

sys.path.append('./sublessons/')
sys.path.append('..')

import os  
  
cur_dir = os.getcwd()  
root = cur_dir.split('project_directory')[0]  


def load_scooter():
    try: 
        with open(root+'/data/scooter_data.json', 'rb') as read_file:
            original_data = json.load(read_file)
    except FileNotFoundError:
        
        with open('../data/scooter_data.json', 'rb') as read_file:
            original_data = json.load(read_file)

    new_data = []
    for ride in original_data:
        try:
            ride['start_community_area_name']
            new_data.append(ride)

        except KeyError:
            pass

    data = sorted(new_data,  key = lambda x: x['start_community_area_number'])
    short_data = []

    for ride in data:
        id_ = ride['trip_id']
        dist = ride['trip_distance']
        duration = ride['trip_duration']
        start_area = ride['start_community_area_number']
        end_area = ride['end_community_area_number']

        short_data.append({'trip_id': id_, 'trip_distance' :dist, 'trip_duration':duration, 'start_community_area_number': start_area, 'end_community_area_number':end_area})

    data = short_data
    
    return data

def load_start_end_numbers():
    
    '''
    Defining strings from community area numbers for string practice.
    '''
    
    data = load_scooter()
    
    trip1_scan = data[0]['start_community_area_number']
    trip1_ecan = data[0]['end_community_area_number']
    
    return trip1_scan, trip1_ecan

def load_start_time_and_distance():
    
    '''
    Defining strings from community area numbers for string practice.
    '''
    
    data = load_scooter()
    
    trip1_dist = data[0]['trip_distance']
    trip1_time = data[0]['trip_duration']
    
    return trip1_dist, trip1_time

def load_trip_distance():
    
    data = load_scooter()
    
    trip_distance = [int(ride['trip_distance']) for ride in data]
    
    return trip_distance

def load_start_community_area():
    
    data = load_scooter()
    
    start_community_area = [ride['start_community_area_number'] for ride in data]
    
    return start_community_area

def load_trip_dictionary():
    
    data = load_scooter()
    
    trips_dictionary = {}
    
    for trip in data:
        trips_dictionary[trip['trip_id']] = {'trip_distance':trip['trip_distance'], 
                                         'trip_duration': trip['trip_duration'], 
                                         'start_community_area_number':trip['start_community_area_number'], 
                                         'end_community_area_number': trip['end_community_area_number']}
    
    return trips_dictionary