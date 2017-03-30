"""
Author: Rajarshi Sarkar
Use: Extract Data from XML into a DataFrame
"""

import itertools
import xml.etree.ElementTree as xmlread

import pandas as pd


def getDataFrameFromXml(xmlAddress):
    df = pd.DataFrame()
    file = xmlread.parse(xmlAddress).getroot()

    for child_nodes in file:
        child = child_nodes.attrib
        dictKeys = child.keys()
        noOfKeys = len(dictKeys)
        keyArray = [0] * noOfKeys
        for i in range(0, noOfKeys, 1):
            try:
                keyArray[i] = child[dictKeys[i]]
            except KeyError:
                continue

        kVDict = dict(itertools.izip_longest(dictKeys, keyArray))
        df = df.append(kVDict, ignore_index=True)

    return df
