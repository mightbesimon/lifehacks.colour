'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from unittest import TestCase, main
from lifehacks.colour import Colour, rgba

from . import AssertColour


################################################################
#######                      tests                       #######
################################################################
class TestRGBA(AssertColour, TestCase):

	def test_init(self) -> None:
		c = rgba(10, 10, 10)
		self.assertIsInstance(c, Colour)
		self.assertIsInstance(c, rgba)
		self.assert_rgba(c, 10, 10, 10, None)


	def test_call(self) -> None:
		c1 = rgba(10, 10, 10)
		c2 = c1.clone()
		c3 = c1.clone(r=30)
		c4 = c3.clone(a=0.5)

		self.assertFalse(c1 is c2)
		self.assert_rgba(c2, 10, 10, 10, None)
		self.assert_rgba(c3, 30, 10, 10, None)
		self.assert_rgba(c4, 30, 10, 10, 0.5)

	def test_clone(self) -> None:
		c1 = rgba(10, 10, 10)
		c2 = c1.clone()
		c3 = c1.clone(r=30)
		c4 = c3.clone(a=0.5)

		self.assertFalse(c1 is c2)
		self.assert_rgba(c2, 10, 10, 10, None)
		self.assert_rgba(c3, 30, 10, 10, None)
		self.assert_rgba(c4, 30, 10, 10, 0.5)

	def test_to_hsla(self) -> None:
		mint = rgba(153, 199, 148)
		self.assert_hsla(mint.to_hsla(), 114, 0.31, 0.68, None)

		orange = rgba(238, 147, 43)
		self.assert_hsla(orange.to_hsla(), 32, 0.85, 0.55, None)

	def test_to_rgba(self) -> None:
		...

	def test_to_hex(self) -> None:
		mint = rgba(153, 199, 148, 100)
		self.assertEqual(mint.to_hex(), '#99c794')

		orange = rgba(238, 147, 43, 100)
		self.assertEqual(orange.to_hex(), '#ee932b')

		transparent = rgba(0, 0, 0, 0)
		self.assertEqual(transparent.to_hex(), '#00000000')


################################################################
#######                 MAIN STARTS HERE                 #######
################################################################
if __name__ == '__main__':
	main()
