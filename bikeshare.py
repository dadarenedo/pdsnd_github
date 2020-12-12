import time
import pandas as pd
import numpy as np

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
    
    while True:
      city = input("\nWhich city would you like to analyze? Choose between: New York City, Chicago or  Washington?\n")
      city = city.lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("Please choose between New York City, Chicago, or Washington. ")
        continue
      else:
        break


    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
      month = input("\nWhich month like to analyze? Choose between: All or a specific month between January and June\n")
      month =  month.lower()
      if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        print("Please check the month you write ")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nWhich day like to analyze? Choose between: All or Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday\n")
      day = day.lower()
      if day not in ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'Saturday'):
            print("Please check the day you write ")
            continue
      else:
            break
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df["Start Time"] = pd.to_datetime(df['Start Time'])
    #df["End Time"] = pd.to_datetime(df['End Time'])
    
    df["month"] = df["Start Time"].dt.strftime("%B").str.lower()
    df["day"] = df["Start Time"].dt.strftime("%A").str.lower()
    
    if month != "all":
        df = df[df.month==month]
    if day != "all":
        df =df[df.day==day]
      
    
    #print(df.head().month)
    #df["month"] = df["Start Time"]
    
    #print(df.head())
    
    #if month != "all":
    #    df = df[df.]
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    
    
    most_common_month = df['month'].mode()
    print('\nMost Common Month:', most_common_month, "\n")

    # TO DO: display the most common day of week
    
    most_common_day = df['day'].mode()
    print('\nMost Common Day of the Week:', most_common_day, "\n") 

    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    most_common_startHour = df['hour'].mode()[0]
    print('\nMost Common Start Hour:', most_common_startHour, "\n") 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    most_common_sStation = df['Start Station'].value_counts().idxmax()
    print('\nMost common Start Station:', most_common_sStation, "\n")


    # TO DO: display most commonly used end station
    
    most_common_eStation = df['End Station'].value_counts().idxmax()
    print('\nMost common End Station:', most_common_eStation, "\n")


    # TO DO: display most frequent combination of start station and end station trip
    
    start_end_combination = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('Most Commonly used combination of start station and end station trip:', start_end_combination, "\n") 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    Total_Travel_Time = sum(df['Trip Duration'])
    print('\nTotal travel time:', Total_Travel_Time/86400, "Days \n")

    # TO DO: display mean travel time
    
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('\nMean travel time:', Mean_Travel_Time/60, "Minutes\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)
  

    # TO DO: Display counts of gender
    
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")


    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data in  this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data in this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data in  this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    
    view_data = view_data.lower()
    while view_data == "yes":
      print(df.iloc[start_loc:start_loc+5])
      start_loc += 5
      view_data = input("Do you wish to continue?:").lower()
    
    
def main():
while True:
    city, month, day = get_filters()
    df = load_data(city, month, day)

    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    display_data(df)   """this fuction was missing """

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
        break


if __name__ == "__main__":
	main()
