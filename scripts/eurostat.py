import requests
import gzip
import os

def download_economic_agriculture_data(url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&downfile=data/aact_eaa01.tsv.gz"):
    content = __download_raw_file(url)
    file_name = url.split('/')[-1]
    raw_file_path = __save_raw_file(content, file_name)
    unzipped_file = __unzip_gz_file(raw_file_path)
    os.remove(raw_file_path)
    return unzipped_file
    
def download_categories_dic(url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&downfile=dic/en/itm_newa.dic"):
    pass

def download_indicators_dic(url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&downfile=dic/en/indic_ag.dic"):
    pass

def download_units_dic(url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&downfile=dic/en/unit.dic"):
    pass

def __download_raw_file(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        raise SystemExit('Unable to download data file. Reason: {} {}'.format(response.status_code, response.reason))
    return response.content

def __save_raw_file(content, file_name: str) -> str:
    raw_file_path = 'data/raw/{}'.format(file_name)
    with open(raw_file_path, 'wb') as f: 
        f.write(content)
    return raw_file_path

def __unzip_gz_file(raw_file_path):
    file_name = 'economic-agriculture-data.tsv'
    with gzip.open(raw_file_path, 'rb') as f:
        __save_raw_file(f.read(), file_name)
    return 'data/raw/{}'.format(file_name)
    