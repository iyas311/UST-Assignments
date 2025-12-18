#!/bin/sh

check_number() {
    if [ $1 -gt 0 ]; then
        echo "Number is Positive"
    elif [ $1 -lt 0 ]; then
        echo "Number is Negative"
    else
        echo "Number is Zero"
    fi
}

echo "Enter a number:"
read num

check_number $num
