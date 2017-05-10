import urllib.request

def download_hourly(datetime):
	file_name = datetime.split("-")
	file_name = "QCLCD" + file_name[0] + file_name[1] + ".zip";
	read_data = urllib.request.urlopen("https://www.ncdc.noaa.gov/orders/qclcd/").read()
	open(file_name, 'wb').write(read_data)

    
