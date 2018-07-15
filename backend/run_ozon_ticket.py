#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

#OK REGEX
RGEX1  = r'([a-zA-Z]{3,10}[\- \.\-]*[0-3]?[0-9])'
RGEX2 = r'([0-3]?[0-9][\/ \.\-][0-3]?[0-9]?[а-яА-Я]*[\/ \.\-](?:[0-9]{2})?[0-9]{2})'

MONTH_RUS = ["январь","февраль", 
			"март", "апрель", 
			"май", "июнь", 
			"июль", "август", 
			"сентябрь", "октябрь", 
			"ноябрь", "декабрь"]


MONTH_ENG = ["january",
"february",
"march",
"april",
"may",
"june",
"july",
"august",
"september"
"october",
"november",
"december"]



text = """"


15:00, 31 декабря 2017
31/11/2017
"""



def search_data(word):
	number = -1
	global MONTH_RUS, MONTH_ENG
	for i, month in enumerate(MONTH_RUS):
		if word in month:
			number = i

	for i, month in enumerate(MONTH_ENG):
		if word in month:
			number = i
	return number



def split_data(data):
	spec_symbols = [" ", "/", "-", "."]
	splitted = []
	for symb in spec_symbols:
		splitted = data.split(symb)
		if len(splitted) > 1:
			break
	return splitted


def run(text):
	global RGEX1, RGEX2
	result1 = re.findall(RGEX1, text)
	result2 = re.findall(RGEX2, text)


	result_list = []
	for elem in result1:
		temp_dict = {}
		splitted = split_data(elem)
		try:
			temp_dict['month'] = int(splitted[0])
		except:
			temp_dict['month'] = search_data(splitted[0].lower())

		temp_dict['data'] = int(splitted[1])

		temp_dict['year'] = None

		result_list.append(temp_dict)

	for elem in result2:
		temp_dict = {}
		splitted = split_data(elem)
		temp_dict['data'] = int(splitted[0])

		try:
			temp_dict['month'] = int(splitted[1])
		except:
			temp_dict['month'] = search_data(splitted[1][:-1].lower())

		temp_dict['year'] = int(splitted[2])
		result_list.append(temp_dict)

	print(result_list)


run(text)

