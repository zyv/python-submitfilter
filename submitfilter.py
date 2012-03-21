# -*- coding: utf-8 -*-
"""
Library of convenience submit filter functions
"""

import re

RE_SHELL = re.compile(r"^#!/.+")
RE_PBS_TAG = re.compile(r"^#PBS\s+")

def add_pbs_tag(data, tag):
    """
    Inserts PBS tag into the job definition; the logic should be as follows:

        - If the script has an interpreter, insert right after
        - If the script has PBS tags, insert right before the first tag
        - In all other cases, insert as the first line
    """

    repl = "{0}\n".format(tag)

    if RE_SHELL.match(data[0]) is not None:
        data.insert(1, repl)
        return data

    for idx, line in enumerate(data):
        if RE_PBS_TAG.match(line) is not None:
            data.insert(idx, repl)
            return data

    data.insert(0, repl)
    return data
