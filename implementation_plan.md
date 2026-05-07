# Goal: Build a Clinical Variant Triage Pipeline

We will build a portfolio-ready bioinformatics pipeline that mimics a clinical genomics informatics platform. This project will demonstrate your skills in Snakemake, Python, Bash, and Clinical Data Formats (VCF/GFF3), perfectly aligning with the BCGSC job requirements.

## Proposed Changes

We will create a new dedicated folder for this project to keep it clean for your GitHub repository.

### 1. Project Structure Setup
Create a new directory `~/projects/Clinical-Variant-Triage/` and initialize it with standard bioinformatics folders (`data/`, `scripts/`, `results/`). We will copy your existing `sequence.gff3` file into the `data/` folder.

### 2. Generate Mock Clinical Data
#### [NEW] `data/patient_sample.vcf`
We will create a highly realistic mock VCF (Variant Call Format) file containing synthetic DNA mutations against the SARS-CoV-2 reference sequence.

### 3. The Python Annotator
#### [NEW] `scripts/annotate_variants.py`
We will write a Python script that takes a VCF file and a GFF3 file. It will parse the mutations, cross-reference their coordinates against the GFF3 file to determine which genes were mutated, and generate a final "Clinical Report" in CSV format.

### 4. The Snakemake Workflow
#### [NEW] `Snakefile`
We will write a master Snakemake workflow with two core rules:
1. `filter_vcf`: Uses your new `awk` skills to filter out low-quality mutations from the raw VCF file (replicating a primary triage step).
2. `generate_clinical_report`: Runs the Python script to combine the filtered VCF with the GFF3 and produce the final clinical report.

## User Review Required
> [!IMPORTANT]
> Since this is for your GitHub portfolio, I highly recommend we initialize this folder as a Git repository (`git init`) right from the start. That way, we can commit our code step-by-step and you can push it straight to GitHub when we finish! Shall we include Git initialization?

## Verification Plan
1. Run `snakemake --cores 1` in the new project folder.
2. Verify that `results/clinical_report.csv` is successfully generated and accurately lists the genes that were mutated in our mock patient data.
