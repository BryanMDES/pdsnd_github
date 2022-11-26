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
        city = input('Would you like to see data for Chicago, New York City, or Washington?').lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            print('\nYou chose: ',city)
            break
        else:
            print('\nINCORRECT!: Enter Chicago, New York, or Washington')
            continue


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter one of the months to filter by [January, February, March, April, May, June, July] or enter \'All\'').capitalize()
        if month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May' or month == 'June' or month == 'July' or month == 'All':
            print('\nyou chose: ',month)
            break
        else:
            print('\nINCORRECT!: Enter January, February, March, April, May, June, July or All')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter one of the days to filter by [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday] or enter \'All\'').capitalize()
        if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday' or day == 'Sunday' or day == 'All':
            print('\nyou chose: ', day)
            break
        else:
            print('\nINCORRECT!: Enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All')
            continue

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

    df['Start Time'] = pd.to_datetime(df['Start Time'], format = '%Y-%m-%d %H:%M:%S')


    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()
    df['Hour'] =df['Start Time'].dt.strftime("%I %p")

    if month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May' or month == 'June' or month == 'July':
        df['Month'] = month

    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday' or day == 'Sunday':
        df['Day'] = day



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nThe Most common month is: ',df['Month'].mode()[0])

    # TO DO: display the most common day of week
    print('\nThe Most common day of the week is: ',df['Day'].mode()[0])

    # TO DO: display the most common start hour
    print('\nThe Most common start hour: ',df['Hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe Most common start station: ',df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('\nThe Most common end station: ',df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End Station'] = df['Start Station'][0:] + ' - ' + df['End Station'][0:]

    print('\nThe Most common Start and End Station: ',df['Start and End Station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nThe total travel time: ',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('\nThe mean travel time: ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nThe count of user types: ',df['User Type'].value_counts())


    # TO DO: Display counts of gender
    try: #I want you to try this, but if something is wrong then do the except
        print('\nThe counts of gender are: ',df['Gender'].value_counts())

    except:#If the try does not work, try this instead
        print('\nWashington does not have gender data')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\nThe earliest birth year: ',df['Birth Year'].min())

        print('\nThe most recent birth year: ',df['Birth Year'].max())

        print('\nThe most common year of birth: ',df['Birth Year'].mode())
    except:
        print('\nWashington does not have birth year data')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Shows you the number of rows of your data frame"""

    i=0
    while True:
        rows = input('Do you want to see 5 rows of data? Enter Yes or No: ').lower()
        if rows == 'yes':
            print(df.iloc[(i+0):(i+6)])
            while True:
                more_rows = input('Do you want to see 5 more rows of data?').lower()
                if more_rows == 'yes':
                    i += 5
                    print(df.iloc[(i+0):(i+6)])
                    continue
                elif more_rows == 'no':
                    break
                else:
                    print('Incorrect!: Enter \'yes\' or \'no\'')
                    continue
            break
        elif rows == 'no':
            break
        else:
            print('Incorrect!: Enter \'yes\' or \'no\'')
            continue

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
