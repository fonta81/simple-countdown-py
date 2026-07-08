import time
# nesesito un  programa q pase los segundos a minuntos  -> y haga cuenta atras


class Time:
    def PedirNumero(self):
        valor = float(input("Ingrese los minutos en seguntos"))
        return valor

    def cronometro_atras(self, segundos):
        while segundos >= 0:
            min, seg = divmod(segundos, 60)
            formanto = f"{min}:02d : {seg}:02d"
