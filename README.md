Create API’s using scrapy.

This is an example to illustrate, how scrapy can be used to create unofficial API’s. Scrapy is used for web page scraping and flask web framework is used for serving the json response.

**Note:** Use this official project from scrapinghub [scrapyrt](https://github.com/scrapinghub/scrapyrt). It provides
a lot of options and functionalities.

<h3>Usage</h3>
```
$ python main.py
```

In browser open http://127.0.0.1:5000/home/news

<h3>Requirements</h3>
scrapy<br>
flask

<h3>Example</h3>
In this example, I have created an api for engadget.com 

Sample JSON response showing the headlines and stories from the home page.
```
{
  "headlines": [
    "John Boehner, politics and Taylor Swift GIFs", 
    "A month with Sony's A7 II mirrorless camera"
  ], 
  "stories": [
    "Sprint snags its first Lumia smartphone", 
    "New York governor wants statewide 100Mbps internet by 2019", 
    "Lizard Squad's paid cyberattack service faces a hack of its own", 
    "NSA brags about turning the tables on cyberwarfare hackers", 
    "Best of CES 2015 Awards, TV Product: LG Art Slim 4K OLED TV", 
    "Sling TV's success, selfie brushes and other stories you might've missed this week", 
    "Best of CES 2015 Awards, Disruptive Tech: Energous WattUp", 
    "Polaris is now in the e-bike business after buying Brammo", 
    "Best of CES 2015 Awards, Home Theater: Sling TV", 
    "DEA kept records of US phone calls for nearly 15 years"
  ]
}
```

<h3>Creating your own api</h3>
1. Create a new spider.
2. Add it to the imports in apiengine.py
3. In main.py do this, apiengine.start('spider_name')

<h3>Suggestions</h3>
If there is a better way of doing the same, feel free to create a pull request or provide your suggestions by opening an issue.
