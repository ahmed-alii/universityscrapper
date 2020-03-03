Task: Scraping University Rankings

Language to use: Python 3

You should work in a virtual environment and install the required libraries in it. You can also lookup venv docs on web. Also need to provide the requirements.txt file. Understanding the following question is also part of the task.

QS World University Rankings is an annual publication of university rankings by Quacquarelli Symonds. With over a thousand universities from all over the world, you are required to sort out countries based on their university rankings. 

Your Task is divided into 2 sub-tasks:
Data Collection
Data Analysis


Section 1: Data Collection

For this task you need to crawl the site “https://cwur.org/2018-19.php” and gather university ranking data that will be used later on for analysis. You have to collect these following fields and save them in either JSON or CSV format file:

World Rank
Institution Name
Location
Score


Bonus: Pick the university domain








Example Output Sample: The output shown below is in JSON format, you may come up with a better structured JSON that will help in analysing.

[
        {
            "university": "Harvard",
            "ranking": 1,
            "location": "USA",
	     "score": "100",
	     "domain": "harvard.edu"
        },
	…
 ]


Section 2: Data Analysis

Now you have done section 1 successfully, your job is to do some meaningful analysis on the gathered data. By reading your output file saved in section 1, display the average ranking per country. This will be done by taking the average of all ranking of a particular country. (Average: less is better)

Country: USA
Universities: Harvard, Stanford, UOF
Total universities: 3
Average ranking: 3

Country: Japan
Universities: Tokyo, Kyoto, Osaka
Total universities: 3
Average ranking: 30


Bonus Task: Display the statistics in more appealing graphical form.





Deliverables

Source Code (Can be multiple files.)
JSON / CSV output file.
Readme: How to run your code.
Requirements.txt file.
A Document that will contain the following:
Screen-Shots of the outputs.
The technology stack and why you chose it.
Hours it took to complete the task.
Any other improvements you would make if you had more time.


NOTE: 
You are advised to use around 3 seconds download delay between consecutive requests to the server to avoid getting blocked. You can also search the web for methods to avoid blocking.
