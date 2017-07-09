## Synopsis

A `python3` script to provide a simple webserver supporting both **IPv6** and IPv4


## Motivation

The python module `httpServer` supports IPv4 out of the box with the simple command:

```
python -m SimpleHTTPServer
```

However it does **not** support IPv6. There is no one line equivalent to support IPv6, so a small script is required.

This is **not** a production web server, but can easily be used to illustrate how to create a small web sever with virtual paths, which could be expanded to a full RESTful interface or a CGI interface. It is useful when one wants to transfer a file from machine A to machine B.

This code was forked from a [gist](https://gist.github.com/akorobov/7903307) published on github four years ago.


#### Why Python?
Python is a wonderful programming language, and getting only better with version 3. There are libraries for most needs, including one which serves up the web.

## Examples

#### running ipv6-httpd

```
$ ./ipv6-httpd.py 
Press ^C to quit
2001:470:ebbd:0:4d18:71cd:b814:9508 - - [09/Jul/2017 11:49:41] "GET / HTTP/1.1" 200 -
^CCaught SIGINT, dying

```



## Installation

Copy `ipv6-htttpd.py` into your directory, and run. The script will serve up files in that directory, including a simple index of the directory.



## Dependencies

Script requires python3 (tested with v 3.4.3)



## Limitations

The script is **not** a production webserver. It does **not** support access lists, PHP, CGI, multi-threading, etc. If you need such a webserver, I recommend `apache` as it has been tried and tested over a period of decades.


## Contributors

All code by Craig Miller cvmiller at gmail dot com. But ideas, and ports to other languages are welcome. 


## License

This project is open source, under the GPLv2 license (see [LICENSE](LICENSE))
