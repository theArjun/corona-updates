'''Retrie CoViD-19 updates by scraping and dividing into world, countries and continents.'''
__version__ = '0.1.0'

import argparse
import datetime
import os
from sys import argv

import requests
import pandas as pd
from tabulate import tabulate
from bs4 import BeautifulSoup


class Covid19:
    '''Gets Covid19 data and divides geographically.'''

    def __init__(self):
        '''Scrape the website text from Worldometer.'''

        self.response = requests.get(
            'https://www.worldometers.info/coronavirus/?').text

        # Commands available.
        self.choices = [
            'confirmed',
            'recovered',
            'dead',
            'critical',
            'newcases',
            'active',
            'newdeaths'
        ]

        # Mapping commands to columns of dataframes.
        self.mappings = {
            'confirmed': 'total_cases',
            'recovered': 'total_recovered',
            'dead': 'total_deaths',
            'critical': 'critical_cases',
            'newcases': 'new_cases',
            'active': 'active_cases',
            'newdeaths': 'new_deaths',
        }

    def get_cleaned_data(self):
        '''Get the cleaned table data from Worldometer by removing HTML tags.'''
        soup = BeautifulSoup(self.response, 'lxml')
        table_content = soup.find(
            'table',
            {
                'id': 'main_table_countries_today'
            }
        )

        data = []
        for row_data in table_content.findAll('tr'):

            cleaned_row_data = []

            for cell_data in row_data.text.split('\n'):
                cleaned_row_data.append(cell_data)

            data.append(cleaned_row_data)

        return data

    def get_country_dataframe(self):
        '''Get the country wise dataframe related to CoViD-19 with various categories available.'''

        cleaned_data = self.get_cleaned_data()

        # We found that country wise data starts from 9th i.e [8:-8] row of table.
        countries_data = cleaned_data[8:-8]

        # Available columns of data.
        country_columns = [
            'blank',
            'country',
            'total_cases',
            'new_cases',
            'total_deaths',
            'new_deaths',
            'total_recovered',
            'active_cases',
            'critical_cases',
            'cases_per_million',
            'deaths_per_million',
            'total_test',
            'tests_per_million',
            'continent',
            'after_blank'
        ]

        # Creating the list for storing column wise data which will be
        # helpful for creating the Dataframe object.
        country_data_lists = {
            'first_blank': [],
            'country_name': [],
            'total_cases': [],
            'new_cases': [],
            'total_deaths': [],
            'new_deaths': [],
            'total_recovered': [],
            'active_cases': [],
            'critical_cases': [],
            'cases_per_million': [],
            'deaths_per_million': [],
            'total_test': [],
            'tests_per_million': [],
            'continent': [],
            'final_blank': [],
        }

        # Adding each columns data to the list for creating Dataframe object.
        for country_data in countries_data:
            country_data_lists['first_blank'].append(country_data[0])
            country_data_lists['country_name'].append(country_data[1])
            country_data_lists['total_cases'].append(country_data[2])
            country_data_lists['new_cases'].append(country_data[3])
            country_data_lists['total_deaths'].append(country_data[4])
            country_data_lists['new_deaths'].append(country_data[5])
            country_data_lists['total_recovered'].append(country_data[6])
            country_data_lists['active_cases'].append(country_data[7])
            country_data_lists['critical_cases'].append(country_data[8])
            country_data_lists['cases_per_million'].append(country_data[9])
            country_data_lists['deaths_per_million'].append(country_data[10])
            country_data_lists['total_test'].append(country_data[11])
            country_data_lists['tests_per_million'].append(country_data[12])
            country_data_lists['continent'].append(country_data[12])
            country_data_lists['final_blank'].append(country_data[14])

        # Creating dictionary like : {column_name: list_of_column_data}
        country_data = {
            country_columns[1]: country_data_lists['country_name'],
            country_columns[2]: country_data_lists['total_cases'],
            country_columns[3]: country_data_lists['new_cases'],
            country_columns[4]: country_data_lists['total_deaths'],
            country_columns[5]: country_data_lists['new_deaths'],
            country_columns[6]: country_data_lists['total_recovered'],
            country_columns[7]: country_data_lists['active_cases'],
            country_columns[8]: country_data_lists['critical_cases'],
            country_columns[9]: country_data_lists['cases_per_million'],
            country_columns[10]: country_data_lists['deaths_per_million'],
            country_columns[11]: country_data_lists['total_test'],
            country_columns[12]: country_data_lists['tests_per_million'],
            country_columns[13]: country_data_lists['continent'],
        }

        # Creating Dataframe object and slicing blank columns.
        country_df = pd.DataFrame(country_data, columns=country_columns[1:-2])
        return country_df

    def get_continent_dataframe(self):
        '''Get continent wise dataframe related to CoViD-19 with various categories available.'''

        # Rest documentation are same as get_country_dataframe().
        cleaned_data = self.get_cleaned_data()
        continent_dataset = cleaned_data[1:7]

        continent_columns = [
            'continent_name',
            'continent_new_cases',
            'continent_total_cases',
            'continent_total_deaths',
            'continent_new_deaths',
            'continent_total_recovered',
            'continent_active_cases',
            'continent_critical_cases',
            'continent_cases_per_million',
            'continent_deaths_per_million',
            'continent_total_test',
            'continent_tests_per_million',
        ]

        continent_data_lists = {

            'continent_name': [],
            'continent_new_cases': [],
            'continent_total_cases': [],
            'continent_total_deaths': [],
            'continent_new_deaths': [],
            'continent_total_recovered': [],
            'continent_active_cases': [],
            'continent_critical_cases': [],
            'continent_cases_per_million': [],
            'continent_deaths_per_million': [],
            'continent_total_test': [],
            'continent_tests_per_million': [],
        }

        for continent_data in continent_dataset:
            continent_data_lists['continent_name'].append(continent_data[2])
            continent_data_lists['continent_new_cases'].append(
                continent_data[4])
            continent_data_lists['continent_total_cases'].append(
                continent_data[5])
            continent_data_lists['continent_total_deaths'].append(
                continent_data[6])
            continent_data_lists['continent_new_deaths'].append(
                continent_data[7])
            continent_data_lists['continent_total_recovered'].append(
                continent_data[8])
            continent_data_lists['continent_active_cases'].append(
                continent_data[9])
            continent_data_lists['continent_critical_cases'].append(
                continent_data[10])
            continent_data_lists['continent_cases_per_million'].append(
                continent_data[11])
            continent_data_lists['continent_deaths_per_million'].append(
                continent_data[12])
            continent_data_lists['continent_total_test'].append(
                continent_data[13])
            continent_data_lists['continent_tests_per_million'].append(
                continent_data[14])

        continent_data = {
            continent_columns[0]: continent_data_lists['continent_name'],
            continent_columns[1]: continent_data_lists['continent_new_cases'],
            continent_columns[2]: continent_data_lists['continent_total_cases'],
            continent_columns[3]: continent_data_lists['continent_total_deaths'],
            continent_columns[4]: continent_data_lists['continent_new_deaths'],
            continent_columns[5]: continent_data_lists['continent_total_recovered'],
            continent_columns[6]: continent_data_lists['continent_active_cases'],
            continent_columns[7]: continent_data_lists['continent_critical_cases'],
            continent_columns[8]: continent_data_lists['continent_cases_per_million'],
            continent_columns[9]: continent_data_lists['continent_deaths_per_million'],
            continent_columns[10]: continent_data_lists['continent_total_test'],
            continent_columns[11]: continent_data_lists['continent_tests_per_million'],
        }

        continent_df = pd.DataFrame(continent_data, columns=continent_columns)

        return continent_df

    def get_world_dataframe(self):
        '''Get the accumulated world data related to CoViD-19 with various categories available.'''

        # We found that the accumulated world data gets sits on the top of list of counties.
        # Thus we retrieved that index and returned it.
        country_dataframe = self.get_country_dataframe()
        world_dataframe = country_dataframe.iloc[0]  # Topmost row.
        return world_dataframe

    def create_csv(self, geography_type=None, filepath=None):
        '''Create CSV file containing CoViD-19 updates.'''

        if geography_type.lower() == 'country':
            dataframe = self.get_country_dataframe()
            geography_type = 'Country'
        elif geography_type.lower() == 'country':
            dataframe = self.get_continent_dataframe()
            geography_type = 'Continent'
        else:
            print('Invalid Geography type.')
            return None

        os.chdir(filepath)
        directory = os.getcwd()
        filepath = f'/{filepath}/'

        timestamp = datetime.datetime.now()
        filename = '{}COVID_19_{}_{}_{}_{}__{}_{}__{}.csv'.format(
            filepath,
            geography_type.upper(),
            timestamp.year,
            timestamp.month,
            timestamp.day,
            timestamp.hour,
            timestamp.minute,
            timestamp.strftime("%A")
        )
        dataframe.to_csv(filename, sep=',')

        print(f'\nCSV file saved at : {directory}')

    def parse_args_from_user(self):
        '''Retrieves arguments from user and processes accordingly.'''

        parser = argparse.ArgumentParser(
            description='Command Line Interface for Corona Virus (CoViD-19) Informations.',
        )

        parser.add_argument('--show',
                            '-s',
                            help='Shows the info by category',
                            choices=self.choices,  # Allowed choices.
                            metavar='category'  # Alias
                            )

        parser.add_argument('--country',
                            '-c',
                            help='Shows the info by country.',
                            metavar='country'
                            )

        parser.add_argument('--downloadcsv',
                            '-d',
                            help='Downloads CSV file containing CoViD-19 updates of real time.',
                            metavar='filepath'
                            )

        args = parser.parse_args()

        if len(argv) < 2:
            parser.parse_args(['-h'])

        if args.show and args.country:

            country_df = self.get_country_dataframe()
            country_df['country'] = country_df['country'].str.upper()
            country_query = args.country.upper()
            country_result = country_df.loc[country_df['country']
                                            == country_query]
            categorical_country_result = country_result[self.mappings[args.show]]
            result = list(categorical_country_result)[0]
            if len(result) < 0 or result == ' ':
                result = 0
            label = self.mappings[args.show].replace('_', ' ').title()
            print(f'\n{label} : {result} in {country_query}\n')

        elif not args.country and args.show:

            world_df = self.get_world_dataframe()
            label = self.mappings[args.show].replace('_', ' ').title()
            result = world_df[self.mappings[args.show]]
            print(f'\n{label} : {result} WORLDWIDE\n')

        elif not args.show and args.country:

            country_df = self.get_country_dataframe()
            country_df['country'] = country_df['country'].str.upper()
            country_query = args.country.upper()
            country_result = country_df.loc[country_df['country']
                                            == country_query]
            country_result = country_result.T
            country_result = country_result[country_result[country_result.columns[0]].map(
                len) != 0]
            print(tabulate(country_result, headers='', tablefmt='psql'))

        if args.downloadcsv:
            self.create_csv(filepath=args.downloadcsv,
                            geography_type='country')
