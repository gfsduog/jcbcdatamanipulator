from pandas import read_excel
from argparse import ArgumentParser
from math import isnan
from os import makedirs


def main():
    parser = ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('stimulus')
    parser = parser.parse_args()
    in_name = parser.file
    stimulus = parser.stimulus
    dir_name = in_name[:in_name.index('.')]
    makedirs(dir_name, exist_ok=True)
    for sample_id, sheet in read_excel(in_name, None).items():
        with open(f'{dir_name}/{sample_id}.csv', 'w') as f:
            f.write(
                'date,plate,well,serum_percent,stimulus,SAMPLE_ID,absorbance_620,stimulus\n')
            for i, row in sheet.iterrows():
                if not (isnan(row[-1]) or row[0] != row[0]):
                    row_letter = None
                    for i, cell in enumerate(row):
                        if row_letter:
                            f.write(
                                f',,{row_letter}{i},,,{sample_id},{cell},{stimulus}\n')
                        else:
                            row_letter = cell


if __name__ == '__main__':
    main()
