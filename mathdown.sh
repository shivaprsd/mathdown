#!/bin/sh
if [ "$1" = "" ] || [ "$1" = "-h" ] || [ "$1" = "--help" ] || [ "$2" = "" ];
then
    echo "Usage: mathdown.sh <input-file> <output-file>"
else
    sed -e 's/%t/'"$(basename "$1")"'/' -e '/%s/{r '"$1" -e 'd;}' \
        mathdown.html > "$2"
fi
