import urllib.request
#import zipfile,io

def download_hourly(datetime):
	fileName = datetime.split("-")
	fileName = "QCLCD" + fileName[0] + fileName[1] + ".zip";
	file = urllib.request.urlopen("https://www.ncdc.noaa.gov/orders/qclcd/").read()
	open(fileName, 'wb').write(file)

    
