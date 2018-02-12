#!/usr/bin/python
# -*- coding: utf-8 -*-

_SUFFIXES = ["", "thousand", "million", "billion"];
_ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
_AFTER_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"];

#handles the nomenclature of a triplet
#number: the number in the string form, index: position of the triplet
def gimmeThemWords(number, index):
    length = len(number);

    if(length > 3):
        return False;

    #pads the number's string representation with 0s on the left
    number = number.zfill(3);
    string = "";

    hundreds_digit = ord(number[0]) - 48;
    tens_digit = ord(number[1]) - 48;
    ones_digit = ord(number[2]) - 48;

    string += "" if number[0] == '0' else _ONES[hundreds_digit];
    string += " hundred " if not string == "" else "";

    if(tens_digit > 1):
        string += _TENS[tens_digit - 2];
        string += " ";
        string += _ONES[ones_digit];

    elif(tens_digit == 1):
        string += _AFTER_TEN[(int(tens_digit + ones_digit) % 10) - 1];

    elif(tens_digit == 0):
        string += _ONES[ones_digit];

    #counter check to determine the positional system
    if(string.endswith("zero")):
        string = string[:-len("zero")];

    else:
        string += " ";

    if(not len(string) == 0):
        string += _SUFFIXES[index];

    return string;

def not_empty(s):
    return not len(s.strip()) == 0

#initiates the process of converting the number into its cardinal form
def to_eng(number):
    length = len(str(number));

    #counter contains the number of size- 3 groupings of digits that can be formed from the number
    counter = int(length / 3) if length % 3 == 0 else int(length / 3) + 1;
    counter_copy = counter;
    word_representation = [];

    for i in range(length - 1, -1, -3):
        word_representation.append(gimmeThemWords(str(number)[0 if i - 2 < 0 else i - 2 : i + 1], counter_copy - counter));
        counter -= 1;
    res = ", ".join(filter(not_empty, reversed(word_representation))).strip()
    return res.capitalize()
