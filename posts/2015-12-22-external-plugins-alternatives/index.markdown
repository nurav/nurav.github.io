<!---
.. title: External Plugins: Alternatives
.. date: 2015-12-22 08:46:06 IST
.. category: KDE
-->
So, while making writer plugins, I felt that it would be really awesome if we could use another language (apart from C++), that has libraries to modify metadata. External extractor plugins were already on the map, so why not add external writer plugins too! This would enable me to use [PyPDF](https://pythonhosted.org/PyPDF2/), [Java Epublib](http://www.siegmann.nl/epublib) and other such libraries that might make it easier to write new plugins. I indentified a couple of ways to go about this:

* Embedding a Python Interpreter:

  [The Python Docs](https://docs.python.org/2/extending/embedding.html) show how this can be done. We can use [Boost.Python](http://www.boost.org/doc/libs/1_59_0/libs/python/doc/index.html) to access a higher-level API. We'd just have to scan the contents of some predefined directory, where each Python script would be in some specific format (with functions like `mimetypes`, `write` or `extract`), and make a C++ shim that would generate a `WriterPlugin` or `ExtractorPlugin` for each script. 
  
  The main limitation to this approach would be that it would involve a lot of effort if I needed to support multiple languages, since I would need to embed all of their interpreters.
  
* Creating a process for each plugin:

  Every plugin would include a manifest that would detail how it is to be used. For example, a Java plugin would have to be run with the JVM, a Python one with CPython etc. The manifest would also have other information like supported mimetypes, properties write-back capabilities, etc. Whenever a `WriterPlugin` or an `ExtractorPlugin` is needed for a particular mimetype, all installed plugins are checked for support. Writing or reading metadata using a new plugin will invoke a new process using the instructions specified in the manifest. There are several ways we could use to communicate with the process:
  
    1. Using DBus: Would allow for more structed communication between the plugin and the framework. It would also decouple the plugins. But it might be overkill since limited communication is needed between the plugin and the framework.
    
    2. Using named pipes: This allows for decoupling too, but again, might be overkill since we aren't transferring large amounts of data.
    
    3. Using stdin/stdout: This is the method Boudhayan Gupta has used in his patch. We need to carefully error conditions.
  
  The data is exchanged in the JSON format.
    
We have decided to create a new process for each plugin and use stdin/stdout for communication, since it is the most straighforward way. If you think that there are other ways, or there is a discernible benefit to using any of the other methods I've listed, please let me know in the comments.

Things to keep in mind (mostly suggested by vhanda on [Boudhayan Gupta's patch](https://git.reviewboard.kde.org/r/125762)):

1. There needs to be a proper error-handling framework, to make sure that an invalid plugin does not block execution for long periods.

2. Dependencies need to be handled, both for languages and language libraries. How I'm planning to do this with Python will be covered in a future post.

3. There needs to be a way to select from amongst several plugins offering support for the same mimetypes.

So that's about it for this post. I'm currently working on this, so you should expect to see some code soon. Thanks, and as always, please feel free to suggest any improvements I could make to my approach!
