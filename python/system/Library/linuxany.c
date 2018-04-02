#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char membin[1024 * 1024 * 20]={0x31,0x31,0x32,0};
int init=0;
//int readFile()
//{
//    FILE *fp=fopen("mem.bin","rb");
//    if(fp==NULL)
//　   {
//　       fclose(fp);
//　       return 0;
//　   }
//
//    fseek(fp,0L,SEEK_END); /* 定位到文件末尾 */
//    int flen=ftell(fp); /* 得到文件大小 */
//
//    fseek(fp,0L,SEEK_SET); /* 定位到文件开头 */
//    fread(membin,flen,1,fp); /* 一次性读取全部文件内容 */
//    return 1;
//}

__attribute ((constructor)) void test_init(void)
{
    printf("加载动态链接库%s\n", __func__);
//    if(!init)
//    {
//        if(readFile())
//        {
//        printf("初始化成功\n");
//        init=1;
//        }
//        else
//        {
//            printf("初始化失败\n");
//        }
//
//     }


}

__attribute ((destructor)) void test_fini(void)
{
    printf("卸载动态链接库%s\n", __func__);
}
void display(char* msg){
    printf("%s\n",msg);
}
 
int add(int a,int b){
    return a+b;
}

void getData(unsigned char * data){
    memcpy(data,membin,sizeof(membin));
}
