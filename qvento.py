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
def read_json(name_File):
    file = open(name_File)
    data_file = json.load(file)
    file.close()
    return data_file

print("-----------------------------------")
print("|            QVENTO.py            |")
print("-----------------------------------")

# input
data = read_json('./input.json')
z = [10, 20, 30]
area_influencia_maior = data["maior_lado"] * data["pe_direito"]
area_influencia_menor = data["menor_lado"] * data["pe_direito"]
ca_maior = data["ca_maior"] # valor retirado do abaco
ca_menor = data["ca_menor"] # valor retirado do abaco

velocidade_caracteristica = []
for i in z:
    s2_temp = data["parametro_meteorologico"]["b"]*data["parametro_meteorologico"]["fr"]*(i/10)**data["parametro_meteorologico"]["p"]
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
