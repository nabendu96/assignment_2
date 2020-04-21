//Question 15
//euler with error bound

#include<stdio.h>
#include<math.h>

float euler(float t,float y)
{
    return(y-pow(t,2)+1);
    }

float f_exact(float t,float y) //Exact solution
{
    return(pow(t+1,2)-0.5*exp(t));
    }

int main()
{
	int N,i;
	float t0=0.0,tf=2.0,h=0.2;   //h is the step size //t0 is the start of the interval //tf is the end of the interval
	N=(tf-t0)/h+1;
	float t[N],y[N],y_exact[N],error[N],error_bound[N];
	t[0]=t0;
    y[0]=0.5;     //initial condition
	for(i=0;i<N;i++)
	{

	    if(i<N-1)
        {
            t[i+1]=t[i]+h;
            y[i+1]=y[i]+h*euler(t[i],y[i]);
            }
		y_exact[i]=f_exact(t[i],y[i]);
		error[i]=y_exact[i]-y[i];	   //absolute error
		error_bound[i]=0.1*(0.5*exp(2)-2)*(exp(t[i])-1);     //error bound as calculated in the class notes
        }

	printf("t         y_euler   y_exact   error     error bound\n");
	for(i=0;i<N;i++)
	{
		printf("%.4f    %.4f    %.4f    %.4f    %.4f\n" ,t[i],y[i],y_exact[i],error[i],error_bound[i]);
        }

	return 0;
    }
