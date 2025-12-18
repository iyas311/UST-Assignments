#!/bin/sh

check_file() {
    file=$1

    if [ -e "$file" ]; then
        echo "File exists"

        if [ -r "$file" ]; then
            echo "Read permission: YES"
        else
            echo "Read permission: NO"
        fi

        if [ -w "$file" ]; then
            echo "Write permission: YES"
        else
            echo "Write permission: NO"
        fi

        if [ -x "$file" ]; then
            echo "Execute permission: YES"
        else
            echo "Execute permission: NO"
        fi
    else
        echo "File does not exist"
    fi
}

echo "Enter file name:"
read fname

check_file "$fname"
