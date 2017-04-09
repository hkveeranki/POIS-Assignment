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
		b>>=1;
	}
	return res%mod;
}

ull phi(ull n){
	ull result = n;
	for (ull p=2; p*p<=n; ++p)
	{
		if (n % p == 0)
		{
			while (n % p == 0)
				n /= p;
			result -= result / p;
		}
	}
	if (n > 1)
		result -= result / n;
	return result;
}

ull bitCount(ull n) {
	/* Numbers of bits in n (log n)*/
	ull counter = 0;
	while(n) {
		counter += 1;
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
	c.assign(r+1,0);
	for(i = 0;i<=r;i++) c[i] = 0;
	for(i = 0; i < a.F.size(); i++){
		if(a.F[i]!=0)
			for(j = 0; j < b.F.size(); j++)
			{
				if(b.F[j]!=0){
					nc = (a.F[i]*b.F[j])%n;
					imr = (i+j);
					if(imr>=r)
						imr%=r;
					c[imr] += nc;
					if(c[imr]>=n)
						c[imr]%=n;
				}
			}
	}
	for(i = 0;i < c.size();i++){
		a.F[i] = c[i];
	}
}


void build_poly(poly&res, poly p, ull n, ull r){
	/* computes p^n % x^r-1 % n */
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
	int lgn = bitCount(n),j;
	lgn*=lgn;
	ull r,q,nmq,jmq,val;
	q = lgn+1;
	bool fl;
	while(1){
		fl = 1;
		for(j = 1;j <= lgn; j++){
			nmq = n%q;
			jmq = j%q;
			val = ipow(nmq,jmq,q);
			if(val == 1){
				fl = 0;
				break;
			}
		}
		if(fl){
			r = q;
			break;
		}
		q++;
	}
	if(r>=n)
		return n;
	for(j = 2;j<r;j++){
		if(gcd(j,n)!=1)return 0;
	}
	return r;
}

ull isAKS(ull n){
	/* Returns 0 if n is not prime else returns 1 */
	ull r = find_r(n);
	if(r == 0)return 0;
	if(r == n) return 1;
	ull lgn = bitCount(n);
	ull limit = sqrt(phi(r))*lgn+1;
	cout << "r,limit => " << r << " , " << limit << "\n";
	ull i;
	poly a,b;
	vector<ull> rhs;
	rhs.assign(r+1,0);
	rhs[n%r] = 1;
	b.S = 1;
	b.F.assign(r+1,0);
	b.F[1] = 1;
	for(i = 1; i<= limit; i++)
	{
		b.F[0] = i;
		rhs[0] = i;
		build_poly(a,b,n,r);
		if(a.F != rhs){
			return 0;
		}
		if(i%50 == 0)
			cout << "itr " <<   i << " Done\n";
	}
	return 1;
}
int main(){

	ull n = 129461;
	cout << "isprime " << isAKS(n) << endl;
}
