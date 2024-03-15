direcciones = {
    'Juan': 'C/Moncofar, 5',
    'Antonio': 'C/Enmedio, 15',
    'Jose': 'C/Mayor, 30'
}

#print(direcciones.get('Juan'))

for nombre, direccion in direcciones.items():
    print(f'{nombre}: {direccion}')