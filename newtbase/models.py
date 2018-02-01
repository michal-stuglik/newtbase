"""Data models to store and process data. """

from django.db import models


class Transcript(models.Model):
    """A class for storing Transcript data. """

    transcript_id = models.CharField(primary_key=True, max_length=100)
    gene_id = models.CharField(max_length=100)
    sequence = models.TextField(null=False)

    objects = models.Manager()

    def __unicode__(self):
        return str(self.transcript_id)

    def get_sequence_length(self):
        return len(self.sequence)


class Orf(models.Model):
    """A class for storing Open reading frames data. """

    orf_id = models.CharField(primary_key=True, max_length=100)
    transcript = models.ForeignKey(Transcript, on_delete=models.SET_NULL)
    length = models.IntegerField()
    strand = models.CharField(max_length=1)
    start = models.IntegerField()
    end = models.IntegerField()
    peptide = models.TextField()

    def __unicode__(self):
        return str(self.orf_id)


class Accession(models.Model):
    """A class for storing accession data. """

    id = models.AutoField(primary_key=True)
    accession_id = models.CharField(max_length=100)
    entry_name = models.CharField(max_length=100, unique=True)
    gene_name = models.TextField(null=True)
    protein_name = models.TextField()
    organism = models.CharField(max_length=255)

    def __unicode__(self):
        return str(self.accession_id)


class Blast(models.Model):
    """A class for storing Blast search results and related data. """

    id = models.AutoField(primary_key=True)
    transcript = models.ForeignKey(Transcript, on_delete=models.SET_NULL)
    accession_fk = models.ForeignKey(Accession, null=True, on_delete=models.SET_NULL)
    accession_id = models.CharField(max_length=100)
    orf_hit = models.BooleanField(default=False)
    orf_fk = models.ForeignKey(Orf, null=True, on_delete=models.SET_NULL)
    database = models.CharField(max_length=100)
    percent_identity = models.FloatField()
    evalue = models.FloatField()
    bitscore = models.FloatField()

    def __unicode__(self):
        return "{},{},{}".format(self.transcript.transcript_id, self.database, self.evalue)

    def get_db_url(self):
        if self.database == "Swissprot":
            return "{}{}".format('http://www.uniprot.org/uniprot/', self.accession_id)
        elif self.database == "TrEMBL":
            return "{}{}".format('http://www.uniprot.org/uniref/', self.accession_id)
        else:
            return "#"

    class Meta:
        ordering = ["evalue", "-bitscore"]
        # proxy = True


class Go(models.Model):
    """A class for storing Gene Ontology data. """

    id = models.CharField(max_length=50, primary_key=True, unique=True)
    name = models.TextField()
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return str(self.id)

    def is_category_biological_process(self):
        return str(self.category) == "biological_process"

    def is_category_molecular_function(self):
        return str(self.category) == "molecular_function"

    def is_category_cellular_component(self):
        return str(self.category) == "cellular_component"


class GoUniprotMapper(models.Model):
    """A mapper class between accessions and gene ontology data. """

    id = models.AutoField(primary_key=True)
    accession = models.ForeignKey(Accession, to_field='entry_name', on_delete=models.SET_NULL)
    go_link = models.ForeignKey(Go, to_field='id', on_delete=models.SET_NULL)
