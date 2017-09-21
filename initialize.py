import sys
print("Python version: {}".format(sys.version))

import IPython
print("IPython version: {}".format(IPython.__version__))

import pandas as pd
print("pandas version: {}".format(pd.__version__) + " name: pd")

import numpy as np
print("NumPy version: {}".format(np.__version__) + " name: np")

import scipy as sp
print("SciPy version: {}".format(sp.__version__) + " name: sp")

import sklearn
print("scikit-learn version: {}".format(sklearn.__version__)+ " name: skl")

import plotly as py
print("plotly version: {}".format(py.__version__) + " name: py")

import matplotlib as mpl
print("matplotlib version: {}".format(mpl.__version__) + " name: mpl")

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"