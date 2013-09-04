#!/usr/bin/python

from pprint import *
import matplotlib.pyplot as plt

"""
house_price         =       439000  # in $
rental_monthly      =       2340    # in $
down_payment        =       25      # in percentage
mortgate_rate       =       4.5     # in percentage
mortgate_year       =       30      # in years
month_per_year      =       12      # rentals collected in months
property_tax        =       1.07    # in percentage
insurance           =       800    # in $
"""

from user_data import *

params = {'house_price'      :        house_price,
          'rental_monthly'   :        rental_monthly,
          'down_payment'     :        down_payment,
          'mortgate_rate'    :        mortgate_rate,
          'mortgate_year'    :        mortgate_year,
          'property_tax'     :        property_tax,
          'insurance'        :        insurance,
}

p0 = params.copy()
p1 = params.copy()
p2 = params.copy()

def f(p, i):
    # monthly mortgate formular
    # c  :  monthly payment
    # P  :  principal
    # r  :  monthly interest
    # N  :  total payments
    # c = P * r * (1 + r) ^ N / ( ( 1 + r) ^ N - 1)
    #
    P =  i['principal']
    r =  p['mortgate_rate'] / 12.0 / 100
    N =  p['mortgate_year'] * 12 
    c = P * r * pow(1 + r, N) / ( pow( 1 + r, N) - 1)
    return c

def investment_return(p):
    investment = {}
    investment['investment']        = p['house_price'] * p['down_payment'] / 100.0
    investment['principal']         = p['house_price'] - investment['investment']
    investment['property_tax']      = p['property_tax']/100.0 * p['house_price']
    investment['monthly_mortgage']  = f(params, investment)
    investment['annual_mortgage']   = investment['monthly_mortgage'] * 12.0
    investment['annual_income']     = p['rental_monthly'] * 12.0 # rental income
    investment['annual_cost']       = investment['annual_mortgage'] + investment['property_tax'] + p['insurance']
    investment['annual_profit']     = investment['annual_income'] - investment['annual_cost']
    investment['return']            = investment['annual_profit'] / investment['investment'] * 100

    return investment


def check_down():
    params = p0
    pprint(params)
    x_range = range (20, 105, 5)
    y_value = []
    for down_p in x_range:
        params['down_payment'] = down_p
        i = investment_return(params)
        y_value.append(i['return'])
        print "Down payment : %d %%, return %f %%" %( down_p, i['return'])
    plt.plot(x_range, y_value, 'ro')
    plt.axis([0, 100, -5, 15])
    plt.show()

def check_rental():
    params = p1
    pprint(params)
    rental = params['rental_monthly']
    x_value = []
    y_value = []
    for r in range (11):
        params['rental_monthly'] = rental + (r-5) * 50  
        i = investment_return(params)
        x_value.append(params['rental_monthly'])
	y_value.append(i['return'])
        print "Monthly rental: $ %d, return %f %%" %( params['rental_monthly'] , i['return'])
    plt.plot(x_value, y_value, 'ro')
    plt.axis([rental-300, rental+300, -5, 15])
    plt.show()
    
check_down()
check_rental()
