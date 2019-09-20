#!/usr/bin/env python
# coding: utf-8

# # Code

from .hanzi import strip_nonhanzi, restore_index
from .SmithWaterman import smith_waterman

def find_substrings( ref, trg, min_len=8 ):

    print("# Texts Preprocessing")
    ref_han, ref_non_han = strip_nonhanzi( ref )
    trg_han, trg_non_han = strip_nonhanzi( trg )

    ref_idx = restore_index(ref_han, ref_non_han )
    trg_idx = restore_index(trg_han, trg_non_han )

    print("# Finding Similar Substrings")
    raw_idx = smith_waterman( ref_han, trg_han, min_len=min_len )

    print("# Building new indices")
    new_idx = []
    for ( i_b, i_e ), ( j_b, j_e)  in raw_idx:
        new_idx.append( ( ( ref_idx.index( i_b ), ref_idx.index( i_e ) ), ( trg_idx.index(j_b), trg_idx.index(j_e) ) ) )

    return new_idx, raw_idx
