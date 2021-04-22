#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<unistd.h>
#include<fcntl.h>

static int write_file(void){
  int fd;
  fd= open("DW",O_WRONLY|O_CREAT,0600);
  if(fd==-1){
    printf("open() error\n");
    return -1;
  }
  dprintf(fd,"hello world!\n");
  close(fd);
  return 0;
}
static int trunc_file(){
  int fd;
  fd=open("DW",O_WRONLY|O_CREAT,0600);
  if(fd==-1){
    printf("open() error");
    return -1;
  }
  dprintf(fd,"hi world\n");
  close(fd);
  return 0;
}
static int append_file(){
  int fd;
  fd=open("DW",O_APPEN|O_WRONLY);
  if(fd==-1){
    printf("open() error\n");
    return -1;
  }
  dprintf(fd,"again write");
  close(fd);
  return 0;
}
int main(int argc, char **argv){
  if(write_file()){
    printf("write file error");
    return -1;
  }
  if(trunc_file()){
    printf("trinc_file error");
    return -1;
  }
  if(append_file()){
    printf("append_file error");
    return -1;
  }
  return 0;
}
