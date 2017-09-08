import pandas
import sys

'''
Some functions for loading a dataset and performing simple data preparation
'''

def load_dataset(filename, filetype='csv', header=True, index_first_col=False):

    '''
    Loads a dataset from file
    
    Parameters:
    -----------
    filename: str
        Name of data file
    filetype: str
        The type of data file (csv, tsv)
    Returns:
    --------
    DataFrame
        Dataset as pandas DataFrame
    '''
	

    in_file = open(filename)
    data = []
    header_row = ''

    # Read the file line by line into instance structure
    for line in in_file.readlines():

        # Skip comments
        if not line.startswith("#"):
            
            # TSV file
            if filetype == 'tsv':
                if header:
                    header_row = line.strip().split('\t')
                else:
                    raw = line.strip().split('\t')
                    
            # CSV file
            elif filetype =='csv':
                if header:
                    header_row = line.strip().split(',')
                else:
                    raw = line.strip().split(',')
            
            # Neither = problem
            else:
                print('Invalid file type')
                exit()

            # Append to dataset appropriately
            if not header:
                data.append(raw)
            header = False
    
    # Build a new dataframe of the data instance list of lists and return
    df = pandas.DataFrame(data, columns=header_row)
	
	# convert to numeric
    df = df.apply(pandas.to_numeric, errors='ignore')
	
	# index first column?
    df.set_index(df.columns.values[0], inplace=True) if index_first_col else None
	
    return df