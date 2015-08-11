from django.test import TestCase


class NewtbaseTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_blast(self):
        resp = self.client.get('/blast/blastn/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('form' in resp.context)
        self.assertIsNotNone(resp.context['form'])
        self.assertTrue('sequence_sample_in_fasta' in resp.context)

    def test_about(self):
        resp = self.client.get('/about/')
        self.assertEqual(resp.status_code, 200)

    def test_download(self):
        resp = self.client.get('/download/')
        self.assertEqual(resp.status_code, 200)

    def test_publications(self):
        resp = self.client.get('/publications/')
        self.assertEqual(resp.status_code, 200)
