===========================================
XAES - CIFRADOR/DESCIFRADOR COMPATIBLE CON OPENSSL
===========================================

🔒 ¿Qué es?
-----------
XAES es una herramienta en Python que permite cifrar y descifrar archivos de forma segura usando:
- AES-128 en modo CBC
- Clave derivada con PBKDF2 y SHA256
- Formato compatible con OpenSSL

No necesitas saber programar para usarlo.

📦 Archivos incluidos
---------------------
- xaes.py          → El programa principal
- install.sh       → Instalador automático
- README.txt       → Este archivo con instrucciones

🚀 Cómo instalar
----------------
1. Abre la carpeta donde están los archivos.
2. Haz clic derecho y elige “Abrir en una terminal”.
3. Escribe el siguiente comando:

    ./install.sh

Esto instalará Python (si hace falta), pip y la librería necesaria para ejecutar el programa.

🔐 Cómo cifrar un archivo
--------------------------
1. Asegúrate de tener el archivo original, por ejemplo: `documento.txt`.
2. En la terminal, escribe:

    cat documento.txt | ./xaes.py -e "TuContraseña" > documento.enc

Esto genera un archivo cifrado llamado `documento.enc`.

🔓 Cómo descifrar un archivo
----------------------------
1. Asegúrate de tener el archivo cifrado: `documento.enc`.
2. En la terminal, escribe:

    cat documento.enc | ./xaes.py -d "TuContraseña" > documento_descifrado.txt

Esto recupera el archivo original (si la contraseña es correcta).

🔁 Compatibilidad con OpenSSL
-----------------------------
Puedes cifrar con OpenSSL y descifrar con XAES (o al revés):

- Cifrar con OpenSSL:

    echo "Hola" | openssl aes-128-cbc -pbkdf2 -k MiClave > hola.enc

- Descifrar con XAES:

    cat hola.enc | ./xaes.py -d "MiClave"

- Cifrar con XAES:

    echo "Hola" | ./xaes.py -e "MiClave" > hola.enc

- Descifrar con OpenSSL:

    openssl aes-128-cbc -pbkdf2 -d -k MiClave -in hola.enc

💡 Consejos
-----------
- Guarda bien tu contraseña. Sin ella no podrás recuperar el contenido.
- Si ves un error de “padding inválido”, puede que la contraseña sea incorrecta o el archivo esté dañado.

📞 Ayuda
--------
Si tienes problemas, asegúrate de:
- Haber ejecutado `install.sh` correctamente.
- Usar comillas alrededor de tu contraseña si tiene espacios.
- No haber modificado el archivo `xaes.py`.

¡Gracias por usar XAES!
