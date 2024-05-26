class EvenFibonacci():

      def __init__(self):
          self.seq = [0, 1]
          self.fibonacci()

      def fibonacci(self):
          x = 1
          while True:
              #next = suma dintre penultimul si ultimul term
              next = self.seq[x-1] + self.seq[x]
              if next >= 4000000:
                  break
              # add new term in sirul lui Fibo
              self.seq.append(next)
              x+=1
      def even_fibo(self):
          evens = list(filter(lambda x: x % 2 == 0, self.seq))
          print( evens )
          return sum( evens )

def main():
    ob = EvenFibonacci()
    print(ob.even_fibo())

    sir = [1,2,3,4]
    print(type(sir))

main()

def is_even(num):
    return num%2 == 0

def main2():
    numbers = [1,2,3,4,5,6,7,8,9,10]

    even_numbers = list(filter(is_even, numbers))

    print(even_numbers)
main2()

def longer_word(word):
    return len(word) > 5

def main3():
    cuvinte = ["apple","it","banana","grapefruits","cars", "trees", "tree"]

    #long_words = list(filter(longer_word, cuvinte))
    long_words = list(filter(lambda x: len(x) > 5, cuvinte))

    print(long_words)

main3()
