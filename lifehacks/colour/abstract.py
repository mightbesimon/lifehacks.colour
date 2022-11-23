'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from __future__ import annotations
from abc import ABC, abstractmethod


################################################################
#######               abstract base class                #######
################################################################
class Colour(ABC):
	'''	abstract base `Colour` class
	'''
	@abstractmethod
	def to_hsla(self) -> ...:
		raise NotImplemented

	@abstractmethod
	def to_rgba(self) -> ...:
		raise NotImplemented

	def to_hex(self) -> str:
		c = self.to_rgba()
		alpha = f'{round(c.a*255):02x}' if c.a is not None and c.a!=1 else ''  # type: ignore
		return f'#{c.r:02x}{c.g:02x}{c.b:02x}{alpha}'  # type: ignore
