""" Module with helper classes and functions. """


def assign_protein_data_to_blast_results(blast_records_in_object_and_list):
    """Searches data related to transcript in local database.

       Modify objects by assigning protein's info to transcript.
    """

    from newtbase.models import Transcript, Blast

    for blast_record in blast_records_in_object_and_list:
        for al in blast_record.alignments:
            try:
                al.hit_url = "/tgm/{}".format(str(al.hit_def))
                al.hit_protein_name = "---"

                t = Transcript.objects.get(transcript_id=al.hit_def)
                b = Blast.objects.filter(transcript=t, database="Swissprot")

                if len(b) > 0:
                    al.hit_protein_name = "{} / {}".format(b[0].accession_fk.gene_name, b[0].accession_fk.protein_name)

            except Exception as inst:
                print(type(inst))  # the exception instance
                print(inst.args)  # arguments stored in .args
                print(inst)  # __str__ allows args to be printed directly

    return blast_records_in_object_and_list
