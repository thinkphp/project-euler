#include <iostream>
using namespace std;
int main(int argc, char const *argv[]) {

  const int limit = 4000000;

  int sum{0};

  int prev = 0, curr = 1,
      next = prev + curr;

  while(next < limit) {

       //even terms
       if(next % 2 == 0) sum = sum + next;


       next = prev + curr;
       prev = curr;
       curr = next;
  }

  cout<<sum;


  return 0;
}
