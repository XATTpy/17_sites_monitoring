# Sites Monitoring Utility

This script checks the status of sites from the specified text file.

# Quickstart

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

Then run the script:

```bash
$ python3 check_sites_health.py /home/xatt/Python/devman/urls.txt -d 60
URL: http://vk.com ; Connection status: True; Payment status: True
URL: http://google.com ; Connection status: True; Payment status: True
URL: http://gggdddd.com ; Connection status: False; Payment status: False
URL: http://devman.org ; Connection status: True; Payment status: False
URL: http://github.com ; Connection status: True; Payment status: True
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
