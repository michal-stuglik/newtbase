""" Methods for annotation data loading into database. """

import sqlite3 as lite
import sys

from newtbase.data_loaders import loader_objects

try:
    con = lite.connect(loader_objects.DB_PATH)
    cur = con.cursor()

    # data load
    # accession_set = blast_annotation_extractor(cur)
    # print("acc_set_length", len(accession_set))
    loader_objects.load_accession(cur, ACCESSION_PATH, accession_set)
    loader_objects.load_transcript(cur)
    loader_objects.load_orf(cur)
    loader_objects.load_blast(cur)
    loader_objects.load_go_defs(cur)
    loader_objects.load_go_uniprot_mapper(cur)

    print "data loaded!"

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()
