'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from . import Colour, rgba


################################################################
#######                   dataclasses                    #######
################################################################
@dataclass
class hsla(Colour):
	'''	`Colour` object in hsla space

		optional `h`: hue `[0, 359]`
		optional `s`: saturation `[0, 100]` or `[0.0, 1.0]`
		optional `l`: lightness `[0, 100]` or `[0.0, 1.0]`
		optional `a`: alpha `[0, 100]` or `[0.0, 1.0]`
	'''
	h: Optional[float] = None	# hue        [0  , 359]
	s: Optional[float] = None	# saturation [0.0, 1.0]
	l: Optional[float] = None	# lightness  [0.0, 1.0]
	a: Optional[float] = None	# alpha      [0.0, 1.0]

	def __init__(self,
		h:Optional[float]=...,
		s:Optional[float]=...,
		l:Optional[float]=...,
		a:Optional[float]=...,
	) -> None:
		'''	optional `h`: hue `[0, 359]`
			optional `s`: saturation `[0, 100]` or `[0.0, 1.0]`
			optional `l`: lightness `[0, 100]` or `[0.0, 1.0]`
			optional `a`: alpha `[0, 100]` or `[0.0, 1.0]`
		'''

	def __call__(self, **kwargs:float) -> hsla: ...

	def clone(self,
		h:Optional[float]=...,
		s:Optional[float]=...,
		l:Optional[float]=...,
		a:Optional[float]=...,
	) -> hsla:
		'''	create a new instance of `hsla`,
			optionally modify value fields
		'''

	def to_hsla(self) -> hsla:
		'''return self'''

	def to_rgba(self) -> rgba:
		'''	[formula](https://www.rapidtables.com/convert/color/hsl-to-rgb.html)
		'''
