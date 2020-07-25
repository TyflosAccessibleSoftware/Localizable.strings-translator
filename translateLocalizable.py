from googletrans import Translator

originFile = "./Localizable.strings"
destinationLanguage = ''

def translateValue(valueString, language):
	translator = Translator()
	print("Translating: " + valueString + "\"...")
	result = translator.translate(valueString,dest = language).text
	if result == '':
		result = '"[Error in translation]'
		print("Error in translation!")
	return result

def parseString(line):
	specialChar = 0
	status = 0
	resultKey = ""
	resultValue = ""
	for char in line:
		if char == '\\':
			specialChar = 1
		if char == '"':
			if specialChar == 0:
				status = status + 1
			else:
				specialChar = 0
		if status == 1 :
			resultKey = resultKey + char
		if status == 3 :
			resultValue = resultValue + char
	resultValue = translateValue(resultValue, destinationLanguage)
	return resultKey + '" = ' + resultValue + '";\n'

def startProcess(originFilePath, destinationFilePath):
	originFile = open(originFilePath, "r")
	destinationFile = open(destinationFilePath, "w")
	for currentRawLine in originFile:
		currentLine = currentRawLine.strip()
		if currentLine.startswith('"'):
			destinationFile.write(parseString(currentLine))
		else:
			destinationFile.write(currentLine)
	originFile.close()
	destinationFile.close()

def introduction():
	print('TranslateLocalizable script')
	print('Version 1.0')

def getDestinationLanguage():
	tmpDestinationLanguage = input('Type the ID language destination>> ')
	print('\nDestination language = "' + tmpDestinationLanguage + '"\n\n')
	return tmpDestinationLanguage.strip()

introduction()
destinationLanguage = getDestinationLanguage()
destinationFile = originFile + "-" + destinationLanguage
startProcess(originFile, destinationFile)