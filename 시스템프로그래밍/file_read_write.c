#include<stdio.h>
#include<string.h>

int write_to_file(void){
  FILE *fp;
  if(fp==NULL){
    perror("fopen error\n");
    return -1;
   }
   fputs("hi world",fp);
   fclose(fp);
   return 0;
 }
 int read_from_file(void){
  FILE *fp;
  char buf[1024];
  fp=open("data","r");
  if(fp==NULL){
    perror("fopen error\n");
    return -1;
    }
    memset(buf,0,sizeof(buf));
    fgets(buf,sizeof(buf),fp);
    fclose(fp);
    printf("%s",buf);
    return 0;
}
int main(int argc,char **argv){
  if(write_to_file()){
    perror("write to file");
    return -1;
   }
   if(read_from_file()){
    perroe("write from file");
    return -1;
}
   
