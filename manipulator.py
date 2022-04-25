from pandas import read_excel
from argparse import ArgumentParser
from math import isnan
from os import mkdir


def main():
    parser = ArgumentParser()
    parser.add_argument('file')
    in_name = parser.parse_args().file
    dir_name = in_name[:in_name.index('.')]
    mkdir(dir_name)
    for sample_id, sheet in read_excel(in_name, None).items():
        with open(f'{dir_name}/{sample_id}.csv', 'w') as f:
            f.write(
                'date,plate,well,serum_percent,stimulus,SAMPLE_ID,absorbance_620\n')
            for i, row in sheet.iterrows():
                if not (isnan(row[-1]) or row[0] != row[0]):
                    row_letter = None
                    for i, cell in enumerate(row):
                        if row_letter:
                            f.write(
                                f',,{row_letter}{i},,,{sample_id},{cell}\n')
                        else:
                            row_letter = cell


if __name__ == '__main__':
    main()