import pandas
import sys

'''
Some functions for loading a dataset and performing simple data preparation
'''

def load_dataset(filename, filetype='csv',index_first_col=False):

	'''
	Loads a dataset from file

	Parameters:
	-----------
	filename: str
		Name of data file
	filetype: str
		The type of data file (csv, xls)
	Returns:
	--------
	DataFrame
		Dataset as pandas DataFrame
	'''

	# CSV file
	if filetype == 'csv':
		df = pandas.read_csv(filename,index_col = 0 if index_first_col else None)
	
	# TSV file	
	if filetype == 'tsv':
		df = pandas.read_table(filename,index_col = 0 if index_first_col else None)

	# XLS file
	elif filetype == 'xls':
		# TODO: add pandas.read_xls functionality
		print('xls not yet implemented')
		#exit()
		
	# Neither = problem
	else:
		print('Invalid file type')
		#exit()

	#convert to numeric
	df = df.apply(pandas.to_numeric, errors='ignore')

	return df