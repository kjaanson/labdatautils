import pandas as pd
from collections import OrderedDict

def load_file(excel_file, fluc='luc2P', rluc='hrlucP'):
    """Loads TECAN exported excel file. Each excel page is assumed to be separate measurement that is added to DataFrame table."""
    #TODO Kirjutada paindlikumaks, las võtab fluc ja hrluc exceli lehtede nimedest.
    #TODO Konstruktid ja treatmendid panna dünaamiliseks excelist.

    luc2p=pd.read_excel(excel_file,sheetname=fluc, header=None)
    hrlucp=pd.read_excel(excel_file,sheetname=rluc, header=None)
    return pd.DataFrame({'Konstruktid':luc2p[0],'Treatments':luc2p[1],'fluc':luc2p[2],'rluc':hrlucp[2]}, columns=['Konstruktid','Treatments','fluc','rluc'])
