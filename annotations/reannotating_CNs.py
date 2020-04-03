import sys
sys.path.append("/Volumes/Google Drive/My Drive/python_code/CATMAID_scripts/")

import pymaid
import pyoctree
from pymaid_creds import url, name, password, token

#pymaid.clear_cache()
rm = pymaid.CatmaidInstance(url, name, password, token)

annotated = pymaid.get_annotated('MB nomenclature')
print(annotated)