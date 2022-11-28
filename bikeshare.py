import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('For which city would you like to explore the data?')
    city= input("please choose one of the following cities: Chicago, New York city, Washington: ").lower()
    
    while city not in ['chicago', 'new york city', 'washington']:
       city=input('It is not a valid city, please choose: Chicago, New York city or Washington:').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month= input("please choose one of the following months: January until June, you can choose all: ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june','all']:
       month=input('It is not a valid month, please choose: January until June, you can choose all: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day= input("please choose one of the following days of the week: Sunday until Saturday, you can choose all: ").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']:
        day=input('It is not a valid day, please choose: Sunday until Saturday, you can choose all: ').lower()

    print('-'*40)
    return city, month, day




def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    time=
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    df['hour'] = df['Start Time'].dt.hour

    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
  
    return df


                
                
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
   
    start_time = time.time()

    
    month={'january', 'february', 'march', 'april', 'may', 'june','all'}
    day={'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday', 'Sunday','All'}

    print('\nCalculating The Most Frequent Times of Travel...\n')
   

    # TO DO: display the most common month
    common_month=df["month"].mode()[0]
    print("Most common month: ", common_month)

    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print("Most common day: ", common_day)
    
 
  
      # TO DO: display the most common start hour
    start_hour=df["hour"].mode()[0] 
    print("Most common hour: ", start_hour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    start_station=df["Start Station"].count()
    end_station=df["End Station"].count()
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start=df['Start Station'].mode()[0]
    print("The most common start station is: {}".format(common_start))
        
        # TO DO: display most commonly used end station
    common_end=df['End Station'].mode()[0]
    print("The most common end station is: {}".format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    start_end_combo = df.groupby(['Start Station','End Station']).size().idxmax()    
    print("The most common start and end station combination is: {}".format(start_end_combo))

       
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_time = (df['Trip Duration'].sum()) 
    print('Total travel time: ',total_time)
         
    
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean travel time: ',mean_travel_time) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def user_stats(df, city): 
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
   
    subscriber=df['User Type'].value_counts()['Subscriber']
    customer=df['User Type'].value_counts()['Customer']
    print ("Number of Subscriber :" , subscriber)
    print ("Number of Customer :" , customer)
    # TO DO: Display counts of gender # not all cities have this value. to check null
    df.isnull().sum()
    if city == "washington" :
        print("Gender and Birth year are not available.")
    else:
        male=df['Gender'].value_counts()['Male']
        female=df['Gender'].value_counts()['Female']
        print ("Number of Male :" , male)
        print ("Number of Female :" , female)
        
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth=df["Birth Year"].min()
        print ("Earliest year of birth :  ", earliest_year_of_birth)
                
        recent_year_of_birth=df["Birth Year"].max()
        print ("Recent year of birth :  ", recent_year_of_birth)
                
        common_year_of_birth=df["Birth Year"].mode()[0]
        print ("Common year of birth :  ", common_year_of_birth)
                
               
        
def displayed_data(df):

    view_data=input("would you like to view 5 rows of individual trip data? Enter yes or no .")
    start_loc=0
    while True:
        print(df.iloc[start_loc:start_loc+5])  #to show every 5 rows
        start_loc+=5
        view_display=input("Do you wish to continue? ").lower()
        if view_display =="yes":
            continue
        else:
            break
            
           
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        
        df= load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        displayed_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
