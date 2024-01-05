from textblob import TextBlob

estimacion_positiva = 0
estimacion_negativa = 0
estimacion_neutral = 0


def suma_sentimientos(estimado):
    global estimacion_positiva, estimacion_negativa, estimacion_neutral
    if estimado > 0:
        estimacion_positiva += 1
        return 0
    elif estimado < 0:
        estimacion_negativa += 1
        return 1
    else:
        estimacion_neutral += 1
        return 2


if __name__ == "__main__":
    f1 = open("opiniones_procesadas.txt", "r")
    opiniones = f1.readlines()
    f1.close()

    f2 = open("puntuaciones.txt", "r")
    puntuaciones = f2.readlines()
    f2.close()

    fpos_est = open("reseñas_estimadas_reales/0.0. positivas_estimadas.txt", "a")
    fpos_real = open("reseñas_estimadas_reales/0.1. positivas_reales.txt", "a")
    fneg_est = open("reseñas_estimadas_reales/0.2. negativas_estimadas.txt", "a")
    fneg_real = open("reseñas_estimadas_reales/0.3. negativas_reales.txt", "a")

    i = 0
    for line in opiniones:
        line = line.split(" experience date")[0]
        blob = TextBlob(line)
        estimacion = suma_sentimientos(blob.polarity)
        real = int(puntuaciones[i].strip("\n"))
        i += 1

        if estimacion == 0:
            fpos_est.write(line)
        elif estimacion == 1:
            fneg_est.write(line)

        if real > 3:
            fpos_real.write(line)
        elif real < 3:
            fneg_real.write(line)

    fpos_est.close()
    fpos_real.close()
    fneg_est.close()
    fneg_real.close()

    print("Positivas estimadas: " + str(estimacion_positiva))
    print("Negativas estimadas: " + str(estimacion_negativa))
    print("Neutrales estimadas: " + str(estimacion_neutral))
