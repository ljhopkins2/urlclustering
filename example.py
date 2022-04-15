#!/usr/bin/env python
from __future__ import print_function
import random
import urlclustering


def pprint(clusters):
    for key, urls in clusters.items():
        print("REGEX:", key[0])
        print("HUMAN:", key[1])
        print("URLS:")
        print("\t" + "\n\t".join(urls) + "\n")


state_cities = {
    "CA": ["SanFrancisco", "LosAngeles", "SanDiego"],
    "OR": ["Portland", "Bend", "Eugene"],
    "WA": ["Seattle", "Tacoma", "WallaWalla"],
}

subcats = ["todo", "eats", "stay"]

info_pages = []
for state, cities in state_cities.items():
    for city in cities:
        for cat in subcats:
            for id in range(random.randint(1, 10)):
                info_pages.append(f"http://example.com/{state}/{city}/{cat}/page{id}.html")

urls = [
    "http://example.com",
    "http://example.com/about",
]

cats = [
    "http://example.com/cat/%s" % x
    for x in ("about", "investors", "careers")
]
tags = [
    "http://example.com/tag/%s/tag%s" % (random.randint(100, 999), x) for x in range(10)
]
arts = ["http://example.com/article/?id=%s" % x for x in range(10)]

# c = urlclustering.cluster(urls + cats + tags + arts + info_pages, 5)
c = urlclustering.cluster(info_pages, 2)

pprint(c['clusters'])
print('UNCLUSTERED:')
print('\t' + '\n\t'.join(c['unclustered']))
