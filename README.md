# Conexión con Raspberry Pi 4

Durante el proceso de conexión con la Raspberry Pi, nos encontramos con el inconveniente de no contar con un display para visualizar lo que estaba ocurriendo debido a limitaciones de hardware. Para solucionar este problema, decidimos conectarnos a través de SSH, utilizando la misma red WiFi tanto para el portátil como para la Raspberry Pi.

### Proceso de conexión por SSH

Para establecer la conexión por SSH, ejecutamos un escaneo de red completo utilizando `nmap`, dado que al estar en una red privada, solo tendríamos conectados nuestro terminal y la Raspberry Pi. 

1. **Obtenemos la dirección IPv4 del dispositivo.**
2. **Verificamos que el puerto 22 (utilizado para la conexión SSH) esté abierto correctamente.**
3. **Nos conectamos al terminal.**

Para realizar la conexión, configuramos previamente las credenciales de usuario:

```bash
ssh turismo@IP_DE_LA_RASP
```


# Configuración del entorno en la Raspberry Pi vía SSH

Una vez dentro del terminal, clonamos este repositorio de GitHub para utilizar los scripts. Dado que solo tenemos acceso a la máquina mediante terminal, el único editor que podremos utilizar será `nano` o algún editor similar (como `vim`), lo cual resulta un poco incómodo.

Al tener la posibilidad de clonar repositorios, podremos programar en nuestros terminales, subir el código a GitHub y mantenerlo actualizado en ambos lugares rápidamente.

## Instalación de dependencias en un entorno virtual

Es importante tener en cuenta que al estar en SSH, no podremos instalar dependencias directamente en el terminal, sino en un entorno virtual. Para crear dicho entorno, ejecutamos los siguientes comandos:

```bash
sudo apt install python3-venv
python3 -m venv NOMBRE_ENTORNO_VIRTUAL
source NOMBRE_ENTORNO_VIRTUAL/bin/activate
```
¡Ya estaríamos dentro del entorno!

Ahora, para instalar las dependencias necesarias, simplemente utilizamos:

```python
pip install DEPENDENCIAS
```