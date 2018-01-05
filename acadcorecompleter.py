import numpy as np
import pandas as pd
#import psycopg2 as pg
#import matplotlib.pyplot as plt
#import seaborn as sns
#import cufflinks as cf
#from getpass import getpass as gp
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#import platly.graph_objs as go
#init_notebook_mode(connected = True)
#cf.go_offline()



#conn = pg2.connect(database = 'stuanalysis', user = input('Username: '), password = getpass.getpass('Password: '))
#cur = conn.cursor()


CreditReqs = {'WL': 10, 'Math': 20, 'English': 20, 'Bio': 10, 'Sci': 10, 'PE': 10, 'SS': 15, 'Health': 5}
def CreditChk(grdDF, outDF):
	for hisEntry in grdDF.index:
		if grdDF['Mk'][hisEntry] == 'D?' or grdDF['Mk'][hisEntry] == '*F*' or grdDF['Mk'][hisEntry] == '*N*':
			pass
		else:
			outDF[grdDF['Subj'][hisEntry]][grdDF['ID'][hisEntry]] += grdDF['Credits'][hisEntry]
	
def EligChk(fullDF):
	for student in fullDF.index:
		fullDF[ACElig][student] = TRUE
		
		for subject in CreditReqs.keys():
			if fullDF[subject][student] < CreditReqs[subject]:
				fullDF[Elig][student] = FALSE
				break
				
def EthChk(demoDF):
	for student in demoDF.index:
		if demoDF['Eth'][student] == 'Y':
			demoDF['Eth'][student] = 'Hispanic'
		
		else:
			if demoDF['rc2'][student] == np.nan:
				demoDF['Eth'][student] = demoDF['rc1'][student]
			
			else:
				demoDF['Eth'][student] = 'Multiple Eth'
				
	demoDF = demoDF.drop(['rc1', 'rc2'], axis = 1)

def LFChk(demoDF):
	for student in demoDF.index:
		if demoDF['LF'][student] == 'Reclassified':
			if np.datetime64(demoDF['Reclass Date'][student]) > np.datetime64('2016-12-31'):
				demoDF['LF'][student] = 'ELD'
			else:
				pass
		else:
			pass


pd.read_csv('')
pd.read_csv('')

finalDF.to_csv('Fully_Calc.csv')
