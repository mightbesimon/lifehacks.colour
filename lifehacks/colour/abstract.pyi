'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from __future__ import annotations
from abc import ABC, abstractmethod

from . import hsla, rgba


################################################################
#######               abstract base class                #######
################################################################
class Colour(ABC):
	'''	abstract base `Colour` class
	'''
	@abstractmethod
	def to_hsla(self) -> hsla: ...

	@abstractmethod
	def to_rgba(self) -> rgba: ...

	def to_hex(self) -> str: ...
