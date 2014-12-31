
Basic tools for working with and around python

Tools added so far:<br>
  Main.py<br>
    This is a skeleton of a python script - it includes a main method, crafted around the suggestions of Guido van Rossum here (http://www.artima.com/weblogs/viewpost.jsp?thread=4829)<br>

  FixCharacters.py<br>
    This takes files and converts characters that won't encode into UTF-8. NLP tools often do this conversion and fail when they see weird characters.<br>
    -Currently converts obvious choices using a hash map, and removes non-obvious choices.<br>
    -Removes lines that are more than 1/3 special characters.<br>
      -Needs language identification to remove non-English (or whatever)<br>
    -Needs flexible usage<br>