'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from decimal import Decimal
from lifehacks.colour import hsla, rgba


################################################################
#######                   base classes                   #######
################################################################
class AssertColour:

	def assert_hsla(self,
		colour:hsla,
		h:int,
		s:Decimal,
		l:Decimal,
		a:Decimal
	) -> None:
		self.assertEqual(colour.h, h)
		self.assertEqual(colour.s, s)
		self.assertEqual(colour.l, l)
		self.assertEqual(colour.a, a)

	def assert_rgba(self,
		colour:rgba,
		r:int,
		g:Decimal,
		b:Decimal,
		a:Decimal
	) -> None:
		self.assertEqual(colour.r, r)
		self.assertEqual(colour.g, g)
		self.assertEqual(colour.b, b)
		self.assertEqual(colour.a, a)
