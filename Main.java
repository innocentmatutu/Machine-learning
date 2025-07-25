import java.util.Scanner;

public class Main{
  int x;//requires input
  int y;//requires input
  char op;//requires input

  public Main(int x,int y,char op){
    this.x = x;
    this.y = y;
    this.op = op;

  }

  public int addition(){
    return x + y;
  }
  public int subtract(){
    return x - y;
  }
  public int modulus(){
    return x % y;
  }
  public int multiply(){
    return x * y;
  }
  public int division(){
    return x / y;
  }

  public static void main(String[] args){
  Scanner data = new Scanner(System.in);
  System.out.println("Enter first number:");
  int x = data.nextInt();

  System.out.println("Enter second number:");
  int y = data.nextInt();

  System.out.println("Enter the operand(-,+,*,/,%):");
  char op = data.next().charAt(0);

  Main calc = new Main(x,y,op);

  if(op == '-'){
    System.out.println("Result is:"+ calc.subtract());
  } else if(op == '+'){
    System.out.println("Result is:"+ calc.addition());
  } else if(op == '/'){
    if(y == 0){
      System.out.println("zerodivision error");
    } else{
      System.out.println("Result is:"+ calc.division());
    }
  } else if(op == '*'){
    System.out.println("Result is:"+ calc.multiply());
  } else if(op == '%'){
    System.out.println("Result is:"+ calc.modulus());
  } else{
    System.out.println("Please enter a valid operand");
  }
  data.close();
  }
}
 