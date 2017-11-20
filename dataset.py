import pandas 
import sys
import os

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
	elif filetype == 'tsv':
		df = pandas.read_table(filename,index_col = 0 if index_first_col else None)

	# XLS file
	elif filetype == 'xls':
		# TODO: add pandas.read_xls functionality
		df = pandas.read_excel(filename, index_col=0 if index_first_col else None)
		#exit()
		
	# Neither = problem
	else:
		print('Invalid file type')
		#exit()

	#convert to numeric
	df = df.apply(pandas.to_numeric, errors='ignore')

	return df
	
def clean_sequence(df, exlude_index=False):
	idx = 1 if exlude_index else 0
	for col in df.columns[idx:]:
			if not any(df[col].isnull()):
				df[col] = list(map(clean, df[col].values))
	return df
	
def clean(seq_string,delimiter=',',num_type=float):
	return list(map(num_type, seq_string.split(delimiter)))
	
def load_all_data(directory):
	data = {}
	for file in os.listdir(directory):
		data[file[:-5]] = load_dataset(os.path.join(directory,file), filetype='xls', index_first_col=True)
	return data