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
    # Reconstrucción esperando las estructuras 1D: DP (valores), last_item y prev_weight
    # Si se pasa la tabla 2D antigua, esta función no funcionará — usamos la nueva solve
    dp, last_item, prev_weight = DP

    items_elegidos_indices = []
    w = capacidad

    # Reconstruimos siguiendo last_item/prev_weight desde w=capacidad hacia atrás
    while w > 0 and last_item[w] != -1:
        idx = last_item[w]
        items_elegidos_indices.append(objetos[idx]['indice'])
        w = prev_weight[w]

    items_elegidos_indices.reverse()
    return items_elegidos_indices

def solve(capacity, objects, n):
    # Implementación optimizada: DP 1D y arrays para reconstrucción
    # dp[w] = mejor valor alcanzable con capacidad w
    dp = [0] * (capacity + 1)

    # Para reconstrucción: last_item[w] = índice del último objeto usado para alcanzar dp[w]
    # prev_weight[w] = peso anterior (w - weight_of_last_item)
    last_item = [-1] * (capacity + 1)
    prev_weight = [-1] * (capacity + 1)

    for i in range(n):
        weight_i = objects[i]["weight"]
        value_i = objects[i]["value"]

        # iteramos hacia atrás para no reusar el mismo objeto varias veces
        for w in range(capacity, weight_i - 1, -1):
            candidate = dp[w - weight_i] + value_i
            if candidate > dp[w]:
                dp[w] = candidate
                last_item[w] = i
                prev_weight[w] = w - weight_i

    # Devolvemos las estructuras necesarias para reconstrucción
    return dp, last_item, prev_weight

def main():
    import sys
    data = sys.stdin.read().splitlines()
    
    linea_actual = 0
    num_caso = 0
    
    while True:
        capacity, objects, linea_actual = leer_caso(data, linea_actual)
        
        if capacity is None:
            break
            
        n = len(objects)

        DP = solve(capacity, objects, n)

        indices = reconstruir_solucion(capacity, objects, DP)
        
        print(len(indices))
        print(' '.join(map(str, indices)))
        
        num_caso += 1

    return

if __name__ == "__main__":
    main()