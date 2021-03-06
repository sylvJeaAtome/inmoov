# ##############################################################################
#						*** RIGHT HAND ***
# ##############################################################################

# Thumb------pin 2
# Index------pin 3
# Majeure----pin 4
# RingFinger-pin 5
# Pinky------pin 6
# wrist------pin 7
 
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
try:
	CheckFileExist(ThisSkeletonPart)
	ThisSkeletonPartConfig = ConfigParser.ConfigParser()
	ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

	isRightHandActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isRightHandActivated') 
	autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')
except:
	errorSpokenFunc('ConfigParserProblem','leftarm.config')
	pass
    
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isRightHandActivated==1 and (ScriptType=="RightSide" or ScriptType=="Full"):
	if RightPortIsConnected:
		talkEvent(lang_startingRightHand)
		rightHand = Runtime.create("i01.rightHand", "InMoovHand")
				
		rightHand.thumb.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'thumb'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'thumb')) 
		rightHand.index.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'index'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'index'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'index'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'index')) 
		rightHand.majeure.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'majeure'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'majeure')) 
		rightHand.ringFinger.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'ringFinger'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'ringFinger')) 
		rightHand.pinky.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'pinky'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'pinky'))
		rightHand.wrist.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'wrist'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'wrist'))
		
		rightHand.thumb.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'thumb'))
		rightHand.index.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'index'))
		rightHand.majeure.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'majeure'))
		rightHand.ringFinger.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'ringFinger'))
		rightHand.pinky.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'pinky'))
		rightHand.wrist.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'wrist'))
		
		rightHand.thumb.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'thumb'))
		rightHand.index.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'index'))
		rightHand.majeure.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'majeure'))
		rightHand.ringFinger.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'ringFinger'))
		rightHand.pinky.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'pinky'))
		rightHand.wrist.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'wrist'))
		
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'thumb'):
			rightHand.thumb.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'index'):
			rightHand.index.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'majeure'):
			rightHand.majeure.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'ringFinger'):
			rightHand.ringFinger.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'pinky'):
			rightHand.pinky.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'wrist'):
			rightHand.wrist.setInverted(True)
		
		i01.startRightHand(MyRightPort)
		
			
		if autoDetach:
			rightHand.thumb.enableAutoAttach(1)
			rightHand.index.enableAutoAttach(1)
			rightHand.majeure.enableAutoAttach(1)
			rightHand.ringFinger.enableAutoAttach(1)
			rightHand.pinky.enableAutoAttach(1)
			rightHand.wrist.enableAutoAttach(1)
		
		rightHand.rest()
		sleep(1)
		rightHand.detach()
		
	else:
		#we force parameter if arduino is off
		isRightHandActivated=0
		
#todo set inverted
