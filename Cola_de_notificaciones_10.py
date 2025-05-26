from collections import deque


class Notificacion:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje
    
    def __str__(self):
        return f"[{self.hora}] {self.aplicacion}: {self.mensaje}"


def eliminar_notificaciones_facebook(cola):
    cola_filtrada = deque()
    count = 0
    
    while cola:
        notificacion = cola.popleft()
        if notificacion.aplicacion.lower() != "facebook":
            cola_filtrada.append(notificacion)
        else:
            count += 1
    
   
    return cola_filtrada, count


def mostrar_notificaciones_twitter_python(cola):
    twitter_python = []
    cola_temporal = deque()
    
    
    while cola:
        notificacion = cola.popleft()
        cola_temporal.append(notificacion)
        
        if (notificacion.aplicacion.lower() == "twitter" and 
            "python" in notificacion.mensaje.lower()):
            twitter_python.append(notificacion)
    
    
    while cola_temporal:
        cola.append(cola_temporal.popleft())
    
    return twitter_python


def notificaciones_entre_horas(cola):
    pila_temporal = []
    cola_temporal = deque()
    count = 0
    
    while cola:
        notificacion = cola.popleft()
        cola_temporal.append(notificacion)
        
        hora = notificacion.hora
        
        try:
            hh, mm = map(int, hora.split(':'))
            minutos = hh * 60 + mm
            
            if 11*60 + 43 <= minutos <= 15*60 + 57:
                pila_temporal.append(notificacion)
                count += 1
        except:
            
            pass
    
    
    while cola_temporal:
        cola.append(cola_temporal.popleft())
    
    return pila_temporal, count


def mostrar_cola(cola, titulo="Notificaciones"):
    print(f"\n--- {titulo} ---")
    for notif in cola:
        print(notif)
    print()


if __name__ == "__main__":
    
    cola_notificaciones = deque([
        Notificacion("10:30", "Facebook", "Tienes 5 nuevas notificaciones"),
        Notificacion("11:45", "Twitter", "Aprende Python hoy"),
        Notificacion("12:00", "Instagram", "Nueva publicación"),
        Notificacion("14:30", "Twitter", "Python es el lenguaje del futuro"),
        Notificacion("15:00", "Facebook", "Juan te ha enviado un mensaje"),
        Notificacion("15:50", "Twitter", "Revisa este código en Python"),
        Notificacion("16:30", "WhatsApp", "Mensaje nuevo"),
        Notificacion("11:42", "Twitter", "Casi en el rango de tiempo"),
        Notificacion("15:58", "Twitter", "Justo después del rango")
    ])
    
    
    mostrar_cola(cola_notificaciones, "Cola Original")
    
    
    cola_sin_facebook, eliminadas = eliminar_notificaciones_facebook(cola_notificaciones.copy())
    print(f"\nSe eliminaron {eliminadas} notificaciones de Facebook")
    mostrar_cola(cola_sin_facebook, "Cola sin Facebook")
    
    
    twitter_python = mostrar_notificaciones_twitter_python(cola_notificaciones.copy())
    print("\nNotificaciones de Twitter que mencionan Python:")
    for notif in twitter_python:
        print(notif)
    
    
    pila_temporal, cantidad = notificaciones_entre_horas(cola_notificaciones.copy())
    print(f"\nHay {cantidad} notificaciones entre 11:43 y 15:57")
    print("\nNotificaciones en la pila temporal:")
    while pila_temporal:
        print(pila_temporal.pop())