"""Convert Soldiworks BOM to McMaster order"""

import re
import argparse
import pandas as pd

def main(args):
    """Load a Bill of Materials CSV, and print a string which
    can be copied into the mcmaster.com order form."""
    data = pd.read_csv(args.sldbom)

    print('I loaded the following data from the SolidWorks BOM:')
    print(data)
    print('\n\n')

    print('To build a McMaster order for this BOM, copy the following')
    print('into "mcmaster.com > Order > Paste products and quantities":\n')

    for _, row in data.iterrows():
        # Find the McMaster part number in the file name field of the BOM.
        regex = re.compile(r'McMaster-([A-Z0-9]+)')
        matches = regex.findall(row['SW-File Name(File Name)'])
        if len(matches) == 1:
            mcmaster_part_number = matches[0]
        else:
            continue
        # print "part number, quantity", which is the format expected by
        # the mcmaster.com order form.
        print(mcmaster_part_number + ', {:d}'.format(row['QTY.']))

    print('\n\n')
    print('Note that many McMaster products are sold by the pack, not by "each",')
    print('so check the quantities after you build your order. This program')
    print('does not know how many items are in a pack.')



if __name__ == '__main__':
    #pylint: disable=invalid-name
    parser = argparse.ArgumentParser(
        description='Create McMaster orders from SolidWorks Bill of Materials.' +
        '\nSee https://github.com/mvernacc/solidworks2mcmaster for detailed instructions.')
    parser.add_argument("sldbom", help='SolidWorks BOM exported as CSV file.')
    arguments = parser.parse_args()
    main(arguments)
