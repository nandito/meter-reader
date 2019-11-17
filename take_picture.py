import requests
from os import environ
from datetime import datetime

print('🎬 Beginning process')

DEFAULT_CAMERA_IP_ADDR = '192.168.1.68'
camera_ip_address = environ.get('CAM_IP_ADDR', DEFAULT_CAMERA_IP_ADDR)
camera_url = 'http://' + camera_ip_address + ':8080'
print('  📟 Camera url: ' + camera_url)

print('  📸 Taking picture')
photo_url = camera_url + '/photoaf.jpg'
r = requests.get(photo_url)

now = datetime.now().strftime("%Y-%m-%d__%Hh%Mm%Ss")
filename = now + ".jpg"
file_with_path = "./output/" + filename

print('  💾 Saving file as ' + filename)
with open(file_with_path, 'wb') as f:
    f.write(r.content)

print('✅ Process completed')
