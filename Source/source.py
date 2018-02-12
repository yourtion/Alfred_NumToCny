#encoding: utf-8

import NumToCny
import NumToEng
import json

def parse(strs, strs2):
    res = { "title": strs, "subtitle": "Copy to clipboard","arg": strs, "icon": "icon.png" }
    res2 = { "title": strs2, "subtitle": "Copy to clipboard","arg": strs2, "icon": "icon.png" }
    return { "items": [res, res2] }

ret = NumToCny.to_rmb_upper('{query}')
ret2 = NumToEng.to_eng('{query}')

print(json.dumps(parse(ret, ret2)))
