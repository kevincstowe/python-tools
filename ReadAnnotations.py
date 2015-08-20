import os
import sys
import string
import re
import cPickle

import Tweet
import FixCharacters
import Writer

from sets import Set

from xml.dom import minidom

source_text_dir = "/home/kevin/Documents/Epic/NER/SourceFiles/source_text/"
XML_dir = "/home/kevin/Documents/Epic/NER/SourceFiles/XML/"
output_dir = "/home/kevin/Documents/Epic/NER/Input/Gold/CrfGold/"

annotation_types = ["Organization", "Location", "Facility", "Person", "Artifact"]

def annotator_okay(annotator_element, file_name):
    annotator_name = annotator_element.firstChild.nodeValue
    annotator_id = annotator_element.attributes["id"].value

    if "Consensus" in annotator_name or "Consensus" in annotator_id:
        return True

def load(xml_file_location):    
    source_file = source_text_dir + minidom.parse(xml_file_location).getElementsByTagName("annotations")[0].attributes["textSource"].value
    tweets = load_tweets(source_file)

    for a in annotation_types:
        annotations = load_annotations(xml_file_location, source_file, a)
        add_anns_to_tweets(tweets, annotations)    
    
    return tweets

def load_annotations(annotation_file, source_file, annotation_type):
    dom = minidom.parse(annotation_file)
    all_annotations = Set()
    all_class_mentions = {}

    annotations = dom.getElementsByTagName("annotation")
    class_mentions = dom.getElementsByTagName("classMention")

    for cm in [cm for cm in class_mentions if cm.getElementsByTagName("mentionClass")[0].attributes["id"].value == annotation_type]:
        all_class_mentions[cm.attributes["id"].value] = cm.getElementsByTagName("mentionClass")[0].attributes["id"].value

    source_data = ""
    with open(source_file) as sf::
        for line in sf:
            source_data += line

    for a in annotations:
        ann = Tweet.Annotation()

        if len(a.getElementsByTagName("annotator")) > 0 and annotator_okay(a.getElementsByTagName("annotator")[0], annotation_file):
            if len(a.getElementsByTagName("mention")) > 0:
                if len(a.getElementsByTagName("span")) > 0:
                    if len(a.getElementsByTagName("spannedText")) > 0 and a.getElementsByTagName("spannedText")[0].firstChild != None:
                        ann.ann_id = a.getElementsByTagName("mention")[0].attributes["id"].value
                        ann.span_start = int(a.getElementsByTagName("span")[0].attributes["start"].value)
                        ann.span_end = int(a.getElementsByTagName("span")[0].attributes["end"].value)
                        ann.span_text = a.getElementsByTagName("spannedText")[0].firstChild.nodeValue.encode("utf-8")
        if ann.ann_id != "":
            if not source_data[ann.span_start:ann.span_end] == ann.span_text:
                if ann.span_text in source_data[ann.span_start-5:ann.span_end+5]:
                    ann.span_start = ann.span_start-5+ (source_data[ann.span_start-5:ann.span_end+5].find(ann.span_text))
                    ann.span_end = ann.span_start + len(ann.span_text)
        if ann.ann_id in all_class_mentions:
            ann.entity_type += all_class_mentions[ann.ann_id] + " "
            all_annotations.add(ann)

    return all_annotations

def load_tweets(file_name):
    tweets = []
    current_start = 0
    text = ""
    tweet_done = False
    start_pattern = re.compile("^[0-9]{6,}[,\s]")
    end_pattern = re.compile("^.+[\s][0-9]{6,}$")

        
    for open(file_name) as fn:
        for line in file_name:
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
    margin = 10
    for t in tweets:
<<<<<<< HEAD
        for a in annotations:
            if t.span_start <= a.span_start and t.span_end >= a.span_end:
                t.annotations.append(a.entity_type)
        if not t.annotations:
            t.annotations = ["None"]
            
=======
        for w in t.words:
            rel_start = t.span_start + w.span_start
            rel_end = t.span_start + w.span_end
            for a in annotations:
                if rel_start+margin >= a.span_start and rel_end-margin <= a.span_end:
                    if w.text in a.span_text:
                        if w.text in a.span_text.split()[0]:
                            w.add_annotation("B-" + a.entity_type.strip())
                        else:
                            w.add_annotation("I-" + a.entity_type.strip())

>>>>>>> 1928e2b7e5d2381cc13d4d0704cb20aa80ad90a2
def main():
    args = sys.argv[1:]
    all_tweets = {}
<<<<<<< HEAD
    annotators_tweets = {"paas8434":[], "saal5182":[]}
    for root, dirs, files in os.walk(XML_dir):
        for i in range(len(files)):
            f = files[i]
            f_data = f.split(".")
            for a in annotators:    
                if len(f_data)>2 and f_data[-2] == "completed" and f_data[-3] == a :
                    
                    annotators_tweets[a] += load(os.path.join(root, f))

    paas_tweets = {}
    saal_tweets = {}
    for tweet in annotators_tweets["paas8434"]:
        paas_tweets[tweet.tweet_id] = tweet
    for tweet in annotators_tweets["saal5182"]:
        saal_tweets[tweet.tweet_id] = tweet
    cPickle.dump(paas_tweets, open("paas8434_anns", "w"))
    cPickle.dump(saal_tweets, open("saal5182_anns", "w"))

                            
        
=======
    if len(args) > -1:
        for root, dirs, files in os.walk(XML_dir):
            for i in range(len(files)):
                f = files[i]
                if i % 10 == 0:
                    print str(i) + " / " + str(len(files))
                if "~" not in f and "#" not in f and not os.path.isdir(root + "/" + f) :
                    crf_test_output = "/home/kevin/Documents/Epic/NER/Input/Test/CrfTest/" + f
                    line_output = "/home/kevin/Documents/Epic/NER/Input/Test/LineTest/" + f
                    crf_gold_output = "/home/kevin/Documents/Epic/NER/Input/Gold/CrfGold/"
                    tweets = load(root + "/" + f)
                    for tweet in tweets:
                        all_tweets[tweet.tweet_id] = tweet

#                    for t in tweets:
#                        print t.tweet_id
#                    Writer.write_tweets_by_line(tweets, line_output)
#                    Writer.write_tweets_crf_test(tweets, crf_test_output)
#                    Writer.write_tweets_crf_gold(tweets, f, crf_gold_output)
        cPickle.dump(all_tweets, open("data/all_tweets.p", "wb"))
    else:
        print "BAD ARGS"
        sys.exit(2)

def main2():
    person_tweets = []
    count = 0
    for f in os.listdir("/home/kevin/Documents/Epic/NER/Input/Gold/CrfGold/Person/"):
        count += 1
        print f
        print count
        person_tweets = Writer.load_tweets_crf_gold(f.split("/")[-1], "/home/kevin/Documents/Epic/NER/Input/Gold/CrfGold/", "Person")

        Writer.write_tweets_crf_gold(person_tweets, f, "/home/kevin/Documents/Epic/NER/Input/Gold/CrfGoldTest/", ["Person"])

>>>>>>> 1928e2b7e5d2381cc13d4d0704cb20aa80ad90a2
if __name__ == "__main__":
    main()
