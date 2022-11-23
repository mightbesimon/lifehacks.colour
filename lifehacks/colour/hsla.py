'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from . import abstract, rgba


################################################################
#######                   dataclasses                    #######
################################################################
@dataclass
class hsla(abstract.Colour):

	h: Optional[float] = None	# hue        [0  , 359]
	s: Optional[float] = None	# saturation [0.0, 1.0]
	l: Optional[float] = None	# lightness  [0.0, 1.0]
	a: Optional[float] = None	# alpha      [0.0, 1.0]

	def __init__(self,
		h:Optional[float]=None,
		s:Optional[float]=None,
		l:Optional[float]=None,
		a:Optional[float]=None,
	) -> None:
		if h and not 0<=h< 360: raise ValueError(f'hue: {h} is not in range [0, 359]')
		if s and not 0<=s<=100: raise ValueError(f'saturation: {s} is not in range [0, 100] or [0.0, 1.0]')
		if l and not 0<=l<=100: raise ValueError(f'lightness: {l} is not in range [0, 100] or [0.0, 1.0]')
		if a and not 0<=a<=100: raise ValueError(f'alpha: {a} is not in range [0, 100] or [0.0, 1.0]')

		if h is not None: self.h = h
		if s is not None: self.s = s/100 if s>1 else s
		if l is not None: self.l = l/100 if l>1 else l
		if a is not None: self.a = a/100 if a>1 else a

	def __call__(self, **kwargs:float) -> hsla:
		return self.clone(**kwargs)

	def clone(self,
		h:Optional[float]=None,
		s:Optional[float]=None,
		l:Optional[float]=None,
		a:Optional[float]=None,
	) -> hsla:
		'''	create a new instance of `hsla`,
			optionally modify value fields
		'''
		return self.__class__(
			h=h if h is not None else self.h,
			s=s if s is not None else self.s,
			l=l if l is not None else self.l,
			a=a if a is not None else self.a,
		)

	def to_hsla(self) -> hsla:  # type: ignore
		'''return self'''
		return self

	def to_rgba(self) -> rgba:
		'''	[formula](https://www.rapidtables.com/convert/color/hsl-to-rgb.html)
		'''
		if self.h is None or self.s is None or self.l is None:
			raise Exception() # todo

		C = (1 - abs(2*self.l - 1)) * self.s
		X = C * (1 - abs(self.h/60 % 2 - 1))
		m = self.l - C/2

		table = {
			(  0,  60): (C, X, 0),
			( 60, 120): (X, C, 0),
			(120, 180): (0, C, X),
			(180, 240): (0, X, C),
			(240, 300): (X, 0, C),
			(300, 360): (C, 0, X),
		}

		r, g, b = [ round((val+m) * 255)
			for bounds, values in table.items()
			if bounds[0]<=self.h<bounds[1]
			for val in values
		]

		return rgba.rgba(r, g, b, self.a)  # type: ignore
