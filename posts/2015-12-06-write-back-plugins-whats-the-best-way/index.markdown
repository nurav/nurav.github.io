<!---
.. title: Write Back Plugins: What's the Best Way?
.. date: 2015-12-06 13:22:18 IST
.. category: KDE
-->
That's been a large gap between posts! I'm really sorry about that, I was busy with my university exams and with coding.

I have mainly been working on the write-back plugin mechanism that we needed to incorporate into KFileMetaData. Most of my changes are visible at [my fork](https://github.com/nurav/kfilemetadata/tree/varun-writerplugins). 

The work yet has involved a couple of decisions:

* Deciding the structure of the framework:

  While writing the code for write-back plugins, I noticed lots of commonalities amongst what I was writing and extractors. I thought of abstracting out these common elements into a generic Plugin class, that would optionally support both reading writing data. Alas, this could not be done. Doing this would involve changing the ABI of KFileMetaData, breaking compatibility with other tools that use the current version. So, after consulting with my [mentor](http://vhanda.in), I decided to rewrite the write-back plugin infrastructure from scratch. Developers working on both writer and extractor plugins will have to find a way to share data outside of the infrastructure we will provide.

* Deciding what writers to write first:

  Some of the libraries that we currently use for extraction don't support writing back yet. Poppler is one case. Though they are working on [adding support for writing back PDF metadata](https://bugs.freedesktop.org/show_bug.cgi?id=36653), it's not ready yet, and I'll have to defer writing a plugin for PDF metadata (or else implement external writer support first, as BaloneyGeek on #kde-devel suggested). I have started with writing a rudimentary TagLib writer, and I'm going to progress into writing a writer for epub books as well.
  
What I have learned yet:

* CMake: Though I have struggled a lot with it, my efforts are starting to bear fruit. I finally feel comfortable making my own CMakeLists.txt.

* Qt: I'm learning a lot about all the functionalities Qt offers, and I try to integrate whatever I can from what I learn into the code. My mentor's suggestions have also taught me a lot about some less obvious parts.

* C++: Exploring the code base, I chanced upon a lot of new patterns, like the PIMPL, object reuse etc. I try my best to know why what is done, so I avoid the pitfalls that the creators of these patterns faced.

That's enough about what I've learned. I'll now outline some of the changes you'll see on my fork that you just might see in the final framework:

* A new `WriterPlugin` class: 

  This class will be subclassed by all plugins that hope to write data to some file. The most important functions are `write` and `writeMimetypes`. `write` is where the action is. `WriterPlugin`s will implement this function to actually write the metadata to disk. `writeMimetypes` simply lists the mimetypes supported by the plugin. A `supportedProperties` function is also something that I plan to add, to make sure that applications do not attempt to write an unsuitable proptery datum to some file. This is sort of analogous to `ExtractorPlugin`.
  
* A `Writer` framework:

  I have put in analogues to most of the functionalities that `Extractor`s offer. Instead of using something similar to `ExtractionResult` that needed to be subclassed, I have used `WriteData`, which is concrete. The rationale behind this is that we won't need to store huge amounts of data to write back, since we don't support writing back text.
  
* A `TagLibWriter` class:

  This shows how the new `Writer` classes can be used. It is really rudimentary at the moment, but I plan to extend it to support writing back all the properties that can be read by `TagLibExtractor`.
  
The road ahead: This is just the beginning of what I have planned for the Season of KDE. I plan to work on [Boudhayan Gupta's patch](https://git.reviewboard.kde.org/r/125762), change it so that it can be used for `Writer`s and implement the suggestions put forth by vHanda to improve it.

It's been an exciting journey so far, and it's going to get even better! And if you have any suggestions for me to improve upon, please do let me know of them via comments. Thank you!

Signing off,
Varun

