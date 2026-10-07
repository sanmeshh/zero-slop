from laya import Router 
import os
import time

os.environ["HF_HOME"] = os.path.expanduser("~/.cache/huggingface")
os.environ["TOKENIZERS_PARALLELISM"] = "false"
router=Router()

state='''
🚀 **I almost quit.**

Then I realized…

The problem wasn’t the market.
The problem wasn’t my team.
The problem wasn’t the economy.

**The problem was my mindset.**

So I woke up at 4:47 AM.
Made a cup of coffee.
Opened Notion.
And wrote down 3 things:

1. Focus on the customer.
2. Embrace failure.
3. Move with urgency.

That changed everything.

6 months later, we’re up **312%**. 📈

But the biggest lesson?

> **Success isn’t about working harder.
> It’s about becoming the person who deserves success.**

If you’re building something right now and nobody believes in you:

**Keep going.**

Your future self will thank you.

#Leadership #Entrepreneurship #GrowthMindset #Startup #Innovation #AI #Success #PersonalGrowth

'''


questions={
 'isslop':{
     "type":'noul',
     "instructions":"Does this entire text appear to have been generated primarily by an AI language model"
     "which is usually posted on LinkedIn"
 },
}

answer=router.predict(state,questions)["answers"]["isslop"]


p = answer["noul"]
print("   P(post is slop) : %.4f" % p)
print("   confidence        : %.4f   (max(p, 1-p), so it is %.4f either way)"
        % (answer["confidence"], answer["confidence"]))


for threshold in (0.5, 0.8, 0.9):
    print(
        "decision at threshold %.1f : %s"
        % (threshold, "AI-generated" if p >= threshold else "not AI-generated")
    )