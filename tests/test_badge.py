import unittest
from badge import BadgeService

sss = '750f948c'
empty_spec = '[0]|61df1d3b00c61e0b076fb00408b916d48d0bc460'
spec_with_1 = '[0,1]|2aef431d1e5188427ef949e69bdbe679883f6014'
spec_with_1_and_2 = '[0,1,2]|c328e6f743528b5e896cc7dc71eee1df0bf3d859'


class TestBadgeService(unittest.TestCase):

	def setUp(self):
		self.service = BadgeService(sss)

	def test_create_badge_spec(self):
		spec = self.service.createBadgeSpec()
		print('Empty spec: {}'.format(spec))
		self.assertEqual(empty_spec, spec, 'msg')

	def test_validate_badge_spec(self):
		self.assertTrue(self.service.validateBadgeSpec(empty_spec), 'msg')
		self.assertTrue(self.service.validateBadgeSpec(spec_with_1), 'msg')
		self.assertTrue(self.service.validateBadgeSpec(spec_with_1_and_2), 'msg')

	def test_add_badge_to_spec(self):
		added_spec = self.service.addBadgeToSpec(empty_spec, 1)
		print('Added spec 1: {}'.format(added_spec))
		self.assertEqual(spec_with_1, added_spec, 'msg')
		added_spec = self.service.addBadgeToSpec(added_spec, 2)
		print('Added spec 2: {}'.format(added_spec))
		self.assertEqual(spec_with_1_and_2, added_spec, 'msg')
