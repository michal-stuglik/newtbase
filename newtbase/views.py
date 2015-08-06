import zipfile
import tempfile

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.servers.basehttp import FileWrapper
from django.template import RequestContext

from models import Transcript, Blast, Orf, Go, GoUniprotMapper


# Create your views here.

def home(request):
    assert request.method == 'GET'
    # do_something_for_get()
    return render_to_response('index.html')


def about(request):
    assert request.method == 'GET'
    # do_something_for_get()
    return render_to_response('about.html')


def download(request):
    assert request.method == 'GET'
    # do_something_for_get()
    return render_to_response('download.html')


def search(request):
    assert request.method == 'GET'
    # do_something_for_get()
    return render_to_response('search.html')


def publications(request):
    assert request.method == 'GET'
    # do_something_for_get()
    return render_to_response('publications.html')


from newtbase.settings.base import DOWNLOAD_DATA
from django.http import StreamingHttpResponse


def send_zipfile(request):
    """
    Create a ZIP file on disk and transmit it in chunks of 8KB,
    without loading the whole file into memory. A similar approach can
    be used for large dynamic PDF files.
    """
    temp = tempfile.TemporaryFile()
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
    for index in range(10):
        filename = __file__  # Select your files here.
        archive.write(filename, 'file%d.txt' % index)
    archive.close()
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=test.zip'
    response['Content-Length'] = temp.tell()
    temp.seek(0)
    return response


def download_tgm(request):
    """
    https://djangosnippets.org/snippets/365/

    """

    assert request.method == 'GET'

    filename = DOWNLOAD_DATA['LvLm_tgm']
    wrapper = FileWrapper(file(filename))

    response = StreamingHttpResponse(wrapper, content_type="application/tar.gz")
    response['Content-Disposition'] = 'attachment; filename="Lvulg_x_Lmont_tgm.tar.gz"'

    return response


def download_L_helveticus_tgm(request):
    """
    https://djangosnippets.org/snippets/365/

    """

    assert request.method == 'GET'

    filename = DOWNLOAD_DATA['Lh_tgm']
    wrapper = FileWrapper(file(filename))

    response = StreamingHttpResponse(wrapper, content_type="application/tar.gz")
    response['Content-Disposition'] = 'attachment; filename="Lhelveticus_tgm.tar.gz"'

    return response


def download_mips(request):
    """
    https://djangosnippets.org/snippets/365/

    """

    assert request.method == 'GET'

    filename = DOWNLOAD_DATA['mips']
    wrapper = FileWrapper(file(filename))

    response = StreamingHttpResponse(wrapper, content_type="application/tar.gz")
    response['Content-Disposition'] = 'attachment; filename="mips.tar.gz"'

    return response


def download_immune_genes(request):
    """
    https://djangosnippets.org/snippets/365/

    """

    assert request.method == 'GET'

    filename = DOWNLOAD_DATA['immune_gene']
    wrapper = FileWrapper(file(filename))

    response = StreamingHttpResponse(wrapper, content_type="application/tar.gz")
    response['Content-Disposition'] = 'attachment; filename="immune_gene.tar.gz"'

    return response


def download_mtdna(request):
    """
    https://djangosnippets.org/snippets/365/

    """

    assert request.method == 'GET'

    filename = DOWNLOAD_DATA['mtdna']
    wrapper = FileWrapper(file(filename))

    response = StreamingHttpResponse(wrapper, content_type="application/tar.gz")
    response['Content-Disposition'] = 'attachment; filename="mtdna.tar.gz"'

    return response


def download_orfs(request):
    """
    https://djangosnippets.org/snippets/365/

    """

    assert request.method == 'GET'

    filename = DOWNLOAD_DATA['orfs']
    wrapper = FileWrapper(file(filename))

    response = StreamingHttpResponse(wrapper, content_type="application/tar.gz")
    response['Content-Disposition'] = 'attachment; filename="orfs.tar.gz"'

    return response


def download_contig_as_fasta(request, contig_name):
    """
    https://djangosnippets.org/snippets/365/

    """

    assert request.method == 'GET'

    transcript = get_object_or_404(Transcript, transcript_id=contig_name)
    ff = tempfile.NamedTemporaryFile(mode='w+b', prefix='contig_name', delete=True)
    ff.write(">{}\n".format(contig_name))
    ff.write("{}\n".format(transcript.sequence))

    wrapper = FileWrapper(file(ff.name))
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

    wrapper = FileWrapper(file(ff.name))
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

    # blast_list_all_dbs = Blast.objects.filter(transcript=transcript).order_by("evalue", "accession_id").distinct("evalue", "accession_id")
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
