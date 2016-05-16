.. title: Multifile Responses in Balrog
.. slug: multifile-responses-in-balrog
.. date: 2016-05-16 23:29:34 UTC+05:30
.. tags: Mozilla
.. category:
.. link:
.. description:
.. type: text
.. author: Varun Joshi

Apart from Firefox, Balrog is also used by Mozilla to provide updates for the Gecko Media Plugin (GMP) package. The Gecko Media Plugin package contains various plugins for media support, like the OpenH264 codec and the Widevine plugin. To handle updates to these, we have a speical GMP blob that lists updates to the plugins. Updates to every plugin are included in one blob. This leads to problems when there are multiple versions of a plugin that we can use. For example, we might serve OpenH264 version 1.5.3 on Firefox 42 on Windows and version 1.5.2 on Firefox 40. We have to maintain a blob for each possible combination of versions. With an increase in the number of versions available, this method of serving updates might become intractable.

Ben and I discussed various strategies we could use to tackle this. A gist of what went through our minds is on `the bug page <https://bugzilla.mozilla.org/show_bug.cgi?id=1245941>`_. What we eventually went ahead with was to add a blob type that got its contents from other blobs. We call this blob type ``SuperBlob``.

=========
SuperBlob
=========

A SuperBlob is basically just a redirection mechanism. It just contains the names of the products that we wish to include in the generated XML.::

     {
        "name": "fake",
        "schema_version": 4000,
        "products": [
            "c",
            "d"
        ]
    }

This superblob is called ``fake``. It just asks to look at the products named ``c`` and ``d``. A rule can be set to point at this SuperBlob if we wish the response product to have all the files listed in products ``c`` and ``d``.

===================
How does this work?
===================

The web interface, while processing requests, checks if the rule evaluates to a SuperBlob. If it is, it gets the product names from the SuperBlob and gets the corresponding blobs by evaluating the query with the requested product changed. So, in our example, the web interface will evaluate the query with the product name changed to ``c`` and ``d`` and obtain the resultant blobs. It will pick up the header and footer XML from the output of processing the blob obtained from the **first product** and the inner XML will include the concatenated inner XMLs of all the blobs obtained from the products listed in the SuperBlob.

So, if product ``a`` gave::

    <updates>
        <update type="minor" version="None" extensionVersion="2.5" buildID="25">
            <patch type="complete" URL="http://a.com/b" hashFunction="sha512" hashValue="23" size="27777777"/>
        </update>
    </updates>

and product ``b`` gave::

    <updates>
        <update type="minor" version="None" extensionVersion="2.5" buildID="25">
            <patch type="complete" URL="http://a.com/public" hashFunction="sha512" hashValue="23" size="22"/>
        </update>
    </updates>

the ``SuperBlob`` will give::

    <updates>
        <update type="minor" version="None" extensionVersion="2.5" buildID="25">
            <patch type="complete" URL="http://a.com/public" hashFunction="sha512" hashValue="23" size="22"/>
            <patch type="complete" URL="http://a.com/b" hashFunction="sha512" hashValue="23" size="27777777"/>
        </update>
    </updates>
    
So, we can now have one fixed rule for all GMP responses and have several rules for each constituent plugin without having to worry about the combinations like we had to do earlier.

While working on this, I also removed the ``createXML`` method in favour of three methods that return the header, the inner XML and the footer respectively. This helped in seperating the various components of the XML output without having to parse it. The XML generation logic has moved to the client view.