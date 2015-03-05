import os
import sys
import string
import re
import cPickle

import Tweet
import FixCharacters

from sets import Set

from xml.dom import minidom

XML_dir = "/data/anafora-epic/anaforaProjectFile/EPIC/nerData/"

annotators = ["paas8434", "saal5182"]
annotation_types = ["Organization", "Location", "Facility", "Person", "Artifact"]

def load(xml_file_location):    
    source_file = xml_file_location.split(".")[0]
    tweets = load_tweets(source_file)

    annotations = load_annotations(xml_file_location, source_file)
    add_anns_to_tweets(tweets, annotations)    
    return tweets

def load_annotations(annotation_file, source_file):
    dom = minidom.parse(annotation_file)
    all_annotations = []
    all_class_mentions = {}

    entities = dom.getElementsByTagName("entity")

    source_data = "\n".join([line for line in open(source_file)])

    for entity in entities:
        ann = Tweet.Annotation()
        ann.ann_id = entity.getElementsByTagName("id")[0].firstChild.nodeValue
        ann.span_start = int(entity.getElementsByTagName("span")[0].firstChild.nodeValue.split(",")[0])
        ann.span_end = int(entity.getElementsByTagName("span")[0].firstChild.nodeValue.split(",")[1])
        ann.entity_type = entity.getElementsByTagName("parentsType")[0].firstChild.nodeValue + "-" + entity.getElementsByTagName("type")[0].firstChild.nodeValue 
        all_annotations.append(ann)
        
    return all_annotations

def load_tweets(file_name):
    tweets = []
    current_start = 0
    text = ""
    tweet_done = False
    start_pattern = re.compile("^[0-9]{6,}[,\s]")
    end_pattern = re.compile("^.+[\s][0-9]{6,}$")

    for line in open(file_name):
        if start_pattern.match(line) or end_pattern.match(line) or "haiti" in file_name.split("/")[-1]:
            tweet_done = True

        text += line

        if tweet_done:
            start = current_start
            end = start + len(text)
            current_start = end
            tweets.append(Tweet.Tweet(text.replace("\n", " ").strip(), start, end, file_name))
            tweet_done = False
            text = ""
            tweet_id = ""
    return tweets
    

def add_anns_to_tweets(tweets, annotations):
    for t in tweets:
        for a in annotations:
            if t.span_start <= a.span_start and t.span_end >= a.span_end:
                t.annotations.append(a.entity_type)

def main():
    all_tweets = {}
    annotators_tweets = {"paas8434":[], "saal5182":[]}
    for root, dirs, files in os.walk(XML_dir):
        for i in range(len(files)):
            f = files[i]
            f_data = f.split(".")
            for a in annotators:    
                if len(f_data)>2 and f_data[-2] == "completed" and f_data[-3] == a :
                    
                    annotators_tweets[a] += load(os.path.join(root, f))
    cPickle.dump(annotators_tweets["paas8434"], open("paas8434_anns", "w"))
    cPickle.dump(annotators_tweets["saal5182"], open("saal5182_anns", "w"))

                            
        
if __name__ == "__main__":
    main()
