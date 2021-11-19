## Duda 01: uso básico git

Por ahora sólo queremos tener acceso a un repositorio github para descargar su contenido y mantenerlo actualizado.

Basta con hacer git clone, y para actualizar git pull desde dentro del directorio:

```bash
~/kk$ git clone https://github.com/IES-Francisco-Romero-Vargas/CETI-PPS-Bloque01.git
Clonando en 'CETI-PPS-Bloque01'...
remote: Enumerating objects: 15, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 15 (delta 1), reused 9 (delta 0), pack-reused 0
Desempaquetando objetos: 100% (15/15), 116.30 KiB | 439.00 KiB/s, listo.
~/kk$ cd CETI-PPS-Bloque01/
~/kk/CETI-PPS-Bloque01$ git pull
Ya está actualizado.
~/kk/CETI-PPS-Bloque01$
```

## Duda 02: activar venv en Windows

Es un pelín distinto...

En Windows:

```
c:\proyecto\> .venv\Scripts\activate
```

En Linux:
```bash
$ source venv/bin/activate
```

Fuente:  https://dev.to/e_farach/setting-up-a-python-virtual-environment-on-windows-for-absolute-beginners-il6





 
