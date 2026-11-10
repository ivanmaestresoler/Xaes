#!/bin/bash

echo "🔧 Instalando dependencias para xaes.py..."


if ! command -v python3 >/dev/null 2>&1; then
    echo "⚠️ Python 3 no está instalado. Intentando instalarlo..."
    sudo apt update && sudo apt install -y python3
    if ! command -v python3 >/dev/null 2>&1; then
        echo "❌ No se pudo instalar Python 3. Instálalo manualmente." >&2
        exit 1
    fi
fi


if ! command -v pip3 >/dev/null 2>&1; then
    echo "⚠️ pip3 no está instalado. Intentando instalarlo..."
    sudo apt update && sudo apt install -y python3-pip
    if ! command -v pip3 >/dev/null 2>&1; then
        echo "❌ No se pudo instalar pip3. Instálalo manualmente." >&2
        exit 1
    fi
fi


echo "📦 Instalando PyCryptodome..."
pip3 install --user pycryptodome


if python3 -c "from Crypto.Cipher import AES" 2>/dev/null; then
    echo ""
    echo "✅ Instalación completada correctamente."
    echo "🟢 Ya puedes cifrar y descifrar con ./xaes.py"
    echo ""
    echo "📌 Ejemplos de uso:"
    echo "   cat archivo.txt | ./xaes.py -e \"TuContraseña\" > archivo.enc"
    echo "   cat archivo.enc | ./xaes.py -d \"TuContraseña\" > archivo.dec"
else
    echo "❌ Error: PyCryptodome no se instaló correctamente." >&2
    exit 1
fi
