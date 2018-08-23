[![Build Status](https://travis-ci.org/jaygel179/smshelper.py.svg?branch=master)](https://travis-ci.org/jaygel179/smshelper.py)
[![Coverage Status](https://coveralls.io/repos/github/jaygel179/smshelper.py/badge.svg)](https://coveralls.io/github/jaygel179/smshelper.py)


SMS Helper
==========
SMS tool that can help you properly count the length of an SMS, calculate the part and what encoding it is.


Installation
------------
`$ pip install smshelper`


Supports
--------
- Python 2


Requirements
------------
- None


Usage
-----
```python
>>> from smshelper import SMSHelper
>>> sms = SMSHelper('Sample message.')
>>> sms.count()
15
>>> sms.parts()
1
>>> sms.detect_encoding()
'GSM_7BIT'
```


Original Idea
-------------
[danxexe/sms-counter](https://github.com/danxexe/sms-counter)



License
-------
MIT licensed. See the bundled [LICENSE](LICENSE) file for more details.
