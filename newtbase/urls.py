from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()
from newtbase import views
from blastplus import views as blast_view
from newtbase.utils import assign_protein_data_to_blast_results

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^search/$', views.search),
    url(r'^publications/$', views.publications),
    url(r'^about/$', views.about),

    # contigs annotation
    url(r'^tgm/([c]\d{1,}[_][g]\d{1,}[_][i]\d{1,})/$', views.get_tgm_by_name),  # "c100007_g1_i1"

    # downloads
    url(r'^download/$', views.download),
    url(r'^download/tgm/$', views.download_tgm),
    url(r'^download/L_helveticus_tgm/$', views.download_L_helveticus_tgm),
    # url(r'^download/mips/$', views.download_mips),
    url(r'^download/immune_genes/$', views.download_immune_genes),
    url(r'^download/mtdna/$', views.download_mtdna),
    url(r'^download/orfs/$', views.download_orfs),

    # annotation download
    url(r'^download_contig_as_fasta/([c]\d{1,}[_][g]\d{1,}[_][i]\d{1,})/$', views.download_contig_as_fasta),
    url(r'^download_orf_as_fasta/([c]\d{1,}[_][g]\d{1,}[_][i]\d{1,}[|][m][.]\d{1,})/$', views.download_orf_as_fasta),
    url(r'^download_hsp_as_txt/$', views.download_hsp_as_txt),
    url(r'^download_seq_as_fasta/$', views.download_seq_as_fasta),

    # # newtbase url/templates override
    url(r'^blast/blastn/$', blast_view.blastn,
        {'template_init': 'blast.html', 'template_result': 'blast_results.html',
         'extra_context': assign_protein_data_to_blast_results}),

    url(r'^blast/tblastn/$', blast_view.tblastn,
        {'template_init': 'blast.html', 'template_result': 'blast_results.html',
         'extra_context': assign_protein_data_to_blast_results}),

    url(r'^blast/blast/$', blast_view.blast,
        {'template_init': 'blast.html', 'template_result': 'blast_results.html',
         'extra_context': assign_protein_data_to_blast_results}),

    url(r'^blast/', include('blastplus.urls')),
]
