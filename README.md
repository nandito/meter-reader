# Meter reader

👨🏻‍🔧 _‍Work in progress!_

The first goal is to track the household's water usage.

1. Periodically take a picture of an analog water meter
1. Use OCR to read value
1. Save data

## Status

Currently it only can take pictures remotely (on a phone) and save it locally (on the device where the script runs).

## Usage

1. Install [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en) on an Android phone
1. Fine tune settings in the app if you want (I changed the photo resolution to the biggest available and set the flash mode to "auto flash")
1. Start server
1. Download this Python script (implemented in 3.7)
1. Create a directory with `output` name
1. Set the IP Webcam address:
  a. either in the code by updating `DEFAULT_CAMERA_IP_ADDR` value
  b. or using `CAM_IP_ADDR` env variable (eg. `CAM_IP_ADDR=192.168.1.12`)
1. Run the app `python take_picture.py`

## License

MIT
