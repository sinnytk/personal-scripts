#!/usr/bin/env python
"""Converts a input bank statement file to Pocketbook friendly CSV format."""
import argparse
from enum import Enum
from typing import List


class SupportedBanks(Enum):
    """Supported banks."""
    MEEZAN = "meezan"   


def main():

    supported_banks: List[str] = [bank.value for bank in SupportedBanks]

    argparser = argparse.ArgumentParser(
        description="Convert a local bank CSV file to Pocketbook friendly CSV format."
    )
    argparser.add_argument("bank", type=str.lower, choices=supported_banks, help="Bank of input CSV")
    argparser.add_argument("input_csv", type=argparse.FileType(mode='r'), help="Path to input CSV file of local bank")
    argparser.add_argument("output_csv", type=argparse.FileType(mode="w"), help="Path to output CSV file for Pocketbook")
    args = argparser.parse_args()

    bank, input_csv, output_csv = args.bank, args.input_csv, args.output_csv
    

if __name__ == "__main__":
    main()
