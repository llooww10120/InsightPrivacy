import pyimgur
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
CLIENT_ID = config.get('imgur', 'CLIENT_ID')
def upload2imgur(PATH,title):
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title=title)
    return uploaded_image.link
def getimg(name):
    im = pyimgur.Imgur(CLIENT_ID)
    image = im.get_image(name)
    return image.link
if __name__=="__main__":
    print(CLIENT_ID)