#!/bin/sh

add() {
    echo "Result: $((a + b))"
}

sub() {
    echo "Result: $((a - b))"
}

mul() {
    echo "Result: $((a * b))"
}

div() {
    if [ $b -ne 0 ]; then
        echo "Result: $((a / b))"
    else
        echo "Division by zero not allowed"
    fi
}

while true
do
    echo "1. Add"
    echo "2. Subtract"
    echo "3. Multiply"
    echo "4. Divide"
    echo "5. Exit"
    echo "Enter choice:"
    read ch

    if [ $ch -eq 5 ]; then
        break
    fi

    echo "Enter first number:"
    read a
    echo "Enter second number:"
    read b

    case $ch in
        1) add ;;
        2) sub ;;
        3) mul ;;
        4) div ;;
        *) echo "Invalid choice" ;;
    esac
done
