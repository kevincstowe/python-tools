from nltk.parse.stanford import StanfordDependencyParser
path_to_jar = '/home/kevin/Java Packages/stanford-parser-full-2015-04-20/stanford-parser.jar'
path_to_models_jar = '/home/kevin/Java Packages/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar'

dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

def parse_sentences(sentences):
    return [dependency_parser.parse(s) for s in sentences]

def parse_sentence(sentence):
    return dependency_parser.parse(sentence.split())
