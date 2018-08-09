[![Build Status](https://travis-ci.org/jaygel179/smshelper.svg?branch=master)](https://travis-ci.org/jaygel179/sms-counter)
[![Coverage Status](https://github.com/jaygel179/smshelper/blob/master/coverage.svg)](https://pypi.org/project/coverage-badge/)


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
