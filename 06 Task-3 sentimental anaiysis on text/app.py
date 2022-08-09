import streamlit as st
import boto3
st.title("Sentimental analysis on text with AWS")
text=st.text_input("Enter Text")
if st.button("predict"):
    client=boto3.client('comprehend')
    response=client.detect_sentiment(
        Text=text,
        LanguageCode='en'
    )
    # st.write(response)

    if(response['Sentiment']=='POSITIVE'):
        st.success("Positive response")
    elif (response['Sentiment']=='NEGATIVE'):
        st.error('Negative')
    elif (response['Sentiment']=='NEUTRAL'):
        st.warning('Neutral')
    else:
        st.write("Mixed text")
    