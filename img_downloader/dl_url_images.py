import os
import errno
import urllib.request

file = "image_urls.txt"
cwd = os.getcwd()
img_dir = os.path.join(cwd, "downloaded_images")

if not os.path.exists(img_dir):
    try:
        os.makedirs(img_dir)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

with open(file, 'r') as image_urls_file:
    os.chdir(img_dir)
    image_urls = image_urls_file.readlines()
    count = 0
    for image_url in image_urls:
        print("Pulling from {}".format(image_url))
        urllib.request.urlretrieve(image_url, "{}.jpg".format(count))
        count += 1
