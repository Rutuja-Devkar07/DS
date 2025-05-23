import scala.io.StdIn._

object BasicCalculator {
  def main(args: Array[String]): Unit = {
    println("Welcome to Scala Calculator")

    print("Enter first number: ")
    val num1 = readDouble()

    print("Enter an operator (+, -, *, /): ")
    val operator = readLine().trim

    print("Enter second number: ")
    val num2 = readDouble()

    val result = operator match {
      case "+" => num1 + num2
      case "-" => num1 - num2
      case "*" => num1 * num2
      case "/" =>
        if (num2 != 0) num1 / num2
        else {
          println("Error: Division by zero")
          return
        }
      case _ =>
        println("Invalid operator")
        return
    }

    println(s"Result: $num1 $operator $num2 = $result")
  }
}