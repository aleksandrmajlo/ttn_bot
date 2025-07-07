def convert_to_pdf(docx_path):
    from docx2pdf import convert
    import os
    output_pdf = docx_path.replace(".docx", ".pdf")
    convert(docx_path, output_pdf)
    return output_pdf