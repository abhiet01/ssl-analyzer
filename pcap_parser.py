import pyshark

def extract_ssl_info(pcap_file):
    cap = pyshark.FileCapture(pcap_file, display_filter='ssl')
    for pkt in cap:
        try:
            print(pkt['ssl'].get_field('record'))
        except:
            continue

