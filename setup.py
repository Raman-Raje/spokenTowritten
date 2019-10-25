from setuptools import setup

with open("README", 'r') as f:
  long_description = f.read()


setup(
  name = 'spoken2written',        
  packages = ['spoken2written'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = long_description,   # Give a short description about your library
  author = 'Raman Shinde',                   # Type in your name
  author_email = 'raman.shinde15@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Raman-Raje/spoken2written',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Raman-Raje/spoken2written/archive/v_1.tar.gz',    # I explain this later on
  install_requires=[            # I get to this in a second
          'forex-python',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
