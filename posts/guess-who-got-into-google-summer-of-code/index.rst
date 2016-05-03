.. title: Guess who got into Google Summer of Code?
.. slug: guess-who-got-into-google-summer-of-code
.. date: 2016-04-30 23:44:47 UTC+05:30
.. tags: Mozilla
.. category:
.. link:
.. description:
.. type: text
.. author: Varun Joshi

I'm really excited to say that I'll be participating in Google Summer of Code this year, with Mozilla! I'm going to be working on the Balrog update server this summer, under `Ben's <http://hearsum.ca>`_ guidance. Thank you Mozilla and Google for giving me this chance!

I'll be optimizing Balrog by devising a mechanism to handle update races. A future blog post will describe how exactly these races occur and how I aim to resolve them. Basically, an algorithm similar to what git uses for 3-way merges is required, but we also need to take care of nesting since the 'Blob' data structure, that we use, has nested data. I will also share my proposal and the timeline I'll be following in the coming weeks.

These three months are going to be amazing and I'm really looking forward to working with the Mozilla RelEng community! I will be blogging weekly once the coding period commences, and I welcome any suggestions that might lead to me presenting a better final product.
