'''Conosle application Driver'''
from coronaupdates import Covid19

if __name__ == "__main__":
    cov = Covid19()
    cov.parse_args_from_user()
