#include<stdio.h>
#include<string.h>
#include "copy.h"
char line[MAXLINE];
char logest[MAXLINE];
void copy(char from[],char to[]);

int main(void){
  int len;
  int max;
  max=0;
  while(fgets(line,MAXLINE,stdin)!=NULL){
    if(max>0){
      printf("%s",logest);
    }
    return 0;
  }
}
