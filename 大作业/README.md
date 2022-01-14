## 使用说明
### 1. 环境配置
1. 运行环境： `python3`, `gcc(or other c compiler support openmp & c99, like icc)`
2. 使用的库： `numpy`, `matplotlib`
3. 库的安装： `pip3 install numpy / matplotlib` 

### 2. 运行命令
1. 编译：
    * `gcc`: `gcc -O3 -march=native -fopenmp generateData.c -o generateData.exe -lm -std=c99`
    * `intel icc`: `icc -O3 -xHost -qopenmp generateData.c -o generateData.exe -std=c99`
2. 运行：
    * `数据计算`: `./generateData.exe`
    * `数据分析`: `python3 analyzeData.py`