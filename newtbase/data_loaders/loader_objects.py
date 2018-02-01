""" Methods for annotation data loading into database. """

# transcript class
from newtbase.models import Transcript, Orf, Accession, Blast, Go, GoUniprotMapper

# Annotation data
DB_PATH = 'Trinotate.sqlite'
ACCESSION_PATH = 'uniprot_annot'


def blast_annotation_extractor(cur):
    accession_set = set()

    # sqlite reader
    cur.execute("SELECT distinct(FullAccession) FROM blastdbase")
    # select distinct(FullAccession) from   blastdbase;
    rows = cur.fetchall()
    table_counter = 0

    for row in rows:

        accession = str(row[0])
        table_counter += 1

        if accession.startswith("sp|"):
            acc = accession.split("|")[1]
            accession_set.add(acc)
        elif accession.startswith("UniRef90"):
            acc = accession.split("_")[1]
            accession_set.add(acc)
        else:
            print("check this!")

        if table_counter % 1000 == 0:
            print('Accessions in Blast: {}'.format(table_counter))

    return accession_set


def load_blast(cur):
    # sqlite reader
    cur.execute("SELECT * FROM blastdbase")
    rows = cur.fetchall()

    table_counter = 0
    false_acc_counter = 0
    accession_id_notindb_counter = 0
    accession_id_notindb_set = set()

    accessions = set([str(a.accession_id) for a in Accession.objects.all()[:]])
    print("# accessions: {}".format(len(accessions)))

    for row in rows:

        transcript = row[0]
        fullaccession = str(row[1])
        database = row[2]
        ident = row[8]
        evalue = float(row[9])

        if evalue > 0.001:
            continue

        bitscore = row[10]
        transcript_id = transcript.split("|")[0]

        orf_hit = False
        if len(transcript.split("|")) > 1:
            orf_hit = True

        accession_id = None
        if fullaccession.startswith("sp|"):
            accession_id = fullaccession.split("|")[1]
        elif fullaccession.startswith("UniRef90"):
            accession_id = fullaccession.split("_")[1]
            # accession_id = fullaccession

        t = Transcript.objects.get(transcript_id=transcript_id)

        if accession_id is None:
            false_acc_counter += 1
            continue

        if accession_id not in accessions:
            accession_id_notindb_counter += 1
            accession_id_notindb_set.add("{}\t{}".format(fullaccession, accession_id))
            if not fullaccession.startswith("UniRef90"): continue

        table_counter += 1
        if table_counter % 100 == 0:
            print('table_counter: {}'.format(table_counter))

        if not fullaccession.startswith("UniRef90"):
            acc = Accession.objects.get(accession_id=accession_id)
        else:
            acc = None

        orf = None
        if orf_hit:
            orf = Orf.objects.get(orf_id=transcript)

        # postgres writer
        blast = Blast(transcript_id=t, accession_fk=acc, accession_id=accession_id, database=database,
                      percent_identity=ident, evalue=evalue,
                      bitscore=bitscore, orf_hit=orf_hit, orf_fk=orf)
        blast.save()

        if table_counter % 1000 == 0:
            print('Blast: {}'.format(table_counter))

    print("false_acc_counter: {}".format(false_acc_counter))
    print("accession_id_notindb_counter: {}".format(accession_id_notindb_counter))


def load_accession(file_path, accession_set):
    with open(file_path, 'r') as f:
        table_counter = 0

        for line in f:
            if line.startswith("#"): continue

            row = line.strip().split('\t')

            # Accession 	Entry name 	Protein name 	Gene name 	Organism
            accession_id = row[0]

            if str(accession_id) not in accession_set: continue

            entry_name = row[1]
            protein_name = row[2]
            gene_name = None
            if len(str(row[3]).strip()) != 0:
                gene_name = row[3]
            organism = row[4]

            # postgres writer
            acc = Accession(accession_id=accession_id, entry_name=entry_name, gene_name=gene_name,
                            protein_name=protein_name, organism=organism)
            acc.save()
            table_counter += 1

            if table_counter % 1000 == 0:
                print('Accession {}'.format(table_counter))

    print('All Accession into db: {}'.format(table_counter))


def load_transcript(cur):
    table_counter = 0

    # sqlite reader
    cur.execute("SELECT * FROM transcript")
    rows = cur.fetchall()

    for row in rows:
        transcript_id = row[1]
        gene_id = row[0]
        sequence = row[3]

        # postgres writer
        t = Transcript(transcript_id=transcript_id, gene_id=gene_id, sequence=sequence)
        t.save()
        table_counter += 1

        if table_counter % 1000 == 0:
            print('Transcript {}'.format(table_counter))


def load_orf(cur):
    table_counter = 0

    # sqlite reader
    cur.execute("SELECT * FROM orf")
    rows = cur.fetchall()

    for row in rows:

        orf_id = row[0]
        transcript_id = row[1]
        length = row[2]
        strand = row[3]
        start = row[4]
        end = row[5]
        peptide = row[6]

        # get transcript object from postgres
        t = Transcript.objects.get(transcript_id=transcript_id)

        # postgres writer
        orf = Orf(orf_id=orf_id, transcript=t, length=length, strand=strand, start=start, end=end, peptide=peptide)
        orf.save()
        table_counter += 1

        if table_counter % 1000 == 0:
            print('Orf {}'.format(table_counter))


def load_go_defs(cur):
    table_counter = 0

    # sqlite reader
    cur.execute("SELECT * FROM go")
    rows = cur.fetchall()

    for row in rows:

        go_id = row[0]
        name = row[1]
        category = row[2]
        desc = row[3]

        # postgres writer
        go = Go(id=go_id, name=name, category=category, description=desc)
        go.save()
        table_counter += 1

        if table_counter % 1000 == 0:
            print('Go {}'.format(table_counter))


def load_go_uniprot_mapper(cur):
    table_counter = 0
    saved_counter = 0

    # sqlite reader
    cur.execute("select * from uniprotindex where Linkid like 'GO:%'")
    rows = cur.fetchall()

    for row in rows:

        accession = str(row[0])
        golink = str(row[1])

        table_counter += 1
        if table_counter % 10000 == 0:
            print('uniprotindex {}'.format(table_counter))

        # values check:
        a = Accession.objects.filter(entry_name=accession)
        if len(a) == 0: continue

        go = Go.objects.filter(id=golink)
        if len(go) == 0: continue

        # postgres writer
        m_GoUniprotMapper = GoUniprotMapper(accession=a[0], go_link=go[0])
        m_GoUniprotMapper.save()

        saved_counter += 1
        if saved_counter % 100 == 0:
            print('saved_counter {}'.format(saved_counter))
