#include <iostream>

int main()
{
    int sum;

    for (int counter = 0; counter < 1000; counter++)
    {
        if (counter % 3 == 0 || counter % 5 == 0)
        {
            sum += counter;
        }
    }

    std::cout << sum;
}
