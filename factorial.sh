#!/bin/sh

factorial() {
    n=$1
    fact=1

    while [ $n -gt 1 ]
    do
        fact=$((fact * n))
        n=$((n - 1))
    done

    echo "Factorial is: $fact"
}

echo "Enter a number:"
read num

factorial $num
