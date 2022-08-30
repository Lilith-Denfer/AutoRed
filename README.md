# AutoRed
An app crafted to help Feminine Dick-Having creators post their smut online, namely Reddit
(Will be working to make the app as general-use as possible in the future, it has just been easier to program a personal interface as a trans woman)

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

The program will return a file called `log.txt`, which records the last terminal output. This can be useful if you schedule posts in far advance and want an easy way to copy and paste your image or video link as well as title for distrubution to other sites after closing the terminal.

The comment formatted in the `comments.json` file includes two different promotions, if you not want anything added to your comment, just write them as empty strings, or `""`. If you don't want a general string, use `""` as well. Unfortunately the current version of the app doesn't include the option to turn off automatic commenting, because it was developed with me in mind; I may add it in a future version. The general string is always included in the comment, and is sort of a general tagline. The 'sub promo' comment is meant for plugging a subreddit and the 'OF promo' is used for plugging an OnlyFans or Manyvids etc.

Internal imgur links must be used, as reddit doesn't allow internal image hosting on NSFW subreddits. The mobile app has a bug that allows it, but if we're using the api we have to host elsewhere. Internal imgur links take the form of https://i.imgur.com/file.jpg, instead of the usual https://imgur.com/image, and directly point to an image rather than the website. Videos are also allowed in the checks using links to `redgifs.com`.

It should also be noted that all posts are automarked as NSFW, as has been most useful for my variety of content


## Usage

After specifying the details of the comments in the `comments.json` file, including the csv files `posts.csv` and `subreddits.csv`, and adding `config.ini` to the same directory as AutoRed.py, run the following. Use the provided samples as templates.

```console
(You will need to navigate the console to the directory containing everything first, this is what my bash script does automatically on my copy of the app. On Mac this would look like `cd Users/your_user_path/Documents/AutoRed`, where cd stands for current directory, and you would specify the path.)

$ python3 AutoRed.py 
...
```
