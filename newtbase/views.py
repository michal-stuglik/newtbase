import zipfile
import tempfile

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
# from django.core.servers.basehttp import FileWrapper
from django.core.files import File

from django.template import RequestContext

from models import Transcript, Blast, Orf, GoUniprotMapper

from newtbase.settings.base import DOWNLOAD_DATA
from django.http import StreamingHttpResponse


def home(request):
    assert request.method == 'GET'
    return render_to_response('index.html')


def about(request):
    assert request.method == 'GET'
    return render_to_response('about.html')


def download(request):
    assert request.method == 'GET'
    return render_to_response('download.html')


def search(request):
    assert request.method == 'GET'
    return render_to_response('search.html')


def publications(request):
    assert request.method == 'GET'
    return render_to_response('publications.html')


def download_data_package(request, download_data_key, out_file_name):
    """ Generic download method for compressed data.
        Download snippet source https://djangosnippets.org/snippets/365/
    """

    assert request.method == 'GET'

    filename = DOWNLOAD_DATA[download_data_key]
    wrapper = File(file(filename))

    response = StreamingHttpResponse(wrapper, content_type="application/tar.gz")
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(out_file_name)

    return response


def download_tgm(request):
    """Dowload TGM for Lv & Lm. """
    return download_data_package(request, 'LvLm_tgm', "Lvulg_x_Lmont_tgm.tar.gz")


def download_L_helveticus_tgm(request):
    """Download TGM for Lh. """
    return download_data_package(request, 'Lh_tgm', "Lhelveticus_tgm.tar.gz")


def download_mips(request):
    """Download mips markers. """
    return download_data_package(request, 'mips', "mips.tar.gz")


def download_immune_genes(request):
    """Download immune genes. """
    return download_data_package(request, 'immune_gene', "immune_gene.tar.gz")


def download_mtdna(request):
    """Download mtDNA. """
    return download_data_package(request, 'mtdna', "mtdna.tar.gz")


def download_orfs(request):
    """Download ORFs. """
    return download_data_package(request, 'orfs', "orfs.tar.gz")


def download_contig_as_fasta(request, contig_name):
    """
    https://djangosnippets.org/snippets/365/

    """

    assert request.method == 'GET'

    transcript = get_object_or_404(Transcript, transcript_id=contig_name)
    ff = tempfile.NamedTemporaryFile(mode='w+b', prefix='contig_name', delete=True)
    ff.write(">{}\n".format(contig_name))
    ff.write("{}\n".format(transcript.sequence))

    wrapper = File(file(ff.name))
    response = StreamingHttpResponse(wrapper, content_type="application/fasta")
    response['Content-Disposition'] = 'attachment; filename="{}.{}"'.format(contig_name, "fasta")

    ff.close()

    return response


def download_orf_as_fasta(request, orf_name):
    assert request.method == 'GET'

    orf = get_object_or_404(Orf, orf_id=orf_name)

    ff = tempfile.NamedTemporaryFile(mode='w+b', prefix='orf_name', delete=True)
    ff.write(">{}\n".format(orf_name))
    ff.write("{}\n".format(orf.peptide))

    wrapper = File(file(ff.name))
    response = StreamingHttpResponse(wrapper, content_type="application/fasta")
    response['Content-Disposition'] = 'attachment; filename="{}.{}"'.format(orf_name, "fasta")

    ff.close()

    return response


def get_tgm_by_name(request, tgm_name):
    # transcript = Transcript.objects.get(transcript_id=tgm_name)
    transcript = get_object_or_404(Transcript, transcript_id=tgm_name)

    gene_name = "---"
    protein_name = "---"

    # protein name & gene name for best blast
    blast_list = Blast.objects.filter(transcript=transcript, database='Swissprot')
    best_blast = None
    if len(blast_list) > 0:
        best_blast = blast_list[0]

        # Accession data if there are any
        if best_blast.accession_fk:
            gene_name, protein_name = best_blast.accession_fk.gene_name, best_blast.accession_fk.protein_name

    blast_list_all_dbs = Blast.objects.filter(transcript=transcript)

    # leave only unique accession ids
    blast_list_all_dbs = filter_unique_accession_ids(blast_list_all_dbs)

    # ORF info
    orfs = Orf.objects.filter(transcript=transcript)

    # GO
    gos_list = []
    if best_blast:
        accession = best_blast.accession_fk
        gos_mapper = GoUniprotMapper.objects.filter(accession=accession)

        if len(gos_mapper) > 0:
            gos_list = [g.go_link for g in gos_mapper]
            # gos = Go.objects.filter()

    return render_to_response('tgm.html', {
        'transcript': transcript,
        'gene_name': gene_name,
        'protein_name': protein_name,
        'blast_list_all_dbs': blast_list_all_dbs,
        'orfs': orfs,
        'gos_list': gos_list,

    }, context_instance=RequestContext(request))


def filter_unique_accession_ids(blast_list_all_dbs):
    accession_hit_set = set()
    uniq_blast_list = []

    for blast in blast_list_all_dbs:
        if blast.accession_id not in accession_hit_set:
            accession_hit_set.add(blast.accession_id)
            uniq_blast_list.append(blast)

    return uniq_blast_list
