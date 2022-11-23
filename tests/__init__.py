'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from typing import Optional
from unittest import TestCase
from lifehacks.colour import hsla, rgba


################################################################
#######                 base test class                  #######
################################################################
class AssertColour(TestCase):

	def assert_hsla(self,
		colour:hsla,
		h:Optional[float],
		s:Optional[float],
		l:Optional[float],
		a:Optional[float],
	) -> None:
		self.assertEqual(colour.h, h)
		self.assertEqual(colour.s, s)
		self.assertEqual(colour.l, l)
		self.assertEqual(colour.a, a)

	def assert_rgba(self,
		colour:rgba,
		r:Optional[ int ],
		g:Optional[ int ],
		b:Optional[ int ],
		a:Optional[float],
	) -> None:
		self.assertEqual(colour.r, r)
		self.assertEqual(colour.g, g)
		self.assertEqual(colour.b, b)
		self.assertEqual(colour.a, a)
