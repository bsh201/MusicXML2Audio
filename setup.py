from setuptools import setup, find_packages

setup(
    name ='MXL2AUDIO',
    version ='0.1.0',
    description ='Change musicxml in audio (mp3, wav...)',
    author ='BSH',
    author_email ='qodbwls9402@gmail.com',
    url ='',
    download_url ='',
    install_requires = ['argparse', 'fluidsynth', 'ffmpeg'],
    packages = find_packages(exclude = []),
    keywords= ['MXL2AUDIO'],
)