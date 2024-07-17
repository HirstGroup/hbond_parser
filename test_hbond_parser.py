import filecmp
import os

from hbond_parser import *


def test_parse_hbond_file():

	d = parse_hbond_file('input/L02P7_R1_hbonds.dat')

	print(d)

	assert d == {'ARG145-Side-NE/L02643-Side-N1': 8.8, 'L02643-Side-N6/GLU137-Side-OE1': 88.6, 'L02643-Side-N6/GLU137-Side-OE2': 32.4, 'ARG145-Main-N/L02643-Side-N1': 20.6, 'VAL117-Main-N/L02643-Side-N4': 3.8, 'ARG139-Side-NH2/L02643-Side-N1': 0.2, 'SER118-Main-N/L02643-Side-N4': 1.6, 'SER118-Side-OG/L02643-Side-N4': 0.6, 'ARG145-Side-NH2/L02643-Side-N3': 2.0, 'VAL117-Main-N/L02643-Side-O1': 0.2}


def test_take_average_hbond_results():

	input_list = []

	for i in range(1,6):
		d = parse_hbond_file(f'input/L02P7_R{i}_hbonds.dat')

		input_list.append(d)

	print(input_list)

	df = take_average_hbond_results(input_list)

	print(df.to_dict())

	assert df.to_dict() == {'ARG145-Side-NE/L02643-Side-N1': 19.2, 'L02643-Side-N6/GLU137-Side-OE1': 72.12, 'L02643-Side-N6/GLU137-Side-OE2': 45.36, 'ARG145-Main-N/L02643-Side-N1': 13.2, 'VAL117-Main-N/L02643-Side-N4': 1.8799999999999997, 'ARG139-Side-NH2/L02643-Side-N1': 3.6799999999999997, 'SER118-Main-N/L02643-Side-N4': 13.919999999999998, 'SER118-Side-OG/L02643-Side-N4': 0.76, 'ARG145-Side-NH2/L02643-Side-N3': 8.16, 'VAL117-Main-N/L02643-Side-O1': 0.64, 'ARG145-Side-NE/L02643-Side-N3': 6.08, 'SER118-Main-N/L02643-Side-O1': 1.92, 'ARG139-Side-NE/L02643-Side-N1': 0.04, 'ARG145-Side-NH2/L02643-Side-N4': 0.08, 'VAL162-Main-N/L02643-Side-N5': 0.04}


def test_main():

	os.system('python hbond_parser.py -i input/L02P7_R1_hbonds.dat input/L02P7_R2_hbonds.dat input/L02P7_R3_hbonds.dat input/L02P7_R4_hbonds.dat input/L02P7_R5_hbonds.dat -o output/L02P7_R1_hbonds_average.csv')

	assert filecmp.cmp('output/L02P7_R1_hbonds_average.csv', 'input/L02P7_R1_hbonds_average.csv') is True