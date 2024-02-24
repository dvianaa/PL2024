import re

def markdownToHTML(markdownText: str) -> str:
    
    # sub cabecalhos
    markdownText = re.sub(r'^#\s(.+)$', r'<h1>\1</h1>', markdownText, flags=re.MULTILINE)
    markdownText = re.sub(r'^##\s(.+)$', r'<h2>\1</h2>', markdownText, flags=re.MULTILINE)
    markdownText = re.sub(r'^###\s(.+)$', r'<h3>\1</h3>', markdownText, flags=re.MULTILINE)
    
    #sub negritos
    markdownText = re.sub(r'\*\*(.+)\*\*', r'<strong>\1</strong>', markdownText)
    
    #substituir italicos
    markdownText = re.sub(r'\*(.+)\*', r'<em>\1</em>', markdownText)
    
    #substituir imagens primeiro do que os links para nao substituir as imagens como se fossem links
    markdownText = re.sub(r"!\[([^\]]+)\]\(([^\)]+)\)", r'<img src="\2" alt="\1"/>', markdownText)
    
    #sub links
    markdownText = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', markdownText)
    
    #sub listas
    markdownText = re.sub(r'(?:(^\d+\.\s.*$)\n)+', processList, markdownText, flags=re.MULTILINE)    
    return markdownText

# func para lidar com listas
def processList(match: re.Match) -> str:
    items = re.findall(r'^\d+\.\s(.+)$', match.group(0), flags=re.MULTILINE)
    if items:
        list_items = '\n'.join([f'<li>{item}</li>' for item in items])
        return f'<ol>\n{list_items}\n</ol>\n'
    return ''

markdownText = """  
# Exemplo
Este é um **exemplo** ...
Este é um *exemplo* ...
1. Primeiro item
2. Segundo item
3. Terceiro item
Como pode ser consultado em [página da UC](http://www.uc.pt)
Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
"""

HTMLText = markdownToHTML(markdownText)
print(HTMLText)