import argparse
import pandas as pd


def parse_hbond_file(input):
	"""
	Parse data from hbond file

	Parameters
	----------
	input : str
		name of input file
	repeat : int
		repeat number

	Returns
	-------
	d : dict
		dictionary mapping donor/acceptor to occupancy
	"""

	with open(input) as f:
		lines = f.readlines()

	n_bonds = int(lines[0].split()[1])

	assert lines[1].strip().split() == ['donor', 'acceptor', 'occupancy']

	d = {}

	for line in lines[2:]:

		donor, acceptor, occupancy = line.strip().split()

		occupancy = float(occupancy.strip('%'))

		d[f'{donor}/{acceptor}'] = occupancy

	assert len(d) == n_bonds

	return d


def take_average_hbond_results(input_list):
	"""
	Take average of hbond results

	Parameters
	----------
	input_list : list of dict
		list of dictionaries with hbond results

	Returns
	-------
	df : pandas dataframe
		pandas dataframe with result average
	"""

	df = pd.DataFrame(input_list[0], index=[0])

	for i in range(1, len(input_list)):

		df2 = pd.DataFrame(input_list[i], index=[i])

		df = pd.concat([df, df2])

	df.fillna(value=0, inplace=True)

	df = df.mean()

	return df


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Parse hbond results')

    # Required arguments
    parser.add_argument('-i','--input', nargs='+', help='List of input file names with hbond results, space-separated', required=True)
    parser.add_argument('-o','--output', help='Output file name',required=False)

    args = parser.parse_args()

    dict_list = []

    for i in args.input:
    	dict_list.append(parse_hbond_file(i))

    df = take_average_hbond_results(dict_list)

    df.to_csv(args.output, sep=',', header=False)