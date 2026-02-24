import streamlit as st
import pandas as pd
import pymysql  # or mysql.connector

st.title("NASA PROJECT - NEO ")

# SQL connection
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password= '1234',
    database= 'stock_analysis'
)

cursor = conn.cursor()


from streamlit_option_menu import option_menu

with st.sidebar:
        selected = option_menu("Main Menu", ["Home","Filters",'Queries'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    

if selected == "Home":
                            
                            st.write("This is my NASA Project")
if selected == "Filters":
                
                st.subheader("Filters page")

if selected == 'Queries':  

                            options = st.selectbox("Queries",["1.Display the entire table",
                                                            "2.Display only the tickers",
                                                            "3. Display al videos and their duration"],placeholder='Choose an option..',index=None)


                            if options == "1.Display the entire table":
                                                    
                                                    cursor.execute('select * from stocks_data_updated')

                                                    result = cursor.fetchall()

                                                    columns = [desc[0] for desc in cursor.description]

                                                    data = pd.DataFrame(result,columns=columns)

                                                    st.dataframe(data) 

                            elif options == "2.Display only the tickers":
                                                    cursor.execute("SELECT Ticker from stocks_data_updated")
                                                    result = cursor.fetchall()

                                                    columns = [desc[0] for desc in cursor.description]

                                                    data = pd.DataFrame(result,columns=columns)

                                                    st.dataframe(data) 

                        
                            conn.close()