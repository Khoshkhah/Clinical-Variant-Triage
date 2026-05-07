# Snakefile for Clinical Variant Triage Pipeline

rule all:
    input:
        "results/clinical_report.csv"

rule filter_vcf:
    """
    Step 1: Primary Triage.
    Use awk to filter the raw VCF. Keep only header lines (starting with #) 
    or variants where the FILTER column (7th column) is exactly "PASS".
    """
    input:
        vcf="data/patient_sample.vcf"
    output:
        filtered_vcf="results/filtered_patient.vcf"
    shell:
        """
        awk '$7 == "PASS" || /^#/' {input.vcf} > {output.filtered_vcf}
        """

rule generate_clinical_report:
    """
    Step 2: Clinical Annotation.
    Pass the filtered VCF and the GFF3 annotation file into our custom Python script
    to generate the final clinical report.
    """
    input:
        filtered_vcf="results/filtered_patient.vcf",
        gff="data/sequence.gff3",
        script="scripts/annotate_variants.py"
    output:
        report="results/clinical_report.csv"
    shell:
        """
        python {input.script} {input.filtered_vcf} {input.gff} {output.report}
        """
