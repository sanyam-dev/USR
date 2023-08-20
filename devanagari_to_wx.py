markers = {"Ora", "evaM", "waWA", "agara", "yaxi", "wo", "kyoMki", 
					"isIlie","jabaki","yaxyapi","waWApi","yaxyapi","Pira BI"
					"lekina","kiMwu","paraMwu","jaba","waba","yA","aWavA"}


discourse_relation = {
	"Ora" : "samuccaya",
	"evaM" : "samuccaya",
	"waWA" : "samuccaya",
	"agara" : "AvaSyakwA-pariNAma",
	"yaxi" : "AvaSyakwA-pariNAma",
	"wo" : "AvaSyakwA-pariNAma",
	"kyoMki" : "karya-kAraNa",
	"isIlie" : "karya-kAraNa",
	"jabaki" : "vyABicAra",
	"yaxyapi" : "vyABicAra",
	"waWApi" : "vyABicAra",
	"Pira BI" : "vyABicAra",
	"lekina" : "viroXi",
	"kiMwu" : "viroXi",
	"paraMwu" : "viroXi",
	"jaba" : "samAnakAla",
	"waba": "samAnakAla",
	"yA": "anyatra",
	"aWava": "anyatra",	
}

discourse_pos = {
	"samuccaya" : 0,
	"anyatra": 0,
	"samAnakAla":0,
	"viroXi": 2,
	"vyABicAra":1,
	"karya-kAraNa": 2,
	"AvaSyakwA-pariNAma": 1
}

def marker_pos_discourse(str1, str2):
	words1 = [str1.split()]
	words2 = [str2.split()]
	
	for word in words1:
		if word in markers:
			print(word)
			return discourse_relation[word]
	
	for word in words2:
		if word in markers:
			print(word)
			return discourse_relation[str(word)]
		


sent1 = "merI pehlI gADZI coTI WI"
sent2 = "lekina xUsarI gAdZI Limousine ke AkAra kI hE"

print(marker_pos_discourse(sent1, sent2))