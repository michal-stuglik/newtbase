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
    def test_transcript(self):
        o = mommy.make(Transcript)
        self.assertEqual(o.__unicode__(), o.transcript_id)
        self.assertTrue(o.sequence is not None)


class OrfTestMommy(TestCase):
    def test_orf(self):
        o = mommy.make(Orf)
        self.assertEquals(o.__unicode__(), o.orf_id)
        self.assertTrue(isinstance(o.transcript, Transcript))


class AccessionTestMommy(TestCase):
    def test_accession(self):
        o = mommy.make(Accession)
        self.assertEquals(o.__unicode__(), o.accession_id)


class BlastTestMommy(TestCase):
    def test_blast(self):
        o = mommy.make(Blast)
        self.assertTrue(isinstance(o, Blast))
        self.assertEquals(o.__unicode__(), "{},{},{}".format(o.transcript_id, o.database, o.evalue))


class GoTestMommy(TestCase):
    def test_go(self):
        o = mommy.make(Go)
        self.assertEquals(o.__unicode__(), o.id)


class GoUniprotMapperTestMommy(TestCase):
    def test_gouniprot(self):
        o = mommy.make(GoUniprotMapper)
        self.assertTrue(isinstance(o, GoUniprotMapper))


if __name__ == '__main__':
    test.main()
