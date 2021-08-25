import pyimgur
CLIENT_ID = '4510074dfaaf1ad'
def upload2imgur(PATH,title):
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title=title)
    return uploaded_image.link
def getimg(name):
    im = pyimgur.Imgur(CLIENT_ID)
    image = im.get_image(name)
    return image.link