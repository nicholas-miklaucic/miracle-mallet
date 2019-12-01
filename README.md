# Miracle Mallet
A bot to invert the gender of posts on [/r/MarriedRedPill](http://reddit.com/r/marriedredpill).
## Disclaimer
This is one step up from an Internet dare. Don't take anything this bot does seriously, and believe
me when I say I'm not responsible for whatever it posts: go talk to whoever made the MRP post, not
me. Anything particularly problematic I'm happy to remove: my Reddit username is
`/r/nicholas-miklaucic`. 
## See It In Action
This bot maintains the parallel subreddit
[/r/TheMarriedBluePill](http://reddit.com/r/themarriedbluepill). Unfortunately, `/r/marriedbluepill`
is taken.
## Roadmap
Right now, I run it manually (which is fine, because the subreddit isn't very active). This prevents
me needing hosting on a server.

Comments are tricky: it's hard to update comments, because you'd have to keep a list of which MRP
posts correspond to which MBP posts. Right now, I just copy some of the top-level comments when I
run the bot. This might be updated in the future.
## How It Works
The bot simply goes through each word in a post and checks it against a list of gendered words with
their pairs. This isn't a very slick approach, but it works well enough.
## It's Missing a Word!
If there are missing words you find, submit an issue and I'll look into it, or submit a pull request
with the added word(s). Note that the order matters: for words with multiple reverses (like "mum"
and "mom" both going to "dad"), the first one in the list is the one that the bot will use.
## Issues
If you have any way of solving these, let me know!
 - "Her" can be an analogue to both "his" and "him", and it's hard to figure out which one applies
   in which case.
