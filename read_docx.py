import sys, zipfile, xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

for path in sys.argv[1:]:
    try:
        if path.endswith('.docx'):
            doc = zipfile.ZipFile(path)
            xml_content = doc.read('word/document.xml')
            doc.close()
            tree = ET.XML(xml_content)
            texts = []
            for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                p_text = ''.join([n.text for n in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if n.text])
                if p_text.strip(): texts.append(p_text.strip())
            print(f'--- {path} ---')
            print('\n'.join(texts[:30]))
        else:
            print(f'--- {path} is not docx ---')
    except Exception as e:
        print(f'Error reading {path}: {e}')
