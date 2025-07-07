def fill_template(data):
    from docx import Document
    import os
    template_path = "templates/ttn_template.docx"
    doc = Document(template_path)
    for p in doc.paragraphs:
        if '{{date}}' in p.text:
            p.text = p.text.replace("{{date}}", data['date'])
        if '{{sender}}' in p.text:
            p.text = p.text.replace("{{sender}}", data['sender'])
        if '{{receiver}}' in p.text:
            p.text = p.text.replace("{{receiver}}", data['receiver'])
        if '{{items}}' in p.text:
            p.text = p.text.replace("{{items}}", data['items'])
    output_path = f"data/output/ttn_filled.docx"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.save(output_path)
    print("fill_template output_path:", output_path)
    return output_path