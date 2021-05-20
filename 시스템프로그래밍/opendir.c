#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<sys/stat.h>
#include<unistd.h>
#include<dirent.h>

#define TYPE2STR(X) \
  ((X)==DT_BLK ? "block device" : \
  (X)==DT_CHR ? "char device" : \
  (X)==DT_DIR ? "directory" : \
  (X)==DT_FiFO ? "fifo" : \
  (X)==DT_LNK ? "symlink" : \
  (X) ==DT_REG ? "regular file" :\
  (X)==DT_SOCK ? "socket":\
  "unkown")

int main(int argc, char ** argv){
  DIR *dp;
  struct dirent *entry;
  
  dp=opendir(".");
  if(!dp){
    printf("opendir () fail\n");
    return -1;
  }
  while(entry = readdir(dp)){
      printf("%s : %s\n",entry->d_name,TYPE2STR(entry->d_type));
  }
  closedir(dp);
  return 0;
}
