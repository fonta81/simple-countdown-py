import time


class TimeClass:
    def PedirNumero(self):  # pedir valores en str y pasarlo a int
        try:
            valor = int(input("Ingrese la cantidad de tiempo: "))
            return valor
        except ValueError:  # en caso de Error:
            print("Ingresa un numero")
        except Exception as e:
            print(f"Error: {e}")

    def Horas(self, horas):  # se le pide la cantidad en hora
        segundos = horas * 3600  # se pasa a segundos
        return segundos  # devuelve la cantidad en segundos

    def Minutos(self, Minutos):  # pide la cantidad en Minutos
        segundos = Minutos * 60  # lo pasa a segundos
        return segundos  # devuelve la cantidad en segundos

    def cronometro_atras(self, segundos):  # Bucle principal del codigo
        while segundos >= 0:  # se le dice que se repita hasta que llegue a 0
            min, seg = divmod(segundos, 60)  # divide segundos a min:seg
            hor = segundos // 3600
            formanto = f"{hor:02d} : {min:02d} : {seg:02d}"  # Formato en q se vera
            print(f"Tiempo restante: {formanto}", end="\r", flush=True)
            time.sleep(1)  # Espera 1 seg
            segundos -= 1  # Se lo resta a la cantidad total de segundos

        print("!!Fin del Tiempo!!")  # mensaje cuando se salga del Bucle

    def Usuario(self):
        print("\n\n")
        print("desea ingrsar la cantidad en")
        print("1.horas")
        print("2.Minutos")
        print("3.segundos")
        el = input("Elige: ")
        if el == "1":  # horas -> Funcion Horas
            self.cronometro_atras(self.Horas(self.PedirNumero()))
        elif el == "2":  # Minutos -> Funcion Minutos
            self.cronometro_atras(self.Minutos(self.PedirNumero()))
        elif el == "3":  # segundos -> Funcion cronometro_atras
            self.cronometro_atras(self.PedirNumero())
        else:
            print("Ingrese un valor valido")


def main():
    tt = TimeClass()
    while True:
        print("\n" + "=" * 60)
        print("1.Iniciar")
        print("2.Salir")
        elige = input("Elige: ")

        if elige == "2":
            print("Saliendo...")
            break

        elif elige == "1":
            tt.Usuario()

        else:
            print("Ingrese un valor valido")


if __name__ == "__main__":
    main()
