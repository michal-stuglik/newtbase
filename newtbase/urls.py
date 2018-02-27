from django.contrib import admin
from django.urls import path, include

admin.autodiscover()
from newtbase import views
from blastplus import views as blast_view
from newtbase.utils import assign_protein_data_to_blast_results

urlpatterns = [
    path(r'^$', views.home, name='home'),
    path(r'^admin/', admin.site.urls),

    path(r'^search/$', views.search),
    path(r'^publications/$', views.publications),
    path(r'^about/$', views.about),

    # contigs annotation
    path(r'^tgm/([c]\d{1,}[_][g]\d{1,}[_][i]\d{1,})/$', views.get_tgm_by_name),  # "c100007_g1_i1"

    # downloads
    path(r'^download/$', views.download),
    path(r'^download/tgm/$', views.download_tgm),
    path(r'^download/L_helveticus_tgm/$', views.download_L_helveticus_tgm),
    # url(r'^download/mips/$', views.download_mips),
    path(r'^download/immune_genes/$', views.download_immune_genes),
    path(r'^download/mtdna/$', views.download_mtdna),
    path(r'^download/orfs/$', views.download_orfs),

    # annotation download
    path(r'^download_contig_as_fasta/([c]\d{1,}[_][g]\d{1,}[_][i]\d{1,})/$', views.download_contig_as_fasta),
    path(r'^download_orf_as_fasta/([c]\d{1,}[_][g]\d{1,}[_][i]\d{1,}[|][m][.]\d{1,})/$', views.download_orf_as_fasta),
    path(r'^download_hsp_as_txt/$', views.download_hsp_as_txt),
    path(r'^download_seq_as_fasta/$', views.download_seq_as_fasta),

    # # newtbase url/templates override
    path(r'^blast/blastn/$', blast_view.blastn,
        {'template_init': 'blast.html', 'template_result': 'blast_results.html',
         'extra_context': assign_protein_data_to_blast_results}),

    path(r'^blast/tblastn/$', blast_view.tblastn,
        {'template_init': 'blast.html', 'template_result': 'blast_results.html',
         'extra_context': assign_protein_data_to_blast_results}),

    path(r'^blast/blast/$', blast_view.blast,
        {'template_init': 'blast.html', 'template_result': 'blast_results.html',
         'extra_context': assign_protein_data_to_blast_results}),

    path(r'^blast/', include('blastplus.urls')),
]
