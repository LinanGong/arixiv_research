
There are 3 directories: Arxiv, conference, analysis
Followings are their functions:

***********************************************************************************

Arxiv      -------   	collecting arXiv data

conference -------   	collecting conference data

analysis   -------   	processing data, 
			computing similarities, 
			building matching model, 
			paper matching,
			evaluation,
			plotting figures
***********************************************************************************


Then important code files and materials in each directories are listed:


***********************************************************************************
				------------------
				|     Arxiv      |
				------------------
arXiv_metadata.py             	--------   	harvesting arxiv metadata         
arXiv_parse_metadata.py       	--------   	parsing xml files


datafiles                     	--------   	metadata xml files
arxiv_parsed_data	        --------   	extracted arXiv data

***********************************************************************************



***********************************************************************************
				------------------
				|   conference   |
				------------------
conference/spiders            	--------   	crawling conference data

xxxxxxxx.json			--------   	conference data

***********************************************************************************



***********************************************************************************
				------------------
				|    analysis    |
				------------------
preprocess.py			--------			data preprocessing
error_data_remove.py		--------			remove error data
features.py			--------			the features of arXiv data
similarity.py			--------			compute similarities
evaluation.py			--------			similarity algorithm evaluation
logistic_model.py		--------			building the logistic model
trend_of_conference.py		--------			plot the trends
icml2012_matched_dates.py	--------			explain the data of ICML2012
deadlines.py			--------			

arXiv 				--------			the processed arXiv data
sim_files			--------			dataset after computing similarities
samples				--------			random samples and labeled data
model 				--------			the well-building model
deadlines.txt 			--------			conference deadlines
pictures			--------			the plots of analysis

************************************************************************************



