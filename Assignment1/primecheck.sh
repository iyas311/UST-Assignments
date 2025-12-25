#!/bin/sh

check_prime() {
    num=$1
    flag=0

    if [ $num -le 1 ]; then
        echo "Not a Prime Number"
        return
    fi

    for i in $(seq 2 $((num - 1)))
    do
        if [ $((num % i)) -eq 0 ]; then
            flag=1
            break
        fi
    done

    if [ $flag -eq 0 ]; then
        echo "Prime Number"
    else
        echo "Not a Prime Number"
    fi
}

echo "Enter a number:"
read n

check_prime $n
