# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime, date
import pytz


# -----------------------------------------------------------------------

# ======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
# ======================


def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
        #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
        #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret


# ======================
# Data structure design
# ======================

# Problem 1


class NewsStory:
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid  # string
        self.title = title  # string
        self.description = description  # string
        self.link = link  # string
        self.pubdate = pubdate  # datetime

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


# ======================
# Triggers
# ======================


class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower() + " "

    def is_phrase_in(self, text):
        for punc in string.punctuation:
            text = text.replace(punc, " ")
        up_text = " ".join(text.split()).lower() + " "

        if self.phrase in up_text:
            return True
        return False


# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())


# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())


# TIME TRIGGERS

# Problem 5
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, dt_string):
        self.time = datetime.strptime(dt_string, "%d %b %Y %H:%M:%S")


# Problem 6
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        # cmp news time and time from time trigger
        try:
            if self.time > story.get_pubdate():
                return True
        except:
            self.time = self.time.replace(tzinfo=pytz.timezone("EST"))
            if self.time > story.get_pubdate():
                return True
        return False


class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        try:
            if self.time < story.get_pubdate():
                return True
        except:
            self.time = self.time.replace(tzinfo=pytz.timezone("EST"))
            if self.time < story.get_pubdate():
                return True
        return False


# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, other):
        self.other = other

    def evaluate(self, story):
        if self.other.evaluate(story):
            return False
        return True


# Problem 8
class AndTrigger(Trigger):
    def __init__(self, other1, other2):
        self.other1 = other1
        self.other2 = other2

    def evaluate(self, story):
        if self.other1.evaluate(story) and self.other2.evaluate(story):
            return True
        return False


# Problem 9
class OrTrigger(Trigger):
    def __init__(self, other1, other2):
        self.other1 = other1
        self.other2 = other2

    def evaluate(self, story):
        if self.other1.evaluate(story) or self.other2.evaluate(story):
            return True
        return False


# ======================
# Filtering
# ======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filter_stories = []
    if len(triggerlist) == 0:
        return stories
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filter_stories.append(story)

    return filter_stories


# ======================
# User-Specified Triggers
# ======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, "r")
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith("//")):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    t_map = {
        "TITLE": TitleTrigger,
        "DESCRIPTION": DescriptionTrigger,
        "AFTER": AfterTrigger,
        "BEFORE": BeforeTrigger,
        "NOT": NotTrigger,
        "AND": AndTrigger,
        "OR": OrTrigger,
    }

    scan_dict = {}
    add_list = []
    t_list = []
    for line in lines:
        if "AND" in line or "OR" in line:
            tname, ttype, tr1, tr2 = line.split(",")
            scan_dict[tname] = t_map[ttype](scan_dict[tr1], scan_dict[tr2])
        elif not "ADD" in line:
            tname, ttype, others = line.split(",", 2)
            scan_dict[tname] = t_map[ttype](others)
        else:
            add_list = line.split(",")
            for i in range(1, len(add_list)):
                t_list.append(scan_dict[add_list[i]])
    return t_list


SLEEPTIME = 120  # seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line
        triggerlist = read_trigger_config("triggers.txt")
        sections = "all"
        sec_dict = {
            "all": "https://www.scmp.com/rss/91/feed",
            "hk": "https://www.scmp.com/rss/2/feed",
            "china": "https://www.scmp.com/rss/4/feed",
            "asia": "https://www.scmp.com/rss/3/feed",
            "world": "https://www.scmp.com/rss/5/feed",
        }

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        t = f"SCMP News {date.today()}"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Calibri", 20))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Calibri Light", 16), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify="center")
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title() + "\n", "title")
                cont.insert(
                    END,
                    "\n---------------------------------------------------------------\n",
                    "title",
                )
                cont.insert(END, newstory.get_description() + "\n\n")
                cont.insert(END, newstory.get_link())
                cont.insert(
                    END,
                    "\n*********************************************************************\n",
                    "title",
                )
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=" ")
            # Get stories from Google's Top Stories RSS news feed
            stories = process(sec_dict.get(sections, "all"))
            # stories = process("https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en")

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    root = Tk()
    root.title("A RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
