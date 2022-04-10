import streamlit as st 
import joblib 
st.title("Restaurant Reviews")
model2 = joblib.load('Project')
ip = st.text_input("Enter the Review :")
op = model2.predict([ip])

def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
# review = ['Positive','Negative'] #you can add this line extra to print the text as the output
if st.button('PREDICT'):
  st.title(op[0])
    
if __name__=='__main__': 
    main()    
