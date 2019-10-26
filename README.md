# ParzenWindow-PR_Experiment
Implement the parzenwindow, which is the experiment 1 in Pattern Recognition.(Harbin Institute of Technology, CS, Master). I've read a few ParzenWindow samples which realized by Pyhton, but none of them are correct, so I spend three days in understanding and programing it. Hope it'll help you:)
### Formula
The implementation strictly follow the ["Pattern Classification second edition"](http://blog.sina.com.cn/s/blog_c3b6050b0102xg24.html). Specifically, the references are in <b>page 138</b>, it is as follows:

<div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/parzenwindow's%20formula.png" width="50%" height="25%" alt="Loading failed"/></div>

### The flowchart of ParzenWindow


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

##### initial distribution 

<div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/initial%20distribution.png" width="50%" height="50%"/></div>

<table width=20><tr>
<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/test%20initaial%20distribution.png"/></div></td>

<td><div align=center><img src="https://github.com/HuiyanWen/ParzenWindow-PR_Experiment/blob/master/pic/traininitaial%20distribution.png"/></div></td>
</tr></table>


