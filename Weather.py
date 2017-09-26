# -*- coding: utf-8 -*-
import json
import urllib.request
import zlib

from city import city

city_name = input('输入：\n')
city_code = city.get(city_name)


if city_code:
	try:
		url = ('http://wthrcdn.etouch.cn/weather_mini?citykey=%s' % city_code)
		content = urllib.request.urlopen(url)
		html = content.read()
		response = zlib.decompress(html, 16 + zlib.MAX_WBITS)
		u = response.decode('utf-8')
		dict_json = json.loads(u)  # 将json格式转化为字典
		weather = dict_json['data']
		sit = weather['forecast']
		print("城市:", weather['city'])
		print("提示:\n", weather['ganmao'])
		for t in sit[0].keys():
			print(sit[0][t], end=' ')
	except Exception as e:
		print("错误!!", e)
else:
	print('没有该城市')
