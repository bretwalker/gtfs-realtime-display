gtfs-realtime-display
=====================

Google Transit Feed Specificiation viewer

This is a super-simple script that will show the contents of Protocol Buffer file that follows the GTFS-realtime Protocol Buffer standard.

**Usage**
>    python display.py --file FeedFile.pb

or
>    python diplay.py --url 'http://www.example.com/FeedFile.pb'
    
And saving the output to a file is easy:
>    python display.py --file FeedFile.pb > output.txt

**Dependencies**
  * Python 2.x (not sure if Python 3 will work)
  
*Note:* I removed the dependency to install Google's Python [Protocol Buffers](http://code.google.com/p/protobuf/downloads/list) module, as this can be confusing to those just starting out with Python (the audience of this script).