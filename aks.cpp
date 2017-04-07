#include <bits/stdc++.h>
#define F first
#define S second
using namespace std;
typedef unsigned long long int ull;
typedef pair<vector<ull> , ull>poly;

ull ipow(ull a, ull b,ull mod){
	/* Caluclate a^b fastly */
	ull res = 1;
	a = a%mod;
	while(b){
		if(b&1)res = (res*a)%mod;
		a = (a*a)%mod;
	}
	return res%mod;
}

ull mod(ull a,ull b){
	/* Caluclates a%b */
	while(a>=b){
		a-=b;
	}
	return a;
}
ull bitCount(ull n) {
	/* Numbers of bits in n (log n)*/
	ull counter = 0;
	while(n) {
		counter += n % 2;
		n >>= 1;
	}
	return counter;
}

ull gcd(ull a, ull b){
	/* finds gcd of a and b */
	ull r;
	while(b!=0){
		r = a % b;
		a = b;
		b = r;
	}
	return a;
}

vector<ull> c;
void mul(poly& a,poly b,ull n,ull r){
	/* Multiplies two polynomials a,b does modulo x^r - 1 and stores it in a */
	int i,j;
	int imr;
	ull nc;
	for(i = 0;i<=r;i++) c[i] = 0;
	for(i = 0; i < a.F.size(); i++){
		if(a.F[i]!=0)
			for(j = 0; j < b.F.size(); j++)
			{
				if(b.F[j]!=0){
					nc = a.F[i]*b.F[j];
					imr = (i+j)%r;
					c[imr] += nc;
					c[imr]%=n;
				}
			}
	}
	for(i = 0;i < c.size();i++){
		a.F[i] = c[i]%n;
	}
}


void build_poly(poly& res, poly p, ull n, ull r){
	/* computes p^n % x^r-1 % n */
	res.F.reserve(r+1);
	res.F.assign(r+1,0);
	res.F[0] = 1;
	ull ord = n;
	int i,tn = 0;
	while(n){
		if(n&1){
			mul(res,p,ord,r);
		}
		n >>= 1;
		mul(p,p,ord,r);
	}
}

ull find_r(ull n){
	/* finds r for n */

}

ull isAKS(ull n){
	/* Returns 0 if n is not prime else returns 1 */

}

int main(){

	ull n = 1e9+7,i,r = 3212;
	poly a;
	poly b;
	b.S = 1;
	b.F.assign(r+1,0);
	c.assign(r+1,0);
	b.F[0] = 1;
	b.F[1] = 1;
	build_poly(a,b,n,r);
	cout << "Done\n";
	for(int i = 0; i < a.F.size();i++){
		cout << a.F[i] << " ";
	}
	cout << "\n";
}
