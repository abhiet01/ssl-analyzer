import streamlit as st
from pcap_parser import extract_ssl_info

st.title("SSL Traffic Analyzer")
pcap_file = st.file_uploader("Upload PCAP File", type=["pcap", "pcapng"])

if pcap_file:
    extract_ssl_info(pcap_file.name)

