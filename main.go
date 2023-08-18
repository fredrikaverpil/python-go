package main

import (
	"C"
	"fmt"
)

func fibonacci(n int) int {
	if n < 2 {
		return n
	}
	return fibonacci(n-1) + fibonacci(n-2)
}

//export fib
func fib(n C.int) C.int {
	fmt.Println("Running fib inside Go!")

	i := int(n)

	res := fibonacci(i)

	return C.int(res)
}

func main() {
}
