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

void mul(poly& a,poly b,ull n){
	/* Multiplies two polynomials a,b and stores it in a */
	ull dega = a.S;
	ull degb = b.S;
	vector<ull> c(dega+degb+1,0);
	int i,j;
	cout << " a => ";
	for(i = 0;i<=a.S;i++) cout  << a.F[i] << " ";cout << endl;
	cout << " b => ";
	for(i = 0;i<=b.S;i++) cout  << b.F[i] << " ";cout << endl;
	for(i = 0; i <= a.S; i++){
		if(a.F[i]!=0)
			for(j = 0; j <= b.S; j++)
			{
				if(b.F[j]!=0){
					cout << "for i , j = " << i << " , " << j << endl;
					cout << "for ci , cj = " << a.F[i] << " , " << b.F[j] << endl;
					cout << "mul from " << c[i+j];
					c[i+j]+=a.F[i]*b.F[j];
					c[i+j]%=n;
					cout << " => " << c[i+j] << endl;
				}
			}
	}
	cout << "mul ";
	for(i = 0;i < c.size();i++){
		a.F[i] = c[i];
		cout << c[i] << " ";
	}
	cout << endl;
	a.S = dega+degb;
	cout << "degree changed " << a.S << endl;
}

void sqr(poly &f,ull n){
	ull i,j;
	ull deg = f.S;
	vector<ull> newco(2*deg+1,0);
	for(i = 0; i <= f.S; i++ ){
		if(f.F[i]!=0){
			for(j = 0; j <= f.S; j++){
				if(f.F[j]!=0){
					cout << "for i , j = " << i << " , " << j << endl;
					cout << "newco from " << newco[i+j];
					newco[i+j] += f.F[i]*f.F[j];
					newco[i+j]%=n;
					cout << " => " << newco[i+j] << endl;
				}
			}
		}
	}
	cout << "sqr ";
	for(i = 0; i < newco.size();i++){
		f.F[i] = newco[i];
		cout << newco[i] << " ";
	}
	cout << endl;
	f.S = 2*deg;
	cout << "sqr done. deg is changed to " << f.S << endl;
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

void polymod(poly& p,ull r){
	/* Caluclates p%x^r-1 */
	ull deg = p.S;
	ull imr;
	ull nc,co;
	ull i = deg;
	while(i >= r){
		co = p.F[i];
		if(co != 0){
			imr = i%r;
			nc = p.F[imr];
			nc += co;
			p.F[imr] = nc;
			p.F[i] = 0;
		}
		i--;
	}
}

void build_poly(poly& res, poly p, ull n, ull r){
	res.S = 0;
	ull newdeg = 2*n*p.S;
	res.F.reserve(newdeg+1);
	res.F.assign(newdeg+1,0);
	res.F[0] = 1;
	ull i,lgn = bitCount(n);
	ull ord = n;
	while(n){
		if(n&1){
			mul(res,p,ord);
			//			cout << "degree after mul is " << res.S << endl;
		}
		if(n!=1)sqr(res,ord);
		//		cout << "degree is " << res.S << endl;
		polymod(res,r);
		//		cout << "for n: " << n << " f: ";
		for(i = 0; i <= res.S; i++) cout << res.F[i] << " "; cout << endl;
		//	cout << "Done\n";
		n >>= 1;
	}
}

ull find_r(ull n){
	/* finds r for n */
}

ull isAKS(ull n){
	/* Returns 0 if n is not prime else returns 1 */
}

int main(){

	ull n = 16,i;
	//poly a;
	poly b;
	b.S = 1;
	b.F.assign(n+1,0);
	b.F[0] = 1;
	b.F[1] = 1;
	poly a ;
	build_poly(a,b,5,3);
	cout << "Done\n";
	for(int i = 0; i <= a.S;i++){
		cout << a.F[i] << " ";
	}
	/*sqr(a,n);
	  sqr(a,n);
	  mul(a,b,n);
	  polymod(a,2);
	  for(int i = 0; i < n;i++){
	  cout << a.F[i] << " ";
	  }
	  */
	cout << "\n";
}
