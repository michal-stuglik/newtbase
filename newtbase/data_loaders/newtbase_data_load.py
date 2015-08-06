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
    # load_Accession(cur, ACCESSION_PATH, accession_set)
    # load_Transcript(cur)
    # load_Orf(cur)
    # load_Blast(cur)
    # load_GO_defs(cur)
    # load_Go_uniprot_mapper(cur)

    print "data loaded!"

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()
