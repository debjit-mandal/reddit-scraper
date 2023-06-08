# Reddit Scraper
Reddit Scraper made using Python


To scrape Reddit using Python, we have to use the praw library, which is a Python wrapper for the Reddit API. Follow the steps below to get started:

1.Install the praw library by running the following command in your terminal or command prompt:

`pip install praw`

2.Create a Reddit developer application:

Go to https://www.reddit.com/prefs/apps and log in to your Reddit account.

Scroll down to the "Developed Applications" section and click on "Create App".

Fill in the required fields (name, description, etc.).

Set the "App type" to "script".

Enter a redirect URI (you can use http://localhost:8080 for testing purposes).

Click on "Create app" to create your application.

Note down the "Client ID" and "Client Secret" values.

Make sure to replace 'YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET', and 'YOUR_USER_AGENT' with your actual Reddit developer application values. 

Also, adjust the `subreddit_name` and `num_posts` variables according to your requirements.

### Sample Output

````
Title: People who haven't pooped in 2019 yet, why are you still holding on to last years shit?
Score: 221998
Author: ShoddySubstance
URL: https://www.reddit.com/r/AskReddit/comments/ablzuq/people_who_havent_pooped_in_2019_yet_why_are_you/
Number of Comments: 7975
Comments:
-  But when I finally do, it'll be the years biggest shit ^^^^^so ^^^^^far
-  I've been pissing out my ass all fuckin day.
-  Bold of you to assume I'm going to take a shit this year.
---
Title: How would you feel about Reddit adding 3 NSFW filters to distinguish between porn, gore, and repetitive posts asking how you would feel about Reddit adding 2 NSFW filters to distinguish between porn and gore?
Score: 217923
Author: SoupIsAHotSmoothie
URL: https://www.reddit.com/r/AskReddit/comments/l7530r/how_would_you_feel_about_reddit_adding_3_nsfw/
Number of Comments: 2914
Comments:
-  While we're at it can we add a fourth filter for posts asking if you'd be willing to stub your toe for a billion dollars?
-  HOW DO YOU FEEL ABOUT HOW DO YOU FEEL POSTS ABOUT HOW YOU FEEL????
-  [removed]
---
Title: Would you watch a show where a billionaire CEO has to go an entire month on their lowest paid employees salary, without access to any other resources than that of the employee? What do you think would happen?
Score: 197596
Author: txhorns1330
URL: https://www.reddit.com/r/AskReddit/comments/f08dxb/would_you_watch_a_show_where_a_billionaire_ceo/
Number of Comments: 13394
Comments:
-  They'd be fine.

The problem with poverty is not usually day-to-day costs. People can adjust to that.  It's unexpected expenses that are crippling.

~~*Edit: Why are people still responding two weeks later! Nobody is reading this thread any more! At least not the responses at the bottom*~~ (Edit2: rant was too whiney. If you have something to say, who am I to say otherwise?)
-  I doubt a month is enough to really feel the effect
-  It would be better if they had to live *with* their lowest salaried employee for a month or two, imo.   
In their house, dinner with the family, travel to and from work together, same lunch, kids with homework, the works.

Building that relation would imo do much more for this problem than just "experiencing below your normal standard of living before returning to it"..   
You're more likely to feel empathy for a family you know, and much less likely to forget them.

Anything else would just be another show about *wealthy people having a fun adventure to talk about at cocktail parties*
---
Title: What if God came down one day and said "It's pronounced 'Jod' then left?
Score: 195924
Author: esi_disi
URL: https://www.reddit.com/r/AskReddit/comments/iwedc5/what_if_god_came_down_one_day_and_said_its/
Number of Comments: 10313
Comments:
-  *What if Jod was one of us?*
-  A large chunk of my taking the lord's name in vain would go away.
-  Do you want a Holy War? Because that's how you get a Holy War.
---
Title: How would you feel about a feature where if someone upvotes a crosspost, the original post is upvoted automatically?
Score: 186439
Author: Ka1-
URL: https://www.reddit.com/r/AskReddit/comments/draola/how_would_you_feel_about_a_feature_where_if/
Number of Comments: 2794
Comments:
-  what about subs that crosspost from other subs to mock them?
-  The karmaceutical companies would be outraged.
-  [deleted]
---
Title: How would you feel about a "if you accidentally scroll to the top, you can go back to where you were," button for Reddit?
Score: 182981
Author: Cheap_Double9726
URL: https://www.reddit.com/r/AskReddit/comments/kr8op6/how_would_you_feel_about_a_if_you_accidentally/
Number of Comments: 4327
Comments:
-  For some reason, reddit cannot be reached when loading the area you were at previously, and thus something went wrong with the scrolling back. Just don't panic!
-  can i post this question next week? mum said it’s my turn.
-  Found this after accidentally losing my place and starting at the top. Give me my place back, Reddit!
---
Title: Stan Lee has passed away at 95 years old
Score: 175369
Author: -eDgAR-
URL: https://www.reddit.com/r/AskReddit/comments/9whgf4/stan_lee_has_passed_away_at_95_years_old/
Number of Comments: 27938
Comments:
-  Not only did this man create an empire that almost everyone loves, but he was a genuine man who just loved to see people smile. 

I had the pleasure of working under him for some pop culture conventions and all he wanted was to see fans smile and enjoy his legacy.  He loved to joke with those around him, and he would tease the ever loving hell out of everyone he could.  

I remember him using his motorised scooter to get around backstage and his poor assistant would speed walk to keep up with him, but he would just keep increasing the speed until she was running beside him. A wicked grin on his face the whole time. 

Or how he would constantly make his staff repeat themselves "what I didn't hear you!" Untill they had repeated themselves four times, witnessing that initially made me sad, thinking his hearing was poor, until he looks at me with that same grin and winks.  

My time with him was short, but I'm so glad I got it, this man changed my life before I even met him, and he made a huge impact when I did as well.   

RIP Stan.  
-  Was really hoping he'd get to see Avengers 4, but at least he did get to see and interact with his creations on the big screen.

RIP.


-  His wife passed away not too long ago, too. It must have been lonely to all of a sudden be without his life partner...
---
Title: Reddit, how would you feel about a law that bans radio stations from playing commercials with honking/beeping/siren noises in them?
Score: 160342
Author: san69cor
URL: https://www.reddit.com/r/AskReddit/comments/9gx68l/reddit_how_would_you_feel_about_a_law_that_bans/
Number of Comments: 6761
Comments:
-  I would feel like "finally. Lawmakers taking the public's issues to heart."
-  I agree, and any ad for a auto service shop that plays squealing brakes or ominous engine sounds as well. 
-  Reddit, how do you feel about [common Reddit opinion]?

Edit: The fact that this is #3 for top of this year astounds me.
---
Title: Bill Gates said, "I will always choose a lazy person to do a difficult job because a lazy person will find an easy way to do it." What's a real-life example of this?
Score: 154338
Author: lauvnoodles
URL: https://www.reddit.com/r/AskReddit/comments/himsju/bill_gates_said_i_will_always_choose_a_lazy/
Number of Comments: 14901
Comments:
-  I was working as a stockboy in a supermarket and when we had to fill the milk cooler people would bust open a 12 pack of milk cartons and put them in one by one. 

On my first day I just placed the 12 pack in the cooler and cut the plastic off on one side with my box cutter and yanked it from under it and the look of the store manager and the other employee who was training me was pure bewilderment.

From that day everyone did it my way.
-  Start of lockdown, my 9 year old son was having worksheets emailed to complete at home. One day, left him at the laptop doing his maths while I made some dinner with my 3 year old daughter. Walked into the living room with his dinner to find him asking the Alexa all of his maths questions.
-  Worked as a laborer at a nursery one summer. Daily tasks included manually watering 15,000 plants each day. Put together a back of the napkin plan to build an irrigation system and spent the next few weeks building it with some money from the boss. That system is still running 15 years later and does all the work now. I did automate myself out of the job and had to find another eventually. 

Couple years later got my engineering degree. I’m convinced Engineers are inherently lazy people that will spend a disproportionate effort to make things easier.
---
Title: What if Earth is like one of those uncontacted tribes in South America, like the whole Galaxy knows we're here but they've agreed not to contact us until we figure it out for ourselves?
Score: 152117
Author: slim_p_
URL: https://www.reddit.com/r/AskReddit/comments/kka536/what_if_earth_is_like_one_of_those_uncontacted/
Number of Comments: 8619
Comments:
-  And crop circles are just teenager aliens doing graffitti.
-  That’s the premise of hitchhikers guide to the galaxy except for the waiting for us to figure it out part
-  I mean we could always just be cosmic ants.

How often do you go out to your garden and try to communicate with the bugs?
````
To run this code locally:

`git clone https://github.com/debjit-mandal/reddit-scraper`

`cd reddit-scraper`

`python main.py`

Feel free to suggest any kind of improvements.
