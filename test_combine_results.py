import filecmp
import os

from combine_results import *


def test_get_new_name():


	assert get_new_name('ARG145-Side-NE', 'L02643-Side-N1') == 'ARG145-Side-NE_donor'

	assert get_new_name('L02643-Side-N6', 'GLU137-Side-OE1') == 'GLU137-Side-OE1_acceptor'


def test_check_unique():

	assert check_unique('input/L02P7_R1_hbonds_average_unique.csv') is True
	assert check_unique('input/L02P7_R1_hbonds_average_notunique.csv') is False


def test_combine_columns_sum():

	df = pd.read_csv('input/L02P7_R1_hbonds_average.csv', header=None, index_col=0)

	df = df.transpose()

	df = combine_columns(df, method='sum')

	assert df.iloc[0].to_dict() == {'ARG145-Side-NE_donor': 25.28, 'GLU137-Side-OE1_acceptor': 72.12, 'GLU137-Side-OE2_acceptor': 45.36, 'ARG145-Main-N_donor': 13.2, 'VAL117-Main-N_donor': 2.52, 'ARG139-Side-NH2_donor': 3.68, 'SER118-Main-N_donor': 15.839999999999998, 'SER118-Side-OG_donor': 0.76, 'ARG145-Side-NH2_donor': 8.24, 'ARG139-Side-NE_donor': 0.04, 'VAL162-Main-N_donor': 0.04}


def test_combine_columns_largest():

	df = pd.read_csv('input/L02P7_R1_hbonds_average.csv', header=None, index_col=0)

	df = df.transpose()

	df = combine_columns(df, method='largest')

	assert df.iloc[0].to_dict() == {'ARG145-Side-NE_donor': 19.2, 'GLU137-Side-OE1_acceptor': 72.12, 'GLU137-Side-OE2_acceptor': 45.36, 'ARG145-Main-N_donor': 13.2, 'VAL117-Main-N_donor': 1.88, 'ARG139-Side-NH2_donor': 3.68, 'SER118-Main-N_donor': 13.919999999999998, 'SER118-Side-OG_donor': 0.76, 'ARG145-Side-NH2_donor': 8.16, 'ARG139-Side-NE_donor': 0.04, 'VAL162-Main-N_donor': 0.04}


def test_main():

	os.system('python combine_results.py -i input/L01_hbonds_average.csv input/L02P7_hbonds_average.csv -o output/L01_L02P7_hbonds_combined.csv -m largest')

	assert filecmp.cmp('input/L01_L02P7_hbonds_combined.csv', 'output/L01_L02P7_hbonds_combined.csv') is True