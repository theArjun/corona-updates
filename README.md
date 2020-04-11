# Corona Updates
Command Line Interface for retrieving CoViD-19 related informations. 

![](header.png)

## Installation



```sh
pip install coronaupdates
```

## Usage examples 

`coronaupdates`can run in two ways:

1. In Your code
2. In Command Line Interface

### In Your Code
```python
from coronaupdates import Covid19

cov = Covid19()

# Run the Command Line Interface from your code
cov.parse_args_from_user()

# Create the CSV of corona updates of real time.
cov.create_csv(geography_type='country', filepath='/path/to/save/')
```
### In Command Line Interface

```sh
usage: coronaupdates [-h] [--show category] [--country country]
             [--downloadcsv filepath]

Command Line Interface for Corona Virus (CoViD-19) Informations.

optional arguments:
  -h, --help            show this help message and exit
  --show category, -s category
                        Shows the info by category
  --country country, -c country
                        Shows the info by country.
  --downloadcsv filepath, -d filepath
                        Downloads the CSV file containing CoViD-19 updates of
                        current time.
```

```sh
 └> $ coronaupdates -s confirmed

Total Cases : 1,700,378 WORLDWIDE
```
```sh
 └> $ coronaupdates -s confirmed -c usa

Total Cases : 502,876 in USA
```
```sh

 └> $ coronaupdates  -c usa
+--------------------+-----------+
| country            | USA       |
| total_cases        | 502,876   |
| total_deaths       | 18,747    |
| total_recovered    | 27,314    |
| active_cases       | 456,815   |
| critical_cases     | 10,917    |
| cases_per_million  | 1,519     |
| deaths_per_million | 57        |
| total_test         | 2,538,888 |
| tests_per_million  | 7,670     |
+--------------------+-----------+
```

## Meta


Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/thearjun/coronaupdates/blob/master/LICENSE.txt](https://github.com/thearjun/coronaupdates/blob/master/LICENSE.txt)

## Contributing

1. Fork it (<https://github.com/thearjun/coronavirus/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM5NTQxNjg4MiwxMzQ3MzE1MDg4XX0=
-->