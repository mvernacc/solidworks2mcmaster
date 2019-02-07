"""Convert Soldiworks BOM to McMaster order"""

import argparse
import pandas as pd
import re

def main(args):
    data = pd.read_csv(args.sldbom)

    print('I loaded the following data from the SolidWorks BOM:')
    print(data)
    print('\n\n')

    print('To build a McMaster order for this BOM, copy the following')
    print('into "mcmaster.com > Order > Paste products and quantities":\n')

    for index, row in data.iterrows():
        regex = re.compile(r'McMaster-([A-Z0-9]+)')
        matches = regex.findall(row['SW-File Name(File Name)'])
        if len(matches) == 1:
            mcmaster_part_number = matches[0]
        else:
            continue
        print(mcmaster_part_number + ', {:d}'.format(row['QTY.']))

    print('\n\n')
    print('Note that many McMaster products are sold by the pack, not by "each",')
    print('so check the quantities after you build your order. This program')
    print('does not know how many items are in a pack.')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("sldbom", help='Solidworks BOM exported as CSV file.')
    args = parser.parse_args()
    main(args)
