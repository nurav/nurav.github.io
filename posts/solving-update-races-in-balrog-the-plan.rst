.. title: Solving Update Races in Balrog: The Plan
.. slug: solving-update-races-in-balrog-the-plan
.. date: 2016-05-24 14:07:57 UTC+05:30
.. tags: Mozilla, draft
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Varun Joshi

The coding period for the Google Summer of Code has begun, so here is the plan for the project, as was promised.

Currently, when two submitter tasks request Balrog for a blob to update at the same time, they both have the same data_version in the blob they send back with the added locale. This leads to the server rejecting one of these and the submitter having to retry. In most cases, the updates can simply be merged, preventing the retries. For example, this series of events is something like what happens now:

1. Submitter 1 requests data_version from Balrog (data_version = 1)
2. Submitter 2 requests data_version from Balrog (data_version = 1)
3. Submitter 1 submits release blob to Balrog with data_version  (data_version changes to 2)
4. Submitter 2 fails to submit release blob to Balrog (since data_version is now 2, but submitter specified 1 in the request)

At most times, the data in the blobs is similar apart from some added data such as added locales. So, we can try to reduce submission failures by devising a way to merge the blob versions when we receive a request with an outdated data_version. As my project, I will seek to implement the merging of two blobs. This will be with the utilization of a three-way merge algorithm, something similar to what git uses for merges. Since we currently do not have any libraries for this task, I will make a module for three-way merges of python data structures (and hopefully get it published on PyPI!) and use that within Balrog to accomplish the goals of this project.

The basic algorithm for three-way merges is described here:

1. We first calculate a diff between the new versions of the file (data_version 2 and the version where we fail, in our example) and the old version (data_version 1). There are multiple tools that allow diffs of the form we want. `DictDiffer <https://github.com/inveniosoftware/dictdiffer>`_ and `deepdiff <https://github.com/seperman/deepdiff>`_ are two alternatives we could utilize for this step. Both of them return an easy to use list of differences in our blobs.
2. If there are no changes for that particular item in either diff or if both diffs have added an element with equal values, we add the item in the resultant object.
3. If both diffs have removed some item, we ignore that item and do not include it in our output.
4. If one diff has added an element while the other hasn't, we add the element.
5. If both diffs have added or changed an element but they have unequal values, we recursively apply our algorithm. If there is a difference in a string that was present in the the root version (data_version 1 in our example), we might apply a string three way merge algorithm.
6. For lists, we can treat every list element as a line in text and apply a traditional three way merge algorithm to it.
7. For all other cases, we may consider the two changes to be conflicting and we may apply some conflict resolution strategies.
8. If the type of an element changes, we can consider it to be a merge conflict.

Further analysis needs to be done for the handling of list and tuple values, since the preservation of order might be important in those data structures. We might want to support two modes: one where the preservation of the order of the list elements is important and another where it isn't.

We may employ several merge-conflict resolution strategies:
    - Select one of the changes.
    - Discard both changes

This algorithm is based on this `research paper <http://www.cis.upenn.edu/~bcpierce/papers/diff3-short.pdf>`_ and this `email <https://www.mercurial-scm.org/pipermail/mercurial-devel/2006-November/000322.html>`_. Both show how a three way merge would work out for strings.

`Here <https://docs.google.com/document/d/1jRi6nPNYvja2vqFWIAZ7JHTpnW8mOp8tTRnfIxxlxDY/edit?usp=sharing>`_  is a link to my proposal. Keep checking this space every week for updates on my project and feel free to point out if I can do anything better! Thank you :)
