#!/usr/bin/env python3
# Created By: Val Ijaola
# Date: October 10, 2023
# This program Calculates the Tax and total of items
# using the HST of New Brunswick

import constant


def main():
    # Input Subtotal
    subtotal = float(input("What is the subtotal\n"))

    # Process - Calculating tax and total
    tax = subtotal * constant.HST
    total = subtotal + tax

    # Output - display tax and total
    print(f"The Tax on your item is ${tax}.")
    print(f"The Total on your item is ${total}.")


if __name__ == "__main__":
    main()
