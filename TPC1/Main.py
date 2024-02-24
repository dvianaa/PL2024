import fileinput


INTERVALO = 5

class Atleta:
    def __init__(self, _id: str, index: int, dataEmd: str, primeiroNome: str, ultimoNome: str, idade: int, genero: str, morada: str, modalidade: str, clube: str, email: str, federado: bool, resultado: bool):
        self._id = _id
        self.index = index
        self.data_emd = dataEmd
        self.primeiro_nome = primeiroNome
        self.ultimo_nome = ultimoNome
        self.idade = idade
        self.genero = genero
        self.morada = morada
        self.modalidade = modalidade
        self.clube = clube
        self.email = email
        self.federado = federado
        self.resultado = resultado

def parseAtletas(arr: list[str]) -> Atleta:
    return Atleta(arr[0], int(arr[1]), arr[2], arr[3], arr[4], int(arr[5]), arr[6], arr[7], arr[8], arr[9], arr[10], arr[11] == 'true', arr[12] == 'true')


def parseCSV(file) -> list[Atleta]:
    file.readline()
    atletas = [];
    for line in file: atletas.append(parseAtletas(line.strip().split(',')))
    return atletas
    
def percentagemApto(listaAtletas: list[Atleta]) -> float:
    length = len(listaAtletas)
    aptos = 0
    for atleta in listaAtletas:
        if(atleta.resultado == True):
            aptos += 1
    return aptos / float(length)

def percentagemInapto(listaAtletas: list[Atleta]) -> float:
    length = len(listaAtletas)
    inaptos = 0
    for atleta in listaAtletas:
        if(atleta.resultado == False):
            inaptos += 1
    return inaptos / float(length)
    
def listarModalidades(listaAtletas: list[Atleta]) -> list[str]:
    listaModalidades = []
    for atleta in listaAtletas:
        listaModalidades.append(atleta.modalidade)
    return sorted(set(listaModalidades))

def percentagemIdades(listaAtletas: list[Atleta]) -> list[tuple[int, int], float]:
    idades = []
    for atleta in listaAtletas:
        idades.append(atleta.idade)
        
    intervalosIdades = []
    for i in range(0, 100, INTERVALO):
        intervalosIdades.append((i, i + INTERVALO))
        
    numIdade = [0] * len(intervalosIdades)
    for idade in idades:
        for i, intervalo in enumerate(intervalosIdades):
            if intervalo[0] <= idade < intervalo[1]:
                numIdade[i] += 1

    percentagens = []
    for contagem, intervalo in zip(numIdade, intervalosIdades):
        percentagem = (contagem/len(idades))*100
        percentagens.append(((intervalo[0], intervalo[1]), percentagem))
        
    return percentagens

def main():
    atletas = parseCSV(fileinput.input())
    print("Percentagem de atletas aptos: ", percentagemApto(atletas))
    print("Percentagem de atletas inaptos: ", percentagemInapto(atletas))
    print("Lista de modalidades: ", listarModalidades(atletas))
    print("Distribuição por intervalo de idades: ", percentagemIdades(atletas))

if __name__ == "__main__":
    main()