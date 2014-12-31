
Basic tools for working with and around python

Tools added so far:
  Main.py
    This is a skeleton of a python script - it includes a main method, crafted around the suggestions of Guido van Rossum here (http://www.artima.com/weblogs/viewpost.jsp?thread=4829)

  FixCharacters.py
    This takes files and converts characters that won't encode into UTF-8. NLP tools often do this conversion and fail when they see weird characters.
    -Currently converts obvious choices using a hash map, and removes non-obvious choices.
    -Removes lines that are more than 1/3 special characters.
      -Needs language identification to remove non-English (or whatever)
    -Needs flexible usage      