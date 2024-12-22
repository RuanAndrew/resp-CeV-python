import urllib
import urllib.error
import urllib.request
try:
    site = urllib.request.urlopen('https://www.youtube.com')
except urllib.error.URLError:
    print(f'não foi possivel acesar o site ')
else:
    print('tudo ok')
