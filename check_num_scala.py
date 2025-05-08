def checkNumber(number: Double): Unit = {
    if (number > 0) {
      println("The number is positive.")
    } else if (number < 0) {
      println("The number is negative.")
    } else {
      println("The number is zero.")
    }
  }

  def main(args: Array[String]): Unit = {
    println("Enter a number:")
    val input = scala.io.StdIn.readDouble()
    checkNumber(input)
  }