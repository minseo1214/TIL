#include<stdio.h>
#include<string.h>

int creat_file(void){
  FILE *fp;
  if(!(fp=fopen("Datafile","w"))){
    printf("fopen() error\n");
    return -1;
  }
  printf("after fopen(), offset= %ld\n",ftell(fp));
  fputs("hello world\n",fp);
  fputs("goodbye world\n",fp);
  fputs("I'm groot\n",fp);
  printf("before fclose : %ld\n",ftell(fp));
  printf("=======================\n");
  fclose(fp);
  return 0;
}
int read_file(void){
  FILE *fp;
  char dw[1024];
  if(!(fp=open("Datafile","r+"))){
    printf("fopen fail\n");
    return -1;
  }
  printf("after fopen(), offset=%ld \n"),ftell(fp));
  memset(dw,0,sizeof(dw));
  fgets(dw,sizeof(dw),fp);
  printf("after fgets : %ld \n"),ftell(fp));
  fseek(fp,0,SEEK_SET);
  printf("after fseek(),offset :%d\n",ftell(fp));
  fputs("end\n",fp);
  printf("before fclose offset : %ld\n",ftell(fp));
  printf("==================================");
  return 0;
}
int main(int argc, chat **argv){
  creat_file();
  read_file();
  return 0;
}
