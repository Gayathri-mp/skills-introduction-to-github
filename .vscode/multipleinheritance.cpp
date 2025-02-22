// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
class Vehicle{
    public:
    Vehicle(){
        cout<<"this is a Vehicle"<< endl;
    }
};
class FourWheeler
{
    public:
    FourWheeler()
    {
        cout<<"this is a FourWheeler"<< endl;
    }
};
class car:public Vehicle, public FourWheeler {
    public:
    car()
    {
        cout<<"this is a car"<< endl;
    }
};
int main() {
   car obj;
   return 0;
}