import time
import datetime
import pandas as pd
import statistics as st

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s see some of our bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('\nWould you like to see data for Chicago, Washington, or New York ?\n').lower()
    #lower is used to get input in any format

    while(True):
        if(city == 'chicago' or city == 'washington' or city == 'new york'):
            break
        else:
            city = input('Oops! Enter Correct city: ').lower()
             #lower is used to get input in any format
    # get user input for month (all, january, february, ... , june)
    month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()
     #lower is used to get input in any format

    while(True):
        if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' ):
            break
        else:
            month = input('Oops! Enter correct month\n').lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day =  input('Which day ? monday, tuesday, wednesday, thursday, friday, saturday , sunday or all to display data of all days?\n').lower()
     #lower is used to get input in any format
    while(True):
        
        if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all'):
            break
        else:
            day = input('Oops! Enter Correct day: ').lower()
             #lower is used to get input in any format

    #return day

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
 
    df = pd.read_csv(CITY_DATA[city])

 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # to_datetime is used to convert date into date format
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        #used to find index of month.
        month = months.index(month) + 1       

        df = df[df['Start Time'].dt.month == month]
        
    #filter data by day.
    if day != 'all': 
        df = df[df['Start Time'].dt.weekday_name == day.title()]
     #print 5 rows.
    print(df.head())
    return df


def time_stats(df, month, day):
    

    print('\n Most Frequent Times of Travel is........\n')
    start_time = time.time()

    # display the most common month
    if(month == 'all'):
        most_common_month = df['Start Time'].dt.month.value_counts().idxmax()
        print('Most common month is ' + str(most_common_month))

    # display the most common day of week
    if(day == 'all'):
        most_common_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
        print('Most common day is ' + str(most_common_day))

    # display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most popular hour is ' + str(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
   

    print('\n Most Popular Stations and Trip is ...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = st.mode(df['Start Station'])
    print('\nThe Most common start station is {}\n'.format(most_common_start_station))

    # display most commonly used end station
    most_common_end_station = st.mode(df['End Station'])
    print('\nThe Most common end station is {}\n'.format(most_common_end_station))

    # display most frequent combination of start station and end station trip
    combination_trip = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    most_frequent_trip = combination_trip.value_counts().idxmax()
    print('\nThe Most popular trip is from {}\n'.format(most_frequent_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
   
    print('\nTrip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    time1 = total_travel_time
    day = time1 // (24 * 3600)
    time1 = time1 % (24 * 3600)
    hour = time1 // 3600
    time1 %= 3600
    minutes = time1 // 60
    time1 %= 60
    seconds = time1
    print('\nThe Total travels time is {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    time2 = mean_travel_time
    day2 = time2 // (24 * 3600)
    time2 = time2 % (24 * 3600)
    hour2 = time2 // 3600
    time2 %= 3600
    minutes2 = time2 // 60
    time2 %= 60
    seconds2 = time2
    print('\nThe Mean travel time is {} hours {} minutes {} seconds'.format(hour2, minutes2, seconds2))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    print('\nThe User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    no_of_subscribers = df['User Type'].str.count('Subscriber').sum()
    no_of_customers = df['User Type'].str.count('Customer').sum()
    print('\nThe Counting of subscribers are {}\n'.format(int(no_of_subscribers)))
    print('\nThe Counting of customers are {}\n'.format(int(no_of_customers)))

    # Display counts of gender
    if('Gender' in df):
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('\nThe Counting of male users are {}\n'.format(int(male_count)))
        print('\nThe Counting of female users are {}\n'.format(int(female_count)))


    # Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()
        #most_common_birth_year = st.mode(df['Birth Year'])
        try:
            print('\nThe Oldest birth year is {}\nAnd Youngest birth year is {}\n The Most popular birth year is {}\n'.format(int(earliest_year), int(recent_year), int(most_common_birth_year)))
        except TypeError:
    
            print('\nThe Oldest birth year is {}\nAnd Youngest birth year is {}\n The Most popular birth year is {}\n'.format(int(earliest_year), int(recent_year), most_common_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def raw(df):
    start=0
    end=5
    show=input("\n would you want to see the raw data? Enter yes or no\n").lower()
    if show=='yes':
        while end<= df.shape[0]-1:
            print(df.iloc[start:end, :])
            start+=5
            end+=5
            end_show= input("\nwould you want continue?Enter yes or no\n").lower()
            if end_show == 'no':
                break
            
 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw(df)
        

        restart = input('\nWould you like to restart the explore ? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":

	main()