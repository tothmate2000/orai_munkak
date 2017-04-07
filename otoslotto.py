import random

def otoslotto():
	szamok = []
	b = 0
	while len(szamok) < 6:
		b = random.randint(1,90)
		if b not in szamok:
			szamok.append(b)
	return szamok
