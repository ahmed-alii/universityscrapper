To run the code;
Make sure you have python3.x. 

Open the project folder.
Install the dependencies using => pip install -r requirements.txt

To scrape the data:
-- cd to arbisoft > scrapper directory
-- run scrape.py using => python scrape.py
-- wait for the scraping to finish.
-- it will write 2 files; 
---- URL_LIST.csv -> contains all URLS of 1000 universities data.
---- data.csv -> contains all details of all universities

To find the rankings:
-- simply run => python run.py
-- type in the country name

To run the server:
-- run command => python app.py
-- server will start listening on localhost:5000

A demo can be found at:
https://unirank.herokuapp.com