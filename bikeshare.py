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
    while True:
        city = input('For what city do you want do select data, New York City, Chicago or Washington? \n')
        if city.lower() in CITY_DATA :
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month_lst = ['all','january', 'february', 'march', 'april', 'may', 'june']

    while True:
        month = input('Specify the month of data to explore. All, January ' +
                      'February, March, April, May, or June? \n')
        if month.lower() in month_lst:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_lst = ['All','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
    while True:
        day = input('Specify the day of data to explore. ' +
                    'All, Monday, Tuesday, Wednesday, Thursday, Friday, ' +
                    'Saturday, Sunday? \n')
        if day.title() in day_lst:
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
    df = pd.read_csv(CITY_DATA[city.lower()])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month ,day and hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('For the selected filter, the month with the most travels is: {}'.format(most_common_month))
    # TO DO: display the most common day of week
    most_common_dow = df['day_of_week'].mode()[0]
    print('For the selected filter, the most common day of the week is: {}'.format(most_common_dow))
    # TO DO: display the most common start hour
    most_common_sh = df['hour'].mode()[0]
    print('For the selected filter, the most common start hour is: {}'.format(most_common_sh))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('For the selected filters, the most common start station is:{}'.format(most_common_start))


    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('For the selected filters, the most common end station is:{}'.format(most_common_end))


    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' - ' + df['End Station']
    combination = df['combination'].mode()[0]
    print('For the selected filters, the most common start-end combination :{}'.format(combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = datetime.timedelta(seconds=int(df['Trip Duration'].sum()))
    print('\nTotal Travel Time: ', total_travel_time)

    # TO DO: display mean travel time
    total_travel_time_mean = datetime.timedelta(seconds=int(df['Trip Duration'].mean()))
    print('\nMean Travel Time: ', total_travel_time_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    counts_of_user_types = df['User Type'].value_counts()
    print(counts_of_user_types)


    # TO DO: Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print(counts_of_gender)
    except:
        print('Data does not include genders')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('For the selected filter, the earliest ', earliest)
        print('For the selected filter, the most recent', most_recent)
        print('For the selected filter, the most common birth year amongst', most_common_year_of_birth)
    except:
        print('Data does not include date of birth')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_input(df):
    print(df.head())
    while True:
        answer = input('View 5 more data entries? Yes or No? \n')
        if answer.lower() == 'yes':
            print(df.head())
        if answer.lower() == 'no':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_input(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
