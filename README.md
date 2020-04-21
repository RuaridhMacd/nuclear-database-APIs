# Nuclear Database APIs

### Purpose
For sharing source code and modules for pulling down important nuclear data from websites. 

### Motivation 
If we can increase the scale of data ETL for nuclear databases, insights developed from examining these constants can
be further refined.

# Getting Started
A Python virtual environment (virtualenv) is recommended for work with the API scripts. 

1. To start the virtual environment, ensure your system level python interpreter has virtualenv installed.
```
$ pip install virtualenv
```
2. From the root directory of the Nuclear Database APIs, activate the virtual environment.
```
$ . ./env/bin/activate
```
If you are using Bash or Zsh, you should see a small change to your terminal's prompt (env).

# Example: Using the XCOM API
1. Download the repo through GitHub via SSH or ZIP.

2. Find the right webdriver for the browser you are using. 

If you use Chrome, download page for Chrome's webdriver: (https://sites.google.com/a/chromium.org/chromedriver/).

3. Add the binary executable webdriver to the virtual environment's bin/ directory.
```
$ cp ./Downloads/webdriver... ./path/to/env/bin/
```

4. Change into the XCOM directory.
```
$ cd ./src/XCOM
```

5. Run the xcom_api.py file after changing the config.json file which determines which data you will retrieve.
```
$ python xcom_api.py
```

# Other Information
These scripts primarily rely on a 'Web Driver' which operates on an instance of a web browser.

For using Chrome, a chrome web driver is needed under your virtual environment's bin/ directory.

# TODOs
-[ ] Update README in further detail.
-[x] Look into using BS4 python library for web scraping.
-[ ] Bootstrap PSTAR, ESTAR, and ASTAR code with XCOM groundwork.
-[ ] Introduce embedded methods under API classes with visualizations from matplotlib.

# Contact
For questions, direct to jacobmiske@gmail.com
