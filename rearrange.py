#!/usr/bin/env python3

import re

def rearrange_name(name):
    """
    func: rearrange_name(name)
    param name: str,
    format: 'lastName, firstName'
    returns 'firstName lastName'
    """
    result = re.search(r'^([\w .]*), ([\w .]*)$')
    if result == None:
        return name
    return '{} {}'.format(result[2], result[1])