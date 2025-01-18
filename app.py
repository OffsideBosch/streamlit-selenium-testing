import streamlit as st
import json
import os
import tempfile
import sys

# Ensure the path to amdcommunity.py is correct
sys.path.append('.')  # Add current directory to path
from amdcommunity import AmdCommunity  # Import your AmdCommunity class

# Initialize the AmdCommunity class
amd_community = AmdCommunity()

def write_json_to_temp_file(data, file_path):
    try:
        with open(file_path, 'w') as temp_file:
            json.dump(data, temp_file, indent=4)
        return file_path
    except OSError as e:
        st.error(f"Error creating file {file_path}: {e}")
        return None

# Streamlit app
def main():
    st.title("AMD Community Data Retriever")

    # Text input for URL
    url = st.text_input("Enter the AMD Community URL:", "")

    # Process the URL and display the result
    if st.button("Get Data"):
        if url.strip():
            try:
                # Retrieve and process the data
                result = amd_community.get_and_process_data([url])
                
                # Display the JSON result
                st.json(result)
                
                # Save to file
                temp_file_path = "./temp.json"
                write_json_to_temp_file(result, temp_file_path)
                st.success("File successfully saved")
                
                # Read and display the saved file
                try:
                    with open(temp_file_path, "r") as f:
                        temp_data = json.load(f)
                    st.code(json.dumps(temp_data, indent=4), language="json")
                except Exception as read_error:
                    st.error(f"Error reading saved file: {read_error}")
                
            except Exception as e:
                st.error(f"Error processing the URL: {e}")
        else:
            st.warning("Please enter a valid URL.")

# Run the app
if __name__ == "__main__":
    main()
