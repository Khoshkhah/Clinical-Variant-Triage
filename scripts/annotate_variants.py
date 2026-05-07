import sys
import csv

def load_gff3(gff3_path):
    """Parses the GFF3 file and extracts feature coordinates."""
    features = []
    with open(gff3_path, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            if len(parts) < 9:
                continue
            
            feature_type = parts[2]
            start = int(parts[3])
            end = int(parts[4])
            
            # Extract Gene Name or ID from the messy 9th column!
            info = parts[8]
            gene_name = "Unknown"
            for item in info.split(';'):
                if item.startswith('Name=') or item.startswith('gene='):
                    gene_name = item.split('=')[1]
                    break
            
            features.append({
                'type': feature_type,
                'start': start,
                'end': end,
                'name': gene_name
            })
    return features

def annotate_variants(vcf_path, gff3_path, output_path):
    """Reads VCF, finds overlapping GFF3 features, and writes a CSV report."""
    print("Loading GFF3 annotations...")
    annotations = load_gff3(gff3_path)
    
    print("Annotating VCF variants...")
    results = []
    
    with open(vcf_path, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            if len(parts) < 8:
                continue
                
            pos = int(parts[1])
            ref = parts[3]
            alt = parts[4]
            qual = parts[5]
            
            # Find which genes this mutation lands inside of!
            overlapping_genes = []
            for feature in annotations:
                # We only care about major features like 'gene' or 'CDS'
                if feature['type'] in ['gene', 'CDS'] and feature['start'] <= pos <= feature['end']:
                    overlapping_genes.append(f"{feature['name']} ({feature['type']})")
            
            # If it didn't hit any genes, label it as Intergenic
            hit_genes = " | ".join(overlapping_genes) if overlapping_genes else "Intergenic (No Gene)"
            
            results.append({
                'Position': pos,
                'Ref': ref,
                'Alt': alt,
                'Quality': qual,
                'Impacted_Genes': hit_genes
            })

    print(f"Writing clinical report to {output_path}...")
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Position', 'Ref', 'Alt', 'Quality', 'Impacted_Genes'])
        writer.writeheader()
        writer.writerows(results)
        
    print("Clinical Triage Complete!")

if __name__ == "__main__":
    # Ensure the user provided the correct number of files
    if len(sys.argv) != 4:
        print("Usage: python annotate_variants.py <filtered_vcf> <gff3> <output_csv>")
        sys.exit(1)
        
    vcf_file = sys.argv[1]
    gff3_file = sys.argv[2]
    out_file = sys.argv[3]
    
    annotate_variants(vcf_file, gff3_file, out_file)
