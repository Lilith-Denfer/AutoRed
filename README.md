# AutoRed
An app crafted to help post your smut online, namely Reddit

## Installation and Set-Up

The only required library is `praw`.
You may potentially need to install the `clean-text` module as well.

Install it as:
```console
$ pip3 install praw
$ pip3 install clean-text
```

Also, you'll have to create a Reddit app of type `script` from https://www.reddit.com/prefs/apps/, and put the `CLIENT_ID`, `CLIENT_SECRET` and `USERNAME` in the file `config.ini`.

You may also include a `WAIT` time (time the console will take between posts and loading dots, but a default is included)
and\or a `PASSWORD` field, which bypasses the console asking for a password input each time the app is launched; Both of these are OPTIONAL.

## IMPORTANT Tips
With the reddit api, posting to your user page is formatted as a subreddit called: u_[yourusernamegoeshere]

You can open and write .csv files using google sheets or excel.

The `time.txt` file determines when you last posted, and will include a message if it hasn't been 24 hours since your last post to account for subreddits with 24 hour post limits.

The comment formatted in the `comments.json` file includes two different promotions, if you not want anything added to your comment, just write them as empty strings, or `""`. If you don't want a general string, use `""` as well. Unfortunately the current version of the app doesn't include the option to turn off automatic commenting, because it was developed with me in mind; I may add it in a future version. The general string is always included in the comment, and is sort of a general tagline. The 'sub promo' comment is meant for plugging a subreddit and the 'OF promo' is used for plugging an OnlyFans or Manyvids etc.

Internal imgur links must be used, as reddit doesn't allow internal image hosting on NSFW subreddits. The mobile app has a bug that allows it, but if we're using the api we have to host elsewhere. Internal imgur links take the form of https://i.imgur.com/file.jpg, instead of the usual https://imgur.com/image, and directly point to an image rather than the website. Videos are also allowed in the checks using links to `redgifs.com`.


## Usage

After specifying the details of the comments in the `info.json` file, including the csv files `posts.csv` and `subreddits.csv`, and adding the files `time.txt` and `config.ini` to the same directory as AutoRed.py, run the following. Use the provided samples as templates. 

```console
(You will need to navigate the console to the directory containing everything first, this is what my bash script does automatically on my copy of the app. On Mac this would look like `cd Users/your_user_path/Documents/AutoRed`, where cd stands for current directory, and you would specify the path.)

$ python3 AutoRed.py 
...
```

## Example Runs
Loading from CSV and posting:
•———————————————————————————————————————————————————————————————•
• Starting AutoRed 4.0
•
•
• Welcome to AutoRed:
• An excellent app crafted to help post your smut online ;)
•
•
• Would you like to read from CSV? (Y/N) y
•
• Title: Wouldn't you like this view every night? 🍆💦
• Url: https://i.imgur.com/AEqNpoF.png
•
• Does this look okay? (Y/N) y
•
• Posted on Alilofeverything. Post ID: v7um29
• Posted on bigdickgirl. Post ID: v7um2w
• Posted on BisexualFantasy. Post ID: v7um3c
• Posted on Cumrades. Post ID: v7um43
• Posted on dickgirlporn. Post ID: v7um4l
• Posted on dickgirls. Post ID: v7um5l
• Posted on EnbyLewds. Post ID: v7um69
• Posted on FemBoys. Post ID: v7um6w
• Posted on Feminization. Post ID: v7um7g
• Posted on ForeskinnyGirls. Post ID: v7um7x
• Posted on GoneWildTrans. Post ID: v7um8t
• Posted on GOONED. Post ID: v7um9a
• Posted on gurlslikeus. Post ID: v7um9z
• Posted on HerCocksBigger. Post ID: v7umaw
• Posted on ImCravingCock. Post ID: v7umbe
• Posted on LGBTGoneWild. Post ID: v7umbz
• Posted on OnlyIfShesPackin. Post ID: v7umcg
• Posted on queerbodies. Post ID: v7umd2
• Posted on Safe4Trans. Post ID: v7umdv
• Posted on ShemaleBeauty. Post ID: v7umei
• Posted on Shemalelove. Post ID: v7umey
• Posted on Shemales. Post ID: v7umfe
• Posted on ShemalesParadise. Post ID: v7umg0
• Posted on Sissies. Post ID: v7umgr
• Posted on TgirlHUB. Post ID: v7umhc
• Posted on Tgirls. Post ID: v7umi8
• Posted on TgirlXXX. Post ID: v7umiz
• Posted on thiccfems. Post ID: v7umjh
• Posted on TransDebauchery. Post ID: v7umk7
• Posted on TransExtravagant. Post ID: v7umkt
• Posted on transgirls. Post ID: v7umm2
• Posted on TransGoneWild. Post ID: v7ummo
• Posted on TransNymphs. Post ID: v7umna
• Posted on transporn. Post ID: v7umnb
• Posted on traps. Post ID: v7umnt
• Posted on trapsfemboystgirls. Post ID: v7umod
• Posted on trapsgonewild. Post ID: v7ump2
• Posted on u_Lilith_Denfer. Post ID: v7umpo
• Posted on (38/38) Subs 
•
• Bye!
•—————————————————————————————————————————————————————————————————————————•

Loading from direct input, time query, and testing:
•———————————————————————————————————————————————————————————————•
• Starting AutoRed 4.0
•
•
• Welcome to AutoRed:
• An excellent app crafted to help post your smut online ;)
•
•
• It has not been 24 hours since your last post(s) at 06/08/2022 13:11:31.
• Do you still want to continue with subreddits without 24-hour limits? (Y/N) y
•
• Would you like to read from CSV? (Y/N) n
•
• Enter a Title: Heyo!  
• You entered: "Heyo!" Is this OK? (Y/N) y
•
• Is this post a test? (Y/N) y
•
• Does this post include 🍆? (Y/N) n
•
• Please paste link url here: https://i.imgur.com/null
• You entered: "https://i.imgur.com/null" Is this OK? (Y/N) y
•
• Title: Heyo!
• Url: https://i.imgur.com/null
•
• Does this look okay? (Y/N) y
•
• Posted on u_Lilith_Denfer. Post ID: v7v52x
• Posted on (1/38) Subs 
•
• Bye!
•—————————————————————————————————————————————————————————————————————————•

Example of throwing exception due to bad link:
•———————————————————————————————————————————————————————————————•
• Starting AutoRed 4.0
•
•
• Welcome to AutoRed:
• An excellent app crafted to help post your smut online ;)
•
•
• It has not been 24 hours since your last post(s) at 06/08/2022 13:11:31.
• Do you still want to continue with subreddits without 24-hour limits? (Y/N) y
•
• Would you like to read from CSV? (Y/N) n
•
• Enter a Title: Test!
• You entered: "Test!" Is this OK? (Y/N) y
•
• Is this post a test? (Y/N) y
•
• Does this post include 🍆? (Y/N) y
•
• Please paste link url here: https://imgur.com/null      
• You entered: "https://imgur.com/null" Is this OK? (Y/N) y
•
• Title: Test!
• Url: https://imgur.com/null
•
• Does this look okay? (Y/N) y
•
• Url is not from a proper host type, use the direct link 
•
• Bye!
•—————————————————————————————————————————————————————————————————————————•
