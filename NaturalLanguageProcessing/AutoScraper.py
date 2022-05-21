from autoscraper import AutoScraper

url='https://ibm-learning.udemy.com/organization/home/'
wanted_list=['Newest to Udemy Business','REST API testing using C# RestSharp and SpecFlow','4.3']

scrapper = AutoScraper.build(url,wanted_list)
print(scrapper)