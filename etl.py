#!/usr/bin/env python3
import os

import pandas as pd


def format_date(date: str):
    """ Return given date in format yyyymm.

    Args:
        date(str): date in the format mm/dd/yyyy.
    Returns:
        string with date in the format yyyymm.
    """

    month, day, year = date.split('/')
    return ''.join([year, month.zfill(2)])

def value_sold_by_contact():
    """ Generates DataFrame containing data for barchart of
    total price sold / contacts.

    Returns:
        pd.DataFrame containing ['contact_id', 'total_price'].
    """

    # get contact_id and price
    deals = pd.read_csv('in/deals.tsv', sep='\t', usecols=[2, 3])
    deals.columns = ['total_price', 'contact_id']

    chart_base = (deals.groupby(['contact_id'])
                  .agg({'total_price': sum})
                  .reset_index())

    # get contact_name
    contacts = pd.read_csv('in/contacts.tsv', sep='\t', usecols=[0, 1])
    contacts.columns = ['contact_id', 'contact_name']
    chart_base = chart_base.merge(contacts, how='left')

    return chart_base.filter(items=['contact_id', 'contact_name',
                                    'total_price'])

def value_sold_by_month(year: str = None):
    """ Generates DataFrame containing data for barchart of
    total price sold / months.

    Args:
        year(str): yyyy, restricts months to a specific year.
    Returns:
        pd.DataFrame containing ['month', 'total_price'].
    """

    deals = pd.read_csv('in/deals.tsv', sep='\t', usecols=[1, 2])
    deals.columns = ['date', 'total_price']

    deals['date'] = deals['date'].apply(format_date)
    if year is not None:
        deals = deals[deals['date'].str[:4] == year]

    chart_base = (deals.groupby(['date'])
                  .agg({'total_price': sum})
                  .reset_index())

    return chart_base

def rank_sectors(month: str = None):
    """ Generates list of ranked company sectors.
    Ranked by percentage of total value sold in a month.

    Args:
        month(str): yyyymm.
    Returns:
        Ranking list for corresponding month.
    """

    deals = pd.read_csv('in/deals.tsv', sep='\t', usecols=[1, 2, 4])
    deals.columns = ['date_created', 'total_price', 'company_id']

    deals['date_created'] = deals['date_created'].apply(format_date)
    if month is not None:
        deals = deals[deals['date_created'] == month]

    deals = (deals.groupby(['company_id'])
             .agg({'total_price': sum})
             .reset_index())

    # get sector keys
    sector_keys = pd.read_csv('in/companies.tsv', sep='\t', usecols=[0, 9])
    sector_keys.columns = ['company_id', 'sector_key']
    deals = deals.merge(sector_keys, how='left')

    # get sector names
    sector_names = pd.read_csv('in/sectors.tsv', sep='\t')
    sector_names.columns = ['sector_key', 'sector_name']
    deals = deals.merge(sector_names, how='left')

    ranked_sectors = (deals.groupby(['sector_key'])
                      .agg({'total_price': sum,
                            'sector_name': 'first'})
                      .reset_index())

    ranked_sectors['percentage_sold'] = (ranked_sectors['total_price']
                                         / (ranked_sectors['total_price']
                                            .sum()))

    ranked_sectors = ranked_sectors.filter(items=['sector_name',
                                                  'percentage_sold'])

    return ranked_sectors.sort_values(['percentage_sold'],
                                      ascending=False)

def write_output():
    sold_by_contact = value_sold_by_contact()
    sold_by_month = value_sold_by_month('2019')
    ranked_sectors = rank_sectors()

    if 'out' not in os.listdir():
        os.mkdir('out')

    sold_by_contact.to_csv('out/sold_by_contact.csv', index=False, sep='|')
    sold_by_month.to_csv('out/sold_by_month.csv', index=False, sep='|')
    ranked_sectors.to_csv('out/ranked_sectors.csv', index=False, sep='|')

if __name__ == '__main__':
    write_output()

################################################################################


# pd.options.display.width = None

# def print_to_html(df):
#     with open('html/df.html', 'w') as f:
#         f.write(df.to_html())
#         return True
#     return False

# print_to_html(rank_sectors())
