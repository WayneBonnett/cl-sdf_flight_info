import pandas as pd


arrivals = pd.read_csv('./combined_data/arrivals.csv', index_col=1)
departures = pd.read_csv('./combined_data/departures.csv', index_col=1)
airlines = pd.read_csv('passenger_airlines.csv', index_col=0)

print(arrivals.head(10))
print(arrivals.info())

print(arrivals.shape)
arrivals_tmp = arrivals.drop_duplicates()
print(arrivals_tmp.shape)
arrivals_tmp.rename(columns={
    'ID' : 'id', 
    'Date (MM/DD/YYYY)' : 'flight_date', 
    'Flight Number' : 'flight_number', 
    'Tail Number' : 'tail_number',
    'Origin Airport' : 'origin', 
    'Scheduled Arrival Time' : 'sched_arr_time', 
    'Actual Arrival Time' : 'act_arr_time',     
    'Scheduled Elapsed Time (Minutes)' : 'sch_elapsed', 
    'Actual Elapsed Time (Minutes)' : 'act_elapsed',   
    'Arrival Delay (Minutes)' : 'arr_delay', 
    'Wheels-on Time' : 'wheels_on', 
    'Taxi-In time (Minutes)' : 'taxi_in', 
    'Delay Carrier (Minutes)' : 'delay_carrier', 
    'Delay Weather (Minutes)' : 'delay_weather',
    'Delay National Aviation System (Minutes)'  : 'delay_natavsys',
    'Delay Security (Minutes)' : 'delay_security',
    'Delay Late Aircraft Arrival (Minutes)' : 'delay_late_arrival'
   
},inplace=True)

print(arrivals_tmp.columns)



print(departures.shape)
departures_tmp = departures.drop_duplicates()
print(departures_tmp.shape)

departures_tmp.rename(columns={
    'ID' : 'id', 
    'Date (MM/DD/YYYY)' : 'flight_date', 
    'Flight Number' : 'flight_number', 
    'Tail Number' : 'tail_number',
    'Destination Airport' : 'dest', 
    'Scheduled departure time' : 'sched_dep_time', 
    'Actual departure time' : 'act_dep_time',     
    'Scheduled elapsed time (Minutes)' : 'sch_elapsed', 
    'Actual elapsed time (Minutes)' : 'act_elapsed',   
    'Departure delay (Minutes)' : 'dep_delay', 
    'Wheels-off Time' : 'wheels_off', 
    'Taxi-Out time (Minutes)' : 'taxi_out', 
    'Delay Carrier (Minutes)' : 'delay_carrier', 
    'Delay Weather (Minutes)' : 'delay_weather',
    'Delay National Aviation System (Minutes)'  : 'delay_natavsys',
    'Delay Security (Minutes)' : 'delay_security',
    'Delay Late Aircraft Arrival (Minutes)' : 'delay_late_arrival'
   
},inplace=True)

print(departures_tmp.columns)
