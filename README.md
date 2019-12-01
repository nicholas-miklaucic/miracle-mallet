# Miracle Mallet
A bot to invert the gender of posts on [/r/MarriedRedPill](http://reddit.com/r/marriedredpill).
## Disclaimer
This is one step up from an Internet dare (there was a BluePill post about doing this and I thought
"why not"). Don't take anything this bot does seriously, and believe me when I say I'm not
responsible for whatever it posts—go talk to whoever made the MRP post, not me. Anything
particularly problematic I'm happy to remove: my Reddit username is `/r/nicholas-miklaucic`.
## See It In Action
This bot maintains the parallel subreddit
[/r/TheMarriedBluePill](http://reddit.com/r/themarriedbluepill). Unfortunately, `/r/marriedbluepill`
is taken.
## Roadmap
Right now, I run it manually (which is fine, because the subreddit isn't very active). This prevents
me needing hosting on a server, but it does mean that the subreddit isn't always up to date.
## How It Works
The bot simply goes through each word in a post and checks it against a list of gendered words with
their pairs. This isn't a very slick approach, but it works well enough and I'm not sure how I'd do
much better (especially for posts about anatomy or using proper names).

I wasn't sure how to copy comment trees correctly, so I only copy the top-level comments from each
post. These aren't updating: they're whenever I run the script. Both of these limitations come from
the fact that there's no good way to see what the corresponding inverted post or comment is for any
particular post or comment on MRP.
## It's Missing a Word!
If there are missing words you find, submit an issue and I'll look into it, or submit a pull request
with the added word(s). Note that the order matters: for words with multiple reverses (like "mum"
and "mom" both going to "dad"), the first one in the list is the one that the bot will use.

The current list is in ~gender_invert.py~ at the top, as a list of female words and a list of male
words.
## Issues
If you have any way of solving these, let me know!
 - "Her" can be an analogue to both "his" and "him", and it's hard to figure out which one applies
   in which case.

