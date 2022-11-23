'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from . import Colour, hsla


################################################################
#######                   dataclasses                    #######
################################################################
@dataclass
class rgba(Colour):

	r: int                   	# red   [0  , 255]
	g: int                   	# green [0  , 255]
	b: int                   	# blue  [0  , 255]
	a: Optional[float] = None	# alpha [0.0, 1.0]

	def __init__(self,
		r:int, g:int, b:int,
		a:Optional[float]=None,
	) -> None:
		if r and not 0<=r<=255: raise ValueError(f'red: {r} is not in range [0, 255]')
		if g and not 0<=g<=255: raise ValueError(f'green: {g} is not in range [0, 255]')
		if b and not 0<=b<=255: raise ValueError(f'blue: {b} is not in range [0, 255]')
		if a and not 0<=a<=100: raise ValueError(f'alpha: {a} is not in range [0, 100] or [0.0, 1.0]')

		if r is not None: self.r = r
		if g is not None: self.g = g
		if b is not None: self.b = b
		if a is not None: self.a = a/100 if a>1 else a

	def clone(self,
		r:Optional[ int ]=None,
		g:Optional[ int ]=None,
		b:Optional[ int ]=None,
		a:Optional[float]=None,
	) -> rgba:
		'''	create a new instance of `rgba`,
			optionally modify value fields
		'''
		return self.__class__(
			r=r if r is not None else self.r,
			g=g if g is not None else self.g,
			b=b if b is not None else self.b,
			a=a if a is not None else self.a,
		)

	def normalise(self) -> tuple[float, float, float]:
		'''	normalise to `(r, g, b)` between `0.0` and `1.0`
		'''
		return (self.r/255, self.g/255, self.b/255)

	def to_hsla(self) -> hsla:
		'''	[formula](https://www.rapidtables.com/convert/color/rgb-to-hsl.html)
		'''
		r_, g_, b_ = self.normalise()
		C_max = max(r_, g_, b_)
		C_min = min(r_, g_, b_)
		delta = C_max - C_min

		H = round(
			0 if delta==0 else
			60 * ((g_-b_)/delta % 6) if C_max==r_ else
			60 * ((b_-r_)/delta + 2) if C_max==g_ else
			60 * ((r_-g_)/delta + 4) if C_max==b_ else
			0
		)
		L = round((C_max+C_min) / 2, 2)
		S = round(delta / (1 - abs(2*L - 1)), 2) if (1 - abs(2*L - 1)) else 0

		return hsla.hsla(H, S, L, self.a)  # type: ignore

	def to_rgba(self) -> rgba:  # type: ignore
		'''return self'''
		return self
