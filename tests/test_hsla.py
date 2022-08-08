'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from unittest import TestCase, main
from lifehacks.colour import Colour, hsla

from . import AssertColour


################################################################
#######                      tests                       #######
################################################################
class TestHSLA(AssertColour, TestCase):

	def test_init(self) -> None:
		c1 = hsla(10, 10, 10)
		self.assertIsInstance(c1, Colour)
		self.assertIsInstance(c1, hsla)
		self.assert_hsla(c1, 10, 0.1, 0.1, None)

		c2 = hsla(s=1, a=50)
		self.assert_hsla(c2, None, 1, None, 0.5)

	def test_call(self) -> None:
		c1 = hsla(10, 10, 10)
		c2 = c1()
		c3 = c1(h=30)
		c4 = c3(a=0.5)

		self.assertFalse(c1 is c2)
		self.assert_hsla(c2, 10, 0.1, 0.1, None)
		self.assert_hsla(c3, 30, 0.1, 0.1, None)
		self.assert_hsla(c4, 30, 0.1, 0.1, 0.5)

	def test_clone(self) -> None:
		c1 = hsla(10, 10, 10)
		c2 = c1.clone()
		c3 = c1.clone(h=30)
		c4 = c3.clone(a=0.5)

		self.assertFalse(c1 is c2)
		self.assert_hsla(c2, 10, 0.1, 0.1, None)
		self.assert_hsla(c3, 30, 0.1, 0.1, None)
		self.assert_hsla(c4, 30, 0.1, 0.1, 0.5)

	def test_to_hsla(self) -> None:
		...

	def test_to_rgba(self) -> None:
		mint = hsla(114, 31, 68)
		self.assert_rgba(mint.to_rgba(), 153, 199, 148, None)

		orange = hsla(32, 85, 55)
		self.assert_rgba(orange.to_rgba(), 238, 147, 43, None)

	def test_to_hex(self) -> None:
		mint = hsla(114, 31, 68)
		self.assertEqual(mint.to_hex(), '#99c794')

		orange = hsla(32, 85, 55)
		self.assertEqual(orange.to_hex(), '#ee932b')


################################################################
#######                 MAIN STARTS HERE                 #######
################################################################
if __name__ == '__main__':
	main()
