import sys
sys.path.append("/Volumes/GoogleDrive/My Drive/python_code/CATMAID_scripts/")

import pymaid
import pyoctree
from pymaid_creds import url, name, password, token
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

rm = pymaid.CatmaidInstance(url, name, password, token)

#annotated = pymaid.get_annotated('MB nomenclature')
#print(annotated)
