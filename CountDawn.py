import time


class TimeClass:
    def PedirNumero(self):  # pedir valores en str y pasarlo a int
        try:
            valor = int(input("Ingrese los minutos en seguntos: "))
            return valor
        except ValueError:  # en caso de Error:
            print("Ingresa un numero")
        except Exception as e:
            print(f"Error: {e}")

    def cronometro_atras(self, segundos):  # Bucle principal del codigo
        while segundos >= 0:  # se le dice que se repita hasta que llegue a 0
            min, seg = divmod(segundos, 60)  # divide segundos a min:seg
            formanto = f"{min:02d} : {seg:02d}"  # Formato en q se vera
            print(f"Tiempo restante: {formanto}", end="\r", flush=True)
            time.sleep(1)  # Espera 1 seg
            segundos -= 1  # Se lo resta a la cantidad total de segundos

        print("!!Fin del Tiempo!!")  # mensaje cuando se salga del Bucle

    def usuario(self):
        print("hola")
        self.cronometro_atras(self.PedirNumero())


tt = TimeClass()
tt.cronometro_atras(tt.PedirNumero())
