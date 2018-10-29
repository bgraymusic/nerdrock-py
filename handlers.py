from badge.service import BadgeService

badgeService = BadgeService()

def createBadge(event, context):
	return badgeService.createBadge()

def validateBadge(event, context):
	return badgeService.validateBadgeSpec()

def addBadge(event, context):
	return badgeService.addBadge()
