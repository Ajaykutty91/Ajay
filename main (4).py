#include <stdio.h>

int main()
{
  int year;

  printf("\n Please Enter any year you wish \n");
  scanf("%d",&year);
  
  if(year%4 == 0)
   {
    if( year%100 == 0) 
     {
      if ( year%400 == 0)
         printf("\n%d is a Leap.", year);
      else
         printf("\n%d is not.", year);
     }
    else
       printf("\n%d is a Leap.", year );
   }
  else
     printf("\n%d is not.", year);
 return 0;
}