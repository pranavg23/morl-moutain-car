#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define T 	1000L //number of time steps
#define Z 	10000L //Number of trials
// #define T 	200 //number of time steps
// #define Z 	1000000 //Number of trials
#define A 	3 //Number of possible actions
#define H 	5	// determines number of states -- Why is this 5?
//To discretize the state:
#define SX 	(10*H)
#define SV 	(10*H)

int main() {
	long t,z;
	int a,ar,b,sx,sv,rx,rv;
	double x,v;
	double V,Q[SX][SV][A],rew;
	double eps,eps0=0.5,eta=0.1,gamma=0.99;
	FILE *dat,*daz;

	if ((dat=fopen("traj","wt"))==NULL) printf("file error\n");
	if ((daz=fopen("dura","wt"))==NULL) printf("file error\n");

	for (sx=0;sx<SX;sx++) {
		for (sv=0;sv<SV;sv++) {
			for (a=0;a<A;a++) {
				//Tabular Q-learning, there random initialization
				Q[sx][sv][a]=0.001*drand48();
			}
		}
	}

	for (z=0;z<Z;z++) {
		eps=eps0*((double)(Z-z)/(double)Z)*((double)(Z-z)/(double)Z);
		v=0.0;
		x=-0.5;
		sx=(int)(H*(x+1.3));	
		sv=(int)(10.0*H*(v+0.1));
		V=-1.0e10;
		for (b=0;b<3;b++) {
			if (Q[sx][sv][b]>V) {
				V=Q[sx][sv][b];
				a=b;
			}
		}
		for (t=0L;t<T;t++) {
			v+=0.001*(a-1.0)-cos(3.0*x)*0.0025;
			// Returning to the velocity bounds
			if (v<-0.07) v=-0.07;
			if (v>0.07) v=0.07;
			x+=v;
			if (x<-1.2) x=-1.2;
			//Reward is constantly getting overwritten
			if (x>=0.6) {
				//When the target state has been reached
				x=0.6;
				rew=100.0;
			}
			else rew=0.1*v*v; //You are multiplying by 0 though how much does it matter if the v^2 is multiplied with it? --> Can be changed to 0.1 etc
			//0.1 gives a different solution
			rx=(int)(10.0*(x+1.3));	
			rv=(int)(100.0*(v+0.1));
			ar=a;
			V=-1.0e10;
			for (b=0;b<3;b++) {
				if (Q[rx][rv][b]>V) {
					V=Q[rx][rv][b];
					a=b;		// new action for next time
				}
			}
			if (drand48()<eps) a=(int)(3.0*drand48());  // exploration
			Q[sx][sv][ar]+=eta*(rew+gamma*V-Q[sx][sv][ar]); // update for previous state and action
			sx=rx;
			sv=rv;
			if (z==Z-1) fprintf(dat,"%ld %g %g %d\n",t,x,v,a); // save last trial
			if (x>=0.6) break;
		}
		fprintf(daz,"%ld %ld\n",z,t); // save time per trial
	}
	return(1);
}
