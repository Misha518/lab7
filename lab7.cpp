#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

double F(double x, double y){
        return x*exp(-x)-2*y;
}
double dF(double x){
        return exp(-x)+x*exp(-x);
}

int main() {
        double a=0; double b=2; double h=0.1;
        double n=(b-a)/h;
        double X[(int)n];
        double Y1[(int)n];
        double Y[(int)n];
        double X1[(int)n];
        double Y3[(int)n];
        ofstream fout;
        ofstream dout;
        ofstream kout;
        fout.open("y.txt");
        kout.open("y1.txt");
        dout.open("faza.txt");
        X[0]=a; Y[0]=0; 
        for(int i=1; i<=n; i++){
                X[i]=a+i*h;
                Y1[i]=Y[i-1]+h*F(X[i-1],Y[i-1]);
                Y[i]=Y[i-1]+h*(F(X[i-1],Y[i-1])+F(X[i],Y1[i]))/2.0;
                
        }
        for(int i=1; i<=n; i++){
                X1[i]=a+i*h;
                Y3[i]=Y3[i-1]+h*(dF(X1[i-1])+dF(X1[i]))/2.0;
                
        }
        X[0]=a; Y[0]=0; Y3[0]=0;
        for(int i=0; i<=n; i++){
                fout<<X[i]<<" "<<Y[i]<<endl;
                kout<<X[i]<<" "<<Y3[i]<<endl;
                dout<<Y3[i]<<" "<<Y[i]<<endl;
        }
        fout.close();
        kout.close();
        dout.close();
        for(int i=0; i<=n; i++){
                cout << "X["<<i<<"]="<<X[i] <<" ";
        }
        cout << endl;
        for(int i=0; i<=n; i++){
                cout << "Y["<<i<<"]="<<Y[i] << " ";
        }
        cout<<endl;
        for(int i=0; i<=n; i++){
                cout << "dY["<<i<<"]="<<Y3[i] << " ";
        }
        cout<<endl;
        system("python3 lab7.py");
        return 0;
}
