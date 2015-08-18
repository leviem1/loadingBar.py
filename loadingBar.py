#    loadingBar is a Python class that displays a progress bar that changes after a step is completed.
#    Copyright (C) 2015  Levi Muniz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys

class loadingBar(object):

	def __init__(self, totalSteps):
		self.totalSteps = totalSteps
		
		try:
			self.totalSteps = int(totalSteps)
		except:
			raise TypeError("totalSteps must be of type integer")
		
		if self.totalSteps < 0:
			raise RuntimeError("totalSteps must be positive integers")
			
		self.completedSteps = 0
		self.printPercent(0)

	def printPercent(self, progress):
		try:
			progress = float(progress)
		except:
			raise TypeError("completedSteps must be integer")
		
		if progress == 100:
			sys.stdout.write("\r[====================>] " + str(progress) + "%\n")
		elif progress < 100 and progress >= 95:
			sys.stdout.write("\r[===================> ] " + str(progress) + "%")
		elif progress < 95 and progress >= 90:
			sys.stdout.write("\r[==================>  ] " + str(progress) + "%")
		elif progress < 90 and progress >= 85:
			sys.stdout.write("\r[=================>   ] " + str(progress) + "%")
		elif progress < 85 and progress >= 80:
			sys.stdout.write("\r[================>    ] " + str(progress) + "%")
		elif progress < 80 and progress >= 75:
			sys.stdout.write("\r[===============>     ] " + str(progress) + "%")
		elif progress < 75 and progress >= 70:
			sys.stdout.write("\r[==============>      ] " + str(progress) + "%")
		elif progress < 70 and progress >= 65:
			sys.stdout.write("\r[=============>       ] " + str(progress) + "%")
		elif progress < 65 and progress >= 60:
			sys.stdout.write("\r[============>        ] " + str(progress) + "%")
		elif progress < 60 and progress >= 55:
			sys.stdout.write("\r[===========>         ] " + str(progress) + "%")
		elif progress < 55 and progress >= 50:
			sys.stdout.write("\r[==========>          ] " + str(progress) + "%")
		elif progress < 50 and progress >= 45:
			sys.stdout.write("\r[=========>           ] " + str(progress) + "%")
		elif progress < 45 and progress >= 40:
			sys.stdout.write("\r[========>            ] " + str(progress) + "%")
		elif progress < 40 and progress >= 35:
			sys.stdout.write("\r[=======>             ] " + str(progress) + "%")
		elif progress < 35 and progress >= 30:
			sys.stdout.write("\r[======>              ] " + str(progress) + "%")
		elif progress < 30 and progress >= 25:
			sys.stdout.write("\r[=====>               ] " + str(progress) + "%")
		elif progress < 25 and progress >= 20:
			sys.stdout.write("\r[====>                ] " + str(progress) + "%")
		elif progress < 20 and progress >= 15:
			sys.stdout.write("\r[===>                 ] " + str(progress) + "%")
		elif progress < 15 and progress >= 10:
			sys.stdout.write("\r[==>                  ] " + str(progress) + "%")
		elif progress < 10 and progress >= 5:
			sys.stdout.write("\r[=>                   ] " + str(progress) + "%")
		elif progress < 5 and progress >= 0:
			sys.stdout.write("\r[>                    ] " + str(progress) + "%")
		else:
			raise RuntimeError("Unexpected error! Is progress greater than 100 or less than 0?")
		sys.stdout.flush()
	
	def stepComplete(self, completeSteps=1):
		try:
			self.completeSteps = int(completeSteps)
		except:
			raise TypeError("completedSteps must be of type integer")
			
		if self.completeSteps < 0:
			raise RuntimeError("Cannot lose progress")
			
		self.completedSteps += completeSteps
		self.progress = (float(self.completedSteps) / float(self.totalSteps)) * 100
		self.progress = round(self.progress, 2)
		
		if self.progress > 100:
			raise RuntimeError("Cannot exceed 100%")
		self.printPercent(self.progress)