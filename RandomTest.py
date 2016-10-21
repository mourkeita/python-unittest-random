# coding: utf-8

import random
import unittest

class RandomTest(unittest.TestCase):

	"""
	Cette classe teste des foncitonnalités du
	module random telles que choice, shuffle et range
	"""

	def test_choice(self):

		"""
		Cette fonction teste si la fonction
		random.choice(tableau) renvoie bien
		un élèment qui appartient au tableau
		"""

		# Tableau de 100 entiers
		tableau = list(range(100))

		#On tire au hasard un entier de la liste
		elt = random.choice(tableau)

		#On teste si elt est bien dans la liste
		self.assertIn(elt, tableau)

	def test_shuffle(self):

		"""
		Cette fonction teste si la fonction random.shuffle
		retourne le même nombre d'élèments de départ
		"""

		# Tableau de 100 élèments
		tableau = list(range(100))

		# Tableau après shuffle
        random.shuffle(tableau)	

        # On trie le tableau
        tableau.sort()

		# Test si on a le résultat escompté
		self.assertEqual(tableau, list(range(100)))

	def test_sample(self):

		"""
		Cette fonction teste si la fonction ranom.range
		retourne bien une partie de l'objet en paramètre
		"""

		# On déclare une liste de 100 élèments
		tableau = range(100)

		# Nouvelle liste à comparer
		tab = random.sample(tableau, 5)

		# On vérifie que tab est une partie de tableau
		for elt in tab:
			self.assertIn(elt, tableau)


unittest.main()
