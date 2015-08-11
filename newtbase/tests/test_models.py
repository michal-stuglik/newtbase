""" Test module for models. """

from django.test import TestCase
from django import test
from model_mommy import mommy
from newtbase.models import Transcript, Orf, Accession, Blast, Go, GoUniprotMapper

""" Example
class TranscriptTestMommy(TestCase):
    def test_transcript(self):
        o = mommy.make(Transcript)
        self.assertTrue(isinstance(o, Transcript))
        self.assertIsInstance(o, Transcript)
        self.assertEqual(o.__unicode__(), o.transcript_id)
        self.assertTrue(o.sequence is not None)
"""


class TranscriptTestMommy(TestCase):
    def setUp(self):
        self.o = mommy.make(Transcript, sequence="AACC")

    def tearDown(self):
        self.o.delete()

    def test_transcript(self):
        self.assertEqual(self.o.__unicode__(), self.o.transcript_id)
        self.assertIsNotNone(self.o.sequence)

    def test_sequence_length(self):
        self.assertTrue(self.o.get_sequence_length() == 4)


class OrfTestMommy(TestCase):

    def setUp(self):
        self.o = mommy.make(Orf)

    def tearDown(self):
        self.o.delete()

    def test_orf(self):
        self.assertEquals(self.o.__unicode__(),self.o.orf_id)
        self.assertTrue(isinstance(self.o.transcript, Transcript))


class AccessionTestMommy(TestCase):

    def setUp(self):
        self.o = mommy.make(Accession)

    def tearDown(self):
        self.o.delete()

    def test_accession(self):
        self.assertEquals(self.o.__unicode__(), self.o.accession_id)


class BlastTestMommy(TestCase):

    def setUp(self):
        self.o = mommy.make(Blast, database="Swissprot")

    def tearDown(self):
        self.o.delete()

    def test_blast(self):
        self.assertIsInstance(self.o, Blast)
        self.assertEquals(self.o.__unicode__(), "{},{},{}".format(self.o.transcript_id, self.o.database, self.o.evalue))
        self.assertTrue(self.o.get_db_url(), "{}{}".format('http://www.uniprot.org/uniprot/', self.o.accession_id))


class GoTestMommy(TestCase):

    def setUp(self):
        self.bd = mommy.make(Go, category="biological_process")
        self.o = mommy.make(Go)

    def tearDown(self):
        self.o.delete()
        self.bd.delete()

    def test_go(self):
        self.assertEquals(self.o.__unicode__(), self.o.id)
        self.assertTrue(self.bd.is_category_biological_process())
        self.assertFalse(self.bd.is_category_molecular_function())
        self.assertFalse(self.bd.is_category_cellular_component())


class GoUniprotMapperTestMommy(TestCase):

    def setUp(self):
        self.o = mommy.make(GoUniprotMapper)

    def tearDown(self):
        self.o.delete()

    def test_gouniprot(self):
        self.assertTrue(isinstance(self.o, GoUniprotMapper))


# if __name__ == '__main__':
#     test.main()
