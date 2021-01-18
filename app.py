import streamlit as st
st.title('Movie Review Sentiment Analysis')

st.write("Packages Loading....")
import time
import emoji
import tensorflow as tf
import numpy as np
st.write("Packages Loaded Successfully XD ")

text = st.text_input("Write your review here...")
st.write(text)

if st.button('Predict'):
	my_bar = st.progress(0)
	for percent_complete in range(80):
		time.sleep(0.01)
		my_bar.progress(percent_complete + 1)
	loaded_model = tf.keras.models.load_model('model')
	prediction=loaded_model.predict(np.array([text]))
	for percent_complete in range(80,100):
		time.sleep(0.1)
		my_bar.progress(percent_complete + 1)
	if prediction[0][0]>0.0:
		st.title(emoji.emojize('Positive review :thumbs_up:'))
	else:
		st.title(emoji.emojize('Negative review :thumbsdown:'))