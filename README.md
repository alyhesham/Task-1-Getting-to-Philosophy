# Task-1-Getting-to-Philosophy

This python script implements the getting to philosophy law. It starts at a random url and then parses the wikipedia page HTML.
The parser is designed to start from the content tag to find the first hyperlink whivh has the tag href. It avoids citations and pronunciation help links
in order to not get to a valid link. It checks if the program is in a loop by checking if the current url is in the visited urls. 
I have added a limit for the links to be 50 for ease of testing but this limit can be easily change to whichever number.
