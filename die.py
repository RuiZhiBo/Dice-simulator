from random import randint

class Die:
	"""表示骰子的类"""
	def  __init__(self, num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		"""返回位于1~max的随机整数"""
		return randint(1, self.num_sides)
