#!/usr/bin/env python3
import pandas as pd

def format_date(date: str):
    """ Return given date in format yyyymm

    Args:
        date(str): date in the format dd/mm/yyyy.
    Returns:
        string with date in the format yyyymm.
    """

    day, month, year = date.split('/')
    return ''.join([year, month.zfill(2)])

def value_sold_by_contact():
    """ Generates DataFrame containing data for barchart of
    total price sold / contacts.

    Returns:
        pd.DataFrame containing ['contact_id', 'total_price']
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

def value_sold_by_month():
    """ Generates DataFrame containing data for barchart of
    total price sold / months.

    Returns:
        pd.DataFrame containing ['month', 'total_price']
    """

    deals = pd.read_csv('in/deals.tsv', sep='\t', usecols=[1, 2])
    deals.columns = ['date', 'total_price']

    deals['date'] = deals['date'].apply(format_date)

    chart_base = (deals.groupby(['date'])
                  .agg({'total_price': sum})
                  .reset_index())

    return chart_base


print(value_sold_by_month().head())
