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
$ python3 check_sites_health.py /path/to/urls.txt
URL: http://vk.com , status: OK, Paid
URL: http://google.com , status: OK, Paid
URL: http://gggdddd.com , status: No connection
URL: http://devman.org , status: OK, Paid
URL: http://github.com , status: OK, Paid
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
