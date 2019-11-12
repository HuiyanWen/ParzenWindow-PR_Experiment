# ParzenWindow-PR_Experiment
Implement the parzenwindow, which is the experiment 1 in Pattern Recognition.(Harbin Institute of Technology, CS, Master). I've read a few ParzenWindow samples which realized by Python, but none of them are correct, so I spend three days in understanding and programing it. Hope it'll help you:)
### Formula
The implementation strictly follow the ["Pattern Classification second edition"](http://blog.sina.com.cn/s/blog_c3b6050b0102xg24.html). Specifically, the references are in <b>page 138</b>, it is as follows:

<div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/parzenwindow's%20formula.png" width="50%" height="25%" alt="Loading failed"/></div>

### The flowchart of ParzenWindow
<div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/flowchart.png" alt="Loading failed"/></div>

### Code illustration
|方法名|所属文件|功能|
|:--|:--|:--|
| generateDate | parzen_main.py | 生成样本 |
| ShowData | parzen_main.py | 绘制样本点 |
| dist | parzen_main.py | 计算L2距离 |
| gaussCore | parzen_main.py | 高斯核函数 |
| ShowData | parzen_main.py | 绘制样本点 |
| PN | parzen_main.py | 绘制样本点 |
| ShowData | parzen_main.py | Pn公式计算 |
| calculate_acc | parzen_main.py | 准确率计算 |
| calculate_acc | parzen_main.py | 样本点预测 |
| main | parzen_main.py | 主函数 |
| calc_statistics | initia_distribution.py | 核对方差、均值 |
| main | initia_distribution.py | 绘制初始分布 |

### Expriments and results
We let test samples' num stay 300 during the whole lab, and adjust the training num <b>N</b> and window size<b>h</b>.

##### initial distribution 

<div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/initial%20distribution.png" width="50%" height="50%"/></div>

##### the left is the test set, the other is the train set. 
<table width=20><tr>
<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/test%20initaial%20distribution.png"/></div></td>

<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/traininitaial%20distribution.png"/></div></td>
</tr></table>

##### N=30 h=0.5 accuracy=0.5367
<div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/10%200.5.png" width="50%" height="50%"/></div>

##### The tint dots are test samples' inference result, you can see most of them are around the corresponding train samples, and this phenomenon illustrates we are right.
<div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/10%200.5%200.5367.png" width="50%" height="50%"/></div>

##### N=30 h=1 accuracy=0.4233
<table width=20><tr>
<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/10%201.png"/></div></td>

<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/10%201%200.4233.png"/></div></td>
</tr></table>

##### N=30 h=5 accuracy=0.3333
<table width=20><tr>
<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/10%205.png"/></div></td>

<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/10%205%200.3333.png"/></div></td>
</tr></table>

##### N=90 h=0.5 accuracy=0.56
<table width=20><tr>
<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/30%200.5.png"/></div></td>

<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/30%200.5%200.56.png"/></div></td>
</tr></table>

##### N=90 h=1 accuracy=0.4667
<table width=20><tr>
<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/30%201.png"/></div></td>

<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/30%201%200.4667.png"/></div></td>
</tr></table>

##### N=90 h=5 accuracy=0.3333
<table width=20><tr>
<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/30%205.png"/></div></td>

<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/30%205%200.3333.png"/></div></td>
</tr></table>

##### N=300 h=0.5 accuracy=0.6
<table width=20><tr>
<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/100%200.5.png"/></div></td>

<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/100%200.5%200.6.png"/></div></td>
</tr></table>

##### N=300 h=1 accuracy=0.5367
<table width=20><tr>
<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/100%201.png"/></div></td>

<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/100%201%200.5367.png"/></div></td>
</tr></table>

##### N=300 h=5 accuracy=0.5367
<table width=20><tr>
<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/100%201.png"/></div></td>

<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/100%201%200.5367.png"/></div></td>
</tr></table>

##### N=1200 h=0.5 accuracy=0.6667
<table width=20><tr>
<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/400%200.5.png"/></div></td>

<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/400%200.5%200.6667.png"/></div></td>
</tr></table>

##### N=1200 h=1 accuracy=0.5667
<table width=20><tr>
<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/400%201.png"/></div></td>

<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/400%201%200.5667.png"/></div></td>
</tr></table>

##### N=1200 h=5 accuracy=0.3833
<table width=20><tr>
<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/400%205.png"/></div></td>

<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/400%205%200.3833.png"/></div></td>
</tr></table>

##### Set N=1200, the accuracy changes with h.
<div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/400%20h%20accuracy.png" width="50%" height="50%"/></div>
