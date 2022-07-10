from pandas import read_excel
from argparse import ArgumentParser
from math import isnan
from os import makedirs


def main():
    parser = ArgumentParser()
    parser.add_argument('file')
    parser = parser.parse_args()
    in_name = parser.file
    dir_name = in_name[:in_name.index('.')]
    makedirs(dir_name, exist_ok=True)
    with open('all.csv', 'w') as alldatacsv:
        for sample_id, sheet in read_excel(in_name, None).items():
            # print(sample_id)
            # if '650' in sample_id:
            #     print('skipping 650 run')
            #     continue
            # if 'alpha' in sample_id:
            #     print('skipping alpha run')
            #     continue
            #     stimulus = 'alpha'
            # elif 'omega' in sample_id:
            #     stimulus = 'omega'
            # else:
            #     stimulus = 'unknown'
            #     print(f'Unknown stimulus for sheet {sample_id}')
            with open(f'{dir_name}/{sample_id}.csv', 'w') as f:
                f.write(
                    'date,plate,well,serum_percent,stimulus,SAMPLE_ID,absorbance_620,stimulus,Read time\n')
                read_date = sheet.iloc[5, 0][6:]
                print(read_date)
                read_time = sheet.iloc[6, 0][6:]
                data = []
                for i, row in sheet.iterrows():
                    if not (isnan(row[-1]) or row[0] != row[0]):
                        row_letter = None
                        for i, cell in enumerate(row):
                            if row_letter:
                                data.append(
                                    f'{row_letter}{i},{sample_id},{read_time},{read_date},{cell}\n')
                            else:
                                row_letter = cell
                for i in range(96):
                    alldatacsv.write(data[(i % 8) * 12 + (i // 8)])


if __name__ == '__main__':
    main()
