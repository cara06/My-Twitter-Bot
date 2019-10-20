# My Twitter Bot

Python Twitter Bot 

1.To use the Twitter bot,you need to have Python 3 installed on your system.
This bot uses tweepy module.
You can install tweepy by using pip command as follows:

 $ pip install tweepy

2.Next,you create a new app on Twitter. 
This can be done by either using your existing account or you can create a new one.
Creating a new account for a bot is better so that your original Twitter account does not get banned.
To create a new application on Twitter, visit the URL below:
 https://apps.twitter.com/

3.Fill all details required to create the new app. Then click on "Key and Access Token" tab under app settings.
There, you will get your app's Consumer Key and Consumer secret key (API Key & API Secret). 
You also need to get Access Token and Access Token Secret of your app. We will use these values in next step.
You need to generate Access Token for first time.


4.Edit credentials.py and copy-paste  all your details carefully.


5.Now,you can run  mytwitterbot_status.py file to run bot which will tweet The Zen of Python texts by using this command :


 $ python mytwitterbot_status.py 
 



6.You can also use any file instead of quotes.txt . To do that,you need to open mytwitterbot_status.py file and edit this line my_file=open('quotes.txt','r') and enter your desired filename instead of 'sample.txt' .



7.Enjoy the service of Twitter Bot which tweets texts of a file .You can also alter sleep time in script as you wish.







# Twitter bot which retweet,like,and follow

8.Use mytwitterbot_retweet.py file for a Twitter bot which retweet tweets based on particular hashtag (script provided here use #100DaysofCode ),like tweets and follow the user who tweeted it .Set your desired Bot settings such as QUERY,LIKE,FOLLOW in config.py file  To run twitterbot_retweet.py ,use this command :

$ python mytwitterbot_retweet.py




9.You can use any desired hashtag(such as #bbnaija ) .Just edit hashtag '#100DaysofCode' in mytwitterbot_retweet.py file with whatever you want.


10. You can also edit code if you do not want your bot to follow  users or you do not want your bot to like tweets.


11.You can also deploy Twitter bot on online based servers if you want to run the bot 24 hours continuously. Take care of sleep/delay if you run bot the whole day.You should try to use large sleep time so that your account does not get banned.






