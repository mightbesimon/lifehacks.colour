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
	'''	`Colour` object in rgba space

		optional `r`: red `[0, 255]`
		optional `g`: green `[0, 255]`
		optional `b`: blue `[0, 255]`
		optional `a`: alpha `[0, 100]` or `[0.0, 1.0]`
	'''
	r: int                   	# red   [0  , 255]
	g: int                   	# green [0  , 255]
	b: int                   	# blue  [0  , 255]
	a: Optional[float] = None	# alpha [0.0, 1.0]

	def __init__(self,
		r:int,
		g:int,
		b:int,
		a:Optional[float]=...,
	) -> None:
		'''	optional `r`: red `[0, 255]`
			optional `g`: green `[0, 255]`
			optional `b`: blue `[0, 255]`
			optional `a`: alpha `[0, 100]` or `[0.0, 1.0]`
		'''

	def clone(self,
		r:Optional[ int ]=...,
		g:Optional[ int ]=...,
		b:Optional[ int ]=...,
		a:Optional[float]=...,
	) -> rgba:
		'''	create a new instance of `rgba`,
			optionally modify value fields
		'''

	def normalise(self) -> tuple[float, float, float]:
		'''	normalise to `(r, g, b)` between `0.0` and `1.0`
		'''

	def to_hsla(self) -> hsla:
		'''	[formula](https://www.rapidtables.com/convert/color/rgb-to-hsl.html)
		'''

	def to_rgba(self) -> rgba:
		'''return self'''
