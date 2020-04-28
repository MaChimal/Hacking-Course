#!/usr/bin/env python
#_*_ coding: utf8 _*_


#python-Wappalyzer está descontinuado 

from wappalyzer import WebPage, Wappalyzer

wap = Wappalyzer.latest()
try:
    web = WebPage.new_from_url("https://www.example.com")
    tecnologias = wap.analyze(web)
    for t in tecnologias:
        print("Tecnología detectada: {}".format(t))
except:
    print("Hay un error")
