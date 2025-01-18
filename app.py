import streamlit as st
import json
import sys
import os
import sys
import json
sys.path.append('./amdcommunity.py')
from amdcommunity import AmdCommunity
 # Import your AmdCommunity class

# Initialize the AmdCommunity class
amd_community = AmdCommunity()

# Streamlit app
st.title("Testing")

# Text input for URL
url = st.text_input("Enter the AMD Community URL:", "")
# Process the URL and display the result
if(os.path.exists("./temp.txt")):
    st.code("file does not exists",language="python")
if st.button("Get Data"):
    if url.strip():
        try:
            # Retrieve and process the data
            result = amd_community.get_and_process_data([url])
            
            # Display the JSON result
            st.code(json.dumps(result, indent=4), language="json")
            with open("./temp.txt","w") as f:
                f.write(result)
            st.code("path exists",language="python")
        except Exception as e:
            st.error(f"Error processing the URL: {e}")
    else:
        st.warning("Please enter a valid URL.")
