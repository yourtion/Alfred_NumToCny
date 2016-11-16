#encoding: utf-8

import NumToCny
import json

def parse(strs):
    res = {"title": strs,"subtitle": "Copy to clipboard","arg": "Copy to clipboard","icon": "icon.png"}
    return {"items": [res]}

ret = NumToCny.to_rmb_upper({query})

print(json.dumps(parse(ret)))
