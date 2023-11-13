#Import libraries
import  streamlit as st
import time
import json
import requests

#Load the model
url = "https://spam-ml.onrender.com/spam_detection"


#Create the spam detector function
def spam_prediction(input_mail):
    
    input_data_for_model = {
        
        'text': input_mail
        
        }
    #Store in a json format
    input_json = json.dumps(input_data_for_model)

    #Post the data to the url 
    response = requests.post(url, data=input_json)
    
    # Return the response
    return response.text
#main function  
def main():
    st.title("SpamGuard Pro")
    
    result=""
    mail=st.text_area("Enter your message")
    if st.button('Prediction'):
        with st.spinner('Processing...'):
            time.sleep(5)
            
        result=spam_prediction(mail)
        st.success(result.strip('"'))
        
        
if __name__ == "__main__":
    main()
