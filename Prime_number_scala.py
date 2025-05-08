import scala.io.StdIn._

object PrimeChecker {
  def main(args: Array[String]): Unit = {
    print("Enter a number: ")
    val number = readInt()

    if (isPrime(number))
      println(s"$number is a prime number.")
    else
      println(s"$number is not a prime number.")
  }

  def isPrime(n: Int): Boolean = {
    if (n <= 1) return false
    for (i <- 2 until n) {
      if (n % i == 0) return false
    }
    true
  }
}