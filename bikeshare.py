import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS_OF_WEEK = [
    'monday', 'tuesday', 'wednesday', 'thursady', 'friday', 'saturday',
    'sunday'
]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    city = None
    while city not in CITY_DATA.keys():
        city = input(
            "What city? Please enter 'chicago', 'washington', or 'new york city': \n"
        ).lower()

    month = None
    while month not in MONTHS and month != 'all':
        month = input(
            "What month would you like to use to filter? Please enter 'all' for no filter, or 'january', 'february', 'march', 'april', 'may', 'june': \n"
        ).lower()

    day = None
    while day not in DAYS_OF_WEEK and day != 'all':
        day = input(
            "What day would you like to use to filter? Please enter 'all' for no filter, or type the name of the day: \n"
        ).lower()

    print('-' * 40)
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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    month_index = df['month'].mode()[0]
    common_month = MONTHS[month_index - 1].title()
    common_day = df['day_of_week'].mode()[0]
    common_start_hour = df['Start Time'].dt.hour.mode()[0]

    print(f"Most common month: {common_month}\n")
    print(f"Most common day: {common_day}\n")
    print(f"Most common start hour: {common_start_hour}\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]
    common_end_station = df['End Station'].mode()[0]
    common_start_and_end_station = (df['Start Station'] + " and " +
                                    df['End Station']).mode()[0]

    print(f"Most common start station: {common_start_station}\n")
    print(f"Most common end station: {common_end_station}\n")
    print(
        f"Most common start and end station: {common_start_and_end_station}\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    mean_trip_duration = df['Trip Duration'].mean()

    print(f"Total travel time: {total_travel_time}\n")
    print(f"Mean trip duration: {mean_trip_duration}\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    if city == 'washington':
        return

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("User Types:\n")
    print(df['User Type'].value_counts())
    print("\n")

    print("Gender:\n")
    print(df['Gender'].value_counts())
    print("\n")

    min_birth_year = df['Birth Year'].min()
    max_birth_year = df['Birth Year'].max()
    common_birth_year = df['Birth Year'].mode()[0]

    print(f"Earliest birth year: {min_birth_year}\n")
    print(f"Most recent birth year: {max_birth_year}\n")
    print(f"Most common birth year: {common_birth_year}\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def show_rows(df):
    show_rows = input("Would you like to see the first 5 rows, yes or no? \n")
    if show_rows == 'yes':
        print(df.head())


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
