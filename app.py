import streamlit as st
import json
import sys
import os
import sys
import json
import tempfile
sys.path.append('./amdcommunity.py')
from amdcommunity import AmdCommunity
 # Import your AmdCommunity class

# Initialize the AmdCommunity class
amd_community = AmdCommunity()



def write_json_to_temp_file(data, directory):
  try:
    with tempfile.NamedTemporaryFile(dir=directory, mode='w+', delete=True) as temp_file:
      json.dump(data, temp_file, indent=4)
      temp_file.flush()
      return temp_file.name
  except OSError as e:
    print(f"Error creating temporary file in {directory}: {e}")
    return None




# Streamlit app
st.title("Testing")
if(os.path.exists("./temp.json")):
    st.text("file does not exists")

# Text input for URL
url = st.text_input("Enter the AMD Community URL:", "")
# Process the URL and display the result

if st.button("Get Data"):
    if url.strip():
        try:
            # Retrieve and process the data
            result = amd_community.get_and_process_data([url])
            
            # Display the JSON result
            st.code(json.dumps(result, indent=4), language="json")
            write_json_to_temp_file(result,"./temp.json")
            st.text("File successfully saved")
            temp = None
            with open("./temp.json","r") as f:
               temp = json.load(f)
            st.code(temp,language="json")
               
        except Exception as e:
            st.error(f"Error processing the URL: {e}")
    else:
        st.warning("Please enter a valid URL.")
