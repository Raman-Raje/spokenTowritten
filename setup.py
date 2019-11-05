from setuptools import setup

with open("README.md", 'r') as f:
  long_description = f.read()


setup(
  name = 'spokenTowritten',
  packages = ['spokenTowritten'],
  version = '1.0',
  license='MIT',        # https://help.github.com/articles/licensing-a-repository
  description = long_description,   # Give a short description about your library
  author = 'Raman Shinde',
  author_email = 'raman.shinde15@gmail.com',
  url = 'https://github.com/Raman-Raje/spoken2written',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Raman-Raje/spoken2written/archive/v_1.tar.gz',
  install_requires=[
          'forex-python',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
