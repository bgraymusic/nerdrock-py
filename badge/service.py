import hashlib
import json


class BadgeService:

	def __init__(self, sss):
		self.sss = sss

	def createBadgeSpec(self):
		return self.generateToken([0])

	def validateBadgeSpec(self, spec):
		spec_data = self.extractDataFromSpec(spec)
		salted_badge = '{}{}'.format(spec_data['BadgeString'], self.sss)
		return spec_data['Hash'] == hashlib.sha1(salted_badge.encode('utf-8')).hexdigest()

	def addBadgeToSpec(self, spec, badge):
		if not self.validateBadgeSpec(spec):
			return self.createBadgeSpec()
		else:
			spec_data = self.extractDataFromSpec(spec)
			spec_data['Badges'].append(badge)
			return self.generateToken(spec_data['Badges'])

	def generateToken(self, badges):
		badge_str = json.dumps(badges, separators=(',',':'))
		salted_badge = '{}{}'.format(badge_str, self.sss)
		salted_hash = hashlib.sha1(salted_badge.encode('utf-8')).hexdigest()
		spec = '|'.join([badge_str, salted_hash])
		return spec

	def extractDataFromSpec(self, spec):
		return {
			'Badges': json.loads(spec.split('|')[0]),
			'BadgeString' : spec.split('|')[0],
			'Hash': spec.split('|')[1]
		}
