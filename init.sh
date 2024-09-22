#!/bin/bash

set -m

streamlit run /irisdev/app/src/python/dataviz/app.py --server.port=8051 --server.address=0.0.0.0 

fg %1