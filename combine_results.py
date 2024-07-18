import argparse
import pandas as pd
import sys

lignames = ['LIG', 'SP2']

for i in range(100):

	lignames.append(f'L{i:02}')


def combine_columns(df, method):
	"""
	Rename columns and combine based on largest or average

	Parameters
	----------
	df : pandas dataframe
	method : str, 'largest' or 'sum'
		method used for combining columns, either
		largest : keep only largest value
		sum : take sum of values

	Returns
	-------
	df : pandas dataframe
		pandas dataframe with combined results
	"""

	d = {}

	for col_name in df.columns.values.tolist():

		donor, acceptor = col_name.split('/')

		new_name = get_new_name(donor, acceptor)

		value = df.iloc[0][col_name]

		if new_name in d:

			if method == 'largest':

				if d[new_name] < value:

					d[new_name] = value

			elif method == 'sum':

				d[new_name] += value

			else:

				raise Exception('Method not implemented:', method)

		else:

			d[new_name] = value

	df = pd.DataFrame(d, index=[0])

	return df


def check_unique(input):
	"""
	Check that amino acid part of bonds are unique

	Parameters
	----------
	input : str
		input csv file name

	Returns
	-------
	bool
	"""

	df = pd.read_csv(input, header=None, index_col=0)

	df = df.transpose()

	col_names = df.columns.values.tolist()

	aa_names = [] # names of amino acids taking part in hbonds (with atoms)

	for i in col_names:

		donor, acceptor = i.split('/')

		if donor[0:3] not in lignames:

			aa = donor

		if acceptor[0:3] not in lignames:

			aa = acceptor

		if donor[0:3] in lignames and acceptor[0:3] in lignames:

			raise Exception(f'Ligand name both in donor and acceptor: {donor} {acceptor}')

		aa_names.append(aa)

	unique = len(col_names) == len(set(aa_names))

	if unique is False:
		print({i:aa_names.count(i) for i in aa_names})

	return unique


def get_new_name(donor, acceptor):
	"""
	Get new name for column based on donor acceptor pairs

	Parameters
	----------
	donor : str
	acceptor : str

	Returns
	-------
	new_name : str
	"""

	if donor[0:3] not in lignames:

		new_name = donor + '_donor'

	if acceptor[0:3] not in lignames:

		new_name = acceptor + '_acceptor'

	if donor[0:3] in lignames and acceptor[0:3] in lignames:

		raise Exception(f'Ligand name both in donor and acceptor: {donor} {acceptor}')

	return new_name


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Combine hbond results')

	# Required arguments
	parser.add_argument('-i','--input', nargs='+', help='List of input file names in csv format with hbond results, space-separated', required=True)
	parser.add_argument('-m','--method', help="Method to use to combine individual hbond results, either 'largest' or 'sum'", required=True)
	parser.add_argument('-o','--output', help='Output file name', required=True)

	args = parser.parse_args()

	df = pd.read_csv(args.input[0], header=None, index_col=0)

	df = df.transpose()

	df = combine_columns(df, method=args.method)

	lig = args.input[0].split('_')[0]

	df = df.rename(index={0:lig})

	for i in args.input[1:]:

		df2 = pd.read_csv(i, header=None, index_col=0)

		df2 = df2.transpose()

		df2 = combine_columns(df2, method=args.method)

		lig = i.split('_')[0]

		df2 = df2.rename(index={0:lig})

		df = pd.concat([df, df2])

		df.fillna(value=0, inplace=True)

	print(df)

	df.to_csv(args.output, sep=',')