package main

import (
	"fmt"
	"math"
)

func main() {

	// 3. If 0.333 is the approximate value of 1/3, find the absolute and relative
	// errors
	absolute := math.Abs(0.333 - 1.0/3.0)
	relative := absolute / (1.0 / 3.0)

	fmt.Println("exercise 3 ", absolute, relative)

	// 4. Find the percentage error if 625.483 is approximated to three significant
	// figures.
	absolute = math.Abs(625.483 - 625.0)
	relative = absolute / 625.0
	percentage := relative * 100

	fmt.Println("exercise 4 ", percentage)

	// 5. Find the relative error in taking n = 3.141593 as 22/7
	absolute = math.Abs(3.141593 - (22.0 / 7.0))
	relative = absolute / (22.0 / 7.0)
	fmt.Println("exercise 5 ", relative)

	// 6. The height of an observation tower was estimated to be 47 m, whereas
	// its actual height was 45 m. Calculate the percentage relative error in the
	// measurement.
	absolute = math.Abs(45.0 - 47.0)
	relative = absolute / 45.0
	percentage = relative * 100

	fmt.Println("exercise 6 ", percentage)

	// 7. Suppose that you have a task of measuring the lengths of a bridge and a
	// rivet, and come up with 9999 and 9 cm, respectively. If the true values
	// are 10,000 and 10 cm, respectively, compute the percentage relative
	// error in each case.
	absoluteFloat := math.Abs(9999.0 - 10000.0)
	relativeFloat := absoluteFloat / 10000.0
	percentageFloat := relativeFloat * 100

	fmt.Println("exercise 7 ", percentageFloat)

	// 8. Find the value of ex using series expansion

	x := 0.5

	absoluteError := 0.005
	n := 1.0
	term := 0.0
	approximation := 1.0

	for {
		approximation += term
		term = math.Pow(x, n) / factorial(n)
		n++
		if math.Abs(term) < absoluteError {
			break
		}
	}
	exact := math.Exp(x)
	absoluteErr := math.Abs(exact - approximation)

	fmt.Println("exercise 8 ", absoluteErr)

	// 9.
	r := 5.0
	exactPi := math.Pi
	approximationPi := 3.14

	s1 := exactPi * r * r
	s2 := approximationPi * r * r

	absoluteErr = math.Abs(s1 - s2)
	relativeErr := absoluteErr / s1
	percentageErr := relativeErr * 100

	fmt.Println("exercise 9 ", absoluteErr, percentageErr)

}

func factorial(n float64) float64 {
	if n == 0 {
		return 1
	}
	result := 1.0
	for i := n; i > 0; i-- {
		result *= i
	}
	return result
}
