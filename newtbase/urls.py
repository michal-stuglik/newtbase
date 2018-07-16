from django.contrib import admin
from django.urls import path, include

admin.autodiscover()
from newtbase import views
from blastplus import views as blast_view
from newtbase.utils import assign_protein_data_to_blast_results

urlpatterns = [
    path('', views.home, name='home'),
    # path('admin', admin.site.urls),

    path('search', views.search),
    path('publications', views.publications),
    path('about', views.about),

    # contigs annotation
    path('tgm_contig/', views.get_tgm_by_name),  # "c100007_g1_i1"

    # downloads
    path('download', views.download),
    path('download/tgm', views.download_tgm),
    path('download/L_helveticus_tgm', views.download_L_helveticus_tgm),
    # url('download/mips/', views.download_mips),
    path('download/immune_genes', views.download_immune_genes),
    path('download/mtdna', views.download_mtdna),
    path('download/orfs', views.download_orfs),

    # annotation download
    path('download_contig_as_fasta/', views.download_contig_as_fasta),
    path('download_orf_as_fasta/', views.download_orf_as_fasta),
    path('download_hsp_as_txt/', views.download_hsp_as_txt),
    path('download_seq_as_fasta/', views.download_seq_as_fasta),

    # # newtbase url/templates override
    path('blast/blastn', blast_view.blastn,
         {'template_init': 'blast.html', 'template_result': 'blast_results.html',
          'extra_context': assign_protein_data_to_blast_results}),

    path('blast/tblastn', blast_view.tblastn,
         {'template_init': 'blast.html', 'template_result': 'blast_results.html',
          'extra_context': assign_protein_data_to_blast_results}),

    path('blast/blast', blast_view.blast,
         {'template_init': 'blast.html', 'template_result': 'blast_results.html',
          'extra_context': assign_protein_data_to_blast_results}),

    path('blast', include('blastplus.urls')),
]
