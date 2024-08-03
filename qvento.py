import json
"""
qvento.py - programa para determinar carga de vento em edificações
------------------------------------------------------------------
info:
 - As especificações aqui foram retiradas da NBR 6123 - ação do vento
 - programa puramente didático
 - edite o arquivo input.json com os dados do seu problema
"""
# functions
def get_param_b(categoria, classe):
    if (categoria-1 > 4 or classe-1 > 2):
        return "Erro"
    b = [[1.1, 1.11, 1.12],
         [1.0, 1.00, 1.00],
         [0.94, 0.94, 0.93],
         [0.86, 0.85, 0.84],
         [0.74, 0.73, 0.71]]
    return b[categoria-1][classe-1]

def get_param_p(categoria, classe):
    if (categoria-1 > 4 or classe-1 > 2):
        return "Erro"
    p = [[0.06, 0.065, 0.07],
         [0.085, 0.09, 0.10],
         [0.10, 0.105, 0.115],
         [0.12, 0.125, 0.135],
         [0.15, 0.16, 0.175]]
    return p[categoria-1][classe-1]

def get_param_fr(classe):
    if (classe-1 > 2):
        return "Erro"
    fr = [1, 0.98, 0.95]
    return fr[classe-1]

def read_json(name_File):
    file = open(name_File)
    data_file = json.load(file)
    file.close()
    return data_file

print("-----------------------------------")
print("|            QVENTO.py            |")
print("-----------------------------------")

# input
data = read_json('./input_example.json')
z=[]
pe=data["pe_direito"]
#Esse processo falha em situacoes onde a divisao nao e inteira
while pe <= data["altura"]:
    z.append(pe)
    pe+=data["pe_direito"]

area_influencia_maior = data["maior_lado"] * data["pe_direito"]
area_influencia_menor = data["menor_lado"] * data["pe_direito"]
ca_maior = data["ca_maior"] # valor retirado do abaco
ca_menor = data["ca_menor"] # valor retirado do abaco

# Depois converter tudo para funcoes
velocidade_caracteristica = []
b = get_param_b(data["categoria"],data["classe"])
p = get_param_p(data["categoria"],data["classe"])
fr = get_param_fr(data["classe"])
for i in z:
    s2_temp = b*fr*(i/10)**p
    v_temp  = data["velocidade_basica"]*data["s1"]*s2_temp*data["s3"]
    velocidade_caracteristica.append(v_temp)

pressao_dinamica = []
for v in velocidade_caracteristica:
    pressao_dinamica_temp = 0.613 * (v**2)
    pressao_dinamica.append(pressao_dinamica_temp)

forca_do_vento_maior_lado = []
forca_do_vento_menor_lado = []
for q in pressao_dinamica:
    forca_maior_lado_temp = ca_maior * q * area_influencia_maior
    forca_do_vento_maior_lado.append(forca_maior_lado_temp)
    
    forca_menor_lado_temp = ca_menor * q * area_influencia_menor
    forca_do_vento_menor_lado.append(forca_menor_lado_temp)

# output
print("-----------------------------------")
print(" z(m)       Vk(m/s)       q (N/m2) ")
print("-----------------------------------")
for i in range(0, len(z)):
  print(f'{z[i]:5.2f} {velocidade_caracteristica[i]:13.2f} {pressao_dinamica[i]:13.2f}')
print("-----------------------------------")
print('\n')
print("----------------------------------------")
print(" z(m)       F maior(N)      F menor(N)")
print("----------------------------------------")
for i in range(0, len(z)):
    print(f'{z[i]:5.2f} {forca_do_vento_maior_lado[i]:15.2f} {forca_do_vento_menor_lado[i]:15.2f}')
print("----------------------------------------")
