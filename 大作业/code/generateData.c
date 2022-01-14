#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

// 宏定义相关参数
#define ITER_LIMIT (3e5)    //迭代次数上限
#define D 1.0               //D
#define ROU 1.0             //Rou
#define SIGMA 1.0           //Sigma
#define DELTA_X (5e-3)      //x的步长
#define DELTA_T (1e-5)      //t的步长
#define PI 3.1415926536     //pi

// 写入文件的函数
void writeFile(double* data, FILE* file, int times);

int main(void)
{
    // 处理输入
    double xValue, tValue;
    int iterTimes;
    printf("Please input the value of x: ");    scanf("%lf", &xValue);
    printf("Please input the value of t: ");    scanf("%lf", &tValue);
    // 计算迭代次数
    iterTimes = (int)(tValue / DELTA_T) + 1;
    iterTimes = iterTimes > ITER_LIMIT ? ITER_LIMIT:iterTimes;
    // 初始化数组用于存放结果
    double *density0 = (double*)calloc(iterTimes+1, sizeof(double)); //恒定浓度
    double *density1 = (double*)calloc(iterTimes+1, sizeof(double));
    density0[0] = density1[0] = ROU;
    double *source0 = (double*)calloc(iterTimes+1, sizeof(double));  //限定源
    double *source1 = (double*)calloc(iterTimes+1, sizeof(double));
    source0[0] = source1[0] = SIGMA;

    // 进行迭代
    int i, j;
    for( i = 1; i <= iterTimes; i++ )
    {
        // 开启多线程，对限定源问题中除x=0处的点进行加法归约
        double sum = 0.0;
        #pragma omp parallel for reduction(+:sum)
        for( j = 1; j <= i; j++ )
        {
            density1[j] = density0[j] + D*DELTA_T/pow(DELTA_X, 2) * (density0[j-1]-2*density0[j]+density0[j+1]);
            source1[j] = source0[j] + D*DELTA_T/pow(DELTA_X, 2) * (source0[j-1]-2*source0[j]+source0[j+1]);
            sum += source1[j];
        }
        source1[0] = SIGMA - sum;   //计算限定源x=0处的面密度
        // 交换指针进行下一次迭代
        double *temp;
        temp = density0;    density0 = density1;    density1 = temp;
        temp = source0;    source0 = source1;    source1 = temp;
    }
    // 将面密度转化为体密度
    #pragma omp parallel for
    for(i = 0; i <= iterTimes; i++)
    {
        source0[i] /= DELTA_X;
    }

    // 计算恒定浓度和限定源的理论值
    double *dstAnalytic = (double*)calloc(iterTimes+1, sizeof(double));
    double *srcAnalytic = (double*)calloc(iterTimes+1, sizeof(double));
    iterTimes = (int)(xValue / DELTA_X) + 1;
    #pragma omp parallel for
    for(i = 0; i <= iterTimes; i++)
    {
        double x = i*DELTA_X;
        dstAnalytic[i] = ROU * erfc(0.5*x/sqrt(tValue*D));
        srcAnalytic[i] = SIGMA/sqrt(D*PI*tValue)*exp((-1)*x*x/(4*D*tValue));
    }
    //保存数值解和解析解
    FILE *dstFile, *srcFile;
    dstFile = fopen("densityData.txt", "w");
    srcFile = fopen("sourceData.txt", "w");
    writeFile(density0, dstFile, iterTimes);    writeFile(dstAnalytic, dstFile, iterTimes);
    writeFile(source0, srcFile, iterTimes);    writeFile(srcAnalytic, srcFile, iterTimes);
    fclose(dstFile);    fclose(srcFile);
    printf("Data have been saved. Please use Python script to analyze.\n");
    system("pause");
    return 0;
}

void writeFile(double* data, FILE* file, int times)
{
    int i;
    for( i = 0; i < times-1; i++ )
    {
        fprintf(file, "%.10f,", data[i]);
    }
    fprintf(file, "%.10f\n", data[i]);
}
