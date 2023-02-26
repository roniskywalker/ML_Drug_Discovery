import streamlit as st
import os
from padelpy import from_smiles
import numpy as np
import pickle
import pandas as pd
from PIL import Image

def app():
		image = Image.open('logo.png')
		st.image(image,use_column_width=True)
		file = st.file_uploader("Upload",type=["csv"])
		if file:
			X = pd.read_csv(file)
			X = X['canonical_smiles']
			st.write(X)
			X_np = np.asarray(X)
			a = []
			for i in X_np:
				a.append(i)
			btn1 = st.button('Create Descripter',key=1)
			if btn1:
				from_smiles(a,output_csv='descripter.csv',fingerprints=True,descriptors=False)
				input_x = pd.read_csv('descripter.csv')
				input_x = input_x.drop(columns=['Name'],axis=1)
				st.write(input_x)
				model = pickle.load(open('trained_model.pkl','rb'))
				global res
				res = model.predict(input_x)
				df = pd.concat([X,pd.DataFrame(res)],axis=1)
				#df = df.iloc[1:,:]
				st.markdown("""### Predicted IC50 VALUES""")
				st.write(df)
				#st.write(type(res))
				os.remove('descripter.csv')

