from FinalOutputInApp import uploadimgur as im
import configparser 

# print(im.upload2imgur("result.jpg","test"))

config = configparser.ConfigParser()
config.read('config.ini')
print(config.get('line-bot', 'channel_secret'))