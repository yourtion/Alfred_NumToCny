#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import NumToCny
import unittest

CASE1 = [
  ['1', '壹圆整'],
  ['20', '贰拾圆整'],
  ['100', '壹佰圆整'],
  ['1000', '壹仟圆整'],
  ['30000', '叁万圆整'],
  ['400000', '肆拾万圆整'],
  ['5000000', '伍佰万圆整'],
  ['60000000', '陆仟万圆整'],
  ['700000000', '柒亿圆整'],
  ['8000000000', '捌拾亿圆整'],
  ['90000000000', '玖佰亿圆整'],
  ['100000000000', '壹仟亿圆整'],
  ['2000000000000', '贰万亿圆整'],
  ['30000000000000', '叁拾万亿圆整'],
  ['400000000000000', '肆佰万亿圆整'],
  ['5000000000000000', '伍仟万亿圆整']
]

CASE2 = [
  ['1000000001234', '壹万亿壹仟贰佰叁拾肆圆整'],
  ['1212.1', '壹仟贰佰壹拾贰圆壹角整'],
]

class NumToCnyTestCase(unittest.TestCase):
  def testInt(self):
    for case in CASE1:
      res = NumToCny.to_rmb_upper(case[0])
      self.assertEqual(res, case[1])
    for case in CASE2:
      res = NumToCny.to_rmb_upper(case[0])
      self.assertEqual(res, case[1])

if __name__ == '__main__':
  unittest.main()
  