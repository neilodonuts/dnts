""" Quickly determine validity of variables as per syntax contracts.

"""
# Standard Python modules
import re

# Globals
RE_HOSTNAME = re.compile(r"(?!-)[a-z0-9-]{1,63}(?<!-)$", re.IGNORECASE)
RE_NUMERIC = re.compile(r"[0-9]+$")


def hostname(hostname):
    """ Determine if a given string is a valid host name.

    NOTE: Does not support a host name terminated with a dot (DNS style).

    :param hostname: Domain name, SLD or TLD.
    :returns: `True` if valid host name else `False`.
    """
    # https://stackoverflow.com/questions/2532053/
    if not isinstance(hostname, str):
        return False
    if len(hostname) > 253:
        return False
    labels = hostname.split(".")
    if RE_NUMERIC.match(labels[-1]):  # the TLD must be not all-numeric
        return False
    return all(RE_HOSTNAME.match(label) for label in labels)
