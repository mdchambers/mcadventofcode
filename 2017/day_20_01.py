#!/usr/bin/env python

# USAGE: day_20_01.py
# Michael Chambers, 2017
import re
import operator

class ParticleField():
	def __init__(self, file):
		self.particles = ParticleField.parseParticles(file)

	@staticmethod
	def parseParticles(file):
		particles = list()
		with open(file, 'r') as fo:
			particleNumber = 0
			for line in fo:
				line = line.rstrip()
				vecs = re.findall(r"<[^>]+>", line)
				vecs = list(map(lambda x: x.replace("<", "").replace(">","").split(","), vecs))
				pos = tuple(map(int, vecs[0]))
				vel = tuple(map(int, vecs[1]))
				acc = tuple(map(int, vecs[2]))
				particles.append(Particle(pos, vel, acc, particleNumber))
				particleNumber += 1
		return(particles)

	def update(self):
		for p in self.particles:
			p.update()

	def removeCollisions(self):
		toRemove = set()
		for i, ix in enumerate(self.particles):
			for j, jx in enumerate(self.particles):
				if i == j:
					continue
				# print("Compare {} to {}".format(i,j))
				if ix.pos == jx.pos:
					# print("Removing particle pair")
					toRemove |= {i,j}
					# print("To Remove {}".format(toRemove))
		self.particles = [x for i,x in enumerate(self.particles) if i not in tuple(toRemove)]


	def findClosest(self):
		pDist = dict()
		for p in self.particles:
			pDist[p.numb] = p.dist
		return(min(pDist.items(), key = operator.itemgetter(1)))


class Particle:
	def __init__(self, pos, vel, acc, particleNumber):
		self.pos = pos
		self.vel = vel
		self.acc = acc
		self.dist = self.distToOrg()
		self.numb = particleNumber

	def update(self):
		self.vel = tuple(sum(i) for i in zip(self.vel, self.acc))
		self.pos = tuple(sum(i) for i in zip(self.pos, self.vel))
		self.dist = self.distToOrg()


	def distToOrg(self):
		return(sum(map(abs,self.pos)))

	def __repr__(self):
		outstr = "{}: Pos: {} Vel: {} Acc: {} Dist: {}".format(self.numb, self.pos, self.vel, self.acc, self.dist)
		return(outstr)





def part1(file):
	field = ParticleField(file)
	# for p in particles:
		# print(p)
	while True:
		field.update()
		closest = field.findClosest()
		print("Particle: {} Dist: {}".format(closest[0], closest[1]))
			# for p in particles:
			# 	p.update()
			# 	pDist[p.numb] = p.dist
			# minParticle = min(pDist.items(), key = operator.itemgetter(1))
			# print("Particle: {} Dist: {}".format(minParticle[0], minParticle[1]))

def part2(file):
	field = ParticleField(file)
	while True:
		field.update()
		field.removeCollisions()
		print("Particles remaining: {}".format(len(field.particles)))
			




def main():
	file = "day_20_input.txt"
	# file = "day_20_test.txt"
	# part1(file)
	part2(file)



if __name__ == "__main__":
	main()

