#!/bin/sh

sum_n() {
    n=$1
    sum=0

    for i in $(seq 1 $n)
    do
        sum=$((sum + i))
    done

    echo "Sum is: $sum"
}

echo "Enter a number:"
read num

sum_n $num
