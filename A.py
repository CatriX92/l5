def leer_caso(data, linea_actual):
    # evita linea en blanco al final del output
    if linea_actual >= len(data):
        return None, None, linea_actual

    primer_linea = list(map(int, data[linea_actual].split()))
    capacidad = primer_linea[0]
    n_objetos = primer_linea[1]
    linea_actual += 1

    objetos = []
    
    # Leer los n objetos
    for i in range(n_objetos):
        linea_obj = data[linea_actual].split()
        valor = int(linea_obj[0])
        peso = int(linea_obj[1])
        
        # peso, valor e índice original (i)
        objetos.append({'indice': i, 'value': valor, 'weight': peso})
        linea_actual += 1

    return capacidad, objetos, linea_actual 

def reconstruir_solucion(capacidad, objetos, DP):
    # Realiza el backtracking para encontrar los indices
    n = len(objetos)
    items_elegidos_indices = []
    w = capacidad
    
    for i in range(n, 0, -1):
        if DP[i][w] != DP[i-1][w]:
            items_elegidos_indices.append(objetos[i-1]['indice'])
            w -= objetos[i-1]['weight']
        
        if w == 0:
            break
            
    items_elegidos_indices.reverse()
    return items_elegidos_indices

def solve(capacity, objects, n):
    DP = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n+1):
        weight_i = objects[i-1]["weight"] 
        value_i = objects[i-1]["value"]

        for w in range(capacity + 1):
            DP[i][w] = DP[i-1][w]
            
            if w >= weight_i:
                value_included = value_i + DP[i-1][w - weight_i]
                DP[i][w] = max(DP[i][w], value_included)
                
    return DP

def main():
    import sys
    data = sys.stdin.read().splitlines()
    
    linea_actual = 0
    
    while linea_actual < len(data):
        capacity, objects, linea_actual = leer_caso(data, linea_actual)
        
        if capacity is None:
            break
            
        n = len(objects)
        DP = solve(capacity, objects, n)
        indices = reconstruir_solucion(capacity, objects, DP)
        
        print(len(indices))
        if indices:
            print(' '.join(map(str, indices)))
        else:
            print()

    return

if __name__ == "__main__":
    main()