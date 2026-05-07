# Clinical Variant Triage Pipeline

This repository contains an automated bioinformatics pipeline designed to mimic a clinical genomics informatics platform. It demonstrates the ability to triage, filter, and annotate genetic variants from Next-Generation Sequencing (NGS) data.

## ⚠️ Disclaimer
**This project uses a "toy" dataset.** The VCF file provided in this repository (`data/patient_sample.vcf`) contains mock, synthetic mutations generated for the purpose of testing the pipeline's architecture and logic. It does not contain real patient data.

## Pipeline Architecture
The pipeline is managed by **Snakemake** and utilizes a combination of Bash (`awk`) and **Python** to process the data.

### Workflow Steps:
1. **Primary Triage (`filter_vcf`)**: 
   - Reads the raw Variant Call Format (VCF) file.
   - Uses `awk` to parse the file and filter out any mutations that do not strictly meet the `"PASS"` criteria in the quality/filter column.
2. **Clinical Annotation (`generate_clinical_report`)**:
   - A custom Python script (`scripts/annotate_variants.py`) reads the filtered VCF and the reference Genome Annotation file (`sequence.gff3`).
   - It cross-references the genomic coordinates of each mutation against the GFF3 features to determine which specific genes or coding sequences (CDS) were impacted.
   - Outputs a final clinical report in CSV format for downstream medical review.

## Setup and Requirements
This project includes an `environment.yml` file to ensure complete reproducibility. You can instantly recreate the exact software environment required to run this pipeline:

```bash
# Create the environment
conda env create -f environment.yml

# Activate the environment
conda activate variant_triage_env
```

## How to Run
Once your environment is activated, execute the pipeline from the root directory by running:
```bash
snakemake --cores 1
```

## Outputs
Upon successful execution, the pipeline will generate:
- `results/filtered_patient.vcf`: The cleaned intermediate VCF file.
- `results/clinical_report.csv`: The final annotated report detailing the genomic impact of each valid mutation.
