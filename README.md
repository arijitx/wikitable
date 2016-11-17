# wikitable
wikitable is a python script to scrap Wikipedia tables into Pandas DataFrame or a List of Dictionaries .

# Example

		python wikitable.py 
		================================================================
		                   Country GDP\n(millions of US$) Rank
		0                 World[8]             75,212,696     
		1            United States             18,561,930    1
		2   European Union[n 1][8]             16,518,723    —
		3               China[n 2]             11,391,619    2
		4                    Japan              4,730,300    3

		[5 rows x 3 columns]
		 
		 
		================================================================
		                   Country GDP\n(millions of US$) Rank
		0                    World             73,433,644     
		1            United States             17,946,996    1
		2   European Union[n 1][9]             16,229,464    —
		3               China[n 7]             10,866,444    2
		4                    Japan              4,123,258    3

		[5 rows x 3 columns]
		 
		 
		================================================================
		                    Country GDP\n(millions of US$) Rank
		0                 World[10]             78,037,089     
		1   European Union[n 1][11]             18,518,430    —
		2             United States             17,348,072    1
		3                China[n 7]             10,430,590    2
		4                     Japan              4,602,419    3

		[5 rows x 3 columns]
		 




		python wikitable.py https://en.wikipedia.org/wiki/List_of_Indian_states_and_union_territories_by_GDP
		================================================================
		                                   GSDP Rank       State/UT
		0  ₹125.41 lakh crore (US$1.9 trillion)               India
		1     ₹16.8 lakh crore (US$250 billion)    1    Maharashtra
		2     ₹9.76 lakh crore (US$150 billion)    2     Tamil Nadu
		3     ₹9.76 lakh crore (US$150 billion)    3  Uttar Pradesh
		4     ₹8.00 lakh crore (US$120 billion)    4    West Bengal

		[5 rows x 3 columns]
		 
		 
		================================================================
		  2001–02\nin ₹ Crore 2002–03\nin ₹ Crore 2003–04\nin ₹ Crore  \
		0           2,097,726           2,261,415           2,538,170   
		1             156,711             167,096             190,017   
		2               2,104               2,071               2,368   
		3              38,313              43,407              47,305   
		4              57,657              64,965              66,174   

		  2004–05\nin ₹ Crore 2005–06\nin ₹ Crore 2006–07\nin ₹ Crore  \
		0           2,971,464           3,390,503           3,953,276   
		1             224,713             255,941             301,035   
		2               3,488               3,755               4,108   
		3              53,398              59,385              64,692   
		4              77,781              82,490             100,737   

		  2007–08\nin ₹ Crore 2008–09\nin ₹ Crore 2009–10\nin ₹ Crore  \
		0           4,582,086           5,303,567           6,108,903   
		1             364,813             426,765             476,835   
		2               4,810               5,687               7,474   
		3              71,076              81,074              95,975   
		4             113,680             142,279             162,923   

		  2010–11\nin ₹ Crore 2011–12\nin ₹ Crore 2012–13\nin ₹ Crore  \
		0           7,248,860           8,391,691           9,388,876   
		1             583,762             662,592             754,409   
		2               9,013              10,619              12,091   
		3             112,688             125,820             141,621   
		4             204,289             247,318             313,995   

		  2013–14\nin ₹ Crore 2014–15\nin ₹ Crore State/union territory  
		0          10,472,807                                     India  
		1             857,364             520,030        Andhra Pradesh  
		2              13,382              15,588     Arunachal Pradesh  
		3             162,652             183,798                 Assam  
		4             368,337             402,283                 Bihar  

		[5 rows x 15 columns]
		 
		 
		================================================================
		  2010–11 % Growth 2011–12 % Growth 2012–13 % Growth 2013–14 % Growth  \
		0            18.66            15.77            11.88            11.54   
		1            17.03            13.25            13.20            13.20   
		2            20.59            17.82            13.86            10.68   
		3            17.41            11.65            12.56            14.85   
		4            25.39            21.06            26.96               25   

		  State/union territory  
		0                 India  
		1        Andhra Pradesh  
		2     Arunachal Pradesh  
		3                 Assam  
		4                 Bihar  

		[5 rows x 5 columns]
		 
