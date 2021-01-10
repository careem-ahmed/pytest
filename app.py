import sqlite3
from sqlite3 import Error
from helper import check_ptable, insert_ptable, create_ptable, update_ptable

def manage_portfolio():

    p_name = input("Enter the Customer's name :\n")
    hrisk_amount = input("Enter hrisk amount :\n")
    retire_amount = input("Enter retirement amount :\n")
    hrisk_amount = int(hrisk_amount)
    retire_amount = int(retire_amount)

    data = check_ptable(p_name)
    if data:
        update_ptable(p_name,hrisk_amount,retire_amount)
    else:
        insert_ptable(p_name,hrisk_amount,retire_amount)

def main():
    create_ptable()
    manage_portfolio()

if __name__ == '__main__':
    main()