from simple_image_download import simple_image_download as smp

response = smp.simple_image_download()  

keywords = ['tony stark robert downey jr', 'tony start rdj']
for kw in keywords:
    response.download(keywords=kw,limit=300)