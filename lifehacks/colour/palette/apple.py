'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from lifehacks.metaclasses import enum
from .. import hsla, rgba

################################################################
#######                     palette                      #######
################################################################
@enum
class Apple:
	'''	MacOS colours
	'''
	DARK_0 = rgba(34,33,35)
	DARK_1 = rgba(57,55,54)
	RED    = rgba(255,91,84)
	YELLOW = rgba(231,192,59)
	GREEN  = rgba(77,192,57)
	LUCK   = rgba(135, 188, 93)
