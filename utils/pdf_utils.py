from PyPDF2 import PdfMerger
import os


def merge_pdfs(pdf_list, output_path):
    """Merge multiple PDFs into a single file."""
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()


def collect_pdfs_from_correction_folders(base_folder, subject="mathematiques"):
    """Collect all PDFs from correction folders for a specific subject."""
    all_pdfs = []
    for root, dirs, files in os.walk(base_folder):
        for dir_name in dirs:
            if dir_name.lower() == subject.lower():
                subject_path = os.path.join(root, dir_name)
                for sub_root, sub_dirs, sub_files in os.walk(subject_path):
                    for sub_dir_name in sub_dirs:
                        if sub_dir_name.lower() == "correction":
                            correction_path = os.path.join(sub_root, sub_dir_name)
                            for file_name in os.listdir(correction_path):
                                if file_name.endswith(".pdf"):
                                    pdf_path = os.path.join(correction_path, file_name)
                                    all_pdfs.append(pdf_path)
    return all_pdfs
