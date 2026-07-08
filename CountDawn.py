import time


class TimeClass:
    def PedirNumero(self):
        try:
            valor = int(input("Ingrese los minutos en seguntos: "))
            return valor
        except ValueError:
            print("Ingresa un numero")
        except Exception as e:
            print(f"Error: {e}")

    def cronometro_atras(self, segundos):
        while segundos >= 0:  # se le dice que se repita hasta que llegue a 0
            min, seg = divmod(segundos, 60)
            formanto = f"{min:02d} : {seg:02d}"
            print(f"Tiempo restante: {formanto}", end="\r", flush=True)
            time.sleep(1)
            segundos -= 1

        print("!!Fin del Tiempo!!")

    def usuario(self):
        print("hola")
        self.cronometro_atras(self.PedirNumero())


tt = TimeClass()
tt.cronometro_atras(tt.PedirNumero())
