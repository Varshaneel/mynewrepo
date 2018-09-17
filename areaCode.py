#!/usr/bin/python
import re

phone = "602-343-8747"

if re.match("602",phone) :
   print "The area code is: 602"
