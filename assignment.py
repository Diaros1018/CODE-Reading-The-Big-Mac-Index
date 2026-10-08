
import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'


def get_big_mac_price_by_year(year, country_code):
    df = pd.read_csv(big_mac_file)

    df = df[df['date'].str[:4] == str(year)]
    df = df[df['iso_a3'] == country_code.upper()]

    price = df['dollar_price'].mean()

    return round(float(price), 2)


def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)

    df = df[df['iso_a3'] == country_code.upper()]

    price = df['dollar_price'].mean()

    return round(float(price), 2)


def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)

    df = df[df['date'].str[:4] == str(year)]

    cheapest = df.loc[df['dollar_price'].idxmin()]

    name = cheapest['name']
    code = cheapest['iso_a3']
    price = round(cheapest['dollar_price'], 2)

    return f"{name}({code}): ${price}"


def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)

    df = df[df['date'].str[:4] == str(year)]

    expensive = df.loc[df['dollar_price'].idxmax()]

    name = expensive['name']
    code = expensive['iso_a3']
    price = round(expensive['dollar_price'], 2)

    return f"{name}({code}): ${price}"


if __name__ == "__main__":

    print(get_big_mac_price_by_year(2008, "mys"))

    print(get_big_mac_price_by_country("usa"))

    print(get_the_cheapest_big_mac_price_by_year(2008))

    print(get_the_most_expensive_big_mac_price_by_year(2003))


 
