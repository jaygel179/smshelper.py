# -*- coding: utf-8 -*-

"""
Copyright (c) 2013 danxexe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import math
import re


# Original idea https://github.com/danxexe/sms-counter
class SMSHelper(object):
    _GSM_7BIT_CHARS = "@£$¥èéùìòÇ\\nØø\\rÅåΔ_ΦΓΛΩΠΨΣΘΞÆæßÉ !\\\"#¤%&'()*+,-./0123456789:;<=>?¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà"
    _GSM_7BIT_EX_CHARS = "\\^{}\\\\\\[~\\]|€"

    _GSM_7BIT_RE = re.compile("^[" + _GSM_7BIT_CHARS + "]*$")
    _GSM_7BIT_EX_RE = re.compile("^[" + '{}{}'.format(_GSM_7BIT_CHARS, _GSM_7BIT_EX_CHARS) + "]*$")
    _GSM_7BIT_EX_ONLY_RE = re.compile("^[\\" + _GSM_7BIT_EX_CHARS + "]*$")

    _GSM_7BIT_ESC = '\u001b'

    GSM_7BIT = 'GSM_7BIT'
    GSM_7BIT_EX = 'GSM_7BIT_EX'
    UTF16 = 'UTF16'

    _MESSAGE_LENGTH = {
        GSM_7BIT: 160,
        GSM_7BIT_EX: 160,
        UTF16: 70,
    }

    _MULTI_MESSAGE_LENGTH = {
        GSM_7BIT: 153,
        GSM_7BIT_EX: 153,
        UTF16: 67,
    }

    def __init__(self, text):
        self._text = text

    def detect_encoding(self):
        if self._GSM_7BIT_RE.match(self._text):
            encoding = self.GSM_7BIT
        elif self._GSM_7BIT_EX_RE.match(self._text):
            encoding = self.GSM_7BIT_EX
        else:
            encoding = self.UTF16
        return encoding

    def count(self):
        encoding = self.detect_encoding()
        if encoding == self.GSM_7BIT:
            length = len(self._text)
        elif encoding == self.GSM_7BIT_EX:
            length = self._count_gsm_7bit_ex()
        elif encoding == self.UTF16:
            length = len(self._text.decode('utf-8'))
        return length

    def parts(self):
        encoding = self.detect_encoding()
        length = self.count()
        parts = 1

        is_multipart = length > self._MESSAGE_LENGTH[encoding]
        if not is_multipart:
            return parts

        per_message_length = self._MULTI_MESSAGE_LENGTH[encoding]
        if encoding in [self.GSM_7BIT, self.UTF16]:
            return int(math.ceil(length / float(per_message_length)))

        new_text = []
        for char in self._text.decode('utf-8'):
            if self._GSM_7BIT_EX_ONLY_RE.match(char.encode('utf-8')):
                new_text.append(self._GSM_7BIT_ESC)
            new_text.append(char)

        count = 0
        for char in new_text:
            count += 1
            if count == 153 and char == self._GSM_7BIT_ESC:
                count = 1
                parts += 1
            elif count == 153:
                count = 0
                parts += 1

        return parts

    def _count_gsm_7bit_ex(self):
        gsm_7bit_chars = []
        gsm_7bit_ex_chars = []
        message = self._text.decode('utf-8')

        for char in message:
            if self._GSM_7BIT_EX_ONLY_RE.match(char.encode('utf-8')):
                gsm_7bit_ex_chars.append(char)
            else:
                gsm_7bit_chars.append(char.encode('utf-8'))

        return len(gsm_7bit_chars) + (len(gsm_7bit_ex_chars) * 2)
