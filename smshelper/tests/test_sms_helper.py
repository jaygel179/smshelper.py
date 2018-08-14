# -*- coding: utf-8 -*-
from unittest import TestCase

from ..smshelper import SMSHelper


class SMSHelperTest(TestCase):

    def test_should_return_correct_encoding(self):
        self.assert_encoding_equal('Sample message', SMSHelper.GSM_7BIT)
        self.assert_encoding_equal('Sample message €', SMSHelper.GSM_7BIT_EX)
        self.assert_encoding_equal('Sample message \ ', SMSHelper.GSM_7BIT_EX)
        self.assert_encoding_equal('Sample message [', SMSHelper.GSM_7BIT_EX)
        self.assert_encoding_equal('Sample message ]', SMSHelper.GSM_7BIT_EX)
        self.assert_encoding_equal('Sample message {', SMSHelper.GSM_7BIT_EX)
        self.assert_encoding_equal('Sample message }', SMSHelper.GSM_7BIT_EX)
        self.assert_encoding_equal('Sample message 最高', SMSHelper.UTF16)

    def test_should_return_correct_count(self):
        self.assert_length_equal('Sample message', 14)
        self.assert_length_equal('\€|[]{}', 14)
        self.assert_length_equal('Sample message €', 17)
        self.assert_length_equal('最高', 2)
        self.assert_length_equal('a 最高', 4)

    def test_should_return_correct_parts(self):
        self.assert_parts_equal('Sample message', 1)
        self.assert_parts_equal('S' * 160, 1)
        self.assert_parts_equal('S' * 161, 2)
        self.assert_parts_equal('S' * 306, 2)
        self.assert_parts_equal('S' * 307, 3)
        self.assert_parts_equal('€' * 80, 1)
        self.assert_parts_equal('€' * 81, 2)
        self.assert_parts_equal('€' * 152, 2)
        self.assert_parts_equal('€' * 153, 3)
        self.assert_parts_equal('最' * 70, 1)
        self.assert_parts_equal('最' * 72, 2)
        self.assert_parts_equal('最' * 134, 2)
        self.assert_parts_equal('最' * 135, 3)
        self.assert_parts_equal('|{}'.format('S' * 158), 1)
        self.assert_parts_equal('|{}'.format('S' * 159), 2)
        self.assert_parts_equal('{}|{}'.format('S' * 152, 'S' * 152), 3)
        self.assert_parts_equal('{}|{}|'.format('S' * 152, 'S' * 150), 3)
        self.assert_parts_equal('{}|{}|{}|'.format('S' * 152, 'S' * 150, 'S' * 150), 4)

    def assert_encoding_equal(self, text, encoding):
        assert SMSHelper(text).detect_encoding() == encoding

    def assert_length_equal(self, text, count):
        assert SMSHelper(text).count() == count

    def assert_parts_equal(self, text, parts):
        assert SMSHelper(text).parts() == parts
