import numpy as np
from matplotlib import pyplot as plt

# 打开文件并读取数值解和解析解
dstFile = open("densityData.txt");  srcFile = open("sourceData.txt")
dstNumerical = dstFile.readline();  dsrAnalytic = dstFile.readline()
srcNumerical = srcFile.readline();  srcAnalytic = srcFile.readline()
dstFile.close();  srcFile.close()

# 数据预处理
dstNumerical = list(map(float, dstNumerical.split(",")))
dsrAnalytic = list(map(float, dsrAnalytic.split(",")))
srcNumerical = list(map(float, srcNumerical.split(",")))
srcAnalytic = list(map(float, srcAnalytic.split(",")))
dstNumerical = np.array(dstNumerical);    dsrAnalytic = np.array(dsrAnalytic)
srcNumerical = np.array(srcNumerical);    srcAnalytic = np.array(srcAnalytic)
xLength = len(dstNumerical);    x = np.arange(0, xLength*0.005-0.001, 0.005)
DPI = 512

# 作图
plt.figure("Constant Density Spread", dpi=DPI)
plt.title("Constant Density Spread")
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.plot(x, dsrAnalytic, "g-", label='Analytic Solution')
plt.plot(x, dstNumerical, "r:", linewidth=2, label='Numerical Solution')
plt.legend()
plt.savefig("./density.png")

plt.figure("Limited Source Spread", dpi=DPI)
plt.title("Limited Source Spread")
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.plot(x, srcAnalytic, "g-", label='Analytic Solution')
plt.plot(x, srcNumerical, "r:", linewidth=2, label='Numerical Solution')
plt.legend()
plt.savefig("./source.png")

dstError = np.abs(dsrAnalytic-dstNumerical) / dsrAnalytic * 100
srcError = np.abs(srcAnalytic-srcNumerical) / srcAnalytic * 100

plt.figure("Constant Density Spread Error(%)", dpi=DPI)
plt.title("Constant Density Spread Error(%)")
plt.xlabel("x")
plt.ylabel("Error(%)", labelpad=0.6)
plt.plot(x, dstError)
plt.savefig("./densityError.png")

plt.figure("Limited Source Spread Error(%)", dpi=DPI)
plt.title("Limited Source Spread Error(%)")
plt.xlabel("x")
plt.ylabel("Error(%)")
plt.plot(x, srcError)
plt.savefig("./sourceError.png")

print("Four figures have been saved.")

