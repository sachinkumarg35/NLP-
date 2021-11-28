import pandas as pd
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
#import spacy
#nlp = spacy.load('en_core_web_sm')


# Sidebar options
option = st.sidebar.selectbox('Navigation', 
["Home",
 #"Email Spam Classifier", 
# "Keyword Sentiment Analysis", 
 #"Word Cloud", 
# "N-Gram Analysis", 
 #"Parts of Speech Analysis", 
# "Named Entity Recognition",
 "Text Summarizer+Sentiment Analysis"])

st.set_option('deprecation.showfileUploaderEncoding', False)



if option == 'Home':
	st.write(
			"""
				## Project Description
				This is a complete text analysis tool developed by Sachinkumar. It's built in with multiple features which can be accessed
				from the left side bar.
			"""
		)
    
# Word Cloud Feature
elif option == "Text Summarizer+Sentiment Analysis":

	st.header("Generate Summary")
	st.subheader("Generate a summary from text containing the most popular words in the text.")

	# Ask for text or text file
	st.header('upload file')
	#text = st.text_area('Type Something', height=400)

	# Upload mask image 
	mask = st.file_uploader('Text file', type = ['txt'])

	if st.button("Generate Summary and sentiments"):
          

		# Generate Summary 
		#st.write(len(text))
      
       
		nlp.create_Summary(text, mask)    # created in a custom module imported as nlp 
		st.pyplot()



