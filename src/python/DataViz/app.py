from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
import pandas as pd
import streamlit as st

from dataVizUtil import DataVizOpr

import iris

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="iris VisEDA",
    layout="wide",
     page_icon="📊"
)

# init variables
selected_table = False

# Establish communication between pygwalker and streamlit
init_streamlit_comm()
 
# Add a title
st.title("📊IRIS-DataViz")
# Create 3 columns in the layout
col1, col2, col3 = st.columns(3)

with col1:   
    ns = iris.cls('dc.DataViz.Util').getNameSpaces()
    namespaces = ns.split(",")
    selected_ns = st.selectbox('Select Namespace', namespaces,index=None)
if selected_ns:    
    with col2:
        dataVizOprRef = DataVizOpr(namespace=selected_ns)
        schms = dataVizOprRef.get_schema()
        schmas = schms.split(",")    
        selected_schma = st.selectbox('Select Schema', schmas,index=None)
        if selected_schma:
            with col3:        
                tbls = dataVizOprRef.get_tables(selected_schma)
                tables = tbls.split(",")    
                selected_table = st.selectbox('Select Table', tables,index=None)
                
if selected_table:
    print("inside selection")
    # Get an instance of pygwalker's renderer. You should cache this instance to effectively prevent the growth of in-process memory.
    #@st.cache_resource                    
    def get_pyg_renderer() -> "StreamlitRenderer": 
        print("inside renderer")       
        docCount = dataVizOprRef.get_df(selected_schma + '.' + selected_table,500)  
        # When you need to publish your app to the public, you should set the debug parameter to False to prevent other users from writing to your chart configuration file.
        return StreamlitRenderer(docCount, spec="gw_config.json",spec_io_mode="simple")
    
    print(selected_schma)
    if dataVizOprRef.get_row_count(selected_schma + '.' + selected_table) > 0:
        print("inside dataViz")
        renderer = get_pyg_renderer()
        renderer.explorer()
    else:
        st.header("No Record Found")    