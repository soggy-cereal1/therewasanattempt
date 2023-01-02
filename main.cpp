// my first program in C++
#include <iostream>
using namespace std;

int pow(int base, int power) {
  for (int i = 1; i>power; i++) {
    base*=base;
  }
  return base;
}

int main()
{
    int a; 
    int b;
    int c;
    
    cin >> a;
    cin >> b;
    cin >> c;
    
    int aSquared = pow(a,2);
    int bSquared = pow(b,2);
    
    int cSquared = pow(c,2);
  cout << "Hello World! " << endl;
  cout << "I am a c++ program. " << endl;
  
  
  if (aSquared + bSquared == cSquared) {
    cout << a << ", " << b << ", and " << c << " form a right triangle." << endl;
    cout << "a squared is " << aSquared << ", b squared is " << bSquared << ", and their sum is " << aSquared + bSquared << ", which is the same as c squared.";
    } else {
    cout << "a and b do not form a right triangle with hypotenuse c.";
    }
}