
public class HelloWorld {
public static void main(String args[]) {
	try {
	System.out.println ("Hello World");
	throw new IndexOutOfBoundsException();
	}
	catch(IndexOutOfBoundsException  e) {
		e.printStackTrace();
	}
	}
}

