gtfs-realtime-display
=====================

Google Transit Feed Specificiation viewer

This is a super-simple script that will show the contents of Protocol Buffer file that follows the GTFS-realtime Protocol Buffer standard.

**Usage**
>    python display.py --file FeedFile.pb

or
>    python diplay.py --url http://www.example.com/FeedFile.pb
    
And saving the output to a file is easy:
>    python display.py --file FeedFile.pb > output.txt

**Dependencies**
  * Google [Protocol Buffers](http://code.google.com/p/protobuf/downloads/list)

As with all Python programs that have dependencies, the best way to install Protocol Buffers would be in a dedicated [virtualenv](http://www.virtualenv.org/en/latest/).
