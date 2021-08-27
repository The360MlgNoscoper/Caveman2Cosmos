#
# TestCode - tab within DebugScreen
#
# Toffer - I intentionally made this very bare bones, hiding technical stuff inside DebugScreen.py
#	This so that python novices can utilize this file as a training/testing ground with minimal intimidation.
from CvPythonExtensions import *
GC = CyGlobalContext()

class TestCode:

	def __init__(self, pDebugScreen):
		self.main = pDebugScreen

		import HelperFunctions
		self.HF = HelperFunctions.HelperFunctions([0])

	# Use this instead of print, it will print to pythonDbg and will also print on screen.
	def log(self, text):
		self.main.testCodelog(text)

	def drawTab(self, screen):
		# Toffer - Add new test code button to the debug screen like this and define the function below.
		#	This is all that is needed for the button to become functional, one line.
		#self.main.addTestCode(screen, functionName, "Button Text", "tooltip")
		self.main.addTestCode(screen, self.checkBuildingRequirements, "Building requirements of buildings", "Checks if building requirements aren't unlocked after building itself")
		self.main.addTestCode(screen, self.checkBuildingRequirementReplacements, "Building requirement replacements", "Checks if building requirements are replaced")
		self.main.addTestCode(screen, self.checkBuildingRequirementObsoletion, "Building obsoletion of requirements", "Checks when requirements obsolete in relation to building itself. Building requirements of building shouldn't obsolete before building itself. For beeliners: If there is requirement obsoletion within 10 columns, then building shall obsolete on same tech as its requirement")
		self.main.addTestCode(screen, self.checkBuildingUnlockObsoletion, "Buildings unlock/obsoletion", "Checks if building obsoletion doesn't happen within 5 columns of building unlock")
		self.main.addTestCode(screen, self.checkBuildingReplacementObsoletion, "Building obsoletion of replacements", "Checks when replacements are unlocked and obsoleted. Base -> Upgrade: Base tech obsoletion/Upgrade tech unlock, beelining might cause base building to go obsolete before replacement is available, difference of more than 5 columns is assumed safe. Replacing building shouldn't obsolete before replaced one")
		self.main.addTestCode(screen, self.checkBuildingImplicitReplacements, "Building - check implicit replacements", "Check if we have implicit replacements - All replacements must be explicitly defined even if building got obsoleted long ago")
		self.main.addTestCode(screen, self.checkBuildingReplacingQuality, "Building - check replacement quality", "Check if building, that replaces earlier buildings is better in various metrics")
		self.main.addTestCode(screen, self.checkBuildingReplacingAvailability, "Building - check replacement availability", "Check if replaced buildings are affected by other buildings, civics, traits, conversely improvements can upgrade, so they are checked too")
		self.main.addTestCode(screen, self.checkBuildingBonusRequirements, "Building bonus requirements", "Checks various bonus prereqs to check if they aren't unlocked after building")
		self.main.addTestCode(screen, self.checkBuildingBonusManufacturerTech, "Building earliest manufacturer on resource tech reveal", "Checks when earliest resource producer is unlocked")
		self.main.addTestCode(screen, self.checkBuildingRequirementTags, "Building - requirement requirements", "Check if additonal requirements don't lock out buildings")
		self.main.addTestCode(screen, self.checkBuildingRequirementCivics, "Building - requirement civic requirements", "Check if building requirements require civics")
		self.main.addTestCode(screen, self.checkBuildingCivicRequirements, "Building - civic requirements and obsoletions", "Checks if various civics aren't unlocked after building. Civic buildings shouldn't obsolete, as effectively it represents unique conditions under that civic")
		self.main.addTestCode(screen, self.checkBuildingCivicInfluences, "Building - check civic tags", "Check if building is available when civic is active")
		self.main.addTestCode(screen, self.checkBuildingReligionRequirement, "Building religion requirement test", "Checks if tags requiring religion share same religion")
		self.main.addTestCode(screen, self.checkBuildingTags, "Building Tags", "Checks if commerce double time exists on wonders, that have relevant flat commerce change, if Commerce Change has relevant flat commerce changes, if hurry modifiers exist on unbuildable buildings, if GP unit references are paired with GP changes, or if freebonus amount is paired with bonus")
		self.main.addTestCode(screen, self.checkBuildingFreeReward, "Building obsoletion of free buildings", "Checks if free buildings - normally unbuildable - obsolete together with building, that gives it for free. Buildable free building shouldn't obsolete before building, that gives it for free")
		self.main.addTestCode(screen, self.checkBuildingTechMods, "Building tech changes and modifiers", "Checks if tech modifiers and changes occur within building lifetime")
		self.main.addTestCode(screen, self.checkBuildingBonusTags, "Building - check bonus tags", "Check if bonus tech reveal is after building obsoletion - those bonus tags affect buildings in various ways")
		self.main.addTestCode(screen, self.checkBuildingAffectingBuildings, "Building - check building tags", "Check if building affecting other building is within lifetime of each other")
		self.main.addTestCode(screen, self.checkBuildingCosts, "Building - check costs", "Check if buildings have correct costs")
		self.main.addTestCode(screen, self.checkUnitUpgrades, "Unit - check unit upgrades", "Checks unit upgrades")
		self.main.addTestCode(screen, self.checkUnitBonusRequirements, "Unit - check bonus requirements", "Checks bonus requirements of units")
		self.main.addTestCode(screen, self.checkUnitRequirements, "Unit - check building requirements", "Checks building requirements of units")
		self.main.addTestCode(screen, self.checkUnitRequirementsReplacements, "Unit - check building requirement replacements", "Checks if unit has building requirement, that gets replaced")
		self.main.addTestCode(screen, self.checkBonusImprovementProductivity, "Bonus - check improvement productivity", "Checks if improvement replacements productivity from bonus, improvement and bonus+improvement is higher compared to base improvement")
		self.main.addTestCode(screen, self.checkBonusProducerReplacements, "Bonus - check potential bonus producer replacements", "Checks replacements of manufactured bonus producers")
		self.main.addTestCode(screen, self.checkCivicImprovementReplacements, "Civic - check potential improvement replacements", "Checks replacements of improvements in civics")
		self.main.addTestCode(screen, self.checkTraitImprovementReplacements, "Trait - check potential improvement replacements", "Checks replacements of improvements in traits")
		self.main.addTestCode(screen, self.checkImprovementTechYieldBoostLocation, "Improvement - yield boost tech requirements", "Checks if yield boosts happen within tech unlock and replacement of improvements")
		self.main.addTestCode(screen, self.checkImprovementYieldValues, "Improvement - all techs boosts compared to upgrade", "Checks if improvement with all tech boosts isn't better than its upgrade")
		self.main.addTestCode(screen, self.checkBuildingWonderMovies, "Building movie wonder list", "Checks movies of noncultural wonders, religious shrines and projects movie location")
		self.main.addTestCode(screen, self.checkTechTypes, "Building and unit - Tech Types check", "Checks if buildings and units main tech is more advanced or equal to Tech Type")
		self.main.addTestCode(screen, self.listObsoleteingBuildings, "Building - list obsoletions without replacement", "Checks if buildings are obsoleteing without replacements. Regular buildings should obsolete only if its replaced")

	#Building requirements of buildings
	def checkBuildingRequirements(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			iBaseTechLoc = self.HF.checkBuildingTechRequirements(CvBuildingInfo)[0]
			aBaseTechIDList = self.HF.checkBuildingTechRequirements(CvBuildingInfo)[2]
			aBaseTechList = self.HF.checkBuildingTechRequirements(CvBuildingInfo)[3]

			#<PrereqInCityBuildings> - require all buildings in list
			aRequirementTechLocList = []
			aReqColumnTechIDList = []
			aReqColumnTechList = []
			for iBuildingRequirement in xrange(CvBuildingInfo.getNumPrereqInCityBuildings()):
				iPrereqBuilding = CvBuildingInfo.getPrereqInCityBuilding(iBuildingRequirement)
				aRequirementTechLocList.append(self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[0])
				aRequirementTechIDList = self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[2]
				aRequirementTechList = self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[3]

				for i in xrange(len(aRequirementTechList)):
					if GC.getTechInfo(GC.getInfoTypeForString(aRequirementTechList[i])).getGridX() == iBaseTechLoc:
						aReqColumnTechIDList.append(aRequirementTechIDList[i])
				for i in xrange(len(aRequirementTechList)):
					if GC.getTechInfo(GC.getInfoTypeForString(aRequirementTechList[i])).getGridX() == iBaseTechLoc:
						aReqColumnTechList.append(aRequirementTechList[i])
			if len(aRequirementTechLocList) > 0 and max(aRequirementTechLocList) > iBaseTechLoc:
				self.log(CvBuildingInfo.getType()+" is unlocked before its AND building requirements "+str(aRequirementTechList)+" "+str(aBaseTechList)+" requirement/base column "+str(max(aRequirementTechLocList))+" / "+str(iBaseTechLoc))
			if len(aRequirementTechLocList) > 0 and max(aRequirementTechLocList) == iBaseTechLoc:
				for i in xrange(len(aReqColumnTechIDList)):
					if aReqColumnTechIDList[i] not in aBaseTechIDList:
						self.log(CvBuildingInfo.getType()+" AND requirement unlocked by different tech in column: "+str(iBaseTechLoc)+" requirement/base "+str(aReqColumnTechList[i])+" / "+str(aBaseTechList))

			#<PrereqOrBuildings> - require one building in list
			aRequirementTechLocList = []
			aReqColumnTechIDList = []
			aReqColumnTechList = []
			for iBuildingRequirement in xrange(CvBuildingInfo.getNumPrereqOrBuilding()):
				iPrereqBuilding = CvBuildingInfo.getPrereqOrBuilding(iBuildingRequirement)
				aRequirementTechLocList.append(self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[0])
				aRequirementTechIDList = self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[2]
				aRequirementTechList = self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[3]

				for i in xrange(len(aRequirementTechList)):
					if GC.getTechInfo(GC.getInfoTypeForString(aRequirementTechList[i])).getGridX() == iBaseTechLoc:
						aReqColumnTechIDList.append(aRequirementTechIDList[i])
				for i in xrange(len(aRequirementTechList)):
					if GC.getTechInfo(GC.getInfoTypeForString(aRequirementTechList[i])).getGridX() == iBaseTechLoc:
						aReqColumnTechList.append(aRequirementTechList[i])
			if len(aRequirementTechLocList) > 0 and min(aRequirementTechLocList) > iBaseTechLoc:
				self.log(CvBuildingInfo.getType()+" is unlocked before its earliest OR building requirements "+str(aRequirementTechList)+" "+str(aBaseTechList)+" requirement/base column "+str(min(aRequirementTechLocList))+" / "+str(iBaseTechLoc))
			if len(aRequirementTechLocList) > 0 and min(aRequirementTechLocList) == iBaseTechLoc:
				for i in xrange(len(aReqColumnTechIDList)):
					if aReqColumnTechIDList[i] not in aBaseTechIDList:
						self.log(CvBuildingInfo.getType()+" Earliest OR requirement unlocked by different tech in column: "+str(iBaseTechLoc)+" requirement/base "+str(aReqColumnTechList[i])+" / "+str(aBaseTechList))

			#<PrereqAmountBuildings> - require all buildings in empire in list
			aRequirementTechLocList = []
			aReqColumnTechIDList = []
			aReqColumnTechList = []
			for pair in CvBuildingInfo.getPrereqNumOfBuildings():
				iPrereqBuilding = pair.id
				aRequirementTechLocList.append(self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[0])
				aRequirementTechIDList = self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[2]
				aRequirementTechList = self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[3]

				for i in xrange(len(aRequirementTechList)):
					if GC.getTechInfo(GC.getInfoTypeForString(aRequirementTechList[i])).getGridX() == iBaseTechLoc:
						aReqColumnTechIDList.append(aRequirementTechIDList[i])
				for i in xrange(len(aRequirementTechList)):
					if GC.getTechInfo(GC.getInfoTypeForString(aRequirementTechList[i])).getGridX() == iBaseTechLoc:
						aReqColumnTechList.append(aRequirementTechList[i])
			if len(aRequirementTechLocList) > 0 and max(aRequirementTechLocList) > iBaseTechLoc:
				self.log(CvBuildingInfo.getType()+" is unlocked before its empire AND building requirements "+str(aRequirementTechList)+" "+str(aBaseTechList)+" requirement/base column "+str(max(aRequirementTechLocList))+" / "+str(iBaseTechLoc))
			if len(aRequirementTechLocList) > 0 and max(aRequirementTechLocList) == iBaseTechLoc:
				for i in xrange(len(aReqColumnTechIDList)):
					if aReqColumnTechIDList[i] not in aBaseTechIDList:
						self.log(CvBuildingInfo.getType()+" Empire AND requirement unlocked by different tech in column: "+str(iBaseTechLoc)+" requirement/base "+str(aReqColumnTechList[i])+" / "+str(aBaseTechList))

			#<ConstructCondition>
			aBuildingGOMReqList = []
			for i in range(2):
				aBuildingGOMReqList.append([])
			self.HF.getGOMReqs(CvBuildingInfo.getConstructCondition(), GOMTypes.GOM_BUILDING, aBuildingGOMReqList)

			#Analyze GOM AND Building reqs
			aRequirementTechLocList = []
			aReqColumnTechIDList = []
			aReqColumnTechList = []
			for iBuildingRequirement in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND])):
				iPrereqBuilding = aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND][iBuildingRequirement]
				aRequirementTechLocList.append(self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[0])
				aRequirementTechIDList = self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[2]
				aRequirementTechList = self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[3]

				for i in xrange(len(aRequirementTechList)):
					if GC.getTechInfo(GC.getInfoTypeForString(aRequirementTechList[i])).getGridX() == iBaseTechLoc:
						aReqColumnTechIDList.append(aRequirementTechIDList[i])
				for i in xrange(len(aRequirementTechList)):
					if GC.getTechInfo(GC.getInfoTypeForString(aRequirementTechList[i])).getGridX() == iBaseTechLoc:
						aReqColumnTechList.append(aRequirementTechList[i])
			if len(aRequirementTechLocList) > 0 and max(aRequirementTechLocList) > iBaseTechLoc:
				self.log(CvBuildingInfo.getType()+" is unlocked before its GOM AND building requirements "+str(aRequirementTechList)+" "+str(aBaseTechList)+" requirement/base column "+str(max(aRequirementTechLocList))+" / "+str(iBaseTechLoc))
			if len(aRequirementTechLocList) > 0 and max(aRequirementTechLocList) == iBaseTechLoc:
				for i in xrange(len(aReqColumnTechIDList)):
					if aReqColumnTechIDList[i] not in aBaseTechIDList:
						self.log(CvBuildingInfo.getType()+" GOM AND requirement unlocked by different tech in column: "+str(iBaseTechLoc)+" requirement/base "+str(aReqColumnTechList[i])+" / "+str(aBaseTechList))

			#Analyze GOM OR Building reqs
			aRequirementTechLocList = []
			aReqColumnTechIDList = []
			aReqColumnTechList = []
			for iBuildingRequirement in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR])):
				iPrereqBuilding = aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR][iBuildingRequirement]
				aRequirementTechLocList.append(self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[0])
				aRequirementTechIDList = self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[2]
				aRequirementTechList = self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(iPrereqBuilding))[3]

				for i in xrange(len(aRequirementTechList)):
					if GC.getTechInfo(GC.getInfoTypeForString(aRequirementTechList[i])).getGridX() == iBaseTechLoc:
						aReqColumnTechIDList.append(aRequirementTechIDList[i])
				for i in xrange(len(aRequirementTechList)):
					if GC.getTechInfo(GC.getInfoTypeForString(aRequirementTechList[i])).getGridX() == iBaseTechLoc:
						aReqColumnTechList.append(aRequirementTechList[i])
			if len(aRequirementTechLocList) > 0 and min(aRequirementTechLocList) > iBaseTechLoc:
				self.log(CvBuildingInfo.getType()+" is unlocked before its GOM OR building requirements "+str(aRequirementTechList)+" "+str(aBaseTechList)+" requirement/base column "+str(min(aRequirementTechLocList))+" / "+str(iBaseTechLoc))
			if len(aRequirementTechLocList) > 0 and min(aRequirementTechLocList) == iBaseTechLoc:
				for i in xrange(len(aReqColumnTechIDList)):
					if aReqColumnTechIDList[i] not in aBaseTechIDList:
						self.log(CvBuildingInfo.getType()+" GOM OR requirement unlocked by different tech in column: "+str(iBaseTechLoc)+" requirement/base "+str(aReqColumnTechList[i])+" / "+str(aBaseTechList))

	#Building replacements of requirements
	def checkBuildingRequirementReplacements(self):
		aSpecialReplacementsList = ["BUILDING_POLLUTION_BLACKENEDSKIES", "BUILDING_GAMBLING_BAN", "BUILDING_ALCOCHOL_PROHIBITION", "BUILDING_DRUG_PROHIBITION", "BUILDING_PROSTITUTION_BAN", "BUILDING_EMANCIPATION_PROCLAMATION_EFFECT"]
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			if CvBuildingInfo.getType().find("_STORIES", -8) == -1: #Ignore stories
				aBuildingRequirementList = []

				#<PrereqInCityBuildings> - require all buildings in list
				for iBuildingRequirement in xrange(CvBuildingInfo.getNumPrereqInCityBuildings()):
					iPrereqBuilding = CvBuildingInfo.getPrereqInCityBuilding(iBuildingRequirement)
					aBuildingRequirementList.append(iPrereqBuilding)

				#<PrereqOrBuildings> - require one building in list
				for iBuildingRequirement in xrange(CvBuildingInfo.getNumPrereqOrBuilding()):
					iPrereqBuilding = CvBuildingInfo.getPrereqOrBuilding(iBuildingRequirement)
					if iPrereqBuilding not in aBuildingRequirementList:
						aBuildingRequirementList.append(iPrereqBuilding)

				#<PrereqAmountBuildings> - require all buildings in empire in list
				for pair in CvBuildingInfo.getPrereqNumOfBuildings():
					iPrereqBuilding = pair.id
					if iPrereqBuilding not in aBuildingRequirementList:
						aBuildingRequirementList.append(iPrereqBuilding)

				#<ConstructCondition>
				aBuildingGOMReqList = []
				for i in range(2):
					aBuildingGOMReqList.append([])
				self.HF.getGOMReqs(CvBuildingInfo.getConstructCondition(), GOMTypes.GOM_BUILDING, aBuildingGOMReqList)

				#Analyze GOM AND Building reqs
				for iBuildingRequirement in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND])):
					iPrereqBuilding = aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND][iBuildingRequirement]
					if iPrereqBuilding not in aBuildingRequirementList:
						aBuildingRequirementList.append(iPrereqBuilding)

				#Analyze GOM OR Building reqs
				for iBuildingRequirement in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR])):
					iPrereqBuilding = aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR][iBuildingRequirement]
					if iPrereqBuilding not in aBuildingRequirementList:
						aBuildingRequirementList.append(iPrereqBuilding)

				#Generate list of buildings, that replace requirements
				aBuildingRequirementReplacementList = []
				for i in xrange(len(aBuildingRequirementList)):
					CvBuildingRequirementInfo = GC.getBuildingInfo(aBuildingRequirementList[i])
					for iBuildingReplacement in xrange(CvBuildingRequirementInfo.getNumReplacementBuilding()):
						iReplacementBuilding = CvBuildingRequirementInfo.getReplacementBuilding(iBuildingReplacement)
						if iReplacementBuilding not in aBuildingRequirementReplacementList:
							aBuildingRequirementReplacementList.append(iReplacementBuilding)

				#Generate list of buildings, that replace currently checked building
				aBuildingReplacementList = []
				for iBuildingReplacement in xrange(CvBuildingInfo.getNumReplacementBuilding()):
					iReplacementBuilding = CvBuildingInfo.getReplacementBuilding(iBuildingReplacement)
					if iReplacementBuilding not in aBuildingReplacementList:
						aBuildingReplacementList.append(iReplacementBuilding)

				#Generate list of buildings, that are replaced by currently checked building
				aBuildingReplacedList = []
				for iBuildingReplaced in xrange(CvBuildingInfo.getNumReplacedBuilding()):
					iReplacedBuilding = CvBuildingInfo.getReplacedBuilding(iBuildingReplaced)
					if iReplacedBuilding not in aBuildingReplacedList:
						aBuildingReplacedList.append(iReplacedBuilding)

				#Check if we have requirement, that is replacement of building
				for i in xrange(len(aBuildingRequirementList)):
					if aBuildingRequirementList[i] in aBuildingReplacementList:
						self.log(CvBuildingInfo.getType()+" is replaced by requirement: "+GC.getBuildingInfo(aBuildingRequirementList[i]).getType())

				#Check if we have requirement, that is replaced by building itself
				for i in xrange(len(aBuildingRequirementList)):
					if aBuildingRequirementList[i] in aBuildingReplacedList:
						self.log(CvBuildingInfo.getType()+" replaces requirement: "+GC.getBuildingInfo(aBuildingRequirementList[i]).getType())

	#Building obsoletion of requirements - requirements shouldn't obsolete before building itself
	def checkBuildingRequirementObsoletion(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			BuildingObsoleteTechLoc = self.HF.checkBuildingTechObsoletionLocation(CvBuildingInfo)[0]
			BuildingObsoleteTechID = self.HF.checkBuildingTechObsoletionLocation(CvBuildingInfo)[1]

			#<PrereqInCityBuildings> - require all buildings in list
			aBuildingRequirementObsoleteTechLocList = []
			aBuildingRequirementObsoleteTechIDList = []
			aBuildingRequirementNameList = []
			for iBuilding in xrange(CvBuildingInfo.getNumPrereqInCityBuildings()):
				iPrereqBuilding = CvBuildingInfo.getPrereqInCityBuilding(iBuilding)
				aBuildingRequirementObsoleteTechLocList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(iPrereqBuilding))[0])
				aBuildingRequirementObsoleteTechIDList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(iPrereqBuilding))[1])
				aBuildingRequirementNameList.append(GC.getBuildingInfo(iPrereqBuilding).getType())
			if len(aBuildingRequirementObsoleteTechLocList) > 0 and min(aBuildingRequirementObsoleteTechLocList) < BuildingObsoleteTechLoc:
				self.log(CvBuildingInfo.getType()+" has AND requirements obsolete before itself "+str(aBuildingRequirementNameList)+str(aBuildingRequirementObsoleteTechLocList)+" "+str(BuildingObsoleteTechLoc))
			if len(aBuildingRequirementObsoleteTechLocList) > 0 and min(aBuildingRequirementObsoleteTechLocList)-10 <= BuildingObsoleteTechLoc and min(aBuildingRequirementObsoleteTechLocList) < 999 and BuildingObsoleteTechID not in aBuildingRequirementObsoleteTechIDList:
				self.log(CvBuildingInfo.getType()+" has AND requirements obsolete fairly soon after base building - consider picking its obsoletion tech "+str(aBuildingRequirementNameList)+str(aBuildingRequirementObsoleteTechIDList)+" "+str(BuildingObsoleteTechID))

			#<PrereqOrBuildings> - require one building in list
			aBuildingRequirementObsoleteTechLocList = []
			aBuildingRequirementObsoleteTechIDList = []
			aBuildingRequirementNameList = []
			for iBuilding in xrange(CvBuildingInfo.getNumPrereqOrBuilding()):
				iPrereqBuilding = CvBuildingInfo.getPrereqOrBuilding(iBuilding)
				aBuildingRequirementObsoleteTechLocList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(iPrereqBuilding))[0])
				aBuildingRequirementObsoleteTechIDList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(iPrereqBuilding))[1])
				aBuildingRequirementNameList.append(GC.getBuildingInfo(iPrereqBuilding).getType())
			if len(aBuildingRequirementObsoleteTechLocList) > 0 and max(aBuildingRequirementObsoleteTechLocList) < BuildingObsoleteTechLoc:
				self.log(CvBuildingInfo.getType()+" has latest OR requirements obsolete before itself "+str(aBuildingRequirementNameList)+str(aBuildingRequirementObsoleteTechLocList)+" "+str(BuildingObsoleteTechLoc))
			if len(aBuildingRequirementObsoleteTechLocList) > 0 and max(aBuildingRequirementObsoleteTechLocList)-10 <= BuildingObsoleteTechLoc and max(aBuildingRequirementObsoleteTechLocList) < 999 and BuildingObsoleteTechID not in aBuildingRequirementObsoleteTechIDList:
				self.log(CvBuildingInfo.getType()+" has latest OR requirements obsolete fairly soon after base building - consider picking its obsoletion tech "+str(aBuildingRequirementNameList)+str(aBuildingRequirementObsoleteTechIDList)+" "+str(BuildingObsoleteTechID))

			#<PrereqAmountBuildings> - require all buildings in empire in list
			aBuildingRequirementObsoleteTechLocList = []
			aBuildingRequirementObsoleteTechIDList = []
			aBuildingRequirementNameList = []
			for pair in CvBuildingInfo.getPrereqNumOfBuildings():
				iPrereqBuilding = pair.id
				aBuildingRequirementObsoleteTechLocList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(iPrereqBuilding))[0])
				aBuildingRequirementObsoleteTechIDList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(iPrereqBuilding))[1])
				aBuildingRequirementNameList.append(GC.getBuildingInfo(iPrereqBuilding).getType())
			if len(aBuildingRequirementObsoleteTechLocList) > 0 and min(aBuildingRequirementObsoleteTechLocList) < BuildingObsoleteTechLoc:
				self.log(CvBuildingInfo.getType()+" has Empire AND requirements obsolete before itself "+str(aBuildingRequirementNameList)+str(aBuildingRequirementObsoleteTechLocList)+" "+str(BuildingObsoleteTechLoc))
			if len(aBuildingRequirementObsoleteTechLocList) > 0 and min(aBuildingRequirementObsoleteTechLocList)-10 <= BuildingObsoleteTechLoc and min(aBuildingRequirementObsoleteTechLocList) < 999 and BuildingObsoleteTechID not in aBuildingRequirementObsoleteTechIDList:
				self.log(CvBuildingInfo.getType()+" has Empire AND requirements obsolete fairly soon after base building - consider picking its obsoletion tech "+str(aBuildingRequirementNameList)+str(aBuildingRequirementObsoleteTechIDList)+" "+str(BuildingObsoleteTechID))

			#<ConstructCondition>
			aBuildingGOMReqList = []
			for i in range(2):
				aBuildingGOMReqList.append([])
			self.HF.getGOMReqs(CvBuildingInfo.getConstructCondition(), GOMTypes.GOM_BUILDING, aBuildingGOMReqList)

			#Analyze GOM AND Building reqs
			aBuildingRequirementObsoleteTechLocList = []
			aBuildingRequirementObsoleteTechIDList = []
			aBuildingRequirementNameList = []
			for iBuilding in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND])):
				iPrereqBuilding = aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND][iBuilding]
				aBuildingRequirementObsoleteTechLocList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(iPrereqBuilding))[0])
				aBuildingRequirementObsoleteTechIDList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(iPrereqBuilding))[1])
				aBuildingRequirementNameList.append(GC.getBuildingInfo(iPrereqBuilding).getType())
			if len(aBuildingRequirementObsoleteTechLocList) > 0 and min(aBuildingRequirementObsoleteTechLocList) < BuildingObsoleteTechLoc:
				self.log(CvBuildingInfo.getType()+" has GOM AND requirements obsolete before itself "+str(aBuildingRequirementNameList)+str(aBuildingRequirementObsoleteTechLocList)+" "+str(BuildingObsoleteTechLoc))
			if len(aBuildingRequirementObsoleteTechLocList) > 0 and min(aBuildingRequirementObsoleteTechLocList)-10 <= BuildingObsoleteTechLoc and min(aBuildingRequirementObsoleteTechLocList) < 999 and BuildingObsoleteTechID not in aBuildingRequirementObsoleteTechIDList:
				self.log(CvBuildingInfo.getType()+" has GOM AND requirements obsolete fairly soon after base building - consider picking its obsoletion tech "+str(aBuildingRequirementNameList)+str(aBuildingRequirementObsoleteTechIDList)+" "+str(BuildingObsoleteTechID))

			#Analyze GOM OR Building reqs
			aBuildingRequirementObsoleteTechLocList = []
			aBuildingRequirementObsoleteTechIDList = []
			aBuildingRequirementNameList = []
			for iBuilding in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR])):
				iPrereqBuilding = aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR][iBuilding]
				aBuildingRequirementObsoleteTechLocList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(iPrereqBuilding))[0])
				aBuildingRequirementObsoleteTechIDList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(iPrereqBuilding))[1])
				aBuildingRequirementNameList.append(GC.getBuildingInfo(iPrereqBuilding).getType())
			if len(aBuildingRequirementObsoleteTechLocList) > 0 and max(aBuildingRequirementObsoleteTechLocList) < BuildingObsoleteTechLoc:
				self.log(CvBuildingInfo.getType()+" has latest GOM OR requirement obsolete before itself "+str(aBuildingRequirementNameList)+str(aBuildingRequirementObsoleteTechLocList)+" "+str(BuildingObsoleteTechLoc))
			if len(aBuildingRequirementObsoleteTechLocList) > 0 and max(aBuildingRequirementObsoleteTechLocList)-10 <= BuildingObsoleteTechLoc and max(aBuildingRequirementObsoleteTechLocList) < 999 and BuildingObsoleteTechID not in aBuildingRequirementObsoleteTechIDList:
				self.log(CvBuildingInfo.getType()+" has latest GOM OR requirement obsolete fairly soon after base building - consider picking its obsoletion tech "+str(aBuildingRequirementNameList)+str(aBuildingRequirementObsoleteTechIDList)+" "+str(BuildingObsoleteTechID))

	#Buildings shouldn't obsolete too fast in relation of tech unlock
	def checkBuildingUnlockObsoletion(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			iTechLoc = self.HF.checkBuildingTechRequirements(CvBuildingInfo)[0]
			if CvBuildingInfo.getObsoleteTech() != -1:
				iObsoleteTechLoc = GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX()
				if iObsoleteTechLoc - iTechLoc <= 5:
					self.log(CvBuildingInfo.getType()+" Unlock: "+str(iTechLoc)+" Obsoletion: "+str(iObsoleteTechLoc)+" Difference: "+str(iObsoleteTechLoc - iTechLoc))

	#Building replacements shouldn't obsolete too fast for sanity of beeliners, replacements also shouldn't obsolete at earlier point compared to base
	def checkBuildingReplacementObsoletion(self):
		aSpecialReplacementsList = [GC.getInfoTypeForString("BUILDING_POLLUTION_BLACKENEDSKIES"), GC.getInfoTypeForString("BUILDING_GAMBLING_BAN"), GC.getInfoTypeForString("BUILDING_ALCOCHOL_PROHIBITION"), GC.getInfoTypeForString("BUILDING_DRUG_PROHIBITION"), GC.getInfoTypeForString("BUILDING_PROSTITUTION_BAN")]
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			iTechLoc = self.HF.checkBuildingTechRequirements(CvBuildingInfo)[0]
			iTechID = max(self.HF.checkBuildingTechRequirements(CvBuildingInfo)[2])
			iTechObsLoc = self.HF.checkBuildingTechObsoletionLocation(CvBuildingInfo)[0]
			iTechObsID = self.HF.checkBuildingTechObsoletionLocation(CvBuildingInfo)[1]

			#All replacements of base
			aBuildingReplacementList = []
			for iReplacement in xrange(CvBuildingInfo.getNumReplacementBuilding()):
				iBuildingReplacement = CvBuildingInfo.getReplacementBuilding(iReplacement)
				aBuildingReplacementList.append(iBuildingReplacement)

			#All replacements of replacements
			aBuildingReplacement2List = []
			aBuildingReplacement2NameList = []
			for i in xrange(len(aBuildingReplacementList)):
				CvBuildingReplacementInfo = GC.getBuildingInfo(aBuildingReplacementList[i])
				for iReplacement2 in xrange(CvBuildingReplacementInfo.getNumReplacementBuilding()):
					iBuildingReplacement2 = CvBuildingReplacementInfo.getReplacementBuilding(iReplacement2)
					if iBuildingReplacement2 not in aBuildingReplacement2List:
						aBuildingReplacement2List.append(iBuildingReplacement2)
						aBuildingReplacement2NameList.append(GC.getBuildingInfo(iBuildingReplacement2).getType())

			#Get replacements, that don't appear as replacements of replacements
			aImmediateReplacementList = []
			for i in xrange(len(aBuildingReplacementList)):
				if aBuildingReplacementList[i] not in aBuildingReplacement2List:
					CvBuildingReplacementInfo = GC.getBuildingInfo(aBuildingReplacementList[i])
					aImmediateReplacementList.append(aBuildingReplacementList[i])

			#There may be several immediate replacements
			if len(aImmediateReplacementList) > 0:
				for i in xrange(len(aImmediateReplacementList)):
					CvBuildingImmediateReplacementInfo = GC.getBuildingInfo(aImmediateReplacementList[i])
					iImmediateReplacementTechLoc = self.HF.checkBuildingTechRequirements(CvBuildingImmediateReplacementInfo)[0]
					iImmediateReplacementTechLocID = max(self.HF.checkBuildingTechRequirements(CvBuildingImmediateReplacementInfo)[2])
					iImmediateReplacementTechObs = self.HF.checkBuildingTechObsoletionLocation(CvBuildingImmediateReplacementInfo)[0]
					iImmediateReplacementTechObsID = self.HF.checkBuildingTechObsoletionLocation(CvBuildingImmediateReplacementInfo)[1]
					if aImmediateReplacementList[i] not in aSpecialReplacementsList and iBuilding != GC.getInfoTypeForString("BUILDING_HOMELESS"):
						if iTechLoc > iImmediateReplacementTechLoc and CvBuildingImmediateReplacementInfo.getType().find("_STORIES_EFFECT", -15) == -1: #Stories Effects are automatic
							self.log(CvBuildingInfo.getType()+" unlocks after unlock of "+CvBuildingImmediateReplacementInfo.getType()+" Base unlock/Replacement unlock "+str(iTechLoc)+"/"+str(iImmediateReplacementTechLoc))
						if iTechObsLoc > iImmediateReplacementTechObs:
							self.log(CvBuildingInfo.getType()+" obsoletes after obsoletion of "+CvBuildingImmediateReplacementInfo.getType()+" Base obsoletion/Replacement obsoletion "+str(iTechObsLoc)+"/"+str(iImmediateReplacementTechObs))
						if iImmediateReplacementTechLoc - iTechLoc < 2 and CvBuildingImmediateReplacementInfo.getProductionCost() > 0: #Ignore short time for all special replacements
							self.log(CvBuildingInfo.getType()+" is swiftly replaced by "+CvBuildingImmediateReplacementInfo.getType()+" Base unlock/Replacement unlock "+str(iTechLoc)+"/"+str(iImmediateReplacementTechLoc))

			#Get replacements of replacements
			for i in xrange(len(aImmediateReplacementList)):
				Cv2BuildingInfo = GC.getBuildingInfo(aImmediateReplacementList[i])
				iReplacementTechLoc = self.HF.checkBuildingTechRequirements(Cv2BuildingInfo)[0]

				#All replacements of replacements
				a2BuildingReplacementList = []
				for iReplacement in xrange(Cv2BuildingInfo.getNumReplacementBuilding()):
					iBuildingReplacement = Cv2BuildingInfo.getReplacementBuilding(iReplacement)
					a2BuildingReplacementList.append(iBuildingReplacement)

				#All third level replacements
				a2BuildingReplacement2List = []
				for i in xrange(len(a2BuildingReplacementList)):
					Cv2BuildingReplacementInfo = GC.getBuildingInfo(a2BuildingReplacementList[i])
					for iReplacement2 in xrange(Cv2BuildingReplacementInfo.getNumReplacementBuilding()):
						iBuildingReplacement2 = Cv2BuildingReplacementInfo.getReplacementBuilding(iReplacement2)
						if iBuildingReplacement2 not in a2BuildingReplacement2List:
							a2BuildingReplacement2List.append(iBuildingReplacement2)

				#Get replacements, that don't appear as third level replacements
				aImmediateReplacement2List = []
				for i in xrange(len(a2BuildingReplacementList)):
					if a2BuildingReplacementList[i] not in a2BuildingReplacement2List:
						Cv2BuildingReplacementInfo = GC.getBuildingInfo(a2BuildingReplacementList[i])
						aImmediateReplacement2List.append(a2BuildingReplacementList[i])

				if len(aImmediateReplacement2List) > 0:
					for i in xrange(len(aImmediateReplacement2List)):
						Cv2BuildingImmediateReplacementInfo = GC.getBuildingInfo(aImmediateReplacement2List[i])
						iReplacement2TechID = max(self.HF.checkBuildingTechRequirements(Cv2BuildingImmediateReplacementInfo)[2])
						if iTechObsID != iReplacement2TechID and aImmediateReplacement2List[i] not in aSpecialReplacementsList and iBuilding != GC.getInfoTypeForString("BUILDING_HOMELESS"):
							self.log(CvBuildingInfo.getType()+" -> "+Cv2BuildingImmediateReplacementInfo.getType()+" Base Obsoletion should happen on Second Replacement Unlock: "+self.HF.getTechName(iTechObsID)+"/"+self.HF.getTechName(iReplacement2TechID))

	#Building - Check if we don't have implicit replacements, also ensure that listed ones aren't unlocked before building
	def checkBuildingImplicitReplacements(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			iBaseTechLoc = self.HF.checkBuildingTechRequirements(CvBuildingInfo)[0]
			iBaseObsLoc = self.HF.checkBuildingTechObsoletionLocation(CvBuildingInfo)[0]

			#Replacements
			aReplacementBuildingList = []
			aReplacementBuildingTechLocList = []
			for i in xrange(CvBuildingInfo.getNumReplacementBuilding()):
				iReplacementBuilding = CvBuildingInfo.getReplacementBuilding(i)
				CvBuildingReplacementInfo = GC.getBuildingInfo(iReplacementBuilding)
				aReplacementBuildingList.append(iReplacementBuilding)
				iReplacementTechLoc = self.HF.checkBuildingTechRequirements(CvBuildingReplacementInfo)[0]
				iReplacementObsLoc = self.HF.checkBuildingTechObsoletionLocation(CvBuildingReplacementInfo)[0]
				if iBaseTechLoc == iReplacementTechLoc and CvBuildingReplacementInfo.getProductionCost() > 0: #Concurrent replacement is fine, if it can't be built normally
					self.log("WARNING: "+CvBuildingInfo.getType()+" is unlocked concurrently with "+CvBuildingReplacementInfo.getType()+" "+str(iBaseTechLoc)+"/"+str(iReplacementTechLoc))
				if iBaseObsLoc == iReplacementObsLoc and CvBuildingInfo.getProductionCost() > 0 and CvBuildingReplacementInfo.getProductionCost() > 0: #Concurrent obsoletion is fine, if it can't be built normally
					self.log("WARNING: "+CvBuildingInfo.getType()+" is obsoleted concurrently with "+CvBuildingReplacementInfo.getType()+" "+str(iBaseObsLoc)+"/"+str(iReplacementObsLoc))

			#Replacements of replacements
			aReplacement2BuildingList = []
			for i in xrange(len(aReplacementBuildingList)):
				CvBuildingReplacementInfo = GC.getBuildingInfo(aReplacementBuildingList[i])
				for j in xrange(CvBuildingReplacementInfo.getNumReplacementBuilding()):
					iReplacement2Building = CvBuildingReplacementInfo.getReplacementBuilding(j)
					aReplacement2BuildingList.append(iReplacement2Building)

			#Get building type names
			aReplacementBuildingTypeList = []
			for i in xrange(len(aReplacementBuildingList)):
				aReplacementBuildingTypeList.append(GC.getBuildingInfo(aReplacementBuildingList[i]).getType())
			aReplacement2BuildingTypeList = []
			for i in xrange(len(aReplacement2BuildingList)):
				aReplacement2BuildingTypeList.append(GC.getBuildingInfo(aReplacement2BuildingList[i]).getType())
			aImplicitReplacementList = []
			for i in xrange(len(aReplacement2BuildingTypeList)):
				if aReplacement2BuildingTypeList[i] not in aReplacementBuildingTypeList:
					aImplicitReplacementList.append(aReplacement2BuildingTypeList[i])
			aImplicitReplacementUniqueList = []
			for i in xrange(len(aImplicitReplacementList)):
				if aImplicitReplacementList[i] not in aImplicitReplacementUniqueList:
					aImplicitReplacementUniqueList.append(aImplicitReplacementList[i])

			#Building can't have replacements, that are implicit - that is unlisted replacements of replacements
			if len(aReplacementBuildingList) > 0 and len(aImplicitReplacementList) > 0:
				if CvBuildingInfo.getNumReplacedBuilding() == 0:
					self.log("BASE: "+CvBuildingInfo.getType()+" -> "+str(aReplacementBuildingTypeList)+" implicit: "+str(aImplicitReplacementUniqueList))
				else:
					self.log(CvBuildingInfo.getType()+" -> "+str(aReplacementBuildingTypeList)+" implicit: "+str(aImplicitReplacementUniqueList))

	#Building - check if replacing building has better yields, commerces, and other stats
	def checkBuildingReplacingQuality(self):
		aSpecialBuildingsList = [GC.getInfoTypeForString("BUILDING_POLLUTION_BLACKENEDSKIES"), GC.getInfoTypeForString("BUILDING_GAMBLING_BAN"), GC.getInfoTypeForString("BUILDING_ALCOCHOL_PROHIBITION"), GC.getInfoTypeForString("BUILDING_DRUG_PROHIBITION"), GC.getInfoTypeForString("BUILDING_PROSTITUTION_BAN")]
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			#Tech location would be good way to sort replacements, as later ones tend to replace more
			iTechID = max(self.HF.checkBuildingTechRequirements(CvBuildingInfo)[2])

			#Ignore Pollution, and Bans
			if iBuilding not in aSpecialBuildingsList and CvBuildingInfo.getNumReplacedBuilding() != 0:
				#Get list of replaced buildings
				aReplacedBuildings = []
				for i in xrange(CvBuildingInfo.getNumReplacedBuilding()):
					aReplacedBuildings.append(CvBuildingInfo.getReplacedBuilding(i))

				#All replaced buildings of replaced ones
				aBuildingReplaced2List = []
				for i in xrange(len(aReplacedBuildings)):
					CvBuildingReplacedInfo = GC.getBuildingInfo(aReplacedBuildings[i])
					for iReplaced2 in xrange(CvBuildingReplacedInfo.getNumReplacedBuilding()):
						iBuildingReplacd2 = CvBuildingReplacedInfo.getReplacedBuilding(iReplaced2)
						if iBuildingReplacd2 not in aBuildingReplaced2List:
							aBuildingReplaced2List.append(iBuildingReplacd2)

				#Get replacements, that don't appear as replaced of replaced.
				aImmediateReplacedList = []
				aImmediateReplacedNameList = []
				for i in xrange(len(aReplacedBuildings)):
					if aReplacedBuildings[i] not in aBuildingReplaced2List:
						CvBuildingReplacedInfo = GC.getBuildingInfo(aReplacedBuildings[i])
						aImmediateReplacedList.append(aReplacedBuildings[i])
						aImmediateReplacedNameList.append(GC.getBuildingInfo(aReplacedBuildings[i]).getType())

				#aTag = [BASE, REPLACED, FINAL]
				#BASE - values/arrays of building, that is currently checked
				#REPLACED - values/arrays of buildings, that got replaced by checked building
				#FINAL - sum of values/arrays of checked building and its replaced buildings
				BASE = 0
				REPLACED = 1
				FINAL = 2
				MAIN_ARRAY_SIZE = 3

				#===== 0D ENTRIES - INTEGERS ===========================================================================================================================#
				#<iTradeRoutes>, <iCoastalTradeRoutes>, <iGlobalTradeRoutes>, <iTradeRouteModifier>, <iForeignTradeRouteModifier>, <iHappiness>, <iHealth>, <iGreatPeopleRateChange>, <iGreatPeopleRateModifier>, <iFreeSpecialist>, <iAreaFreeSpecialist>, <iGlobalFreeSpecialist>, <iMaintenanceModifier>, <iHappinessPercentPerPopulation>, <iHealthPercentPerPopulation>, <iWarWearinessModifier>, <iGlobalWarWearinessModifier>, <iEnemyWarWearinessModifier>, <iAllCityDefense>, <iBombardDefense>, <iBuildingDefenseRecoverySpeedModifier>, <iCityDefenseRecoverySpeedModifier>, <iDefense>, <iEspionageDefense>, <iLocalDynamicDefense>, <iMinDefense>, <iNoEntryDefenseLevel>, <iRiverDefensePenalty>, <iExperience>, <iGlobalExperience>, <FreePromotion/2/3>, <iFoodKept> <iPopulationgrowthratepercentage> - base
				aTradeRoutes = [CvBuildingInfo.getTradeRoutes(), 0, 0]
				aCoastalTradeRoutes = [CvBuildingInfo.getCoastalTradeRoutes(), 0, 0]
				aGlobalTradeRoutes = [CvBuildingInfo.getGlobalTradeRoutes(), 0, 0]
				aTradeRouteModifier = [CvBuildingInfo.getTradeRouteModifier(), 0, 0]
				aForeignTradeRouteModifier = [CvBuildingInfo.getForeignTradeRouteModifier(), 0, 0]
				aHappiness = [CvBuildingInfo.getHappiness(), 0, 0]
				aHealth = [CvBuildingInfo.getHealth(), 0, 0]
				aGreatPeopleRateChange = [CvBuildingInfo.getGreatPeopleRateChange(), 0, 0]
				aGreatPeopleRateModifier = [CvBuildingInfo.getGreatPeopleRateModifier(), 0, 0]
				aFreeSpecialist = [CvBuildingInfo.getFreeSpecialist(), 0, 0]
				aAreaFreeSpecialist = [CvBuildingInfo.getAreaFreeSpecialist(), 0, 0]
				aGlobalFreeSpecialist = [CvBuildingInfo.getGlobalFreeSpecialist(), 0, 0]
				aMaintenanceModifier = [CvBuildingInfo.getMaintenanceModifier(), 0, 0]  #iMaintenanceModifier - lower value is better
				aHappinessPercentPerPopulation = [CvBuildingInfo.getHappinessPercentPerPopulation(), 0, 0]
				aHealthPercentPerPopulation = [CvBuildingInfo.getHealthPercentPerPopulation(), 0, 0]
				aWarWearinessModifier = [CvBuildingInfo.getWarWearinessModifier(), 0, 0]  #iWarWearinessModifier - lower value is better
				aGlobalWarWearinessModifier = [CvBuildingInfo.getGlobalWarWearinessModifier(), 0, 0]  #iGlobalWarWearinessModifier - lower value is better
				aEnemyWarWearinessModifier = [CvBuildingInfo.getEnemyWarWearinessModifier(), 0, 0]
				aAllCityDefense = [CvBuildingInfo.getAllCityDefenseModifier(), 0, 0]
				aBombardDefense = [CvBuildingInfo.getBombardDefenseModifier(), 0, 0]
				aBuildingDefenseRecoverySpeedModifier = [CvBuildingInfo.getBuildingDefenseRecoverySpeedModifier(), 0, 0]
				aCityDefenseRecoverySpeedModifier = [CvBuildingInfo.getCityDefenseRecoverySpeedModifier(), 0, 0]
				aDefense = [CvBuildingInfo.getDefenseModifier(), 0, 0]
				aEspionageDefense = [CvBuildingInfo.getEspionageDefenseModifier(), 0, 0]
				aLocalDynamicDefense = [CvBuildingInfo.getLocalDynamicDefense(), 0, 0]
				aMinDefense = [CvBuildingInfo.getMinDefense(), 0, 0]
				aNoEntryDefenseLevel = [CvBuildingInfo.getNoEntryDefenseLevel(), 0, 0]   #iNoEntryDefenseLevel - lower value is better
				aRiverDefensePenalty = [CvBuildingInfo.getRiverDefensePenalty(), 0, 0]
				aExperience = [CvBuildingInfo.getFreeExperience(), 0, 0]
				aGlobalExperience = [CvBuildingInfo.getGlobalFreeExperience(), 0, 0]
				aBaseFreePromotion = [CvBuildingInfo.getFreePromotion(), CvBuildingInfo.getFreePromotion_2(), CvBuildingInfo.getFreePromotion_3()]
				aFoodKept = [CvBuildingInfo.getFoodKept(), 0, 0]
				aPopulationgrowthratepercentage = [CvBuildingInfo.getPopulationgrowthratepercentage(), 0, 0]

				#Analyze replacements by tag
				for i in xrange(len(aImmediateReplacedList)):
					CvReplacedBuildingInfo = GC.getBuildingInfo(aImmediateReplacedList[i])
					#<iTradeRoutes>, <iCoastalTradeRoutes>, <iGlobalTradeRoutes>, <iTradeRouteModifier>, <iForeignTradeRouteModifier>, <iHappiness>, <iHealth>, <iGreatPeopleRateChange>, <iGreatPeopleRateModifier>, <iFreeSpecialist>, <iAreaFreeSpecialist>, <iGlobalFreeSpecialist>, <iMaintenanceModifier>, <iHappinessPercentPerPopulation>, <iHealthPercentPerPopulation>, <iWarWearinessModifier>, <iGlobalWarWearinessModifier>, <iEnemyWarWearinessModifier>, <iAllCityDefense>, <iBombardDefense>, <iBuildingDefenseRecoverySpeedModifier>, <iCityDefenseRecoverySpeedModifier>, <iDefense>, <iEspionageDefense>, <iLocalDynamicDefense>, <iMinDefense>, <iNoEntryDefenseLevel>, <iRiverDefensePenalty>, <iExperience>, <iGlobalExperience>, <FreePromotion/2/3>, <iFoodKept> <iPopulationgrowthratepercentage>
					aTradeRoutes[REPLACED] += CvReplacedBuildingInfo.getTradeRoutes()
					aCoastalTradeRoutes[REPLACED] += CvReplacedBuildingInfo.getCoastalTradeRoutes()
					aGlobalTradeRoutes[REPLACED] += CvReplacedBuildingInfo.getGlobalTradeRoutes()
					aTradeRouteModifier[REPLACED] += CvReplacedBuildingInfo.getTradeRouteModifier()
					aForeignTradeRouteModifier[REPLACED] += CvReplacedBuildingInfo.getForeignTradeRouteModifier()
					aHappiness[REPLACED] += CvReplacedBuildingInfo.getHappiness()
					aHealth[REPLACED] += CvReplacedBuildingInfo.getHealth()
					aGreatPeopleRateChange[REPLACED] += CvReplacedBuildingInfo.getGreatPeopleRateChange()
					if CvBuildingInfo.getGreatPeopleUnitType() != CvReplacedBuildingInfo.getGreatPeopleUnitType() and CvReplacedBuildingInfo.getGreatPeopleUnitType() != -1:
						self.log("WARNING: "+CvBuildingInfo.getType()+", "+CvReplacedBuildingInfo.getType()+" have different GPs, remove GPUnitType from both buildings, or unify entire replacement tree")
					aGreatPeopleRateModifier[REPLACED] += CvReplacedBuildingInfo.getGreatPeopleRateModifier()
					aFreeSpecialist[REPLACED] += CvReplacedBuildingInfo.getFreeSpecialist()
					aAreaFreeSpecialist[REPLACED] += CvReplacedBuildingInfo.getAreaFreeSpecialist()
					aGlobalFreeSpecialist[REPLACED] += CvReplacedBuildingInfo.getGlobalFreeSpecialist()
					aMaintenanceModifier[REPLACED] += CvReplacedBuildingInfo.getMaintenanceModifier() #iMaintenanceModifier - lower value is better
					aHappinessPercentPerPopulation[REPLACED] += CvReplacedBuildingInfo.getHappinessPercentPerPopulation()
					aHealthPercentPerPopulation[REPLACED] += CvReplacedBuildingInfo.getHealthPercentPerPopulation()
					aWarWearinessModifier[REPLACED] += CvReplacedBuildingInfo.getWarWearinessModifier() #iWarWearinessModifier - lower value is better
					aGlobalWarWearinessModifier[REPLACED] += CvReplacedBuildingInfo.getGlobalWarWearinessModifier() #iGlobalWarWearinessModifier - lower value is better
					aEnemyWarWearinessModifier[REPLACED] += CvReplacedBuildingInfo.getEnemyWarWearinessModifier()
					aAllCityDefense[REPLACED] += CvReplacedBuildingInfo.getAllCityDefenseModifier()
					aBombardDefense[REPLACED] += CvReplacedBuildingInfo.getBombardDefenseModifier()
					aBuildingDefenseRecoverySpeedModifier[REPLACED] += CvReplacedBuildingInfo.getBuildingDefenseRecoverySpeedModifier()
					aCityDefenseRecoverySpeedModifier[REPLACED] += CvReplacedBuildingInfo.getCityDefenseRecoverySpeedModifier()
					aDefense[REPLACED] += CvReplacedBuildingInfo.getDefenseModifier()
					aEspionageDefense[REPLACED] += CvReplacedBuildingInfo.getEspionageDefenseModifier()
					aLocalDynamicDefense[REPLACED] += CvReplacedBuildingInfo.getLocalDynamicDefense()
					aMinDefense[REPLACED] += CvReplacedBuildingInfo.getMinDefense()
					aNoEntryDefenseLevel[REPLACED] += CvReplacedBuildingInfo.getNoEntryDefenseLevel()  #iNoEntryDefenseLevel - lower value is better
					aRiverDefensePenalty[REPLACED] += CvReplacedBuildingInfo.getRiverDefensePenalty()
					aExperience[REPLACED] += CvReplacedBuildingInfo.getFreeExperience()
					aGlobalExperience[REPLACED] += CvReplacedBuildingInfo.getGlobalFreeExperience()
					aFreePromotion = [CvReplacedBuildingInfo.getFreePromotion(), CvReplacedBuildingInfo.getFreePromotion_2(), CvReplacedBuildingInfo.getFreePromotion_3()]
					for i in xrange(len(aBaseFreePromotion)):
						if aBaseFreePromotion[i] != aFreePromotion[i] and aFreePromotion[i] != -1:
							self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" base free promotion: "+str(aBaseFreePromotion[i])+" replaced free promotion: "+GC.getPromotionInfo(aFreePromotion[i]).getType()+" "+str(aImmediateReplacedNameList))
					aFoodKept[REPLACED] += CvReplacedBuildingInfo.getFoodKept()
					aPopulationgrowthratepercentage[REPLACED] += CvReplacedBuildingInfo.getPopulationgrowthratepercentage()

				#Keep already existing <iTradeRoutes>, <iCoastalTradeRoutes>, <iGlobalTradeRoutes>, <iTradeRouteModifier>, <iForeignTradeRouteModifier>, <iHappiness>, <iHealth>, <iGreatPeopleRateChange>, <iGreatPeopleRateModifier>, <iFreeSpecialist>, <iAreaFreeSpecialist>, <iGlobalFreeSpecialist>, <iMaintenanceModifier>, <iHappinessPercentPerPopulation>, <iHealthPercentPerPopulation>, <iWarWearinessModifier>, <iGlobalWarWearinessModifier>, <iEnemyWarWearinessModifier>, <iAllCityDefense>, <iBombardDefense>, <iBuildingDefenseRecoverySpeedModifier>, <iCityDefenseRecoverySpeedModifier>, <iDefense>, <iEspionageDefense>, <iLocalDynamicDefense>, <iMinDefense>, <iNoEntryDefenseLevel>, <iRiverDefensePenalty>, <iExperience>, <iGlobalExperience>, <FreePromotion/2/3>, <iFoodKept> <iPopulationgrowthratepercentage> in base
				aTradeRoutes[FINAL] = aTradeRoutes[BASE] + aTradeRoutes[REPLACED]
				aCoastalTradeRoutes[FINAL] = aCoastalTradeRoutes[BASE] + aCoastalTradeRoutes[REPLACED]
				aGlobalTradeRoutes[FINAL] = aGlobalTradeRoutes[BASE] + aGlobalTradeRoutes[REPLACED]
				aTradeRouteModifier[FINAL] = aTradeRouteModifier[BASE] + aTradeRouteModifier[REPLACED]
				aForeignTradeRouteModifier[FINAL] = aForeignTradeRouteModifier[BASE] + aForeignTradeRouteModifier[REPLACED]
				aHappiness[FINAL] = aHappiness[BASE] + aHappiness[REPLACED]
				aHealth[FINAL] = aHealth[BASE] + aHealth[REPLACED]
				aGreatPeopleRateChange[FINAL] = aGreatPeopleRateChange[BASE] + aGreatPeopleRateChange[REPLACED]
				aGreatPeopleRateModifier[FINAL] = aGreatPeopleRateModifier[BASE] + aGreatPeopleRateModifier[REPLACED]
				aFreeSpecialist[FINAL] = aFreeSpecialist[BASE] + aFreeSpecialist[REPLACED]
				aAreaFreeSpecialist[FINAL] = aAreaFreeSpecialist[BASE] + aAreaFreeSpecialist[REPLACED]
				aGlobalFreeSpecialist[FINAL] = aGlobalFreeSpecialist[BASE] + aGlobalFreeSpecialist[REPLACED]
				aMaintenanceModifier[FINAL] = aMaintenanceModifier[BASE] + aMaintenanceModifier[REPLACED] #iMaintenanceModifier - lower value is better
				aHappinessPercentPerPopulation[FINAL] = aHappinessPercentPerPopulation[BASE] + aHappinessPercentPerPopulation[REPLACED]
				aHealthPercentPerPopulation[FINAL] = aHealthPercentPerPopulation[BASE] + aHealthPercentPerPopulation[REPLACED]
				aWarWearinessModifier[FINAL] = aWarWearinessModifier[BASE] + aWarWearinessModifier[REPLACED] #iWarWearinessModifier - lower value is better
				aGlobalWarWearinessModifier[FINAL] = aGlobalWarWearinessModifier[BASE] + aGlobalWarWearinessModifier[REPLACED] #iGlobalWarWearinessModifier - lower value is better
				aEnemyWarWearinessModifier[FINAL] = aEnemyWarWearinessModifier[BASE] + aEnemyWarWearinessModifier[REPLACED]
				aAllCityDefense[FINAL] = aAllCityDefense[BASE] + aAllCityDefense[REPLACED]
				aBombardDefense[FINAL] = aBombardDefense[BASE] + aBombardDefense[REPLACED]
				aBuildingDefenseRecoverySpeedModifier[FINAL] = aBuildingDefenseRecoverySpeedModifier[BASE] + aBuildingDefenseRecoverySpeedModifier[REPLACED]
				aCityDefenseRecoverySpeedModifier[FINAL] = aCityDefenseRecoverySpeedModifier[BASE] + aCityDefenseRecoverySpeedModifier[REPLACED]
				aDefense[FINAL] = aDefense[BASE] + aDefense[REPLACED]
				aEspionageDefense[FINAL] = aEspionageDefense[BASE] + aEspionageDefense[REPLACED]
				aLocalDynamicDefense[FINAL] = aLocalDynamicDefense[BASE] + aLocalDynamicDefense[REPLACED]
				aMinDefense[FINAL] = aMinDefense[BASE] + aMinDefense[REPLACED]
				aNoEntryDefenseLevel[FINAL] = aNoEntryDefenseLevel[BASE] + aNoEntryDefenseLevel[REPLACED] #iNoEntryDefenseLevel - lower value is better
				aRiverDefensePenalty[FINAL] = aRiverDefensePenalty[BASE] + aRiverDefensePenalty[REPLACED]
				aExperience[FINAL] = aExperience[BASE] + aExperience[REPLACED]
				aGlobalExperience[FINAL] = aGlobalExperience[BASE] + aGlobalExperience[REPLACED]
				aFoodKept[FINAL] = aFoodKept[BASE] + aFoodKept[REPLACED]
				aPopulationgrowthratepercentage[FINAL] = aPopulationgrowthratepercentage[BASE] + aPopulationgrowthratepercentage[REPLACED]

				#Building shouldn't be worse than replaced one!
				if aTradeRoutes[BASE] < aTradeRoutes[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Trade Routes "+str(aTradeRoutes[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aCoastalTradeRoutes[BASE] < aCoastalTradeRoutes[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Coastal Trade Routes "+str(aCoastalTradeRoutes[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aGlobalTradeRoutes[BASE] < aGlobalTradeRoutes[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Global Trade Routes "+str(aGlobalTradeRoutes[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aTradeRouteModifier[BASE] < aTradeRouteModifier[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Trade Route Modifier "+str(aTradeRouteModifier[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aForeignTradeRouteModifier[BASE] < aForeignTradeRouteModifier[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Foreign Trade Route Modifier "+str(aForeignTradeRouteModifier[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aHappiness[BASE] < aHappiness[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Happiness "+str(aHappiness[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aHealth[BASE] < aHealth[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Health "+str(aHealth[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aGreatPeopleRateChange[BASE] < aGreatPeopleRateChange[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have GP Rate Change "+str(aGreatPeopleRateChange[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aGreatPeopleRateModifier[BASE] < aGreatPeopleRateModifier[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have GP Rate Modifier "+str(aGreatPeopleRateModifier[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aFreeSpecialist[BASE] < aFreeSpecialist[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Free Specialist "+str(aFreeSpecialist[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aAreaFreeSpecialist[BASE] < aAreaFreeSpecialist[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Area free Specialist "+str(aAreaFreeSpecialist[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aGlobalFreeSpecialist[BASE] < aGlobalFreeSpecialist[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Global free Specialist "+str(aGlobalFreeSpecialist[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aMaintenanceModifier[BASE] > aMaintenanceModifier[REPLACED]: #iMaintenanceModifier - lower value is better, as it increases cost of running city
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Maintaince Modifier "+str(aMaintenanceModifier[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aHappinessPercentPerPopulation[BASE] < aHappinessPercentPerPopulation[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Happiness per Pop "+str(aHappinessPercentPerPopulation[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aHealthPercentPerPopulation[BASE] < aHealthPercentPerPopulation[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Health per Pop "+str(aHealthPercentPerPopulation[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aWarWearinessModifier[BASE] > aWarWearinessModifier[REPLACED]: #iWarWearinessModifier - lower value is better, as it increases unhappiness from war
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have War Weariness "+str(aWarWearinessModifier[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aGlobalWarWearinessModifier[BASE] > aGlobalWarWearinessModifier[REPLACED]: #iGlobalWarWearinessModifier - lower value is better, as it increases unhappiness from war
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Global War Weariness "+str(aGlobalWarWearinessModifier[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aEnemyWarWearinessModifier[BASE] < aEnemyWarWearinessModifier[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Enemy War Weariness "+str(aEnemyWarWearinessModifier[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aAllCityDefense[BASE] < aAllCityDefense[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have All City Defense "+str(aAllCityDefense[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aBombardDefense[BASE] < aBombardDefense[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Bombard Defense "+str(aBombardDefense[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aBuildingDefenseRecoverySpeedModifier[BASE] < aBuildingDefenseRecoverySpeedModifier[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Building Defense Recovery Speed "+str(aBuildingDefenseRecoverySpeedModifier[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aCityDefenseRecoverySpeedModifier[BASE] < aCityDefenseRecoverySpeedModifier[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have City Defense Recovery Speed "+str(aCityDefenseRecoverySpeedModifier[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aDefense[BASE] < aDefense[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Defense "+str(aDefense[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aEspionageDefense[BASE] < aEspionageDefense[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Espionage Defense "+str(aEspionageDefense[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aLocalDynamicDefense[BASE] < aLocalDynamicDefense[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Local Dynamic Defense "+str(aLocalDynamicDefense[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aMinDefense[BASE] < aMinDefense[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Min Defense "+str(aMinDefense[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aNoEntryDefenseLevel[BASE] > aNoEntryDefenseLevel[REPLACED] and not (aNoEntryDefenseLevel[BASE] > 0 and aNoEntryDefenseLevel[REPLACED] == 0):  #iNoEntryDefenseLevel - lower value is better, as units have to dig trough to lower level of defense, value of 0 means no need to dig trough defense.
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have No Entry Defense Level "+str(aNoEntryDefenseLevel[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aRiverDefensePenalty[BASE] < aRiverDefensePenalty[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have River Defense Penalty "+str(aRiverDefensePenalty[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aExperience[BASE] < aExperience[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Free Experience "+str(aExperience[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aGlobalExperience[BASE] < aGlobalExperience[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Free global Experience "+str(aGlobalExperience[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aFoodKept[BASE] < aFoodKept[REPLACED]:
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Food Kept "+str(aFoodKept[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
				if aPopulationgrowthratepercentage[BASE] > aPopulationgrowthratepercentage[REPLACED]: #iPopulationgrowthratepercentage - lower value is better, as it decreases food needed for next pop
					self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have Population growth rate percentage "+str(aPopulationgrowthratepercentage[FINAL])+" replaced: "+str(aImmediateReplacedNameList))

				#===== 1D ENTRIES - ARRAYS, index of array is an infotype ENUM =================================================================#
				#<YieldChanges>, <YieldPerPopChanges>, <SeaPlotYieldChanges>, <RiverPlotYieldChanges>, <YieldModifiers>, <PowerYieldModifiers>, <AreaYieldModifiers>, <GlobalYieldModifiers> - base
				aYieldChangesList = [[0 for x in xrange(YieldTypes.NUM_YIELD_TYPES)] for y in xrange(MAIN_ARRAY_SIZE)]
				aYieldPerPopChangesList = [[0 for x in xrange(YieldTypes.NUM_YIELD_TYPES)] for y in xrange(MAIN_ARRAY_SIZE)]
				aSeaPlotYieldChangesList = [[0 for x in xrange(YieldTypes.NUM_YIELD_TYPES)] for y in xrange(MAIN_ARRAY_SIZE)]
				aRiverPlotYieldChangesList = [[0 for x in xrange(YieldTypes.NUM_YIELD_TYPES)] for y in xrange(MAIN_ARRAY_SIZE)]
				aYieldModifiersList = [[0 for x in xrange(YieldTypes.NUM_YIELD_TYPES)] for y in xrange(MAIN_ARRAY_SIZE)]
				aPowerYieldModifiersList = [[0 for x in xrange(YieldTypes.NUM_YIELD_TYPES)] for y in xrange(MAIN_ARRAY_SIZE)]
				aAreaYieldModifiersList = [[0 for x in xrange(YieldTypes.NUM_YIELD_TYPES)] for y in xrange(MAIN_ARRAY_SIZE)]
				aGlobalYieldModifiersList = [[0 for x in xrange(YieldTypes.NUM_YIELD_TYPES)] for y in xrange(MAIN_ARRAY_SIZE)]
				for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
					aYieldChangesList[BASE][iYield] += CvBuildingInfo.getYieldChange(iYield)
					aYieldPerPopChangesList[BASE][iYield] += CvBuildingInfo.getYieldPerPopChange(iYield)
					aSeaPlotYieldChangesList[BASE][iYield] += CvBuildingInfo.getSeaPlotYieldChange(iYield)
					aRiverPlotYieldChangesList[BASE][iYield] += CvBuildingInfo.getRiverPlotYieldChange(iYield)
					aYieldModifiersList[BASE][iYield] += CvBuildingInfo.getYieldModifier(iYield)
					aPowerYieldModifiersList[BASE][iYield] += CvBuildingInfo.getPowerYieldModifier(iYield)
					aAreaYieldModifiersList[BASE][iYield] += CvBuildingInfo.getAreaYieldModifier(iYield)
					aGlobalYieldModifiersList[BASE][iYield] += CvBuildingInfo.getGlobalYieldModifier(iYield)

				#Analyze replacements by tag
				for i in xrange(len(aImmediateReplacedList)):
					CvReplacedBuildingInfo = GC.getBuildingInfo(aImmediateReplacedList[i])
					#<YieldChanges>, <YieldPerPopChanges>, <SeaPlotYieldChanges>, <RiverPlotYieldChanges>, <YieldModifiers>, <PowerYieldModifiers>, <AreaYieldModifiers>, <GlobalYieldModifiers>
					for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
						aYieldChangesList[REPLACED][iYield] += CvReplacedBuildingInfo.getYieldChange(iYield)
						aYieldPerPopChangesList[REPLACED][iYield] += CvReplacedBuildingInfo.getYieldPerPopChange(iYield)
						aSeaPlotYieldChangesList[REPLACED][iYield] += CvReplacedBuildingInfo.getSeaPlotYieldChange(iYield)
						aRiverPlotYieldChangesList[REPLACED][iYield] += CvReplacedBuildingInfo.getRiverPlotYieldChange(iYield)
						aYieldModifiersList[REPLACED][iYield] += CvReplacedBuildingInfo.getYieldModifier(iYield)
						aPowerYieldModifiersList[REPLACED][iYield] += CvReplacedBuildingInfo.getPowerYieldModifier(iYield)
						aAreaYieldModifiersList[REPLACED][iYield] += CvReplacedBuildingInfo.getAreaYieldModifier(iYield)
						aGlobalYieldModifiersList[REPLACED][iYield] += CvReplacedBuildingInfo.getGlobalYieldModifier(iYield)

				#Keep already existing <YieldChanges>, <YieldPerPopChanges>, <SeaPlotYieldChanges>, <RiverPlotYieldChanges>, <YieldModifiers>, <PowerYieldModifiers>, <AreaYieldModifiers>, <GlobalYieldModifiers> in base
				for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
					aYieldChangesList[FINAL][iYield] = aYieldChangesList[BASE][iYield] + aYieldChangesList[REPLACED][iYield]
					aYieldPerPopChangesList[FINAL][iYield] = aYieldPerPopChangesList[BASE][iYield] + aYieldPerPopChangesList[REPLACED][iYield]
					aSeaPlotYieldChangesList[FINAL][iYield] = aSeaPlotYieldChangesList[BASE][iYield] + aSeaPlotYieldChangesList[REPLACED][iYield]
					aRiverPlotYieldChangesList[FINAL][iYield] = aRiverPlotYieldChangesList[BASE][iYield] + aRiverPlotYieldChangesList[REPLACED][iYield]
					aYieldModifiersList[FINAL][iYield] = aYieldModifiersList[BASE][iYield] + aYieldModifiersList[REPLACED][iYield]
					aPowerYieldModifiersList[FINAL][iYield] = aPowerYieldModifiersList[BASE][iYield] + aPowerYieldModifiersList[REPLACED][iYield]
					aAreaYieldModifiersList[FINAL][iYield] = aAreaYieldModifiersList[BASE][iYield] + aAreaYieldModifiersList[REPLACED][iYield]
					aGlobalYieldModifiersList[FINAL][iYield] = aGlobalYieldModifiersList[BASE][iYield] + aGlobalYieldModifiersList[REPLACED][iYield]

				#Building shouldn't be worse than replaced one!
				for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
					if aYieldChangesList[BASE][iYield] < aYieldChangesList[REPLACED][iYield]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have F/P/C Changes "+str(aYieldChangesList[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
					if aYieldPerPopChangesList[BASE][iYield] < aYieldPerPopChangesList[REPLACED][iYield]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have F/P/C Per pop Changes "+str(aYieldPerPopChangesList[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
					if aSeaPlotYieldChangesList[BASE][iYield] < aSeaPlotYieldChangesList[REPLACED][iYield]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have F/P/C Sea plot Yield Changes "+str(aSeaPlotYieldChangesList[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
					if aRiverPlotYieldChangesList[BASE][iYield] < aRiverPlotYieldChangesList[REPLACED][iYield]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have F/P/C River plot Yield Changes "+str(aRiverPlotYieldChangesList[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
					if aYieldModifiersList[BASE][iYield] < aYieldModifiersList[REPLACED][iYield]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have F/P/C Modifiers "+str(aYieldModifiersList[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
					if aPowerYieldModifiersList[BASE][iYield] < aPowerYieldModifiersList[REPLACED][iYield]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have F/P/C Power Modifiers "+str(aPowerYieldModifiersList[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
					if aAreaYieldModifiersList[BASE][iYield] < aAreaYieldModifiersList[REPLACED][iYield]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have F/P/C Area Modifiers "+str(aAreaYieldModifiersList[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
					if aGlobalYieldModifiersList[BASE][iYield] < aGlobalYieldModifiersList[REPLACED][iYield]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have F/P/C Global Modifiers "+str(aGlobalYieldModifiersList[FINAL])+" replaced: "+str(aImmediateReplacedNameList))

				#=================================================================================================
				#<CommerceChanges>, <CommercePerPopChanges>, <CommerceModifiers>, <GlobalCommerceModifiers> - base
				aCommerceChanges = [[0 for x in xrange(CommerceTypes.NUM_COMMERCE_TYPES)] for y in xrange(MAIN_ARRAY_SIZE)]
				aCommercePerPopChanges = [[0 for x in xrange(CommerceTypes.NUM_COMMERCE_TYPES)] for y in xrange(MAIN_ARRAY_SIZE)]
				aCommerceModifiers = [[0 for x in xrange(CommerceTypes.NUM_COMMERCE_TYPES)] for y in xrange(MAIN_ARRAY_SIZE)]
				aGlobalCommerceModifiers = [[0 for x in xrange(CommerceTypes.NUM_COMMERCE_TYPES)] for y in xrange(MAIN_ARRAY_SIZE)]
				for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
					aCommerceChanges[BASE][iCommerce] += CvBuildingInfo.getCommerceChange(iCommerce)
					aCommercePerPopChanges[BASE][iCommerce] += CvBuildingInfo.getCommercePerPopChange(iCommerce)
					aCommerceModifiers[BASE][iCommerce] += CvBuildingInfo.getCommerceModifier(iCommerce)
					aGlobalCommerceModifiers[BASE][iCommerce] += CvBuildingInfo.getGlobalCommerceModifier(iCommerce)

				#Analyze replacements by tag
				for i in xrange(len(aImmediateReplacedList)):
					CvReplacedBuildingInfo = GC.getBuildingInfo(aImmediateReplacedList[i])
					#<CommerceChanges>, <CommercePerPopChanges>, <CommerceModifiers>, <GlobalCommerceModifiers>
					for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
						aCommerceChanges[REPLACED][iCommerce] += CvReplacedBuildingInfo.getCommerceChange(iCommerce)
						aCommercePerPopChanges[REPLACED][iCommerce] += CvReplacedBuildingInfo.getCommercePerPopChange(iCommerce)
						aCommerceModifiers[REPLACED][iCommerce] += CvReplacedBuildingInfo.getCommerceModifier(iCommerce)
						aGlobalCommerceModifiers[REPLACED][iCommerce] += CvReplacedBuildingInfo.getGlobalCommerceModifier(iCommerce)

				#Keep already existing <CommerceChanges>, <CommercePerPopChanges>, <CommerceModifiers>, <GlobalCommerceModifiers> in base
				for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
					aCommerceChanges[FINAL][iCommerce] = aCommerceChanges[BASE][iCommerce] + aCommerceChanges[REPLACED][iCommerce]
					aCommercePerPopChanges[FINAL][iCommerce] = aCommercePerPopChanges[BASE][iCommerce] + aCommercePerPopChanges[REPLACED][iCommerce]
					aCommerceModifiers[FINAL][iCommerce] = aCommerceModifiers[BASE][iCommerce] + aCommerceModifiers[REPLACED][iCommerce]
					aGlobalCommerceModifiers[FINAL][iCommerce] = aGlobalCommerceModifiers[BASE][iCommerce] + aGlobalCommerceModifiers[REPLACED][iCommerce]

				#Building shouldn't be worse than replaced one!
				for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
					if aCommerceChanges[BASE][iCommerce] < aCommerceChanges[REPLACED][iCommerce]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have G/R/C/E Changes "+str(aCommerceChanges[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
					if aCommercePerPopChanges[BASE][iCommerce] < aCommercePerPopChanges[REPLACED][iCommerce]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have G/R/C/E Per pop Changes "+str(aCommercePerPopChanges[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
					if aCommerceModifiers[BASE][iCommerce] < aCommerceModifiers[REPLACED][iCommerce]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have G/R/C/E Modifiers "+str(aCommerceModifiers[FINAL])+" replaced: "+str(aImmediateReplacedNameList))
					if aGlobalCommerceModifiers[BASE][iCommerce] < aGlobalCommerceModifiers[REPLACED][iCommerce]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have G/R/C/E Global Modifiers "+str(aGlobalCommerceModifiers[FINAL])+" replaced: "+str(aImmediateReplacedNameList))

				#=================================================================================================
				#<SpecialistCounts>, <FreeSpecialistCounts> - base
				aSpecialistCounts = [[0 for x in xrange(GC.getNumSpecialistInfos())] for y in xrange(MAIN_ARRAY_SIZE)]
				aFreeSpecialistCounts = [[0 for x in xrange(GC.getNumSpecialistInfos())] for y in xrange(MAIN_ARRAY_SIZE)]
				for iSpecialist in xrange(GC.getNumSpecialistInfos()):
					aSpecialistCounts[BASE][iSpecialist] += CvBuildingInfo.getSpecialistCount(iSpecialist)
					aFreeSpecialistCounts[BASE][iSpecialist] += CvBuildingInfo.getFreeSpecialistCount(iSpecialist)

				#Analyze replacements by tag
				for i in xrange(len(aImmediateReplacedList)):
					CvReplacedBuildingInfo = GC.getBuildingInfo(aImmediateReplacedList[i])
					#<SpecialistCounts>, <FreeSpecialistCounts>
					for iSpecialist in xrange(GC.getNumSpecialistInfos()):
						aSpecialistCounts[REPLACED][iSpecialist] += CvReplacedBuildingInfo.getSpecialistCount(iSpecialist)
						aFreeSpecialistCounts[REPLACED][iSpecialist] += CvReplacedBuildingInfo.getFreeSpecialistCount(iSpecialist)

				#Keep already existing <SpecialistCounts>, <FreeSpecialistCounts> in base
				for iSpecialist in xrange(GC.getNumSpecialistInfos()):
					aSpecialistCounts[FINAL][iSpecialist] = aSpecialistCounts[BASE][iSpecialist] + aSpecialistCounts[REPLACED][iSpecialist]
					aFreeSpecialistCounts[FINAL][iSpecialist] = aFreeSpecialistCounts[BASE][iSpecialist] + aFreeSpecialistCounts[REPLACED][iSpecialist]

				#Building shouldn't be worse than replaced one!
				#Emancipation Proclamation removes worldview buildings, python is needed for it to actually erase all slave specialists
				for iSpecialist in xrange(GC.getNumSpecialistInfos()):
					if aSpecialistCounts[BASE][iSpecialist] < aSpecialistCounts[REPLACED][iSpecialist] and iBuilding != GC.getInfoTypeForString("BUILDING_EMANCIPATION_PROCLAMATION_EFFECT"):
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getSpecialistInfo(iSpecialist).getType()+" Specialists Count "+str(aSpecialistCounts[FINAL][iSpecialist])+" replaced: "+str(aImmediateReplacedNameList))
					if aFreeSpecialistCounts[BASE][iSpecialist] < aFreeSpecialistCounts[REPLACED][iSpecialist] and iBuilding != GC.getInfoTypeForString("BUILDING_EMANCIPATION_PROCLAMATION_EFFECT"):
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getSpecialistInfo(iSpecialist).getType()+" Free specialists Count "+str(aFreeSpecialistCounts[FINAL][iSpecialist])+" replaced: "+str(aImmediateReplacedNameList))

				#=================================================================================================
				#<ImprovementFreeSpecialists> - base
				aImprovementFreeSpecialists = [[0 for x in xrange(GC.getNumImprovementInfos())] for y in xrange(MAIN_ARRAY_SIZE)]
				for iImprovement in xrange(GC.getNumImprovementInfos()):
					aImprovementFreeSpecialists[BASE][iImprovement] += CvBuildingInfo.getImprovementFreeSpecialist(iImprovement)

				#Analyze replacements by tag
				for i in xrange(len(aImmediateReplacedList)):
					CvReplacedBuildingInfo = GC.getBuildingInfo(aImmediateReplacedList[i])
					#<ImprovementFreeSpecialists>
					for iImprovement in xrange(GC.getNumImprovementInfos()):
						aImprovementFreeSpecialists[REPLACED][iImprovement] += CvReplacedBuildingInfo.getImprovementFreeSpecialist(iImprovement)

				#Keep already existing <ImprovementFreeSpecialists> in base
				for iImprovement in xrange(GC.getNumImprovementInfos()):
					aImprovementFreeSpecialists[FINAL][iImprovement] = aImprovementFreeSpecialists[BASE][iImprovement] + aImprovementFreeSpecialists[REPLACED][iImprovement]

				#Building shouldn't be worse than replaced one!
				for iImprovement in xrange(GC.getNumImprovementInfos()):
					if aImprovementFreeSpecialists[BASE][iImprovement] < aImprovementFreeSpecialists[REPLACED][iImprovement]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getImprovementInfo(iImprovement).getType()+" Improvement free Specialist "+str(aImprovementFreeSpecialists[FINAL][iImprovement])+" replaced: "+str(aImmediateReplacedNameList))

				#=================================================================================================
				#<BonusHappinessChanges>, <BonusHealthChanges>, <FreeBonus>+<ExtraFreeBonuses> - base
				aBonusHappinessChanges = [[0 for x in xrange(GC.getNumBonusInfos())] for y in xrange(MAIN_ARRAY_SIZE)]
				aBonusHealthChanges = [[0 for x in xrange(GC.getNumBonusInfos())] for y in xrange(MAIN_ARRAY_SIZE)]
				aExtraFreeBonuses = [[0 for x in xrange(GC.getNumBonusInfos())] for y in xrange(MAIN_ARRAY_SIZE)]
				for pair in CvBuildingInfo.getBonusHappiness():
					aBonusHappinessChanges[BASE][pair.id] += pair.value
				for pair in CvBuildingInfo.getBonusHealth():
					aBonusHealthChanges[BASE][pair.id] += pair.value
				if CvBuildingInfo.getFreeBonus() != -1:
					aExtraFreeBonuses[BASE][CvBuildingInfo.getFreeBonus()] += CvBuildingInfo.getNumFreeBonuses()
				for iBonus in xrange(CvBuildingInfo.getNumExtraFreeBonuses()):
					aExtraFreeBonuses[BASE][CvBuildingInfo.getExtraFreeBonus(iBonus)] += CvBuildingInfo.getExtraFreeBonusNum(iBonus)

				#Analyze replacements by tag
				for i in xrange(len(aImmediateReplacedList)):
					CvReplacedBuildingInfo = GC.getBuildingInfo(aImmediateReplacedList[i])
					#<BonusHappinessChanges>, <BonusHealthChanges>, <FreeBonus>+<ExtraFreeBonuses>
					for pair in CvReplacedBuildingInfo.getBonusHappiness():
						aBonusHappinessChanges[REPLACED][pair.id] += pair.value
					for pair in CvReplacedBuildingInfo.getBonusHealth():
						aBonusHealthChanges[REPLACED][pair.id] += pair.value
					if CvReplacedBuildingInfo.getFreeBonus() != -1:
						aExtraFreeBonuses[REPLACED][CvReplacedBuildingInfo.getFreeBonus()] += CvReplacedBuildingInfo.getNumFreeBonuses()
					for iBonus in xrange(CvReplacedBuildingInfo.getNumExtraFreeBonuses()):
						aExtraFreeBonuses[REPLACED][CvReplacedBuildingInfo.getExtraFreeBonus(iBonus)] += CvReplacedBuildingInfo.getExtraFreeBonusNum(iBonus)

				#Keep already existing <BonusHappinessChanges>, <BonusHealthChanges>, <FreeBonus>+<ExtraFreeBonuses> in base
				for iBonus in xrange(GC.getNumBonusInfos()):
					aBonusHappinessChanges[FINAL][iBonus] = aBonusHappinessChanges[BASE][iBonus] + aBonusHappinessChanges[REPLACED][iBonus]
					aBonusHealthChanges[FINAL][iBonus] = aBonusHealthChanges[BASE][iBonus] + aBonusHealthChanges[REPLACED][iBonus]
					#aExtraFreeBonuses[FINAL][iBonus] = aExtraFreeBonuses[BASE][iBonus] + aExtraFreeBonuses[REPLACED][iBonus] Maybe when we have volumetric resources...

				#Building shouldn't be worse than replaced one!
				for iBonus in xrange(GC.getNumBonusInfos()):
					if aBonusHappinessChanges[BASE][iBonus] < aBonusHappinessChanges[REPLACED][iBonus]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getBonusInfo(iBonus).getType()+" Bonus happiness Changes "+str(aBonusHappinessChanges[FINAL][iBonus])+" replaced: "+str(aImmediateReplacedNameList))
					if aBonusHealthChanges[BASE][iBonus] < aBonusHealthChanges[REPLACED][iBonus]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getBonusInfo(iBonus).getType()+" Bonus health Changes "+str(aBonusHealthChanges[FINAL][iBonus])+" replaced: "+str(aImmediateReplacedNameList))
					if aExtraFreeBonuses[BASE][iBonus] == 0 and aExtraFreeBonuses[REPLACED][iBonus] > 0: #No volumetric bonues - just check presence of it
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should give "+GC.getBonusInfo(iBonus).getType()+" Bonus - replaced: "+str(aImmediateReplacedNameList))

				#=================================================================================================
				#<TechHappinessChanges>, <TechHealthChanges> - base
				aTechHappinessChanges = [[0 for x in xrange(GC.getNumTechInfos())] for y in xrange(MAIN_ARRAY_SIZE)]
				aTechHealthChanges = [[0 for x in xrange(GC.getNumTechInfos())] for y in xrange(MAIN_ARRAY_SIZE)]
				for pair in CvBuildingInfo.getTechHappinessChanges():
					aTechHappinessChanges[BASE][pair.id] += pair.value
				for pair in CvBuildingInfo.getTechHealthChanges():
					aTechHealthChanges[BASE][pair.id] += pair.value

				#Analyze replacements by tag
				for i in xrange(len(aImmediateReplacedList)):
					CvReplacedBuildingInfo = GC.getBuildingInfo(aImmediateReplacedList[i])
					#<TechHappinessChanges>, <TechHealthChanges>
					for pair in CvReplacedBuildingInfo.getTechHappinessChanges():
						aTechHappinessChanges[REPLACED][pair.id] += pair.value
					for pair in CvReplacedBuildingInfo.getTechHealthChanges():
						aTechHealthChanges[REPLACED][pair.id] += pair.value

				#Keep already existing <TechHappinessChanges>, <TechHealthChanges> in base
				for iTech in xrange(GC.getNumTechInfos()):
					aTechHappinessChanges[FINAL][iTech] = aTechHappinessChanges[BASE][iTech] + aTechHappinessChanges[REPLACED][iTech]
					aTechHealthChanges[FINAL][iTech] = aTechHealthChanges[BASE][iTech] + aTechHealthChanges[REPLACED][iTech]

				#Building shouldn't be worse than replaced one!
				for iTech in xrange(GC.getNumTechInfos()):
					if aTechHappinessChanges[BASE][iTech] < aTechHappinessChanges[REPLACED][iTech]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getTechInfo(iTech).getType()+" Tech happiness Changes "+str(aTechHappinessChanges[FINAL][iTech])+" replaced: "+str(aImmediateReplacedNameList))
					if aTechHealthChanges[BASE][iTech] < aTechHealthChanges[REPLACED][iTech]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getTechInfo(iTech).getType()+" Tech health Changes "+str(aTechHealthChanges[FINAL][iTech])+" replaced: "+str(aImmediateReplacedNameList))

				#=============================================================================================================================
				#<GlobalBuildingCostModifiers>, <GlobalBuildingProductionModifiers>, <BuildingHappinessChanges>, <BuildingProductionModifiers> - base
				aGlobalBuildingCostModifiers = [[0 for x in xrange(GC.getNumBuildingInfos())] for y in xrange(MAIN_ARRAY_SIZE)]
				aGlobalBuildingProductionModifiers = [[0 for x in xrange(GC.getNumBuildingInfos())] for y in xrange(MAIN_ARRAY_SIZE)]
				aBuildingHappinessChanges = [[0 for x in xrange(GC.getNumBuildingInfos())] for y in xrange(MAIN_ARRAY_SIZE)]
				aBuildingProductionModifiers = [[0 for x in xrange(GC.getNumBuildingInfos())] for y in xrange(MAIN_ARRAY_SIZE)]
				for pair in CvBuildingInfo.getGlobalBuildingCostModifiers():
					aGlobalBuildingCostModifiers[BASE][pair.id] += pair.value
				for pair in CvBuildingInfo.getGlobalBuildingProductionModifiers():
					aGlobalBuildingProductionModifiers[BASE][pair.id] += pair.value
				for pair in CvBuildingInfo.getBuildingHappinessChanges():
					aBuildingHappinessChanges[BASE][pair.id] += pair.value
				for pair in CvBuildingInfo.getBuildingProductionModifiers():
					aBuildingProductionModifiers[BASE][pair.id] += pair.value

				#Analyze replacements by tag
				for i in xrange(len(aImmediateReplacedList)):
					CvReplacedBuildingInfo = GC.getBuildingInfo(aImmediateReplacedList[i])
					#<GlobalBuildingCostModifiers>, <GlobalBuildingProductionModifiers>, <BuildingHappinessChanges>, <BuildingProductionModifiers>
					for pair in CvReplacedBuildingInfo.getGlobalBuildingCostModifiers():
						aGlobalBuildingCostModifiers[REPLACED][pair.id] += pair.value
					for pair in CvReplacedBuildingInfo.getGlobalBuildingProductionModifiers():
						aGlobalBuildingProductionModifiers[REPLACED][pair.id] += pair.value
					for pair in CvReplacedBuildingInfo.getBuildingHappinessChanges():
						aBuildingHappinessChanges[REPLACED][pair.id] += pair.value
					for pair in CvReplacedBuildingInfo.getBuildingProductionModifiers():
						aBuildingProductionModifiers[REPLACED][pair.id] += pair.value

				#Keep already existing <GlobalBuildingCostModifiers>, <GlobalBuildingProductionModifiers>, <BuildingHappinessChanges>, <BuildingProductionModifiers> in base
				for iAffectedBuildings in xrange(GC.getNumBuildingInfos()):
					aGlobalBuildingCostModifiers[FINAL][iAffectedBuildings] = aGlobalBuildingCostModifiers[BASE][iAffectedBuildings] + aGlobalBuildingCostModifiers[REPLACED][iAffectedBuildings]
					aGlobalBuildingProductionModifiers[FINAL][iAffectedBuildings] = aGlobalBuildingProductionModifiers[BASE][iAffectedBuildings] + aGlobalBuildingProductionModifiers[REPLACED][iAffectedBuildings]
					aBuildingHappinessChanges[FINAL][iAffectedBuildings] = aBuildingHappinessChanges[BASE][iAffectedBuildings] + aBuildingHappinessChanges[REPLACED][iAffectedBuildings]
					aBuildingProductionModifiers[FINAL][iAffectedBuildings] = aBuildingProductionModifiers[BASE][iAffectedBuildings] + aBuildingProductionModifiers[REPLACED][iAffectedBuildings]

				#Building shouldn't be worse than replaced one!
				for iAffectedBuildings in xrange(GC.getNumBuildingInfos()):
					if aGlobalBuildingCostModifiers[BASE][iAffectedBuildings] < aGlobalBuildingCostModifiers[REPLACED][iAffectedBuildings]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getBuildingInfo(iAffectedBuildings).getType()+" Global Building cost Modifiers "+str(aGlobalBuildingCostModifiers[FINAL][iAffectedBuildings])+" replaced: "+str(aImmediateReplacedNameList))
					if aGlobalBuildingProductionModifiers[BASE][iAffectedBuildings] < aGlobalBuildingProductionModifiers[REPLACED][iAffectedBuildings]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getBuildingInfo(iAffectedBuildings).getType()+" Global Building production Modifiers "+str(aGlobalBuildingProductionModifiers[FINAL][iAffectedBuildings])+" replaced: "+str(aImmediateReplacedNameList))
					if aBuildingHappinessChanges[BASE][iAffectedBuildings] < aBuildingHappinessChanges[REPLACED][iAffectedBuildings]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getBuildingInfo(iAffectedBuildings).getType()+" Building Happiness Changes "+str(aBuildingHappinessChanges[FINAL][iAffectedBuildings])+" replaced: "+str(aImmediateReplacedNameList))
					if aBuildingProductionModifiers[BASE][iAffectedBuildings] < aBuildingProductionModifiers[REPLACED][iAffectedBuildings]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getBuildingInfo(iAffectedBuildings).getType()+" Building production Modifiers "+str(aBuildingProductionModifiers[FINAL][iAffectedBuildings])+" replaced: "+str(aImmediateReplacedNameList))

				#=================================================================================================
				#<DomainFreeExperiences> - base
				aDomainFreeExperiences = [[0 for x in xrange(DomainTypes.NUM_DOMAIN_TYPES)] for y in xrange(MAIN_ARRAY_SIZE)]
				for iDomain in xrange(DomainTypes.NUM_DOMAIN_TYPES):
					aDomainFreeExperiences[BASE][iDomain] += CvBuildingInfo.getDomainFreeExperience(iDomain)

				#Analyze replacements by tag
				for i in xrange(len(aImmediateReplacedList)):
					CvReplacedBuildingInfo = GC.getBuildingInfo(aImmediateReplacedList[i])
					#<DomainFreeExperiences>
					for iDomain in xrange(DomainTypes.NUM_DOMAIN_TYPES):
						aDomainFreeExperiences[REPLACED][iDomain] += CvReplacedBuildingInfo.getDomainFreeExperience(iDomain)

				#Keep already existing <DomainFreeExperiences> in base
				for iDomain in xrange(DomainTypes.NUM_DOMAIN_TYPES):
					aDomainFreeExperiences[FINAL][iDomain] = aDomainFreeExperiences[BASE][iDomain] + aDomainFreeExperiences[REPLACED][iDomain]

				#Building shouldn't be worse than replaced one!
				for iDomain in xrange(DomainTypes.NUM_DOMAIN_TYPES):
					if aDomainFreeExperiences[BASE][iDomain] < aDomainFreeExperiences[REPLACED][iDomain]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getDomainInfo(iDomain).getType()+" Domain Free Experience "+str(aDomainFreeExperiences[FINAL][iDomain])+" replaced: "+str(aImmediateReplacedNameList))

				#=================================================================================================
				#<UnitCombatFreeExperiences> - base
				aUnitCombatFreeExperiences = [[0 for x in xrange(GC.getNumUnitCombatInfos())] for y in xrange(MAIN_ARRAY_SIZE)]
				for pair in CvBuildingInfo.getUnitCombatFreeExperience():
					aUnitCombatFreeExperiences[BASE][pair.id] += pair.value

				#Analyze replacements by tag
				for i in xrange(len(aImmediateReplacedList)):
					CvReplacedBuildingInfo = GC.getBuildingInfo(aImmediateReplacedList[i])
					#<UnitCombatFreeExperiences>
					for pair in CvReplacedBuildingInfo.getUnitCombatFreeExperience():
						aUnitCombatFreeExperiences[REPLACED][pair.id] += pair.value

				#Keep already existing <UnitCombatFreeExperiences> in base
				for iUnitCombat in xrange(GC.getNumUnitCombatInfos()):
					aUnitCombatFreeExperiences[FINAL][iUnitCombat] = aUnitCombatFreeExperiences[BASE][iUnitCombat] + aUnitCombatFreeExperiences[REPLACED][iUnitCombat]

				#Building shouldn't be worse than replaced one!
				for iUnitCombat in xrange(GC.getNumUnitCombatInfos()):
					if aUnitCombatFreeExperiences[BASE][iUnitCombat] < aUnitCombatFreeExperiences[REPLACED][iUnitCombat]:
						self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getUnitCombatInfo(iUnitCombat).getType()+" Unit Combat free Experience "+str(aUnitCombatFreeExperiences[FINAL][iUnitCombat])+" replaced: "+str(aImmediateReplacedNameList))

				#===== 2D ENTRIES - coupling between two infotypes, like yield changing in presence of bonus =====#
				#<BonusYieldChanges>, <VicinityBonusYieldChanges>, <BonusYieldModifiers>, <BonusCommercePercentChanges>, <BonusCommerceModifiers> - base
				aBonusYieldChanges = [[[0 for x in xrange(YieldTypes.NUM_YIELD_TYPES)] for y in xrange(GC.getNumBonusInfos())] for z in xrange(MAIN_ARRAY_SIZE)]
				aVicinityBonusYieldChanges = [[[0 for x in xrange(YieldTypes.NUM_YIELD_TYPES)] for y in xrange(GC.getNumBonusInfos())] for z in xrange(MAIN_ARRAY_SIZE)]
				aBonusYieldModifiers = [[[0 for x in xrange(YieldTypes.NUM_YIELD_TYPES)] for y in xrange(GC.getNumBonusInfos())] for z in xrange(MAIN_ARRAY_SIZE)]
				aBonusCommercePercentChanges = [[[0 for x in xrange(CommerceTypes.NUM_COMMERCE_TYPES)] for y in xrange(GC.getNumBonusInfos())] for z in xrange(MAIN_ARRAY_SIZE)]
				aBonusCommerceModifiers = [[[0 for x in xrange(CommerceTypes.NUM_COMMERCE_TYPES)] for y in xrange(GC.getNumBonusInfos())] for z in xrange(MAIN_ARRAY_SIZE)]

				if CvBuildingInfo.isAnyBonusYieldChanges():
					for iBonus in xrange(GC.getNumBonusInfos()):
						for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
							aBonusYieldChanges[BASE][iBonus][iYield] += CvBuildingInfo.getBonusYieldChanges(iBonus, iYield)
				if CvBuildingInfo.isAnyVicinityBonusYieldChanges():
					for iBonus in xrange(GC.getNumBonusInfos()):
						for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
							aVicinityBonusYieldChanges[BASE][iBonus][iYield] += CvBuildingInfo.getVicinityBonusYieldChanges(iBonus, iYield)
				if CvBuildingInfo.isAnyBonusYieldModifiers():
					for iBonus in xrange(GC.getNumBonusInfos()):
						for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
							aBonusYieldModifiers[BASE][iBonus][iYield] += CvBuildingInfo.getBonusYieldModifier(iBonus, iYield)
				if CvBuildingInfo.isAnyBonusCommercePercentChanges():
					for iBonus in xrange(GC.getNumBonusInfos()):
						for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
							aBonusCommercePercentChanges[BASE][iBonus][iCommerce] += CvBuildingInfo.getBonusCommercePercentChanges(iBonus, iCommerce)
				if CvBuildingInfo.isAnyBonusCommerceModifiers():
					for iBonus in xrange(GC.getNumBonusInfos()):
						for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
							aBonusCommerceModifiers[BASE][iBonus][iCommerce] += CvBuildingInfo.getBonusCommerceModifier(iBonus, iCommerce)

				#Analyze replacements by tag
				for i in xrange(len(aImmediateReplacedList)):
					CvReplacedBuildingInfo = GC.getBuildingInfo(aImmediateReplacedList[i])
					#<BonusYieldChanges>, <VicinityBonusYieldChanges>, <BonusYieldModifiers>, <BonusCommercePercentChanges>, <BonusCommerceModifiers>
					if CvReplacedBuildingInfo.isAnyBonusYieldChanges():
						for iBonus in xrange(GC.getNumBonusInfos()):
							for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
								aBonusYieldChanges[REPLACED][iBonus][iYield] += CvReplacedBuildingInfo.getBonusYieldChanges(iBonus, iYield)
					if CvReplacedBuildingInfo.isAnyVicinityBonusYieldChanges():
						for iBonus in xrange(GC.getNumBonusInfos()):
							for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
								aVicinityBonusYieldChanges[REPLACED][iBonus][iYield] += CvReplacedBuildingInfo.getVicinityBonusYieldChanges(iBonus, iYield)
					if CvReplacedBuildingInfo.isAnyBonusYieldModifiers():
						for iBonus in xrange(GC.getNumBonusInfos()):
							for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
								aBonusYieldModifiers[REPLACED][iBonus][iYield] += CvReplacedBuildingInfo.getBonusYieldModifier(iBonus, iYield)
					if CvReplacedBuildingInfo.isAnyBonusCommercePercentChanges():
						for iBonus in xrange(GC.getNumBonusInfos()):
							for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
								aBonusCommercePercentChanges[REPLACED][iBonus][iCommerce] += CvReplacedBuildingInfo.getBonusCommercePercentChanges(iBonus, iCommerce)
					if CvReplacedBuildingInfo.isAnyBonusCommerceModifiers():
						for iBonus in xrange(GC.getNumBonusInfos()):
							for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
								aBonusCommerceModifiers[REPLACED][iBonus][iCommerce] += CvReplacedBuildingInfo.getBonusCommerceModifier(iBonus, iCommerce)

				#Keep already existing <BonusYieldChanges>, <VicinityBonusYieldChanges>, <BonusYieldModifiers>, <BonusCommercePercentChanges>, <BonusCommerceModifiers> in base
				for iBonus in xrange(GC.getNumBonusInfos()):
					for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
						aBonusYieldChanges[FINAL][iBonus][iYield] = aBonusYieldChanges[BASE][iBonus][iYield] + aBonusYieldChanges[REPLACED][iBonus][iYield]
						aVicinityBonusYieldChanges[FINAL][iBonus][iYield] = aVicinityBonusYieldChanges[BASE][iBonus][iYield] + aVicinityBonusYieldChanges[REPLACED][iBonus][iYield]
						aBonusYieldModifiers[FINAL][iBonus][iYield] = aBonusYieldModifiers[BASE][iBonus][iYield] + aBonusYieldModifiers[REPLACED][iBonus][iYield]
					for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
						aBonusCommercePercentChanges[FINAL][iBonus][iCommerce] = aBonusCommercePercentChanges[BASE][iBonus][iCommerce] + aBonusCommercePercentChanges[REPLACED][iBonus][iCommerce]
						aBonusCommerceModifiers[FINAL][iBonus][iCommerce] = aBonusCommerceModifiers[BASE][iBonus][iCommerce] + aBonusCommerceModifiers[REPLACED][iBonus][iCommerce]

				#Building shouldn't be worse than replaced one!
				for iBonus in xrange(GC.getNumBonusInfos()):
					for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
						if aBonusYieldChanges[BASE][iBonus][iYield] < aBonusYieldChanges[REPLACED][iBonus][iYield]:
							self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getBonusInfo(iBonus).getType()+" Bonus Yield Changes "+str(aBonusYieldChanges[FINAL][iBonus])+" replaced: "+str(aImmediateReplacedNameList))
						if aVicinityBonusYieldChanges[BASE][iBonus][iYield] < aVicinityBonusYieldChanges[REPLACED][iBonus][iYield]:
							self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getBonusInfo(iBonus).getType()+" Bonus vicinity Yield Changes "+str(aVicinityBonusYieldChanges[FINAL][iBonus])+" replaced: "+str(aImmediateReplacedNameList))
						if aBonusYieldModifiers[BASE][iBonus][iYield] < aBonusYieldModifiers[REPLACED][iBonus][iYield]:
							self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getBonusInfo(iBonus).getType()+" Bonus Yield Modifiers "+str(aBonusYieldModifiers[FINAL][iBonus])+" replaced: "+str(aImmediateReplacedNameList))
					for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
						if aBonusCommercePercentChanges[BASE][iBonus][iCommerce] < aBonusCommercePercentChanges[REPLACED][iBonus][iCommerce]:
							self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getBonusInfo(iBonus).getType()+" Bonus Commerce percent Changes "+str(aBonusCommercePercentChanges[FINAL][iBonus])+" replaced: "+str(aImmediateReplacedNameList))
						if aBonusCommerceModifiers[BASE][iBonus][iCommerce] < aBonusCommerceModifiers[REPLACED][iBonus][iCommerce]:
							self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getBonusInfo(iBonus).getType()+" Bonus Commerce Modifiers "+str(aBonusCommerceModifiers[FINAL][iBonus])+" replaced: "+str(aImmediateReplacedNameList))

				#======================================================================================================================================
				#<TechCommerceChanges>, <TechYieldModifiers>, <TechCommerceChanges>, <TechCommerceModifiers>, <TechSpecialistChanges> - base
				aTechYieldChanges = [[[0 for x in xrange(YieldTypes.NUM_YIELD_TYPES)] for y in xrange(GC.getNumTechInfos())] for z in xrange(MAIN_ARRAY_SIZE)]
				aTechYieldModifiers = [[[0 for x in xrange(YieldTypes.NUM_YIELD_TYPES)] for y in xrange(GC.getNumTechInfos())] for z in xrange(MAIN_ARRAY_SIZE)]
				aTechCommerceChanges = [[[0 for x in xrange(CommerceTypes.NUM_COMMERCE_TYPES)] for y in xrange(GC.getNumTechInfos())] for z in xrange(MAIN_ARRAY_SIZE)]
				aTechCommerceModifiers = [[[0 for x in xrange(CommerceTypes.NUM_COMMERCE_TYPES)] for y in xrange(GC.getNumTechInfos())] for z in xrange(MAIN_ARRAY_SIZE)]
				aTechSpecialistChanges = [[[0 for x in xrange(GC.getNumSpecialistInfos())] for y in xrange(GC.getNumTechInfos())] for z in xrange(MAIN_ARRAY_SIZE)]

				if CvBuildingInfo.isAnyTechYieldChanges():
					for iTech in xrange(GC.getNumTechInfos()):
						for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
							aTechYieldChanges[BASE][iTech][iYield] += CvBuildingInfo.getTechYieldChange(iTech, iYield)
				if CvBuildingInfo.isAnyTechYieldModifiers():
					for iTech in xrange(GC.getNumTechInfos()):
						for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
							aTechYieldModifiers[BASE][iTech][iYield] += CvBuildingInfo.getTechYieldModifier(iTech, iYield)
				if CvBuildingInfo.isAnyTechCommerceChanges():
					for iTech in xrange(GC.getNumTechInfos()):
						for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
							aTechCommerceChanges[BASE][iTech][iCommerce] += CvBuildingInfo.getTechCommerceChange(iTech, iCommerce)
				if CvBuildingInfo.isAnyTechCommerceModifiers():
					for iTech in xrange(GC.getNumTechInfos()):
						for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
							aTechCommerceModifiers[BASE][iTech][iCommerce] += CvBuildingInfo.getTechCommerceModifier(iTech, iCommerce)
				if CvBuildingInfo.isAnyTechSpecialistChanges():
					for iTech in xrange(GC.getNumTechInfos()):
						for iSpecialist in xrange(GC.getNumSpecialistInfos()):
							aTechSpecialistChanges[BASE][iTech][iSpecialist] += CvBuildingInfo.getTechSpecialistChange(iTech, iSpecialist)

				#Analyze replacements by tag
				for i in xrange(len(aImmediateReplacedList)):
					CvReplacedBuildingInfo = GC.getBuildingInfo(aImmediateReplacedList[i])
					#<TechCommerceChanges>, <TechYieldModifiers>, <TechCommerceChanges>, <TechCommerceModifiers>, <TechSpecialistChanges>
					if CvReplacedBuildingInfo.isAnyTechYieldChanges():
						for iTech in xrange(GC.getNumTechInfos()):
							for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
								aTechYieldChanges[REPLACED][iTech][iYield] += CvReplacedBuildingInfo.getTechYieldChange(iTech, iYield)
					if CvReplacedBuildingInfo.isAnyTechYieldModifiers():
						for iTech in xrange(GC.getNumTechInfos()):
							for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
								aTechYieldModifiers[REPLACED][iTech][iYield] += CvReplacedBuildingInfo.getTechYieldModifier(iTech, iYield)
					if CvReplacedBuildingInfo.isAnyTechCommerceChanges():
						for iTech in xrange(GC.getNumTechInfos()):
							for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
								aTechCommerceChanges[REPLACED][iTech][iCommerce] += CvReplacedBuildingInfo.getTechCommerceChange(iTech, iCommerce)
					if CvReplacedBuildingInfo.isAnyTechCommerceModifiers():
						for iTech in xrange(GC.getNumTechInfos()):
							for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
								aTechCommerceModifiers[REPLACED][iTech][iCommerce] += CvReplacedBuildingInfo.getTechCommerceModifier(iTech, iCommerce)
					if CvReplacedBuildingInfo.isAnyTechSpecialistChanges():
						for iTech in xrange(GC.getNumTechInfos()):
							for iSpecialist in xrange(GC.getNumSpecialistInfos()):
								aTechSpecialistChanges[REPLACED][iTech][iSpecialist] += CvReplacedBuildingInfo.getTechSpecialistChange(iTech, iSpecialist)

				#Keep already existing <TechCommerceChanges>, <TechYieldModifiers>, <TechCommerceChanges>, <TechCommerceModifiers>, <TechSpecialistChanges> in base
				for iTech in xrange(GC.getNumTechInfos()):
					for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
						aTechYieldChanges[FINAL][iTech][iYield] = aTechYieldChanges[BASE][iTech][iYield] + aTechYieldChanges[REPLACED][iTech][iYield]
						aTechYieldModifiers[FINAL][iTech][iYield] = aTechYieldModifiers[BASE][iTech][iYield] + aTechYieldModifiers[REPLACED][iTech][iYield]
					for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
						aTechCommerceChanges[FINAL][iTech][iCommerce] = aTechCommerceChanges[BASE][iTech][iCommerce] + aTechCommerceChanges[REPLACED][iTech][iCommerce]
						aTechCommerceModifiers[FINAL][iTech][iCommerce] = aTechCommerceModifiers[BASE][iTech][iCommerce] + aTechCommerceModifiers[REPLACED][iTech][iCommerce]
					for iSpecialist in xrange(GC.getNumSpecialistInfos()):
						aTechSpecialistChanges[FINAL][iTech][iSpecialist] = aTechSpecialistChanges[BASE][iTech][iSpecialist] + aTechSpecialistChanges[REPLACED][iTech][iSpecialist]

				#Building shouldn't be worse than replaced one!
				for iTech in xrange(GC.getNumTechInfos()):
					for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
						if aTechYieldChanges[BASE][iTech][iYield] < aTechYieldChanges[REPLACED][iTech][iYield]:
							self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getTechInfo(iTech).getType()+" Tech Yield Changes "+str(aTechYieldChanges[FINAL][iTech])+" replaced: "+str(aImmediateReplacedNameList))
						if aTechYieldModifiers[BASE][iTech][iYield] < aTechYieldModifiers[REPLACED][iTech][iYield]:
							self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getTechInfo(iTech).getType()+" Tech Yield Modifiers "+str(aTechYieldModifiers[FINAL][iTech])+" replaced: "+str(aImmediateReplacedNameList))
					for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
						if aTechCommerceChanges[BASE][iTech][iCommerce] < aTechCommerceChanges[REPLACED][iTech][iCommerce]:
							self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getTechInfo(iTech).getType()+" Tech Commerce Changes "+str(aTechCommerceChanges[FINAL][iTech])+" replaced: "+str(aImmediateReplacedNameList))
						if aTechCommerceModifiers[BASE][iTech][iCommerce] < aTechCommerceModifiers[REPLACED][iTech][iCommerce]:
							self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getTechInfo(iTech).getType()+" Tech Commerce Modifiers "+str(aTechCommerceModifiers[FINAL][iTech])+" replaced: "+str(aImmediateReplacedNameList))
					for iSpecialist in xrange(GC.getNumSpecialistInfos()):
						if aTechSpecialistChanges[BASE][iTech][iSpecialist] < aTechSpecialistChanges[REPLACED][iTech][iSpecialist]:
							self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getTechInfo(iTech).getType()+" Tech Specialist Changes "+GC.getSpecialistInfo(iSpecialist).getType()+" replaced: "+str(aFinalTechSpecialistChanges))

				#==============================================================================================================
				#<GlobalBuildingExtraCommerces> - base
				aGlobalBuildingExtraCommerces = [[[0 for x in xrange(CommerceTypes.NUM_COMMERCE_TYPES)] for y in xrange(GC.getNumBuildingInfos())] for z in xrange(MAIN_ARRAY_SIZE)]
				for pBuildingCommerceChange in CvBuildingInfo.getGlobalBuildingCommerceChanges():
					iAffectedBuilding = pBuildingCommerceChange.eBuilding
					iCommerce = pBuildingCommerceChange.eCommerce
					aGlobalBuildingExtraCommerces[BASE][iAffectedBuilding][iCommerce] += pBuildingCommerceChange.value

				#Analyze replacements by tag
				for i in xrange(len(aImmediateReplacedList)):
					CvReplacedBuildingInfo = GC.getBuildingInfo(aImmediateReplacedList[i])
					#<GlobalBuildingExtraCommerces>
					for pBuildingCommerceChange in CvReplacedBuildingInfo.getGlobalBuildingCommerceChanges():
						iAffectedBuilding = pBuildingCommerceChange.eBuilding
						iCommerce = pBuildingCommerceChange.eCommerce
						aGlobalBuildingExtraCommerces[REPLACED][iAffectedBuilding][iCommerce] += pBuildingCommerceChange.value

				#Keep already existing <GlobalBuildingExtraCommerces> in base
				for iAffectedBuilding in xrange(GC.getNumBuildingInfos()):
					for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
						aGlobalBuildingExtraCommerces[FINAL][iAffectedBuilding][iCommerce] = aGlobalBuildingExtraCommerces[BASE][iAffectedBuilding][iCommerce] + aGlobalBuildingExtraCommerces[REPLACED][iAffectedBuilding][iCommerce]

				#Building shouldn't be worse than replaced one!
				for iAffectedBuilding in xrange(GC.getNumBuildingInfos()):
					for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
						if aGlobalBuildingExtraCommerces[BASE][iAffectedBuilding][iCommerce] < aGlobalBuildingExtraCommerces[REPLACED][iAffectedBuilding][iCommerce]:
							self.log(str(iTechID)+" "+CvBuildingInfo.getType()+" should have "+GC.getBuildingInfo(iAffectedBuilding).getType()+" Global Building extra Commerces "+str(aGlobalBuildingExtraCommerces[FINAL][iAffectedBuilding])+" replaced: "+str(aImmediateReplacedNameList))

	#Building - check if building replacements are present in tags affecting buildings
	def checkBuildingReplacingAvailability(self):
		aSpecialBuildingsList = [GC.getInfoTypeForString("BUILDING_POLLUTION_BLACKENEDSKIES"), GC.getInfoTypeForString("BUILDING_GAMBLING_BAN"), GC.getInfoTypeForString("BUILDING_ALCOCHOL_PROHIBITION"), GC.getInfoTypeForString("BUILDING_DRUG_PROHIBITION"), GC.getInfoTypeForString("BUILDING_PROSTITUTION_BAN")]
		#Buildings referencing buildings
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)

			#<GlobalBuildingExtraCommerces>
			for pBuildingCommerceChange in CvBuildingInfo.getGlobalBuildingCommerceChanges():
				iAffectedBuilding = pBuildingCommerceChange.eBuilding
				CvAffectedBuildingInfo = GC.getBuildingInfo(iAffectedBuilding)
				aReplacementBuildingsList = []
				if iAffectedBuilding not in aSpecialBuildingsList and CvAffectedBuildingInfo.getType().find("_STORIES_EFFECT", -15) == -1:
					for i in xrange(CvAffectedBuildingInfo.getNumReplacementBuilding()):
						if CvAffectedBuildingInfo.getReplacementBuilding(i) not in aSpecialBuildingsList: #Get Replacement buildings
							aReplacementBuildingsList.append(GC.getBuildingInfo(CvAffectedBuildingInfo.getReplacementBuilding(i)).getType())
				#If affected building replacement is listed, then remove it from buildings to be added
				for pBuildingCommerceChange in CvBuildingInfo.getGlobalBuildingCommerceChanges():
					iAffectedBuilding = pBuildingCommerceChange.eBuilding
					if GC.getBuildingInfo(iAffectedBuilding).getType() in aReplacementBuildingsList:
						aReplacementBuildingsList.remove(GC.getBuildingInfo(iAffectedBuilding).getType())
				if len(aReplacementBuildingsList) > 0:
					self.log(CvBuildingInfo.getType()+" GlobalBuildingExtraCommerces "+CvAffectedBuildingInfo.getType()+" -> "+str(aReplacementBuildingsList))

			#<GlobalBuildingCostModifiers>
			for pair in CvBuildingInfo.getGlobalBuildingCostModifiers():
				iAffectedBuilding = pair.id
				CvAffectedBuildingInfo = GC.getBuildingInfo(iAffectedBuilding)
				aReplacementBuildingsList = []
				if iAffectedBuilding not in aSpecialBuildingsList and CvAffectedBuildingInfo.getType().find("_STORIES_EFFECT", -15) == -1:
					for i in xrange(CvAffectedBuildingInfo.getNumReplacementBuilding()):
						if CvAffectedBuildingInfo.getReplacementBuilding(i) not in aSpecialBuildingsList: #Get Replacement buildings
							aReplacementBuildingsList.append(GC.getBuildingInfo(CvAffectedBuildingInfo.getReplacementBuilding(i)).getType())
				#If affected building replacement is listed, then remove it from buildings to be added
				for pair in CvBuildingInfo.getGlobalBuildingCostModifiers():
					iAffectedBuilding = pair.id
					if GC.getBuildingInfo(iAffectedBuilding).getType() in aReplacementBuildingsList:
						aReplacementBuildingsList.remove(GC.getBuildingInfo(iAffectedBuilding).getType())
				if len(aReplacementBuildingsList) > 0:
					self.log(CvBuildingInfo.getType()+" GlobalBuildingCostModifiers "+CvAffectedBuildingInfo.getType()+" -> "+str(aReplacementBuildingsList))

			#<GlobalBuildingProductionModifiers>
			for pair in CvBuildingInfo.getGlobalBuildingProductionModifiers():
				iAffectedBuilding = pair.id
				CvAffectedBuildingInfo = GC.getBuildingInfo(iAffectedBuilding)
				aReplacementBuildingsList = []
				if iAffectedBuilding not in aSpecialBuildingsList and CvAffectedBuildingInfo.getType().find("_STORIES_EFFECT", -15) == -1:
					for i in xrange(CvAffectedBuildingInfo.getNumReplacementBuilding()):
						if CvAffectedBuildingInfo.getReplacementBuilding(i) not in aSpecialBuildingsList: #Get Replacement buildings
							aReplacementBuildingsList.append(GC.getBuildingInfo(CvAffectedBuildingInfo.getReplacementBuilding(i)).getType())
				#If affected building replacement is listed, then remove it from buildings to be added
				for pair in CvBuildingInfo.getGlobalBuildingProductionModifiers():
					iAffectedBuilding = pair.id
					if GC.getBuildingInfo(iAffectedBuilding).getType() in aReplacementBuildingsList:
						aReplacementBuildingsList.remove(GC.getBuildingInfo(iAffectedBuilding).getType())
				if len(aReplacementBuildingsList) > 0:
					self.log(CvBuildingInfo.getType()+" GlobalBuildingProductionModifiers "+CvAffectedBuildingInfo.getType()+" -> "+str(aReplacementBuildingsList))

			#<BuildingHappinessChanges>
			for pair in CvBuildingInfo.getBuildingHappinessChanges():
				iAffectedBuilding = pair.id
				CvAffectedBuildingInfo = GC.getBuildingInfo(iAffectedBuilding)
				aReplacementBuildingsList = []
				if iAffectedBuilding not in aSpecialBuildingsList and CvAffectedBuildingInfo.getType().find("_STORIES_EFFECT", -15) == -1:
					for i in xrange(CvAffectedBuildingInfo.getNumReplacementBuilding()):
						if CvAffectedBuildingInfo.getReplacementBuilding(i) not in aSpecialBuildingsList: #Get Replacement buildings
							aReplacementBuildingsList.append(GC.getBuildingInfo(CvAffectedBuildingInfo.getReplacementBuilding(i)).getType())
				#If affected building replacement is listed, then remove it from buildings to be added
				for pair in CvBuildingInfo.getBuildingHappinessChanges():
					iAffectedBuilding = pair.id
					if GC.getBuildingInfo(iAffectedBuilding).getType() in aReplacementBuildingsList:
						aReplacementBuildingsList.remove(GC.getBuildingInfo(iAffectedBuilding).getType())
				if len(aReplacementBuildingsList) > 0:
					self.log(CvBuildingInfo.getType()+" BuildingHappinessChanges "+CvAffectedBuildingInfo.getType()+" -> "+str(aReplacementBuildingsList))

			#<BuildingProductionModifiers>
			for pair in CvBuildingInfo.getBuildingProductionModifiers():
				iAffectedBuilding = pair.id
				CvAffectedBuildingInfo = GC.getBuildingInfo(iAffectedBuilding)
				aReplacementBuildingsList = []
				if iAffectedBuilding not in aSpecialBuildingsList and CvAffectedBuildingInfo.getType().find("_STORIES_EFFECT", -15) == -1:
					for i in xrange(CvAffectedBuildingInfo.getNumReplacementBuilding()):
						if CvAffectedBuildingInfo.getReplacementBuilding(i) not in aSpecialBuildingsList: #Get Replacement buildings
							aReplacementBuildingsList.append(GC.getBuildingInfo(CvAffectedBuildingInfo.getReplacementBuilding(i)).getType())
				#If affected building replacement is listed, then remove it from buildings to be added
				for pair in CvBuildingInfo.getBuildingProductionModifiers():
					iAffectedBuilding = pair.id
					if GC.getBuildingInfo(iAffectedBuilding).getType() in aReplacementBuildingsList:
						aReplacementBuildingsList.remove(GC.getBuildingInfo(iAffectedBuilding).getType())
				if len(aReplacementBuildingsList) > 0:
					self.log(CvBuildingInfo.getType()+" BuildingProductionModifiers "+CvAffectedBuildingInfo.getType()+" -> "+str(aReplacementBuildingsList))

			#<ImprovementFreeSpecialists> - building references improvements, those potentially can upgrade
			aImprovementUnlistedUpgrades = []
			for iImprovement in xrange(GC.getNumImprovementInfos()):
				if CvBuildingInfo.getImprovementFreeSpecialist(iImprovement) != 0:
					CvImprovementInfo = GC.getImprovementInfo(iImprovement)
					if CvImprovementInfo.getImprovementUpgrade() != -1:
						aImprovementUnlistedUpgrades.append(GC.getImprovementInfo(CvImprovementInfo.getImprovementUpgrade()).getType())
					for iImprovementReplacement in xrange(CvImprovementInfo.getNumAlternativeImprovementUpgradeTypes()):
						if GC.getImprovementInfo(CvImprovementInfo.getAlternativeImprovementUpgradeType(iImprovementReplacement)).getType() not in aImprovementUnlistedUpgrades:
							aImprovementUnlistedUpgrades.append(GC.getImprovementInfo(CvImprovementInfo.getAlternativeImprovementUpgradeType(iImprovementReplacement)).getType())
			#If improvement is listed, then remove it
			for iImprovement in xrange(GC.getNumImprovementInfos()):
				if CvBuildingInfo.getImprovementFreeSpecialist(iImprovement) != 0 and GC.getImprovementInfo(iImprovement).getType() in aImprovementUnlistedUpgrades:
					aImprovementUnlistedUpgrades.remove(GC.getImprovementInfo(iImprovement).getType())
			if len(aImprovementUnlistedUpgrades) > 0:
				self.log(CvBuildingInfo.getType()+" should have improvement upgrades for ImprovementFreeSpecialists "+str(aImprovementUnlistedUpgrades))

			#<PrereqOrImprovement> - Improvement requirement replacement
			aImprovementUnlistedUpgrades = []
			for iImprovement in xrange(GC.getNumImprovementInfos()):
				if CvBuildingInfo.isPrereqOrImprovement(iImprovement):
					CvImprovementInfo = GC.getImprovementInfo(iImprovement)
					if CvImprovementInfo.getImprovementUpgrade() != -1:
						aImprovementUnlistedUpgrades.append(GC.getImprovementInfo(CvImprovementInfo.getImprovementUpgrade()).getType())
					for iImprovementReplacement in xrange(CvImprovementInfo.getNumAlternativeImprovementUpgradeTypes()):
						if GC.getImprovementInfo(CvImprovementInfo.getAlternativeImprovementUpgradeType(iImprovementReplacement)).getType() not in aImprovementUnlistedUpgrades:
							aImprovementUnlistedUpgrades.append(GC.getImprovementInfo(CvImprovementInfo.getAlternativeImprovementUpgradeType(iImprovementReplacement)).getType())
			#If improvement is listed, then remove it
			for iImprovement in xrange(GC.getNumImprovementInfos()):
				if CvBuildingInfo.isPrereqOrImprovement(iImprovement) and GC.getImprovementInfo(iImprovement).getType() in aImprovementUnlistedUpgrades:
					aImprovementUnlistedUpgrades.remove(GC.getImprovementInfo(iImprovement).getType())
			if len(aImprovementUnlistedUpgrades) > 0:
				self.log(CvBuildingInfo.getType()+" should have improvement upgrades for PrereqOrImprovement "+str(aImprovementUnlistedUpgrades))

		#Civics referencing buildings
		for iCivic in xrange(GC.getNumCivicInfos()):
			CvCivicInfo = GC.getCivicInfo(iCivic)

			#<BuildingHappinessChanges>
			aBuildingList = []
			if CvCivicInfo.isAnyBuildingHappinessChange():
				for iBuilding in xrange(GC.getNumBuildingInfos()):
					if CvCivicInfo.getBuildingHappinessChanges(iBuilding) != 0:
						aBuildingList.append(iBuilding)

			if len(aBuildingList) > 0:
				#Analyze list of Buildings
				aBuildingUpgrades = []
				for i in xrange(len(aBuildingList)):
					CvBuildingInfo = GC.getBuildingInfo(aBuildingList[i])
					for i in xrange(CvBuildingInfo.getNumReplacementBuilding()):
						aBuildingUpgrades.append(CvBuildingInfo.getReplacementBuilding(i))
				#We want nonrepeating list
				aBuildingUniqueUpgrades = []
				for i in xrange(len(aBuildingUpgrades)):
					if aBuildingUpgrades[i] not in aBuildingUniqueUpgrades:
						aBuildingUniqueUpgrades.append(aBuildingUpgrades[i])
				#If Building is listed, then remove it
				for i in xrange(len(aBuildingList)):
					if aBuildingList[i] in aBuildingUniqueUpgrades:
						aBuildingUniqueUpgrades.remove(aBuildingList[i])
				#Get names
				aBuildingsList = []
				for i in xrange(len(aBuildingUniqueUpgrades)):
					aBuildingsList.append(GC.getBuildingInfo(aBuildingUniqueUpgrades[i]).getType())
				if len(aBuildingsList) > 0:
					self.log(CvCivicInfo.getType()+" should have Building upgrades for BuildingHappinessChanges "+str(aBuildingsList))

			#<BuildingHealthChanges>
			aBuildingList = []
			if CvCivicInfo.isAnyBuildingHealthChange():
				for iBuilding in xrange(GC.getNumBuildingInfos()):
					if CvCivicInfo.getBuildingHealthChanges(iBuilding) != 0:
						aBuildingList.append(iBuilding)

			if len(aBuildingList) > 0:
				#Analyze list of Buildings
				aBuildingUpgrades = []
				for i in xrange(len(aBuildingList)):
					CvBuildingInfo = GC.getBuildingInfo(aBuildingList[i])
					for i in xrange(CvBuildingInfo.getNumReplacementBuilding()):
						aBuildingUpgrades.append(CvBuildingInfo.getReplacementBuilding(i))
				#We want nonrepeating list
				aBuildingUniqueUpgrades = []
				for i in xrange(len(aBuildingUpgrades)):
					if aBuildingUpgrades[i] not in aBuildingUniqueUpgrades:
						aBuildingUniqueUpgrades.append(aBuildingUpgrades[i])
				#If Building is listed, then remove it
				for i in xrange(len(aBuildingList)):
					if aBuildingList[i] in aBuildingUniqueUpgrades:
						aBuildingUniqueUpgrades.remove(aBuildingList[i])
				#Get names
				aBuildingsList = []
				for i in xrange(len(aBuildingUniqueUpgrades)):
					aBuildingsList.append(GC.getBuildingInfo(aBuildingUniqueUpgrades[i]).getType())
				if len(aBuildingsList) > 0:
					self.log(CvCivicInfo.getType()+" should have Building upgrades for BuildingHealthChanges "+str(aBuildingsList))

			#<BuildingProductionModifiers>
			aBuildingList = []
			for iBuilding in xrange(GC.getNumBuildingInfos()):
				if CvCivicInfo.getBuildingProductionModifier(iBuilding) != 0:
					aBuildingList.append(iBuilding)

			if len(aBuildingList) > 0:
				#Analyze list of Buildings
				aBuildingUpgrades = []
				for i in xrange(len(aBuildingList)):
					CvBuildingInfo = GC.getBuildingInfo(aBuildingList[i])
					for i in xrange(CvBuildingInfo.getNumReplacementBuilding()):
						aBuildingUpgrades.append(CvBuildingInfo.getReplacementBuilding(i))
				#We want nonrepeating list
				aBuildingUniqueUpgrades = []
				for i in xrange(len(aBuildingUpgrades)):
					if aBuildingUpgrades[i] not in aBuildingUniqueUpgrades:
						aBuildingUniqueUpgrades.append(aBuildingUpgrades[i])
				#If Building is listed, then remove it
				for i in xrange(len(aBuildingList)):
					if aBuildingList[i] in aBuildingUniqueUpgrades:
						aBuildingUniqueUpgrades.remove(aBuildingList[i])
				#Get names
				aBuildingsList = []
				for i in xrange(len(aBuildingUniqueUpgrades)):
					aBuildingsList.append(GC.getBuildingInfo(aBuildingUniqueUpgrades[i]).getType())
				if len(aBuildingsList) > 0:
					self.log(CvCivicInfo.getType()+" should have Building upgrades for BuildingProductionModifiers "+str(aBuildingsList))

			#<BuildingCommerceModifiers>
			aBuildingList = []
			for iBuilding in xrange(GC.getNumBuildingInfos()):
				for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
					if CvCivicInfo.getBuildingCommerceModifier(iBuilding, iCommerce) != 0:
						aBuildingList.append(iBuilding)

			if len(aBuildingList) > 0:
				#Analyze list of Buildings
				aBuildingUpgrades = []
				for i in xrange(len(aBuildingList)):
					CvBuildingInfo = GC.getBuildingInfo(aBuildingList[i])
					for i in xrange(CvBuildingInfo.getNumReplacementBuilding()):
						aBuildingUpgrades.append(CvBuildingInfo.getReplacementBuilding(i))
				#We want nonrepeating list
				aBuildingUniqueUpgrades = []
				for i in xrange(len(aBuildingUpgrades)):
					if aBuildingUpgrades[i] not in aBuildingUniqueUpgrades:
						aBuildingUniqueUpgrades.append(aBuildingUpgrades[i])
				#If Building is listed, then remove it
				for i in xrange(len(aBuildingList)):
					if aBuildingList[i] in aBuildingUniqueUpgrades:
						aBuildingUniqueUpgrades.remove(aBuildingList[i])
				#Get names
				aBuildingsList = []
				for i in xrange(len(aBuildingUniqueUpgrades)):
					aBuildingsList.append(GC.getBuildingInfo(aBuildingUniqueUpgrades[i]).getType())
				if len(aBuildingsList) > 0:
					self.log(CvCivicInfo.getType()+" should have Building upgrades for BuildingCommerceModifiers "+str(aBuildingsList))

		#Traits referencing buildings
		for iTrait in xrange(GC.getNumTraitInfos()):
			CvTraitInfo = GC.getTraitInfo(iTrait)

			#<BuildingProductionModifierTypes>
			aReplacementBuildingsList = []
			aUniqueReplacementBuildingsList = []
			for i in xrange(CvTraitInfo.getNumBuildingProductionModifiers()):
				iAffectedBuilding = CvTraitInfo.getBuildingProductionModifier(i).id
				CvAffectedBuildingInfo = GC.getBuildingInfo(iAffectedBuilding)
				if iAffectedBuilding not in aSpecialBuildingsList and CvAffectedBuildingInfo.getType().find("_STORIES_EFFECT", -15) == -1:
					for i in xrange(CvAffectedBuildingInfo.getNumReplacementBuilding()):
						if CvAffectedBuildingInfo.getReplacementBuilding(i) not in aSpecialBuildingsList: #Get Replacement buildings
							aReplacementBuildingsList.append(GC.getBuildingInfo(CvAffectedBuildingInfo.getReplacementBuilding(i)).getType())
				#If affected building replacement is listed, then remove it from buildings to be added
				for i in xrange(CvTraitInfo.getNumBuildingProductionModifiers()):
					iAffectedBuilding = CvTraitInfo.getBuildingProductionModifier(i).id
					if GC.getBuildingInfo(iAffectedBuilding).getType() in aReplacementBuildingsList:
						aReplacementBuildingsList.remove(GC.getBuildingInfo(iAffectedBuilding).getType())
			#Get unique unlisted replacements
			for i in xrange(len(aReplacementBuildingsList)):
				iBuilding = GC.getInfoTypeForString(aReplacementBuildingsList[i])
				if aReplacementBuildingsList[i] not in aUniqueReplacementBuildingsList and GC.getBuildingInfo(iBuilding).getProductionCost() > 0:
					aUniqueReplacementBuildingsList.append(aReplacementBuildingsList[i])
			if len(aUniqueReplacementBuildingsList) > 0:
				self.log(CvTraitInfo.getType()+" BuildingProductionModifierTypes "+str(aUniqueReplacementBuildingsList))

			#<BuildingHappinessModifierTypes>
			aReplacementBuildingsList = []
			aUniqueReplacementBuildingsList = []
			for i in xrange(CvTraitInfo.getNumBuildingHappinessModifiers()):
				iAffectedBuilding = CvTraitInfo.getBuildingHappinessModifier(i).id
				CvAffectedBuildingInfo = GC.getBuildingInfo(iAffectedBuilding)
				if iAffectedBuilding not in aSpecialBuildingsList and CvAffectedBuildingInfo.getType().find("_STORIES_EFFECT", -15) == -1:
					for i in xrange(CvAffectedBuildingInfo.getNumReplacementBuilding()):
						if CvAffectedBuildingInfo.getReplacementBuilding(i) not in aSpecialBuildingsList: #Get Replacement buildings
							aReplacementBuildingsList.append(GC.getBuildingInfo(CvAffectedBuildingInfo.getReplacementBuilding(i)).getType())
				#If affected building replacement is listed, then remove it from buildings to be added
				for i in xrange(CvTraitInfo.getNumBuildingHappinessModifiers()):
					iAffectedBuilding = CvTraitInfo.getBuildingHappinessModifier(i).id
					if GC.getBuildingInfo(iAffectedBuilding).getType() in aReplacementBuildingsList:
						aReplacementBuildingsList.remove(GC.getBuildingInfo(iAffectedBuilding).getType())
			#Get unique unlisted replacements
			for i in xrange(len(aReplacementBuildingsList)):
				if aReplacementBuildingsList[i] not in aUniqueReplacementBuildingsList:
					aUniqueReplacementBuildingsList.append(aReplacementBuildingsList[i])
			if len(aUniqueReplacementBuildingsList) > 0:
				self.log(CvTraitInfo.getType()+" BuildingHappinessModifierTypes "+str(aUniqueReplacementBuildingsList))

	#Building bonus requirements
	def checkBuildingBonusRequirements(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			iTechLoc = self.HF.checkBuildingTechRequirements(CvBuildingInfo)[0]
			#<Bonus>BONUS_X
			iBonus = CvBuildingInfo.getPrereqAndBonus()
			if iBonus != -1:
				bonusTechLoc = self.HF.checkBonusTechRequirementLocation(GC.getBonusInfo(iBonus))[2]
				if bonusTechLoc > iTechLoc:
					self.log(CvBuildingInfo.getType()+" - Singular AND bonus prereq late! "+str(bonusTechLoc)+" "+str(iTechLoc))

			#<VicinityBonus>BONUS_X
			iBonus = CvBuildingInfo.getPrereqVicinityBonus()
			if iBonus != -1:
				bonusTechLoc = self.HF.checkBonusTechRequirementLocation(GC.getBonusInfo(iBonus))[2]
				if bonusTechLoc > iTechLoc:
					self.log(CvBuildingInfo.getType()+" - Singular AND vicinity bonus prereq late! "+str(bonusTechLoc)+" "+str(iTechLoc))

			#<RawVicinityBonus>BONUS_X
			iBonus = CvBuildingInfo.getPrereqRawVicinityBonus()
			if iBonus != -1:
				bonusTechLoc = self.HF.checkBonusTechRequirementLocation(GC.getBonusInfo(iBonus))[0]
				if bonusTechLoc > iTechLoc:
					self.log(CvBuildingInfo.getType()+" - Singular AND raw vicinity bonus prereq late! "+str(bonusTechLoc)+" "+str(iTechLoc))

			#<PrereqBonuses>
			aBonusTechLocList = []
			for iBonus in CvBuildingInfo.getPrereqOrBonuses():
				aBonusTechLocList.append(self.HF.checkBonusTechRequirementLocation(GC.getBonusInfo(iBonus))[2])
			if len(aBonusTechLocList) > 0 and min(aBonusTechLocList) > iTechLoc:
				self.log(CvBuildingInfo.getType()+" - Earliest OR bonus prereq late! "+str(aBonusTechLocList)+" "+str(iTechLoc))

			#<PrereqVicinityBonuses>
			aBonusTechLocList = []
			for iBonus in CvBuildingInfo.getPrereqOrVicinityBonuses():
				aBonusTechLocList.append(self.HF.checkBonusTechRequirementLocation(GC.getBonusInfo(iBonus))[2])
			if len(aBonusTechLocList) > 0 and min(aBonusTechLocList) > iTechLoc:
				self.log(CvBuildingInfo.getType()+" - Earliest OR vicinity bonus prereq late! "+str(aBonusTechLocList)+" "+str(iTechLoc))

			#<PrereqRawVicinityBonuses>
			aBonusTechLocList = []
			for iBonus in CvBuildingInfo.getPrereqOrRawVicinityBonuses():
				aBonusTechLocList.append(self.HF.checkBonusTechRequirementLocation(GC.getBonusInfo(iBonus))[0])
			if len(aBonusTechLocList) > 0 and min(aBonusTechLocList) > iTechLoc:
				self.log(CvBuildingInfo.getType()+" - Earliest OR raw vicinity bonus prereq late! "+str(aBonusTechLocList)+" "+str(iTechLoc))

			#<ConstructCondition>
			aBonusGOMReqList = []
			for i in range(2):
				aBonusGOMReqList.append([])
			self.HF.getGOMReqs(CvBuildingInfo.getConstructCondition(), GOMTypes.GOM_BONUS, aBonusGOMReqList)

			#Analyze GOM AND Bonus reqs
			aBonusTechLocList = []
			for iBonus in xrange(len(aBonusGOMReqList[BoolExprTypes.BOOLEXPR_AND])):
				aBonusTechLocList.append(self.HF.checkBonusTechRequirementLocation(GC.getBonusInfo(aBonusGOMReqList[BoolExprTypes.BOOLEXPR_AND][iBonus]))[2])
			if len(aBonusTechLocList) > 0 and max(aBonusTechLocList) > iTechLoc:
				self.log(CvBuildingInfo.getType()+" - GOM AND bonus requirements are late! "+str(aBonusTechLocList)+" "+str(iTechLoc))

			#Analyze GOM OR Bonus reqs
			aBonusTechLocList = []
			for iBonus in xrange(len(aBonusGOMReqList[BoolExprTypes.BOOLEXPR_OR])):
				aBonusTechLocList.append(self.HF.checkBonusTechRequirementLocation(GC.getBonusInfo(aBonusGOMReqList[BoolExprTypes.BOOLEXPR_OR][iBonus]))[2])
			if len(aBonusTechLocList) > 0 and min(aBonusTechLocList) > iTechLoc:
				self.log(CvBuildingInfo.getType()+" - GOM OR bonus requirements are late! "+str(aBonusTechLocList)+" "+str(iTechLoc))

	#Building earliest manufacturer on resource tech reveal
	def checkBuildingBonusManufacturerTech(self):
		#Index of array - Bonus ID, array value at index - producers highest tech requirement location
		aBonusList = [-1]*GC.getNumBonusInfos()
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			iTechLoc = self.HF.checkBuildingTechRequirements(CvBuildingInfo)[0]

			#Singular <FreeBonus>
			iBonus = CvBuildingInfo.getFreeBonus()
			if iBonus != -1 and CvBuildingInfo.getType().find("_NATURAL_WONDER_") == -1 and iTechLoc != 0: #Natural wonder giving bonus is secondary effect - ignore natural wonders
				if aBonusList[iBonus] == -1:
					aBonusList[iBonus] = iTechLoc
				elif aBonusList[iBonus] != -1 and aBonusList[iBonus] > iTechLoc:
					aBonusList[iBonus] = iTechLoc

			#<ExtraFreeBonuses>
			if CvBuildingInfo.getType().find("_NATURAL_WONDER_") == -1 and iTechLoc != 0: #Ignore producers without tech requirements - those are subdued animal rewards most commonly
				for iBuildingProducer in xrange(CvBuildingInfo.getNumExtraFreeBonuses()):
					iBonus = CvBuildingInfo.getExtraFreeBonus(iBuildingProducer)
					if aBonusList[iBonus] == -1:
						aBonusList[iBonus] = iTechLoc
					elif aBonusList[iBonus] != -1 and aBonusList[iBonus] > iTechLoc:
						aBonusList[iBonus] = iTechLoc

		for iBonus in xrange(len(aBonusList)):
			iBonusTechLoc = self.HF.checkBonusTechRequirementLocation(GC.getBonusInfo(iBonus))[2]
			if aBonusList[iBonus] != -1 and GC.getBonusInfo(iBonus).getTechCityTrade() != -1 and not GC.getBonusInfo(iBonus).getConstAppearance() > 0:
				if aBonusList[iBonus] - iBonusTechLoc != 0:
					self.log(GC.getBonusInfo(iBonus).getType()+" "+str(iBonusTechLoc)+" Earliest bonus producer located at: "+str(aBonusList[iBonus]))

	#Building requirement extra requirements
	def checkBuildingRequirementTags(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			aBuildingRequirementList = []

			#<PrereqInCityBuildings> - require all buildings in list
			for iBuildingRequirement in xrange(CvBuildingInfo.getNumPrereqInCityBuildings()):
				iPrereqBuilding = CvBuildingInfo.getPrereqInCityBuilding(iBuildingRequirement)
				aBuildingRequirementList.append(iPrereqBuilding)

			aBuildingRequirementORList = []
			#<PrereqOrBuildings> - require one building in list
			for iBuildingRequirement in xrange(CvBuildingInfo.getNumPrereqOrBuilding()):
				iPrereqBuilding = CvBuildingInfo.getPrereqOrBuilding(iBuildingRequirement)
				if iPrereqBuilding not in aBuildingRequirementORList:
					aBuildingRequirementORList.append(iPrereqBuilding)

			#<PrereqAmountBuildings> - require all buildings in empire in list
			for pair in CvBuildingInfo.getPrereqNumOfBuildings():
				iPrereqBuilding = pair.id
				if iPrereqBuilding not in aBuildingRequirementList:
					aBuildingRequirementList.append(iPrereqBuilding)

			#<ConstructCondition>
			aBuildingGOMReqList = []
			for i in range(2):
				aBuildingGOMReqList.append([])
			self.HF.getGOMReqs(CvBuildingInfo.getConstructCondition(), GOMTypes.GOM_BUILDING, aBuildingGOMReqList)

			#Analyze GOM AND Building reqs
			for iBuildingRequirement in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND])):
				iPrereqBuilding = aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND][iBuildingRequirement]
				if iPrereqBuilding not in aBuildingRequirementList:
					aBuildingRequirementList.append(iPrereqBuilding)

			#Analyze GOM OR Building reqs
			aBuildingRequirementGOMORList = []
			for iBuildingRequirement in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR])):
				iPrereqBuilding = aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR][iBuildingRequirement]
				if iPrereqBuilding not in aBuildingRequirementGOMORList:
					aBuildingRequirementGOMORList.append(iPrereqBuilding)

			#Analyze tags
			for iRequirement in xrange(len(aBuildingRequirementList)):
				CvBuildingRequirement = GC.getBuildingInfo(aBuildingRequirementList[iRequirement])
				if CvBuildingInfo.getMinLatitude() < CvBuildingRequirement.getMinLatitude():
					self.log(CvBuildingInfo.getType()+" requires "+CvBuildingRequirement.getType()+", and can't be built below latitude of "+str(CvBuildingRequirement.getMinLatitude()))
				if CvBuildingInfo.getMaxLatitude() > CvBuildingRequirement.getMaxLatitude():
					self.log(CvBuildingInfo.getType()+" requires "+CvBuildingRequirement.getType()+", and can't be built above latitude of "+str(CvBuildingRequirement.getMaxLatitude()))
				if CvBuildingInfo.getMinAreaSize() < CvBuildingRequirement.getMinAreaSize():
					self.log(CvBuildingInfo.getType()+" requires "+CvBuildingRequirement.getType()+", and can't be built below area size "+str(CvBuildingRequirement.getMinAreaSize()))
				if CvBuildingInfo.getPrereqPopulation() < CvBuildingRequirement.getPrereqPopulation():
					self.log(CvBuildingInfo.getType()+" requires "+CvBuildingRequirement.getType()+", and can't be built below population "+str(CvBuildingRequirement.getPrereqPopulation()))
				if CvBuildingInfo.getNumCitiesPrereq() < CvBuildingRequirement.getNumCitiesPrereq():
					self.log(CvBuildingInfo.getType()+" requires "+CvBuildingRequirement.getType()+", and can't be built below amount of cities "+str(CvBuildingRequirement.getNumCitiesPrereq()))
				if CvBuildingInfo.getNumTeamsPrereq() < CvBuildingRequirement.getNumTeamsPrereq():
					self.log(CvBuildingInfo.getType()+" requires "+CvBuildingRequirement.getType()+", and can't be built below amount of teams "+str(CvBuildingRequirement.getNumTeamsPrereq()))
				if CvBuildingInfo.getUnitLevelPrereq() < CvBuildingRequirement.getUnitLevelPrereq():
					self.log(CvBuildingInfo.getType()+" requires "+CvBuildingRequirement.getType()+", and can't be built below unit level "+str(CvBuildingRequirement.getUnitLevelPrereq()))
				if not CvBuildingInfo.isWater() and CvBuildingRequirement.isWater():
					self.log(CvBuildingInfo.getType()+" requires "+CvBuildingRequirement.getType()+", and can't be built because of coastal requirement")
				if not CvBuildingInfo.isRiver() and CvBuildingRequirement.isRiver():
					self.log(CvBuildingInfo.getType()+" requires "+CvBuildingRequirement.getType()+", and can't be built because of river requirement")
				if not CvBuildingInfo.isFreshWater() and CvBuildingRequirement.isFreshWater():
					self.log(CvBuildingInfo.getType()+" requires "+CvBuildingRequirement.getType()+", and can't be built because of fresh water requirement")
				if not CvBuildingInfo.isPrereqPower() and CvBuildingRequirement.isPrereqPower():
					self.log(CvBuildingInfo.getType()+" requires "+CvBuildingRequirement.getType()+", and can't be built because of electricity requirement")

			#Independently check OR and GOM OR requirements
			aBuildingList = []
			aORMinLatitude = []
			aORMaxLatitude = []
			aORMinAreaSize = []
			aORPrereqPopulation = []
			aORNumCitiesPrereq = []
			aORNumTeamsPrereq = []
			aORUnitLevelPrereq = []
			aORisWater = []
			aORisRiver = []
			aORisFreshWater = []
			aORisPrereqPower = []
			for iRequirement in xrange(len(aBuildingRequirementORList)):
				CvBuildingRequirement = GC.getBuildingInfo(aBuildingRequirementORList[iRequirement])
				aBuildingList.append(CvBuildingRequirement.getType())
				aORMinLatitude.append(CvBuildingRequirement.getMinLatitude())
				aORMaxLatitude.append(CvBuildingRequirement.getMaxLatitude())
				aORMinAreaSize.append(CvBuildingRequirement.getMinAreaSize())
				aORPrereqPopulation.append(CvBuildingRequirement.getPrereqPopulation())
				aORNumCitiesPrereq.append(CvBuildingRequirement.getNumCitiesPrereq())
				aORNumTeamsPrereq.append(CvBuildingRequirement.getNumTeamsPrereq())
				aORUnitLevelPrereq.append(CvBuildingRequirement.getUnitLevelPrereq())
				aORisWater.append(CvBuildingRequirement.isWater())
				aORisRiver.append(CvBuildingRequirement.isRiver())
				aORisFreshWater.append(CvBuildingRequirement.isFreshWater())
				aORisPrereqPower.append(CvBuildingRequirement.isPrereqPower())
			if len(aBuildingList) > 0 and CvBuildingInfo.getMinLatitude() < min(aORMinLatitude):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORMinLatitude.index(min(aORMinLatitude))]+", and can't be built below latitude of "+str(min(aORMinLatitude)))
			if len(aBuildingList) > 0 and CvBuildingInfo.getMaxLatitude() > max(aORMaxLatitude):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORMaxLatitude.index(max(aORMaxLatitude))]+", and can't be built above latitude of "+str(max(aORMaxLatitude)))
			if len(aBuildingList) > 0 and CvBuildingInfo.getMinAreaSize() < min(aORMinAreaSize):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORMinAreaSize.index(min(aORMinAreaSize))]+", and can't be built below area size "+str(min(aORMinAreaSize)))
			if len(aBuildingList) > 0 and CvBuildingInfo.getPrereqPopulation() < min(aORPrereqPopulation):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORPrereqPopulation.index(min(aORPrereqPopulation))]+", and can't be built below population "+str(min(aORPrereqPopulation)))
			if len(aBuildingList) > 0 and CvBuildingInfo.getNumCitiesPrereq() < min(aORNumCitiesPrereq):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORNumCitiesPrereq.index(min(aORNumCitiesPrereq))]+", and can't be built below amount of cities "+str(min(aORNumCitiesPrereq)))
			if len(aBuildingList) > 0 and CvBuildingInfo.getNumTeamsPrereq() < min(aORNumTeamsPrereq):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORNumTeamsPrereq.index(min(aORNumTeamsPrereq))]+", and can't be built below amount of teams "+str(min(aORNumTeamsPrereq)))
			if len(aBuildingList) > 0 and CvBuildingInfo.getUnitLevelPrereq() < min(aORUnitLevelPrereq):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORUnitLevelPrereq.index(min(aORUnitLevelPrereq))]+", and can't be built below unit level "+str(min(aORUnitLevelPrereq)))
			if len(aBuildingList) > 0 and CvBuildingInfo.isWater() < min(aORisWater):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORisWater.index(min(aORisWater))]+", and can't be built because of coastal requirement")
			if len(aBuildingList) > 0 and CvBuildingInfo.isRiver() < min(aORisRiver):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORisRiver.index(min(aORisRiver))]+", and can't be built because of river requirement")
			if len(aBuildingList) > 0 and CvBuildingInfo.isFreshWater() < min(aORisFreshWater):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORisFreshWater.index(min(aORisFreshWater))]+", and can't be built because of fresh water requirement")
			if len(aBuildingList) > 0 and CvBuildingInfo.isPrereqPower() < min(aORisPrereqPower):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORisPrereqPower.index(min(aORisPrereqPower))]+", and can't be built because of electricity requirement")

			aBuildingList = []
			aORMinLatitude = []
			aORMaxLatitude = []
			aORMinAreaSize = []
			aORPrereqPopulation = []
			aORNumCitiesPrereq = []
			aORNumTeamsPrereq = []
			aORUnitLevelPrereq = []
			aORisWater = []
			aORisRiver = []
			aORisFreshWater = []
			aORisPrereqPower = []
			for iRequirement in xrange(len(aBuildingRequirementGOMORList)):
				CvBuildingRequirement = GC.getBuildingInfo(aBuildingRequirementGOMORList[iRequirement])
				aBuildingList.append(CvBuildingRequirement.getType())
				aORMinLatitude.append(CvBuildingRequirement.getMinLatitude())
				aORMaxLatitude.append(CvBuildingRequirement.getMaxLatitude())
				aORMinAreaSize.append(CvBuildingRequirement.getMinAreaSize())
				aORPrereqPopulation.append(CvBuildingRequirement.getPrereqPopulation())
				aORNumCitiesPrereq.append(CvBuildingRequirement.getNumCitiesPrereq())
				aORNumTeamsPrereq.append(CvBuildingRequirement.getNumTeamsPrereq())
				aORUnitLevelPrereq.append(CvBuildingRequirement.getUnitLevelPrereq())
				aORisWater.append(CvBuildingRequirement.isWater())
				aORisRiver.append(CvBuildingRequirement.isRiver())
				aORisFreshWater.append(CvBuildingRequirement.isFreshWater())
				aORisPrereqPower.append(CvBuildingRequirement.isPrereqPower())
			if len(aBuildingList) > 0 and CvBuildingInfo.getMinLatitude() < min(aORMinLatitude):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORMinLatitude.index(min(aORMinLatitude))]+", and can't be built below latitude of "+str(min(aORMinLatitude)))
			if len(aBuildingList) > 0 and CvBuildingInfo.getMaxLatitude() > max(aORMaxLatitude):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORMaxLatitude.index(max(aORMaxLatitude))]+", and can't be built above latitude of "+str(max(aORMaxLatitude)))
			if len(aBuildingList) > 0 and CvBuildingInfo.getMinAreaSize() < min(aORMinAreaSize):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORMinAreaSize.index(min(aORMinAreaSize))]+", and can't be built below area size "+str(min(aORMinAreaSize)))
			if len(aBuildingList) > 0 and CvBuildingInfo.getPrereqPopulation() < min(aORPrereqPopulation):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORPrereqPopulation.index(min(aORPrereqPopulation))]+", and can't be built below population "+str(min(aORPrereqPopulation)))
			if len(aBuildingList) > 0 and CvBuildingInfo.getNumCitiesPrereq() < min(aORNumCitiesPrereq):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORNumCitiesPrereq.index(min(aORNumCitiesPrereq))]+", and can't be built below amount of cities "+str(min(aORNumCitiesPrereq)))
			if len(aBuildingList) > 0 and CvBuildingInfo.getNumTeamsPrereq() < min(aORNumTeamsPrereq):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORNumTeamsPrereq.index(min(aORNumTeamsPrereq))]+", and can't be built below amount of teams "+str(min(aORNumTeamsPrereq)))
			if len(aBuildingList) > 0 and CvBuildingInfo.getUnitLevelPrereq() < min(aORUnitLevelPrereq):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORUnitLevelPrereq.index(min(aORUnitLevelPrereq))]+", and can't be built below unit level "+str(min(aORUnitLevelPrereq)))
			if len(aBuildingList) > 0 and CvBuildingInfo.isWater() < min(aORisWater):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORisWater.index(min(aORisWater))]+", and can't be built because of coastal requirement")
			if len(aBuildingList) > 0 and CvBuildingInfo.isRiver() < min(aORisRiver):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORisRiver.index(min(aORisRiver))]+", and can't be built because of river requirement")
			if len(aBuildingList) > 0 and CvBuildingInfo.isFreshWater() < min(aORisFreshWater):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORisFreshWater.index(min(aORisFreshWater))]+", and can't be built because of fresh water requirement")
			if len(aBuildingList) > 0 and CvBuildingInfo.isPrereqPower() < min(aORisPrereqPower):
				self.log(CvBuildingInfo.getType()+" requires "+aBuildingList[aORisPrereqPower.index(min(aORisPrereqPower))]+", and can't be built because of electricity requirement")

	#Building requirement civic requirements
	def checkBuildingRequirementCivics(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			aBuildingRequirementList = []

			#<PrereqInCityBuildings> - require all buildings in list
			for iBuildingRequirement in xrange(CvBuildingInfo.getNumPrereqInCityBuildings()):
				iPrereqBuilding = CvBuildingInfo.getPrereqInCityBuilding(iBuildingRequirement)
				aBuildingRequirementList.append(iPrereqBuilding)

			#<PrereqOrBuildings> - require one building in list
			for iBuildingRequirement in xrange(CvBuildingInfo.getNumPrereqOrBuilding()):
				iPrereqBuilding = CvBuildingInfo.getPrereqOrBuilding(iBuildingRequirement)
				if iPrereqBuilding not in aBuildingRequirementList:
					aBuildingRequirementList.append(iPrereqBuilding)

			#<PrereqAmountBuildings> - require all buildings in empire in list
			for pair in CvBuildingInfo.getPrereqNumOfBuildings():
				iPrereqBuilding = pair.id
				if iPrereqBuilding not in aBuildingRequirementList:
					aBuildingRequirementList.append(iPrereqBuilding)

			#<ConstructCondition>
			aBuildingGOMReqList = []
			for i in range(2):
				aBuildingGOMReqList.append([])
			self.HF.getGOMReqs(CvBuildingInfo.getConstructCondition(), GOMTypes.GOM_BUILDING, aBuildingGOMReqList)

			#Analyze GOM AND Building reqs
			for iBuildingRequirement in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND])):
				iPrereqBuilding = aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND][iBuildingRequirement]
				if iPrereqBuilding not in aBuildingRequirementList:
					aBuildingRequirementList.append(iPrereqBuilding)

			#Analyze GOM OR Building reqs
			for iBuildingRequirement in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR])):
				iPrereqBuilding = aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR][iBuildingRequirement]
				if iPrereqBuilding not in aBuildingRequirementList:
					aBuildingRequirementList.append(iPrereqBuilding)

			#Find if requirement needs civics
			for i in xrange(len(aBuildingRequirementList)):
				CvBuildingRequirementInfo = GC.getBuildingInfo(aBuildingRequirementList[i])
				aCivicList = []
				for iCivic in xrange(GC.getNumCivicInfos()):
					if CvBuildingRequirementInfo.isPrereqOrCivics(iCivic) or CvBuildingRequirementInfo.isPrereqAndCivics(iCivic):
						aCivicList.append(GC.getCivicInfo(iCivic).getType())
				if len(aCivicList) > 0:
					self.log(CvBuildingInfo.getType()+" requirement "+CvBuildingRequirementInfo.getType()+" needs civics "+str(aCivicList))

	#Building - civic requirements and obsoletions
	def checkBuildingCivicRequirements(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			iTechLoc = self.HF.checkBuildingTechRequirements(CvBuildingInfo)[0]

			aCivicAndTechLocList = []
			aCivicOrTechLocList = []
			for iCivic in xrange(GC.getNumCivicInfos()):
				#<PrereqAndCivics> - require all civics in list
				if CvBuildingInfo.isPrereqAndCivics(iCivic):
					iCivicTechLoc = self.HF.checkCivicTechRequirementLocation(GC.getCivicInfo(iCivic))[0]
					aCivicAndTechLocList.append(iCivicTechLoc)

				#<PrereqOrCivics> - require one civics in list
				if CvBuildingInfo.isPrereqOrCivics(iCivic):
					iCivicTechLoc = self.HF.checkCivicTechRequirementLocation(GC.getCivicInfo(iCivic))[0]
					aCivicOrTechLocList.append(iCivicTechLoc)

			if len(aCivicAndTechLocList) > 0 and max(aCivicAndTechLocList) > iTechLoc and iTechLoc > 0:
				self.log(CvBuildingInfo.getType()+" is unlocked before its civic AND requirements "+str(aCivicAndTechLocList)+" "+str(iTechLoc))
			if len(aCivicOrTechLocList) > 0 and min(aCivicOrTechLocList) > iTechLoc and iTechLoc > 0:
				self.log(CvBuildingInfo.getType()+" is unlocked before its earliest OR civic requirement "+str(aCivicOrTechLocList)+" "+str(iTechLoc))

			if len(aCivicAndTechLocList) > 0 or len(aCivicOrTechLocList) > 0:
				if CvBuildingInfo.getObsoleteTech() != -1:
					self.log(CvBuildingInfo.getType()+" civic extension shouldn't obsolete!")
				if CvBuildingInfo.isRequiresActiveCivics() == 0:
					self.log(CvBuildingInfo.getType()+" should be active only when civics are present")
				if CvBuildingInfo.getNumReplacementBuilding() != 0 or CvBuildingInfo.getNumReplacedBuilding() != 0:
					self.log(CvBuildingInfo.getType()+" shouldn't be replaced and shouldn't be replacing stuff, as its civic building")

	#Building - check if building doesn't obsolete before civic is available
	def checkBuildingCivicInfluences(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			iBuildingObsoleteTechLoc = self.HF.checkBuildingTechObsoletionLocation(CvBuildingInfo)[0]
			for iCivic in xrange(GC.getNumCivicInfos()):
				CvCivicInfo = GC.getCivicInfo(iCivic)
				iCivicTechUnlock = self.HF.checkCivicTechRequirementLocation(CvCivicInfo)[0]
				if iBuildingObsoleteTechLoc < iCivicTechUnlock:

					#<BuildingHappinessChanges>
					if CvCivicInfo.getBuildingHappinessChanges(iBuilding) != 0:
						self.log(CvBuildingInfo.getType()+" obsoletes before "+CvCivicInfo.getType()+" unlock - BuildingHappinessChanges")

					#<BuildingHealthChanges>
					if CvCivicInfo.getBuildingHealthChanges(iBuilding) != 0:
						self.log(CvBuildingInfo.getType()+" obsoletes before "+CvCivicInfo.getType()+" unlock - BuildingHealthChanges")

					#<BuildingProductionModifiers>
					if CvCivicInfo.getBuildingProductionModifier(iBuilding) != 0:
						self.log(CvBuildingInfo.getType()+" obsoletes before "+CvCivicInfo.getType()+" unlock - BuildingProductionModifiers")

					#<BuildingCommerceModifiers>
					for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
						if CvCivicInfo.getBuildingCommerceModifier(iBuilding, iCommerce) != 0:
							self.log(CvBuildingInfo.getType()+" obsoletes before "+CvCivicInfo.getType()+" unlock - BuildingCommerceModifiers")

	#Building - ensure that building religious tags always reference same religion
	def checkBuildingReligionRequirement(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			iRelPrereq1 = CvBuildingInfo.getPrereqReligion()
			iRelPrereq2 = CvBuildingInfo.getReligionType()
			iRelPrereq3 = CvBuildingInfo.getPrereqStateReligion()

			if iRelPrereq1 != -1 and iRelPrereq2 != -1 and iRelPrereq1 != iRelPrereq2:
				self.log(CvBuildingInfo.getType()+" mismatch between getPrereqReligion and getReligionType: "+GC.getReligionType(iRelPrereq1).getType()+" "+GC.getReligionType(iRelPrereq2).getType())
			if iRelPrereq2 != -1 and iRelPrereq3 != -1 and iRelPrereq2 != iRelPrereq3:
				self.log(CvBuildingInfo.getType()+" mismatch between getReligionType and getPrereqStateReligion: "+GC.getReligionType(iRelPrereq2).getType()+" "+GC.getReligionType(iRelPrereq3).getType())
			if iRelPrereq3 != -1 and iRelPrereq1 != -1 and iRelPrereq3 != iRelPrereq1:
				self.log(CvBuildingInfo.getType()+" mismatch between getPrereqStateReligion and getPrereqReligion: "+GC.getReligionType(iRelPrereq3).getType()+" "+GC.getReligionType(iRelPrereq1).getType())

	#Building - variety of tags
	def checkBuildingTags(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			#Commerce double time - wonders only, and ensure flat change exists
			for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
				if CvBuildingInfo.getCommerceChangeDoubleTime(iCommerce) != 0 and not (isWorldWonder(iBuilding) or isNationalWonder(iBuilding) or CvBuildingInfo.getHolyCity() != -1):
					self.log(CvBuildingInfo.getType()+" Non-wonder has commerce change double time")

			for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
				if CvBuildingInfo.getCommerceChangeDoubleTime(iCommerce) != 0 and CvBuildingInfo.getCommerceChange(iCommerce) == 0:
					self.log(CvBuildingInfo.getType()+" has commerce change double time but no relevant flat commerce change")

			#Owner change - ensure flat commerce change exists
			for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
				if CvBuildingInfo.isCommerceChangeOriginalOwner(iCommerce) and CvBuildingInfo.getCommerceChange(iCommerce) == 0:
					self.log(CvBuildingInfo.getType()+" has CommerceChangeOriginalOwners but no flat commerce change")

			#Hurry modifiers works only on buildable buildings
			if CvBuildingInfo.getProductionCost() == -1 and (CvBuildingInfo.getHurryCostModifier() != 0 or CvBuildingInfo.getHurryAngerModifier() != 0):
				self.log(CvBuildingInfo.getType()+" can't be hurried at first place")

			#GreatPeopleRateChange must be present, if GreatPeopleUnitType is present
			if CvBuildingInfo.getGreatPeopleUnitType() != -1 and CvBuildingInfo.getGreatPeopleRateChange() == 0:
				self.log(CvBuildingInfo.getType()+" has zero rate change of "+GC.getUnitInfo(CvBuildingInfo.getGreatPeopleUnitType()).getType())

			#FreeBonus must be present if iNumFreeBonuses is present and viceversa.
			if CvBuildingInfo.getFreeBonus() != -1 and CvBuildingInfo.getNumFreeBonuses() == 0:
				self.log(CvBuildingInfo.getType()+" has free bonus tag, but actually doesn't give bonus")
			if CvBuildingInfo.getFreeBonus() == -1 and CvBuildingInfo.getNumFreeBonuses() != 0:
				self.log(CvBuildingInfo.getType()+" has unspecified free bonus type")
			for i in xrange(CvBuildingInfo.getNumExtraFreeBonuses()):
				if CvBuildingInfo.getExtraFreeBonus(i) != -1 and CvBuildingInfo.getExtraFreeBonusNum(i) == 0:
					self.log(CvBuildingInfo.getType()+" has extra free bonus tag, but actually doesn't give bonus")
				if CvBuildingInfo.getExtraFreeBonus(i) == -1 and CvBuildingInfo.getExtraFreeBonusNum(i) != 0:
					self.log(CvBuildingInfo.getType()+" has unspecified extra free bonus type")

			#GlobalBuildingExtraCommerces is meant to be placed on wonders
			for pBuildingCommerceChange in CvBuildingInfo.getGlobalBuildingCommerceChanges():
				CvTargetBuilding = GC.getBuildingInfo(pBuildingCommerceChange.eBuilding)
				if not (isWorldWonder(iBuilding) or isNationalWonder(iBuilding) or CvBuildingInfo.getHolyCity() != -1):
					self.log(CvBuildingInfo.getType()+" GlobalBuildingExtraCommerces should be swapped with "+CvTargetBuilding.getType())

	#Buildings - free rewards. Their obsoletion should be correlated with obsoletion of building.
	def checkBuildingFreeReward(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			iObsoleteTechLoc = self.HF.checkBuildingTechObsoletionLocation(CvBuildingInfo)[0]

			iFreeBuilding = CvBuildingInfo.getFreeBuilding()
			if iFreeBuilding != -1:
				CvFreeBuilding = GC.getBuildingInfo(iFreeBuilding)
				iObsoleteFreeBuildingTechLoc = self.HF.checkBuildingTechObsoletionLocation(CvFreeBuilding)[0]
				if iObsoleteTechLoc != iObsoleteFreeBuildingTechLoc and CvFreeBuilding.getProductionCost() == -1 or iObsoleteTechLoc < iObsoleteFreeBuildingTechLoc:
					self.log(CvBuildingInfo.getType()+" obsoletes at: "+str(iObsoleteTechLoc)+", free building "+CvFreeBuilding.getType()+" obsoletes at: "+str(iObsoleteFreeBuildingTechLoc))

			iFreeAreaBuilding = CvBuildingInfo.getFreeAreaBuilding()
			if iFreeAreaBuilding != -1:
				CvFreeAreaBuilding = GC.getBuildingInfo(iFreeAreaBuilding)
				iObsoleteFreeAreaBuildingTechLoc = self.HF.checkBuildingTechObsoletionLocation(CvFreeAreaBuilding)[0]
				if iObsoleteTechLoc != iObsoleteFreeAreaBuildingTechLoc and CvFreeAreaBuilding.getProductionCost() == -1 or iObsoleteTechLoc < iObsoleteFreeAreaBuildingTechLoc:
					self.log(CvBuildingInfo.getType()+" obsoletes at: "+str(iObsoleteTechLoc)+", free area building "+CvFreeAreaBuilding.getType()+" obsoletes at: "+str(iObsoleteFreeAreaBuildingTechLoc))

	#Building tech changes and modifiers
	def checkBuildingTechMods(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			iTechLoc = self.HF.checkBuildingTechRequirements(CvBuildingInfo)[0]
			#Check if Happiness Changes techs don't appear before building can be unlocked or after is obsoleted
			for pair in CvBuildingInfo.getTechHappinessChanges():
				iTech = pair.id
				iTechTLoc = GC.getTechInfo(iTech).getGridX()
				if iTechTLoc <= iTechLoc:
					self.log(CvBuildingInfo.getType()+" Tech unlock: "+str(iTechLoc)+" Happiness Changes early tech: "+str(iTechTLoc)+" "+GC.getTechInfo(iTech).getType())
				elif CvBuildingInfo.getObsoleteTech() != -1 and iTechTLoc >= GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX():
					self.log(CvBuildingInfo.getType()+" Tech obsolete: "+str(GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX())+" Happiness Changes late tech: "+str(iTechTLoc)+" "+GC.getTechInfo(iTech).getType())

			#Check if Health Changes techs don't appear before building can be unlocked or after is obsoleted
			for pair in CvBuildingInfo.getTechHealthChanges():
				iTech = pair.id
				iTechTLoc = GC.getTechInfo(iTech).getGridX()
				if iTechTLoc <= iTechLoc:
					self.log(CvBuildingInfo.getType()+" Tech unlock: "+str(iTechLoc)+" Health Changes early tech: "+str(iTechTLoc)+" "+GC.getTechInfo(iTech).getType())
				elif CvBuildingInfo.getObsoleteTech() != -1 and iTechTLoc >= GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX():
					self.log(CvBuildingInfo.getType()+" Tech obsolete: "+str(GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX())+" Health Changes late tech: "+str(iTechTLoc)+" "+GC.getTechInfo(iTech).getType())

			#Check if Yield Changes techs don't appear before building can be unlocked or after is obsoleted
			if CvBuildingInfo.isAnyTechYieldChanges():
				for iTech in xrange(GC.getNumTechInfos()):
					for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
						if CvBuildingInfo.getTechYieldChange(iTech, iYield):
							iTechMLoc = GC.getTechInfo(iTech).getGridX()
							if iTechMLoc <= iTechLoc:
								self.log(CvBuildingInfo.getType()+" Tech unlock: "+str(iTechLoc)+" Yield Changes early tech: "+str(iTechMLoc)+" "+GC.getTechInfo(iTech).getType())
							elif CvBuildingInfo.getObsoleteTech() != -1 and iTechMLoc >= GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX():
								self.log(CvBuildingInfo.getType()+" Tech obsolete: "+str(GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX())+" Yield Changes late tech: "+str(iTechMLoc)+" "+GC.getTechInfo(iTech).getType())

			#Check if Yield Modifiers techs don't appear before building can be unlocked or after is obsoleted
			if CvBuildingInfo.isAnyTechYieldModifiers():
				for iTech in xrange(GC.getNumTechInfos()):
					for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
						if CvBuildingInfo.getTechYieldModifier(iTech, iYield):
							iTechMLoc = GC.getTechInfo(iTech).getGridX()
							if iTechMLoc <= iTechLoc:
								self.log(CvBuildingInfo.getType()+" Tech unlock: "+str(iTechLoc)+" Yield Modifiers early tech: "+str(iTechMLoc)+" "+GC.getTechInfo(iTech).getType())
							elif CvBuildingInfo.getObsoleteTech() != -1 and iTechMLoc >= GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX():
								self.log(CvBuildingInfo.getType()+" Tech obsolete: "+str(GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX())+" Yield Modifiers late tech: "+str(iTechMLoc)+" "+GC.getTechInfo(iTech).getType())

			#Check if Commerce Changes techs don't appear before building can be unlocked or after is obsoleted
			if CvBuildingInfo.isAnyTechCommerceChanges():
				for iTech in xrange(GC.getNumTechInfos()):
					for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
						if CvBuildingInfo.getTechCommerceChange(iTech, iCommerce):
							iTechMLoc = GC.getTechInfo(iTech).getGridX()
							if iTechMLoc <= iTechLoc:
								self.log(CvBuildingInfo.getType()+" Tech unlock: "+str(iTechLoc)+" Commerce Changes early tech: "+str(iTechMLoc)+" "+GC.getTechInfo(iTech).getType())
							elif CvBuildingInfo.getObsoleteTech() != -1 and iTechMLoc >= GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX():
								self.log(CvBuildingInfo.getType()+" Tech obsolete: "+str(GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX())+" Commerce Changes late tech: "+str(iTechMLoc)+" "+GC.getTechInfo(iTech).getType())

			#Check if Commerce Modifiers techs don't appear before building can be unlocked or after is obsoleted
			if CvBuildingInfo.isAnyTechCommerceModifiers():
				for iTech in xrange(GC.getNumTechInfos()):
					for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
						if CvBuildingInfo.getTechCommerceModifier(iTech, iCommerce):
							iTechMLoc = GC.getTechInfo(iTech).getGridX()
							if iTechMLoc <= iTechLoc:
								self.log(CvBuildingInfo.getType()+" Tech unlock: "+str(iTechLoc)+" Commerce Modifiers early tech: "+str(iTechMLoc)+" "+GC.getTechInfo(iTech).getType())
							elif CvBuildingInfo.getObsoleteTech() != -1 and iTechMLoc >= GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX():
								self.log(CvBuildingInfo.getType()+" Tech obsolete: "+str(GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX())+" Commerce Modifiers late tech: "+str(iTechMLoc)+" "+GC.getTechInfo(iTech).getType())

			#Check if Specialist Changes techs don't appear before building can be unlocked or after is obsoleted
			if CvBuildingInfo.isAnyTechSpecialistChanges():
				for iTech in xrange(GC.getNumSpecialistInfos()):
					for iSpecialist in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
						if CvBuildingInfo.getTechSpecialistChange(iTech, iSpecialist):
							iTechMLoc = GC.getTechInfo(iTech).getGridX()
							if iTechMLoc <= iTechLoc:
								self.log(CvBuildingInfo.getType()+" Tech unlock: "+str(iTechLoc)+" Specialist Changes early tech: "+str(iTechMLoc)+" "+GC.getTechInfo(iTech).getType())
							elif CvBuildingInfo.getObsoleteTech() != -1 and iTechMLoc >= GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX():
								self.log(CvBuildingInfo.getType()+" Tech obsolete: "+str(GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getGridX())+" Specialist Changes late tech: "+str(iTechMLoc)+" "+GC.getTechInfo(iTech).getType())

	#Building - bonus must be unlocked before building obsoletion so it can affect building at first place
	def checkBuildingBonusTags(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			iBuildingObsoleteTechLoc = self.HF.checkBuildingTechObsoletionLocation(CvBuildingInfo)[0]

			if CvBuildingInfo.isAnyBonusYieldChanges():
				for iBonus in xrange(GC.getNumBonusInfos()):
					CvBonusInfo = GC.getBonusInfo(iBonus)
					iBonusTechEnable = self.HF.checkBonusTechRequirementLocation(CvBonusInfo)[2]
					if iBuildingObsoleteTechLoc < iBonusTechEnable:
						for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
							#<BonusYieldChanges>
							if CvBuildingInfo.getBonusYieldChanges(iBonus, iYield) != 0:
								self.log(CvBuildingInfo.getType()+" obsoletes before "+CvBonusInfo.getType()+" Tech enable - BonusYieldChanges")

			if CvBuildingInfo.isAnyBonusYieldModifiers():
				for iBonus in xrange(GC.getNumBonusInfos()):
					CvBonusInfo = GC.getBonusInfo(iBonus)
					iBonusTechEnable = self.HF.checkBonusTechRequirementLocation(CvBonusInfo)[2]
					if iBuildingObsoleteTechLoc < iBonusTechEnable:
						for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
							#<BonusYieldModifiers>
							if CvBuildingInfo.getBonusYieldModifier(iBonus, iYield) != 0:
								self.log(CvBuildingInfo.getType()+" obsoletes before "+CvBonusInfo.getType()+" Tech enable - BonusYieldModifiers")

			if CvBuildingInfo.isAnyVicinityBonusYieldChanges():
				for iBonus in xrange(GC.getNumBonusInfos()):
					CvBonusInfo = GC.getBonusInfo(iBonus)
					iBonusTechEnable = self.HF.checkBonusTechRequirementLocation(CvBonusInfo)[2]
					if iBuildingObsoleteTechLoc < iBonusTechEnable:
						for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
							#<VicinityBonusYieldChanges>
							if CvBuildingInfo.getVicinityBonusYieldChanges(iBonus, iYield) != 0:
								self.log(CvBuildingInfo.getType()+" obsoletes before "+CvBonusInfo.getType()+" Tech enable - VicinityBonusYieldChanges")

			if CvBuildingInfo.isAnyBonusCommerceModifiers():
				for iBonus in xrange(GC.getNumBonusInfos()):
					CvBonusInfo = GC.getBonusInfo(iBonus)
					iBonusTechEnable = self.HF.checkBonusTechRequirementLocation(CvBonusInfo)[2]
					if iBuildingObsoleteTechLoc < iBonusTechEnable:
						for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
							#<BonusCommerceModifiers>
							if CvBuildingInfo.getBonusCommerceModifier(iBonus, iCommerce) != 0:
								self.log(CvBuildingInfo.getType()+" obsoletes before "+CvBonusInfo.getType()+" Tech enable - BonusCommerceModifiers")

			if CvBuildingInfo.isAnyBonusCommercePercentChanges():
				for iBonus in xrange(GC.getNumBonusInfos()):
					CvBonusInfo = GC.getBonusInfo(iBonus)
					iBonusTechEnable = self.HF.checkBonusTechRequirementLocation(CvBonusInfo)[2]
					if iBuildingObsoleteTechLoc < iBonusTechEnable:
						for iCommerce in xrange(CommerceTypes.NUM_COMMERCE_TYPES):
							#<BonusCommercePercentChanges>
							if CvBuildingInfo.getBonusCommercePercentChanges(iBonus, iCommerce) != 0:
								self.log(CvBuildingInfo.getType()+" obsoletes before "+CvBonusInfo.getType()+" Tech enable - getBonusCommercePercentChanges")

			for iBonus in xrange(GC.getNumBonusInfos()):
				CvBonusInfo = GC.getBonusInfo(iBonus)
				iBonusTechEnable = self.HF.checkBonusTechRequirementLocation(CvBonusInfo)[2]
				if iBuildingObsoleteTechLoc < iBonusTechEnable:
					#<BonusHappinessChanges>
					if CvBuildingInfo.getBonusHappinessChanges(iBonus) != 0:
						self.log(CvBuildingInfo.getType()+" obsoletes before "+CvBonusInfo.getType()+" Tech enable - BonusHappinessChanges")

					#<BonusHealthChanges>
					if CvBuildingInfo.getBonusHealthChanges(iBonus) != 0:
						self.log(CvBuildingInfo.getType()+" obsoletes before "+CvBonusInfo.getType()+" Tech enable - BonusHealthChanges")

					#<BonusProductionModifiers>
					if CvBuildingInfo.getBonusProductionModifier(iBonus) != 0:
						self.log(CvBuildingInfo.getType()+" obsoletes before "+CvBonusInfo.getType()+" Tech enable - BonusProductionModifiers")

	#Buildings X -> Y: X shouldn't be obsolete before Y is available, and X should be unlocked before Y is obsolete
	def checkBuildingAffectingBuildings(self):
		aAffectedBuildingTechUnlockList = []
		aAffectedBuildingTechObsoletionList = []
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			aAffectedBuildingTechUnlockList.append(self.HF.checkBuildingTechRequirements(CvBuildingInfo)[0])
			aAffectedBuildingTechObsoletionList.append(self.HF.checkBuildingTechObsoletionLocation(CvBuildingInfo)[0])

		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvAffectingBuildingInfo = GC.getBuildingInfo(iBuilding)
			iAffectingBuildingUnlockTechLoc = self.HF.checkBuildingTechRequirements(CvAffectingBuildingInfo)[0]
			iAffectingBuildingObsoleteTechLoc = self.HF.checkBuildingTechObsoletionLocation(CvAffectingBuildingInfo)[0]

			#<GlobalBuildingExtraCommerces>
			for pBuildingCommerceChange in CvAffectingBuildingInfo.getGlobalBuildingCommerceChanges():
				i = pBuildingCommerceChange.eBuilding
				if iAffectingBuildingObsoleteTechLoc < aAffectedBuildingTechUnlockList[i] or iAffectingBuildingUnlockTechLoc > aAffectedBuildingTechObsoletionList[i]:
					CvAffectedBuildingInfo = GC.getBuildingInfo(i)
					self.log(CvAffectingBuildingInfo.getType()+" can't affect "+CvAffectedBuildingInfo.getType()+" as buildings have disjointed tech ranges - GlobalBuildingExtraCommerces")

			#<GlobalBuildingCostModifiers>
			for pair in CvAffectingBuildingInfo.getGlobalBuildingCostModifiers():
				if pair.value != 0 and (iAffectingBuildingObsoleteTechLoc < aAffectedBuildingTechUnlockList[pair.id] or iAffectingBuildingUnlockTechLoc > aAffectedBuildingTechObsoletionList[pair.id]):
					CvAffectedBuildingInfo = GC.getBuildingInfo(pair.id)
					self.log(CvAffectingBuildingInfo.getType()+" can't affect "+CvAffectedBuildingInfo.getType()+" as buildings have disjointed tech ranges - GlobalBuildingProductionModifiers")

			#<GlobalBuildingProductionModifiers>
			for pair in CvAffectingBuildingInfo.getGlobalBuildingProductionModifiers():
				if pair.value != 0 and (iAffectingBuildingObsoleteTechLoc < aAffectedBuildingTechUnlockList[pair.id] or iAffectingBuildingUnlockTechLoc > aAffectedBuildingTechObsoletionList[pair.id]):
					CvAffectedBuildingInfo = GC.getBuildingInfo(pair.id)
					self.log(CvAffectingBuildingInfo.getType()+" can't affect "+CvAffectedBuildingInfo.getType()+" as buildings have disjointed tech ranges - GlobalBuildingProductionModifiers")

			#<BuildingHappinessChanges>
			for pair in CvAffectingBuildingInfo.getBuildingHappinessChanges():
				if pair.value != 0 and (iAffectingBuildingObsoleteTechLoc < aAffectedBuildingTechUnlockList[pair.id] or iAffectingBuildingUnlockTechLoc > aAffectedBuildingTechObsoletionList[pair.id]):
					CvAffectedBuildingInfo = GC.getBuildingInfo(pair.id)
					self.log(CvAffectingBuildingInfo.getType()+" can't affect "+CvAffectedBuildingInfo.getType()+" as buildings have disjointed tech ranges - BuildingHappinessChanges")

			#<BuildingProductionModifiers>
			for pair in CvAffectingBuildingInfo.getBuildingProductionModifiers():
				if pair.value != 0 and (iAffectingBuildingObsoleteTechLoc < aAffectedBuildingTechUnlockList[pair.id] or iAffectingBuildingUnlockTechLoc > aAffectedBuildingTechObsoletionList[pair.id]):
					CvAffectedBuildingInfo = GC.getBuildingInfo(pair.id)
					self.log(CvAffectingBuildingInfo.getType()+" can't affect "+CvAffectedBuildingInfo.getType()+" as buildings have disjointed tech ranges - BuildingProductionModifiers")

			#<PrereqNotInCityBuildings>
			for i in xrange(CvAffectingBuildingInfo.getNumPrereqNotInCityBuildings()):
				iAffectedBuilding = CvAffectingBuildingInfo.getPrereqNotInCityBuilding(i)
				if iAffectingBuildingObsoleteTechLoc < aAffectedBuildingTechUnlockList[iAffectedBuilding] or iAffectingBuildingUnlockTechLoc > aAffectedBuildingTechObsoletionList[iAffectedBuilding]:
					CvAffectedBuildingInfo = GC.getBuildingInfo(iAffectedBuilding)
					self.log(CvAffectingBuildingInfo.getType()+" can't affect "+CvAffectedBuildingInfo.getType()+" as buildings have disjointed tech ranges - PrereqNotInCityBuildings")

			#<ExtendsBuilding>
			iAffectedBuilding = CvAffectingBuildingInfo.getExtendsBuilding()
			if iAffectedBuilding != -1:
				if iAffectingBuildingObsoleteTechLoc < aAffectedBuildingTechUnlockList[iAffectedBuilding] or iAffectingBuildingUnlockTechLoc > aAffectedBuildingTechObsoletionList[iAffectedBuilding]:
					CvAffectedBuildingInfo = GC.getBuildingInfo(iAffectedBuilding)
					self.log(CvAffectingBuildingInfo.getType()+" can't affect "+CvAffectedBuildingInfo.getType()+" as buildings have disjointed tech ranges - ExtendsBuilding")

	#Building - Check if buildings have proper costs
	def checkBuildingCosts(self):
		aBaseCostList = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 56, 62, 68, 74, 80, 86, 92, 98, 104, 111, 118, 125, 132, 139, 146, 153, 160, 168, 176, 184, 192, 200, 208, 216, 225, 234, 243, 252, 261, 270, 280, 290, 300, 310, 320, 332, 344, 356, 368, 380, 395, 410, 425, 440, 455, 475, 495, 515, 535, 555, 580, 605, 630, 655, 680, 710, 740, 770, 800, 830, 870, 910, 950, 990, 1030, 1080, 1130, 1180, 1230, 1280, 1345, 1410, 1475, 1540, 1605, 1685, 1765, 1845, 1925, 2005, 2105, 2205, 2305, 2405, 2505, 2625, 2745, 2865, 2985, 3105, 3245, 3385, 3525, 3665, 3805, 3975, 4145, 4315, 4485, 4655, 4855, 5055, 5255, 5455, 5655, 5905, 6155, 6405, 6655, 6905, 7205, 7505, 7805, 8105, 8405, 8755, 9105, 9455, 9805, 10155, 10555, 10955, 11355, 11755, 12155, 12655, 13155, 13655, 14155, 14655, 15255, 15855, 16455, 17055, 17655, 18355, 19055, 19755, 20455, 21155, 21955, 22755, 23555, 24355, 25155, 26055, 26955, 27855, 28755, 29655, 30655] #Building cost depend on most advanced tech to unlock. *2 for National, *4 for Group, *6 for World wonders, *8 for Projects
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)

			if CvBuildingInfo.getProductionCost() > 0 and GC.getInfoTypeForString("MAPCATEGORY_EARTH") in CvBuildingInfo.getMapCategories() and iBuilding != GC.getInfoTypeForString("BUILDING_PALACE") and CvBuildingInfo.getType().find("_CULTURE_LOCAL_") == -1:
				iTechLoc = self.HF.checkBuildingTechRequirements(CvBuildingInfo)[0] #Pick one of most advanced: Main/TechTypes/Religious/Special/GOM OR (earliest)
				iSpecialBuilding = CvBuildingInfo.getSpecialBuildingType()

				#Regular
				if not isNationalWonder(iBuilding) and not isWorldWonder(iBuilding) and CvBuildingInfo.getProductionCost() != aBaseCostList[iTechLoc]:
					self.log(CvBuildingInfo.getType()+" should have Cost of "+str(aBaseCostList[iTechLoc]))

				#National Wonder
				if isNationalWonder(iBuilding) and CvBuildingInfo.getProductionCost() != 2*aBaseCostList[iTechLoc]:
					self.log(CvBuildingInfo.getType()+" should have Cost of "+str(2*aBaseCostList[iTechLoc]))

				#Group Wonder
				if iSpecialBuilding != -1 and GC.getSpecialBuildingInfo(iSpecialBuilding).getType().find("_GROUP_") != -1 and CvBuildingInfo.getProductionCost() != 4*aBaseCostList[iTechLoc]:
					self.log(CvBuildingInfo.getType()+" should have Cost of "+str(4*aBaseCostList[iTechLoc]))

				#World Wonder
				if isWorldWonder(iBuilding) and not (iSpecialBuilding != -1 and GC.getSpecialBuildingInfo(iSpecialBuilding).getType().find("_GROUP_") != -1) and CvBuildingInfo.getProductionCost() != 6*aBaseCostList[iTechLoc]:
					self.log(CvBuildingInfo.getType()+" should have Cost of "+str(6*aBaseCostList[iTechLoc]))

		#Project
		for iProject in xrange(GC.getNumProjectInfos()):
			CvProjectInfo = GC.getProjectInfo(iProject)
			iTechLoc = GC.getTechInfo(CvProjectInfo.getTechPrereq()).getGridX()

			if CvProjectInfo.getProductionCost() != 8*aBaseCostList[iTechLoc]:
				self.log(CvProjectInfo.getType()+" should have Cost of "+str(8*aBaseCostList[iTechLoc]))

	#Unit - check unit upgrades
	def checkUnitUpgrades(self):
		for iUnit in xrange(GC.getNumUnitInfos()):
			CvUnitInfo = GC.getUnitInfo(iUnit)
			iTechLoc = self.HF.checkUnitTechRequirementLocation(CvUnitInfo)[0]

			if CvUnitInfo.getNumUnitUpgrades() > 0:
				iCost = CvUnitInfo.getProductionCost()
				for iUnitUpgrade in xrange(CvUnitInfo.getNumUnitUpgrades()):
					upgradedDesc = GC.getUnitInfo(CvUnitInfo.getUnitUpgrade(iUnitUpgrade)).getType()
					upgradedCost = GC.getUnitInfo(CvUnitInfo.getUnitUpgrade(iUnitUpgrade)).getProductionCost()
					upgradedTechLoc = self.HF.checkUnitTechRequirementLocation(GC.getUnitInfo(CvUnitInfo.getUnitUpgrade(iUnitUpgrade)))[0]

					dist = upgradedTechLoc - iTechLoc
					costdiff = upgradedCost - iCost

					upgradedUnit = GC.getUnitInfo(CvUnitInfo.getUnitUpgrade(iUnitUpgrade))
					aSecondUpgradeList = []
					for iUnitUpgrade2 in xrange(upgradedUnit.getNumUnitUpgrades()):
						aSecondUpgradeList.append(GC.getUnitInfo(upgradedUnit.getUnitUpgrade(iUnitUpgrade2)).getType())
					if CvUnitInfo.getNumUnitUpgrades() == 1 and (dist <= 2 or costdiff <= 0):
						self.log(str(iTechLoc)+" - "+str(CvUnitInfo.getType())+"; Upgrade: "+str(upgradedTechLoc)+" - "+str(upgradedDesc)+" -> Distance: "+str(dist)+", Cost difference: "+str(costdiff)+" Upgrade of upgrade "+str(aSecondUpgradeList))
					elif CvUnitInfo.getNumUnitUpgrades() > 1 and (dist <= 2 or costdiff <= 0):
						self.log(str(iTechLoc)+" - "+str(CvUnitInfo.getType())+"; Upgrade #"+str(iUnitUpgrade+1)+"/"+str(CvUnitInfo.getNumUnitUpgrades())+": "+str(upgradedTechLoc)+" - "+str(upgradedDesc)+" -> Distance: "+str(dist)+", Cost difference: "+str(costdiff)+" Upgrade of upgrade "+str(aSecondUpgradeList))

	#Unit - check unit bonus requirements
	def checkUnitBonusRequirements(self):
		for iUnit in xrange(GC.getNumUnitInfos()):
			CvUnitInfo = GC.getUnitInfo(iUnit)
			iTechLoc = self.HF.checkUnitTechRequirementLocation(CvUnitInfo)[0]

			#<BonusType>BONUS_X
			iBonus = CvUnitInfo.getPrereqAndBonus()
			if iBonus != -1:
				bonusTechLoc = self.HF.checkBonusTechRequirementLocation(GC.getBonusInfo(iBonus))[2]
				if bonusTechLoc > iTechLoc:
					self.log(CvUnitInfo.getType()+" - Singular AND bonus prereq late! "+str(bonusTechLoc)+" "+str(iTechLoc))

			#<PrereqBonuses>
			aBonusTechLocList = []
			for iBonus in CvUnitInfo.getPrereqOrBonuses():
				aBonusTechLocList.append(self.HF.checkBonusTechRequirementLocation(GC.getBonusInfo(iBonus))[2])
			if len(aBonusTechLocList) > 0 and min(aBonusTechLocList) > iTechLoc:
				self.log(CvUnitInfo.getType()+" - Earliest OR bonus prereq late! "+str(aBonusTechLocList)+" "+str(iTechLoc))

			#<TrainCondition>
			aBonusGOMReqList = []
			for i in range(2):
				aBonusGOMReqList.append([])
			self.HF.getGOMReqs(CvUnitInfo.getTrainCondition(), GOMTypes.GOM_BONUS, aBonusGOMReqList)

			#Analyze GOM AND Bonus reqs
			aBonusTechLocList = []
			for iBonus in xrange(len(aBonusGOMReqList[BoolExprTypes.BOOLEXPR_AND])):
				aBonusTechLocList.append(self.HF.checkBonusTechRequirementLocation(GC.getBonusInfo(aBonusGOMReqList[BoolExprTypes.BOOLEXPR_AND][iBonus]))[2])
			if len(aBonusTechLocList) > 0 and max(aBonusTechLocList) > iTechLoc:
				self.log(CvUnitInfo.getType()+" - GOM AND bonus requirements are late! "+str(aBonusTechLocList)+" "+str(iTechLoc))

			#Analyze GOM OR Bonus reqs
			aBonusTechLocList = []
			for iBonus in xrange(len(aBonusGOMReqList[BoolExprTypes.BOOLEXPR_OR])):
				aBonusTechLocList.append(self.HF.checkBonusTechRequirementLocation(GC.getBonusInfo(aBonusGOMReqList[BoolExprTypes.BOOLEXPR_OR][iBonus]))[2])
			if len(aBonusTechLocList) > 0 and min(aBonusTechLocList) > iTechLoc:
				self.log(CvUnitInfo.getType()+" - GOM OR bonus requirements are late! "+str(aBonusTechLocList)+" "+str(iTechLoc))

	#Unit - check building requirements
	def checkUnitRequirements(self):
		for iUnit in xrange(GC.getNumUnitInfos()):
			CvUnitInfo = GC.getUnitInfo(iUnit)
			iTechLoc = self.HF.checkUnitTechRequirementLocation(CvUnitInfo)[0]

			#<PrereqAndBuildings> - require all buildings in list
			aBuildingNameList = []
			aBuildingTechLocList = []
			aBuildingTechObsList = []
			for iBuilding in xrange(CvUnitInfo.getNumPrereqAndBuildings()):
				aBuildingNameList.append(GC.getBuildingInfo(CvUnitInfo.getPrereqAndBuilding(iBuilding)).getType())
				aBuildingTechLocList.append(self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(CvUnitInfo.getPrereqAndBuilding(iBuilding)))[0])
				aBuildingTechObsList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(CvUnitInfo.getPrereqAndBuilding(iBuilding)))[0])
			if len(aBuildingTechLocList) > 0 and max(aBuildingTechLocList) > iTechLoc and iTechLoc > 0:
				self.log(CvUnitInfo.getType()+" is unlocked before its AND building requirements "+str(aBuildingTechLocList)+" "+str(iTechLoc))
			if len(aBuildingTechObsList) > 0 and min(aBuildingTechObsList) < 999:
				self.log(CvUnitInfo.getType()+" has obsoleteing AND requirements "+str(aBuildingTechObsList)+" "+str(aBuildingNameList))

			#<PrereqOrBuildings> - require one building in list
			aBuildingNameList = []
			aBuildingTechLocList = []
			aBuildingTechObsList = []
			for iBuilding in xrange(CvUnitInfo.getPrereqOrBuildingsNum()):
				aBuildingNameList.append(GC.getBuildingInfo(CvUnitInfo.getPrereqOrBuilding(iBuilding)).getType())
				aBuildingTechLocList.append(self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(CvUnitInfo.getPrereqOrBuilding(iBuilding)))[0])
				aBuildingTechObsList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(CvUnitInfo.getPrereqOrBuilding(iBuilding)))[0])
			if len(aBuildingTechLocList) > 0 and min(aBuildingTechLocList) > iTechLoc and iTechLoc > 0:
				self.log(CvUnitInfo.getType()+" is unlocked before its earliest OR building requirement "+str(aBuildingTechLocList)+" "+str(iTechLoc))
			if len(aBuildingTechObsList) > 0 and max(aBuildingTechObsList) < 999:
				self.log(CvUnitInfo.getType()+" has obsoleteing OR requirements "+str(aBuildingTechObsList)+" "+str(aBuildingNameList))

			#<TrainCondition>
			aBuildingGOMReqList = []
			for i in range(2):
				aBuildingGOMReqList.append([])
			self.HF.getGOMReqs(CvUnitInfo.getTrainCondition(), GOMTypes.GOM_BUILDING, aBuildingGOMReqList)

			#Analyze GOM AND Building reqs
			aBuildingNameList = []
			aBuildingTechLocList = []
			aBuildingTechObsList = []
			for iBuilding in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND])):
				aBuildingNameList.append(GC.getBuildingInfo(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND][iBuilding]).getType())
				aBuildingTechLocList.append(self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND][iBuilding]))[0])
				aBuildingTechObsList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND][iBuilding]))[0])
			if len(aBuildingTechLocList) > 0 and max(aBuildingTechLocList) > iTechLoc and iTechLoc > 0:
				self.log(CvUnitInfo.getType()+" - GOM AND building requirements are late! "+str(aBuildingTechLocList)+" "+str(iTechLoc))
			if len(aBuildingTechObsList) > 0 and min(aBuildingTechObsList) < 999:
				self.log(CvUnitInfo.getType()+" has obsoleteing GOM AND requirements "+str(aBuildingTechObsList)+" "+str(aBuildingNameList))

			#Analyze GOM OR Building reqs
			aBuildingNameList = []
			aBuildingTechLocList = []
			aBuildingTechObsList = []
			for iBuilding in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR])):
				aBuildingNameList.append(GC.getBuildingInfo(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR][iBuilding]).getType())
				aBuildingTechLocList.append(self.HF.checkBuildingTechRequirements(GC.getBuildingInfo(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR][iBuilding]))[0])
				aBuildingTechObsList.append(self.HF.checkBuildingTechObsoletionLocation(GC.getBuildingInfo(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR][iBuilding]))[0])
			if len(aBuildingTechLocList) > 0 and min(aBuildingTechLocList) > iTechLoc and iTechLoc > 0:
				self.log(CvUnitInfo.getType()+" - GOM OR building requirements are late! "+str(aBuildingTechLocList)+" "+str(iTechLoc))
			if len(aBuildingTechObsList) > 0 and max(aBuildingTechObsList) < 999:
				self.log(CvUnitInfo.getType()+" has obsoleteing GOM OR requirements "+str(aBuildingTechObsList)+" "+str(aBuildingNameList))

	#Unit - check building requirement replacements
	def checkUnitRequirementsReplacements(self):
		for iUnit in xrange(GC.getNumUnitInfos()):
			CvUnitInfo = GC.getUnitInfo(iUnit)

			#<PrereqAndBuildings> - require all buildings in list
			aBuildingList = []
			for iBuilding in xrange(CvUnitInfo.getNumPrereqAndBuildings()):
				if CvUnitInfo.getPrereqAndBuilding(iBuilding) not in aBuildingList:
					aBuildingList.append(CvUnitInfo.getPrereqAndBuilding(iBuilding))

			#<PrereqOrBuildings> - require one building in list
			for iBuilding in xrange(CvUnitInfo.getPrereqOrBuildingsNum()):
				if CvUnitInfo.getPrereqOrBuilding(iBuilding) not in aBuildingList:
					aBuildingList.append(CvUnitInfo.getPrereqOrBuilding(iBuilding))

			#<TrainCondition>
			aBuildingGOMReqList = []
			for i in range(2):
				aBuildingGOMReqList.append([])
			self.HF.getGOMReqs(CvUnitInfo.getTrainCondition(), GOMTypes.GOM_BUILDING, aBuildingGOMReqList)

			#Analyze GOM AND Building reqs
			for iBuilding in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND])):
				if aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND][iBuilding] not in aBuildingList:
					aBuildingList.append(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_AND][iBuilding])

			#Analyze GOM OR Building reqs
			for iBuilding in xrange(len(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR])):
				if aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR][iBuilding] not in aBuildingList:
					aBuildingList.append(aBuildingGOMReqList[BoolExprTypes.BOOLEXPR_OR][iBuilding])

			#Get unique buildings - distinct requirements
			aBuildingUniqueList = []
			for iBuilding in xrange(len(aBuildingList)):
				if aBuildingList[iBuilding] not in aBuildingUniqueList:
					aBuildingUniqueList.append(aBuildingList[iBuilding])

			#Get building replacements - all replacements are explicitly defined
			aBuildingReplacementList = []
			for iBuilding in xrange(len(aBuildingUniqueList)):
				CvBuildingInfo = GC.getBuildingInfo(aBuildingUniqueList[iBuilding])
				for iReplacement in xrange(CvBuildingInfo.getNumReplacementBuilding()):
					aBuildingReplacementList.append(CvBuildingInfo.getReplacementBuilding(iReplacement))

			#Get unique replacements
			aReplacementUniqueList = []
			for iBuilding in xrange(len(aBuildingReplacementList)):
				if aBuildingReplacementList[iBuilding] not in aReplacementUniqueList:
					aReplacementUniqueList.append(aBuildingReplacementList[iBuilding])

			#Get replacements of requirements, that aren't listed as requirements
			aReplacedRequirements = []
			for iBuilding in xrange(len(aReplacementUniqueList)):
				if aReplacementUniqueList[iBuilding] not in aBuildingUniqueList:
					aReplacedRequirements.append(aReplacementUniqueList[iBuilding])

			#Get unique requirement replacements
			aReplacedUniqueRequirements = []
			for iBuilding in xrange(len(aReplacedRequirements)):
				if aReplacedRequirements[iBuilding] not in aReplacedUniqueRequirements:
					aReplacedUniqueRequirements.append(aReplacedRequirements[iBuilding])

			#Convert to Types
			aBuildingTypeList = []
			for iBuilding in xrange(len(aReplacedUniqueRequirements)):
				aBuildingTypeList.append(GC.getBuildingInfo(aReplacedUniqueRequirements[iBuilding]).getType())

			if len(aBuildingTypeList) > 0:
				self.log(CvUnitInfo.getType()+" requires "+str(aBuildingTypeList))

	#Bonus - check improvement productivity
	def checkBonusImprovementProductivity(self):
		for iBonus in xrange(GC.getNumBonusInfos()):
			CvBonusInfo = GC.getBonusInfo(iBonus)
			#Check total productivity: from resource, improvement, improvement+resource coupling, and with all tech boosts.
			if CvBonusInfo.getConstAppearance() > 0: # Only care about map resources
				for iImprovement in xrange(GC.getNumImprovementInfos()):
					CvImprovementInfo = GC.getImprovementInfo(iImprovement)
					if CvImprovementInfo.getImprovementUpgrade() != -1 or CvImprovementInfo.getNumAlternativeImprovementUpgradeTypes() > 0 or CvImprovementInfo.getImprovementPillage() != -1: # Only care about improvements, that can upgrade or downgrade.
						if CvImprovementInfo.isImprovementBonusTrade(iBonus) and not CvImprovementInfo.isActsAsCity(): # Only care about improvements, that can improve bonus
							#Zero out data
							aBonusYield = [0]*YieldTypes.NUM_YIELD_TYPES
							aImprovementYield = [0]*YieldTypes.NUM_YIELD_TYPES
							aTechImprovementYield = [0]*YieldTypes.NUM_YIELD_TYPES
							aBonusImprovementYield = [0]*YieldTypes.NUM_YIELD_TYPES
							aFinalYield = [0]*YieldTypes.NUM_YIELD_TYPES

							aImprovementUpgradeYield = [0]*YieldTypes.NUM_YIELD_TYPES
							aBonusImprovementUpgradeYield = [0]*YieldTypes.NUM_YIELD_TYPES
							aFinalImpUpgradeYield = [0]*YieldTypes.NUM_YIELD_TYPES
							for iYield in xrange(YieldTypes.NUM_YIELD_TYPES): # Food, Production, Commerce
								aBonusYield[iYield] = CvBonusInfo.getYieldChange(iYield) # Bonus yields
								aImprovementYield[iYield] = CvImprovementInfo.getYieldChange(iYield) # Improvement yields
								aBonusImprovementYield[iYield] = CvImprovementInfo.getImprovementBonusYield(iBonus, iYield) # Bonus-Improvement coupling yields

								for iTech in xrange(GC.getNumTechInfos()):  # Find techs, that boost base improvement
									if CvImprovementInfo.getTechYieldChanges(iTech, iYield) != 0:
										aTechImprovementYield[iYield] += CvImprovementInfo.getTechYieldChanges(iTech, iYield)

								aFinalYield[iYield] = aBonusYield[iYield] + aImprovementYield[iYield] + aTechImprovementYield[iYield] + aBonusImprovementYield[iYield]

								CvImprovementUpgradeInfo = GC.getImprovementInfo(CvImprovementInfo.getImprovementUpgrade())
								if CvImprovementInfo.getImprovementUpgrade() != -1 and CvImprovementUpgradeInfo.isImprovementBonusTrade(iBonus):
									aImprovementUpgradeYield[iYield] = CvImprovementUpgradeInfo.getYieldChange(iYield)
									aBonusImprovementUpgradeYield[iYield] = CvImprovementUpgradeInfo.getImprovementBonusYield(iBonus, iYield)
									aFinalImpUpgradeYield[iYield] = aBonusYield[iYield] + aImprovementUpgradeYield[iYield] + aBonusImprovementUpgradeYield[iYield]

							# Upgrades
							if (CvImprovementInfo.getImprovementUpgrade() != -1 and CvImprovementUpgradeInfo.isImprovementBonusTrade(iBonus)) and (aFinalImpUpgradeYield[0] < aFinalYield[0] or aFinalImpUpgradeYield[1] < aFinalYield[1] or aFinalImpUpgradeYield[2] < aFinalYield[2]):
								self.log(CvImprovementInfo.getType()+" with "+CvBonusInfo.getType()+": F/P/C -> "+str(aFinalYield)+" upgrade: "+CvImprovementUpgradeInfo.getType()+": F/P/C -> "+str((aFinalImpUpgradeYield, (aFinalImpUpgradeYield[0]-aFinalYield[0], aFinalImpUpgradeYield[1]-aFinalYield[1], aFinalImpUpgradeYield[2]-aFinalYield[2]))))

							# Alt upgrades
							for iImprovementUpgrade in xrange(CvImprovementInfo.getNumAlternativeImprovementUpgradeTypes()):
								CvImprovementAltUpgradeInfo = GC.getImprovementInfo(CvImprovementInfo.getAlternativeImprovementUpgradeType(iImprovementUpgrade))
								if CvImprovementAltUpgradeInfo.isImprovementBonusTrade(iBonus):
									aImprovementAltUpgradeYield = [0]*YieldTypes.NUM_YIELD_TYPES
									aBonusImprovementAltUpgradeYield = [0]*YieldTypes.NUM_YIELD_TYPES
									aFinalImpAltUpgradeYield = [0]*YieldTypes.NUM_YIELD_TYPES
									for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
										aImprovementAltUpgradeYield[iYield] = CvImprovementAltUpgradeInfo.getYieldChange(iYield)
										aBonusImprovementAltUpgradeYield[iYield] = CvImprovementAltUpgradeInfo.getImprovementBonusYield(iBonus, iYield)
										aFinalImpAltUpgradeYield[iYield] = aBonusYield[iYield] + aImprovementAltUpgradeYield[iYield] + aBonusImprovementAltUpgradeYield[iYield]
									if (aFinalImpAltUpgradeYield[0] < aFinalYield[0] or aFinalImpAltUpgradeYield[1] < aFinalYield[1] or aFinalImpAltUpgradeYield[2] < aFinalYield[2]):
										self.log(CvImprovementInfo.getType()+" with "+CvBonusInfo.getType()+": F/P/C -> "+str(aFinalYield)+" Alt upgrade: "+CvImprovementAltUpgradeInfo.getType()+": F/P/C -> "+str((aFinalImpAltUpgradeYield, (aFinalImpAltUpgradeYield[0]-aFinalYield[0], aFinalImpAltUpgradeYield[1]-aFinalYield[1], aFinalImpAltUpgradeYield[2]-aFinalYield[2]))))

	#Bonus - check potential bonus producer replacements
	def checkBonusProducerReplacements(self):
		BONUSCLASS_CULTURE = GC.getInfoTypeForString("BONUSCLASS_CULTURE")
		BONUSCLASS_GENMODS = GC.getInfoTypeForString("BONUSCLASS_GENMODS")
		BONUSCLASS_WONDER = GC.getInfoTypeForString("BONUSCLASS_WONDER")

		for iBonus in xrange(GC.getNumBonusInfos()):
			CvBonusInfo = GC.getBonusInfo(iBonus)

			#Check replacements of bonus producers
			if CvBonusInfo.getConstAppearance() == 0 and not (( BONUSCLASS_CULTURE > -1 and CvBonusInfo.getBonusClassType() == BONUSCLASS_CULTURE) or (BONUSCLASS_GENMODS > -1 and CvBonusInfo.getBonusClassType() == BONUSCLASS_GENMODS) or (BONUSCLASS_WONDER > -1 and CvBonusInfo.getBonusClassType() == BONUSCLASS_WONDER)):
			# Check Manufactured bonuses, that aren't Culture or Techno-culture or Unique types.
				aNumBonusManufacturers = [] # Count manufacturers and add their locations
				aBuildingObsoletions = [] # List xgrid of manufacturer tech obsoletions
				for iBuilding in xrange(GC.getNumBuildingInfos()): # Collect statistics about buildings - location of producer and its obsoletion
					CvBuildingInfo = GC.getBuildingInfo(iBuilding)
					if GC.getInfoTypeForString("MAPCATEGORY_EARTH") in CvBuildingInfo.getMapCategories() and not isNationalWonder(iBuilding) and not isWorldWonder(iBuilding): # Exclude space based and wonders
						if CvBuildingInfo.getFreeBonus() == iBonus:
							aNumBonusManufacturers.append(self.HF.checkBuildingTechRequirements(CvBuildingInfo)[0])
							aBuildingObsoletions.append(self.HF.checkBuildingTechObsoletionLocation(CvBuildingInfo)[0])

						for iBonuses in xrange(CvBuildingInfo.getNumExtraFreeBonuses()):
							if CvBuildingInfo.getExtraFreeBonus(iBonuses) == iBonus:
								aNumBonusManufacturers.append(self.HF.checkBuildingTechRequirements(CvBuildingInfo)[0])
								aBuildingObsoletions.append(self.HF.checkBuildingTechObsoletionLocation(CvBuildingInfo)[0])

				# Check all bonus producers
				if len(aNumBonusManufacturers) > 0:
					for iBuilding in xrange(GC.getNumBuildingInfos()):
						CvBuildingInfo = GC.getBuildingInfo(iBuilding)
						if GC.getInfoTypeForString("MAPCATEGORY_EARTH") in CvBuildingInfo.getMapCategories() and not isNationalWonder(iBuilding) and not isWorldWonder(iBuilding): # Exclude space based and wonders
							aBuildingReplacements = [] # List building replacements
							iTechLoc = self.HF.checkBuildingTechRequirements(CvBuildingInfo)[0]
							iObsoleteTechLoc = self.HF.checkBuildingTechObsoletionLocation(CvBuildingInfo)[0]
							for iReplacement in xrange(CvBuildingInfo.getNumReplacementBuilding()):
								CvBuildingReplacement = GC.getBuildingInfo(CvBuildingInfo.getReplacementBuilding(iReplacement))
								aBuildingReplacements.append(CvBuildingReplacement.getType())

							if CvBuildingInfo.getFreeBonus() == iBonus:
								self.log(CvBonusInfo.getType()+" "+str(iTechLoc)+"/"+str(iObsoleteTechLoc)+" Type: "+CvBuildingInfo.getType()+" Replacement: "+str(aBuildingReplacements))

							for iBonuses in xrange(CvBuildingInfo.getNumExtraFreeBonuses()):
								if CvBuildingInfo.getExtraFreeBonus(iBonuses) == iBonus:
									self.log(CvBonusInfo.getType()+" "+str(iTechLoc)+"/"+str(iObsoleteTechLoc)+" Type: "+CvBuildingInfo.getType()+" Replacement: "+str(aBuildingReplacements))

	#Civic - check if civic yield bonus for improvement is carried into its upgrade
	def checkCivicImprovementReplacements(self):
		for iCivic in xrange(GC.getNumCivicInfos()):
			CvCivicInfo = GC.getCivicInfo(iCivic)

			aImprovementList = []
			aImprovementUpgrades = []
			aImprovementUniqueUpgrades = []
			aImprovementsList = []

			if CvCivicInfo.isAnyImprovementYieldChange():
				#Get <ImprovementYieldChanges>
				for iImprovement in xrange(GC.getNumImprovementInfos()):
					if CvCivicInfo.getImprovementYieldChanges(iImprovement, 0) != 0 or CvCivicInfo.getImprovementYieldChanges(iImprovement, 1) != 0 or CvCivicInfo.getImprovementYieldChanges(iImprovement, 2) != 0:
						aImprovementList.append(iImprovement)

				#Analyze list of improvements
				for i in xrange(len(aImprovementList)):
					CvImprovementInfo = GC.getImprovementInfo(aImprovementList[i])
					if CvImprovementInfo.getImprovementUpgrade() != -1:
						iImprovementUpgrade = CvImprovementInfo.getImprovementUpgrade()
						szUpgradedImprovement = GC.getImprovementInfo(iImprovementUpgrade).getType()
						aImprovementUpgrades.append(iImprovementUpgrade)
						for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
							if CvCivicInfo.getImprovementYieldChanges(aImprovementList[i], iYield) > CvCivicInfo.getImprovementYieldChanges(iImprovementUpgrade, iYield):
								self.log(CvCivicInfo.getType()+" "+CvImprovementInfo.getType()+" -> "+szUpgradedImprovement+" yield degradation")
					for iImprovementReplacement in xrange(CvImprovementInfo.getNumAlternativeImprovementUpgradeTypes()):
						iImprovementUpgrade = CvImprovementInfo.getAlternativeImprovementUpgradeType(iImprovementReplacement)
						szUpgradedImprovement = GC.getImprovementInfo(iImprovementUpgrade).getType()
						aImprovementUpgrades.append(iImprovementUpgrade)
						for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
							if CvCivicInfo.getImprovementYieldChanges(aImprovementList[i], iYield) > CvCivicInfo.getImprovementYieldChanges(iImprovementUpgrade, iYield):
								self.log(CvCivicInfo.getType()+" "+CvImprovementInfo.getType()+" alt -> "+szUpgradedImprovement+" yield degradation")

				#We want nonrepeating list
				for i in xrange(len(aImprovementUpgrades)):
					if aImprovementUpgrades[i] not in aImprovementUniqueUpgrades:
						aImprovementUniqueUpgrades.append(aImprovementUpgrades[i])

				#If improvement is listed, then remove it
				for i in xrange(len(aImprovementList)):
					if aImprovementList[i] in aImprovementUniqueUpgrades:
						aImprovementUniqueUpgrades.remove(aImprovementList[i])

				#Get names
				for i in xrange(len(aImprovementUniqueUpgrades)):
					aImprovementsList.append(GC.getImprovementInfo(aImprovementUniqueUpgrades[i]).getType())

				if len(aImprovementsList) > 0:
					self.log(CvCivicInfo.getType()+" should have improvement upgrades for ImprovementYieldChanges "+str(aImprovementsList))

	#Trait - check if trait yield bonus for improvement is carried into its upgrade
	def checkTraitImprovementReplacements(self):
		for iTrait in xrange(GC.getNumTraitInfos()):
			CvTraitInfo = GC.getTraitInfo(iTrait)

			aImprovementList = []
			aImprovementUpgrades = []
			aImprovementUniqueUpgrades = []
			aImprovementsList = []

			#Get <ImprovementYieldChange>
			for iImprovement in xrange(GC.getNumImprovementInfos()):
				if CvTraitInfo.getImprovementYieldChange(iImprovement, 0) != 0 or CvTraitInfo.getImprovementYieldChange(iImprovement, 1) != 0 or CvTraitInfo.getImprovementYieldChange(iImprovement, 2) != 0:
					aImprovementList.append(iImprovement)

			if len(aImprovementList) > 0:
				#Analyze list of improvements
				for i in xrange(len(aImprovementList)):
					CvImprovementInfo = GC.getImprovementInfo(aImprovementList[i])
					if CvImprovementInfo.getImprovementUpgrade() != -1:
						iImprovementUpgrade = CvImprovementInfo.getImprovementUpgrade()
						szUpgradedImprovement = GC.getImprovementInfo(iImprovementUpgrade).getType()
						aImprovementUpgrades.append(iImprovementUpgrade)
						for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
							if CvTraitInfo.getImprovementYieldChange(aImprovementList[i], iYield) > CvTraitInfo.getImprovementYieldChange(iImprovementUpgrade, iYield):
								self.log(CvTraitInfo.getType()+" "+CvImprovementInfo.getType()+" -> "+szUpgradedImprovement+" yield degradation")
					for iImprovementReplacement in xrange(CvImprovementInfo.getNumAlternativeImprovementUpgradeTypes()):
						iImprovementUpgrade = CvImprovementInfo.getAlternativeImprovementUpgradeType(iImprovementReplacement)
						szUpgradedImprovement = GC.getImprovementInfo(iImprovementUpgrade).getType()
						aImprovementUpgrades.append(iImprovementUpgrade)
						for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
							if CvTraitInfo.getImprovementYieldChange(aImprovementList[i], iYield) > CvTraitInfo.getImprovementYieldChange(iImprovementUpgrade, iYield):
								self.log(CvTraitInfo.getType()+" "+CvImprovementInfo.getType()+" alt -> "+szUpgradedImprovement+" yield degradation")

				#We want nonrepeating list
				for i in xrange(len(aImprovementUpgrades)):
					if aImprovementUpgrades[i] not in aImprovementUniqueUpgrades:
						aImprovementUniqueUpgrades.append(aImprovementUpgrades[i])

				#If improvement is listed, then remove it
				for i in xrange(len(aImprovementList)):
					if aImprovementList[i] in aImprovementUniqueUpgrades:
						aImprovementUniqueUpgrades.remove(aImprovementList[i])

				#Get names
				for i in xrange(len(aImprovementUniqueUpgrades)):
					aImprovementsList.append(GC.getImprovementInfo(aImprovementUniqueUpgrades[i]).getType())

				if len(aImprovementsList) > 0:
					self.log(CvTraitInfo.getType()+" should have improvement upgrades for ImprovementYieldChanges "+str(aImprovementsList))

	#Improvement - yield boosts should be between improvement unlock and upgrade
	def checkImprovementTechYieldBoostLocation(self):
		for iImprovement in xrange(GC.getNumImprovementInfos()):
			CvImprovementInfo = GC.getImprovementInfo(iImprovement)
			iTechLoc = self.HF.checkImprovementTechRequirementLocation(CvImprovementInfo)[0]

			if CvImprovementInfo.getImprovementUpgrade() != -1 or CvImprovementInfo.getNumAlternativeImprovementUpgradeTypes() > 0 or CvImprovementInfo.getImprovementPillage() != -1: #Only those, that can upgrade, or are top of upgrade chain
				aTechBoost = []
				CvImprovementUpgradeInfo = GC.getImprovementInfo(CvImprovementInfo.getImprovementUpgrade())
				iImpUpgradeTechLoc = 0
				if CvImprovementUpgradeInfo != None: # Main upgrade
					iImpUpgradeTechLoc = self.HF.checkImprovementTechRequirementLocation(CvImprovementUpgradeInfo)[0]
				for iTech in xrange(GC.getNumTechInfos()):  # Find techs, that boost base improvement
					for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
						if CvImprovementInfo.getTechYieldChanges(iTech, iYield) != 0:
							aTechBoost.append(GC.getTechInfo(iTech).getGridX())
				if aTechBoost and iTechLoc >= min(aTechBoost):
					self.log(CvImprovementInfo.getType()+" Xgrid: "+str(iTechLoc)+" Tech boosts location: "+str(aTechBoost))
				if iImpUpgradeTechLoc and aTechBoost and iImpUpgradeTechLoc <= max(aTechBoost):
					self.log(CvImprovementInfo.getType()+" Xgrid: "+str(iTechLoc)+" Tech boosts location: "+str(aTechBoost)+" Upgrade: "+CvImprovementUpgradeInfo.getType()+": "+str(iImpUpgradeTechLoc))

				#Alt upgrades
				for iImprovementUpgrade in xrange(CvImprovementInfo.getNumAlternativeImprovementUpgradeTypes()):
					CvImprovementAltUpgradeInfo = GC.getImprovementInfo(CvImprovementInfo.getAlternativeImprovementUpgradeType(iImprovementUpgrade))
					iImpAltUpgradeTechLoc = 0
					if CvImprovementAltUpgradeInfo != None: # Alt upgrade
						iImpAltUpgradeTechLoc = self.HF.checkImprovementTechRequirementLocation(CvImprovementUpgradeInfo)[0]
						if iImpAltUpgradeTechLoc and aTechBoost and iImpAltUpgradeTechLoc <= max(aTechBoost):
							self.log(CvImprovementInfo.getType()+" Xgrid: "+str(iTechLoc)+" Tech boosts location: "+str(aTechBoost)+" Alt Upgrade: "+CvImprovementAltUpgradeInfo.getType()+": "+str(iImpAltUpgradeTechLoc))

	#Improvement - base + tech improvement yields compared to upgraded improvement
	def checkImprovementYieldValues(self):
		for iImprovement in xrange(GC.getNumImprovementInfos()):
			CvImprovementInfo = GC.getImprovementInfo(iImprovement)
			if CvImprovementInfo.getImprovementUpgrade() != -1 or CvImprovementInfo.getNumAlternativeImprovementUpgradeTypes() > 0 or CvImprovementInfo.getImprovementPillage() != -1: #Only those, that can upgrade, or are top of upgrade chain
				iTechLoc = self.HF.checkImprovementTechRequirementLocation(CvImprovementInfo)[0]
				#Improvement yield with all techs
				aBaseImprovementYield = [0]*YieldTypes.NUM_YIELD_TYPES
				aBaseUpgradeImprovementYield = [0]*YieldTypes.NUM_YIELD_TYPES
				aTechImprovementYield = [0]*YieldTypes.NUM_YIELD_TYPES
				aTotalImprovementYield = [0]*YieldTypes.NUM_YIELD_TYPES

				CvImprovementUpgradeInfo = GC.getImprovementInfo(CvImprovementInfo.getImprovementUpgrade())
				for iYield in xrange(YieldTypes.NUM_YIELD_TYPES): # Food, Production, Commerce
					aBaseImprovementYield[iYield] = CvImprovementInfo.getYieldChange(iYield) # Improvement yields
					for iTech in xrange(GC.getNumTechInfos()):  # Find techs, that boost base improvement
						if CvImprovementInfo.getTechYieldChanges(iTech, iYield) != 0:
							aTechImprovementYield[iYield] += CvImprovementInfo.getTechYieldChanges(iTech, iYield)
					aTotalImprovementYield[iYield] = aBaseImprovementYield[iYield] + aTechImprovementYield[iYield]
					if CvImprovementUpgradeInfo != None: # Main upgrade
						aBaseUpgradeImprovementYield[iYield] = CvImprovementUpgradeInfo.getYieldChange(iYield)

				if CvImprovementUpgradeInfo != None and (aTotalImprovementYield[0] > aBaseUpgradeImprovementYield[0] or aTotalImprovementYield[1] > aBaseUpgradeImprovementYield[1] or aTotalImprovementYield[2] > aBaseUpgradeImprovementYield[2]):
					self.log(CvImprovementInfo.getType()+" Total F/P/C: "+str(aTotalImprovementYield)+", "+CvImprovementUpgradeInfo.getType()+" Upgrade F/P/C: "+str(aBaseUpgradeImprovementYield))

				for iImprovementUpgrade in xrange(CvImprovementInfo.getNumAlternativeImprovementUpgradeTypes()):
					aBaseAltUpgradeImprovementYield = [0]*YieldTypes.NUM_YIELD_TYPES
					CvImprovementAltUpgradeInfo = GC.getImprovementInfo(CvImprovementInfo.getAlternativeImprovementUpgradeType(iImprovementUpgrade))
					for iYield in xrange(YieldTypes.NUM_YIELD_TYPES):
						aBaseAltUpgradeImprovementYield[iYield] = CvImprovementAltUpgradeInfo.getYieldChange(iYield)
					if aTotalImprovementYield[0] > aBaseAltUpgradeImprovementYield[0] or aTotalImprovementYield[1] > aBaseAltUpgradeImprovementYield[1] or aTotalImprovementYield[2] > aBaseAltUpgradeImprovementYield[2]:
						self.log(CvImprovementInfo.getType()+" Total F/P/C: "+str(aTotalImprovementYield)+", "+CvImprovementAltUpgradeInfo.getType()+" Alt Upgrade F/P/C: "+str(aBaseAltUpgradeImprovementYield))

	#Buildings - noncultural wonders, religious shrines and projects should have wonder movie tag, preferably in DDS format
	def checkBuildingWonderMovies(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			iSpecialBuilding = CvBuildingInfo.getSpecialBuildingType()
			bCultural = 0
			if iSpecialBuilding != -1 and iSpecialBuilding == GC.getInfoTypeForString("SPECIALBUILDING_C2C_CULTURE"):
				bCultural = 1

			if isNationalWonder(iBuilding) or (isWorldWonder(iBuilding) and not bCultural) or CvBuildingInfo.getHolyCity() != -1:
				if CvBuildingInfo.getMovie() != None:
					self.log(CvBuildingInfo.getType()+" has movie in "+CvBuildingInfo.getMovie())
				else:
					self.log(CvBuildingInfo.getType()+" is missing a wonder movie!")

		for iProject in xrange(GC.getNumProjectInfos()):
			CvProjectInfo = GC.getProjectInfo(iProject)
			if not CvProjectInfo.isSpaceship():
				if CvProjectInfo.getMovieArtDef() != "":
					self.log(CvProjectInfo.getType()+" has movie art define tag: "+CvProjectInfo.getMovieArtDef())
				else:
					self.log(CvProjectInfo.getType()+" is missing a wonder movie!")

	#Building and unit - check if main tech requirement is more advanced or equal to tech types, main tech requirement determinates where to put icon in tech tree
	def checkTechTypes(self):
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			aTechList = []
			aTechXY = []

			#Main tech requirement
			iTechMainReq = CvBuildingInfo.getPrereqAndTech()
			if iTechMainReq != -1:
				iTechMainLoc = GC.getTechInfo(iTechMainReq).getGridX()
				iTechMainRow = GC.getTechInfo(iTechMainReq).getGridY()
				aTechList.append(GC.getTechInfo(iTechMainReq).getType())
				aTechXY.append(100*iTechMainLoc+iTechMainRow)

			#Tech Type requirement
			aTechTypeLocList = []
			aTechTypeRowList = []
			for iTechType in CvBuildingInfo.getPrereqAndTechs():
				aTechList.append(GC.getTechInfo(iTechType).getType())
				aTechXY.append(100*GC.getTechInfo(iTechType).getGridX()+GC.getTechInfo(iTechType).getGridY())

			if len(aTechXY) > 1 and 100*iTechMainLoc+iTechMainRow != max(aTechXY):
				self.log(CvBuildingInfo.getType()+" Main tech isn't most advanced, switch it to "+str(aTechList[aTechXY.index(max(aTechXY))]))

		for iUnit in xrange(GC.getNumUnitInfos()):
			CvUnitInfo = GC.getUnitInfo(iUnit)
			aTechList = []
			aTechXY = []

			#Main tech requirement
			iTechMainReq = CvUnitInfo.getPrereqAndTech()
			if iTechMainReq != -1:
				iTechMainLoc = GC.getTechInfo(iTechMainReq).getGridX()
				iTechMainRow = GC.getTechInfo(iTechMainReq).getGridY()
				aTechList.append(GC.getTechInfo(iTechMainReq).getType())
				aTechXY.append(100*iTechMainLoc+iTechMainRow)

			#Tech Type requirement
			aTechTypeLocList = []
			aTechTypeRowList = []
			for iTechType in CvUnitInfo.getPrereqAndTechs():
				aTechList.append(GC.getTechInfo(iTechType).getType())
				aTechXY.append(100*GC.getTechInfo(iTechType).getGridX()+GC.getTechInfo(iTechType).getGridY())

			if len(aTechXY) > 1 and 100*iTechMainLoc+iTechMainRow != max(aTechXY):
				self.log(CvUnitInfo.getType()+" Main tech isn't most advanced, switch it to "+str(aTechList[aTechXY.index(max(aTechXY))]))

	#Building - list buildings, that obsolete without replacement
	def listObsoleteingBuildings(self):
		aSpecialReplacementsList = ["BUILDING_POLLUTION_BLACKENEDSKIES", "BUILDING_GAMBLING_BAN", "BUILDING_ALCOCHOL_PROHIBITION", "BUILDING_DRUG_PROHIBITION", "BUILDING_PROSTITUTION_BAN"]
		aObsoleteTechList = [0]*GC.getNumTechInfos()
		szText = ""
		for iBuilding in xrange(GC.getNumBuildingInfos()):
			CvBuildingInfo = GC.getBuildingInfo(iBuilding)
			aReplacementList = []

			if not isNationalWonder(iBuilding) and not isWorldWonder(iBuilding) and CvBuildingInfo.getProductionCost() > 0 and CvBuildingInfo.getObsoleteTech() != -1:
				for i in xrange(CvBuildingInfo.getNumReplacementBuilding()):
					if GC.getBuildingInfo(CvBuildingInfo.getReplacementBuilding(i)).getType() not in aSpecialReplacementsList:
						aReplacementList.append(CvBuildingInfo.getReplacementBuilding(i))

				if len(aReplacementList) == 0:
					self.log(CvBuildingInfo.getType()+" obsoletes at "+GC.getTechInfo(CvBuildingInfo.getObsoleteTech()).getType()+" without valid replacement")
					aObsoleteTechList[CvBuildingInfo.getObsoleteTech()] += 1

		szText = " Regular obsoleting buildings without replacements: "
		for i in xrange(len(aObsoleteTechList)):
			if aObsoleteTechList[i] > 0:
				szText += str(aObsoleteTechList[i])+" items at "+GC.getTechInfo(i).getType()+", "
		self.log(szText)