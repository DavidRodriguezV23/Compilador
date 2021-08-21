#include <iostream>
#include <windows.h>

using namespace std;

int main() {
	
	float t1, t2, t3, t4, t_med, t_min, t_max;

	cout << "El programa empieza a las 12 am" << endl;
	cout << "Ingrese la temperatura 1" << endl;
	cin >> t1;
	Sleep(6000); // Espera 6 segundos
	cout << "Ingrese la temperatura 2" << endl;
	cin >> t2;
	Sleep(6000);
	cout << "Ingrese la temperatura 3" << endl;
	cin >> t3;
	Sleep(6000);
	cout << "Ingrese la temperatura 4" << endl;
	cin >> t4;

	t_med = (t1 + t2 + t3 + t4) / 4;

	if(t1 <= t2 && t1 <= t3 && t1 <= t4) {
		t_min = t1;
	} else if(t2 <= t1 && t2 <= t3 && t2 <= t4) {
		t_min = t2;
	} else if(t3 <= t1 && t3 <= t2 && t3 <= t4) {
		t_min = t3;
	} else {
		t_min = t4;
	}

	if(t1 >= t2 && t1 >= t3 && t1 >= t4) {
		t_max = t1;
	} else if(t2 >= t1 && t2 >= t3 && t2 >= t4) {
		t_max = t2;
	} else if(t3 >= t1 && t3 >= t2 && t3 >= t4) {
		t_max = t3;
	} else {
		t_max = t4;
	}
	
	cout << "La temperatura media es: " << t_med << endl;
	cout << "La temperatura minima es: " << t_min << endl;
	cout << "La temperatura maxima es: " << t_max << endl;



	return 0;
}
