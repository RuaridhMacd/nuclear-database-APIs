"""
src main encapulating script.
Can be run independently from modules.
"""

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    # from .PSTAR.pstar_api import pstar_api
