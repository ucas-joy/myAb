# myAb
##网站压力测试工具的实现  
2.运行环境
系统  windows7  
python 版本: Python 2.7.10   
依赖包 pycurl   tablib    

##该工具首先通过主进程检查各种参数，然后创建http（也可以是https）请求及全局变量，再根据并发数创建多个子进程，
由子进程测试http（也可以是https）请求，并把结果写到全局变量中，之后由父进程读取全局变量测试结果，经过计算后最后输出测试结果。

                                                              
主进程检测各种参数----创建http请求----创建全局变量-----创建子进程   
-------------父进程读取变量测试结果 ------- 输出测试结果  
-------------子进程测试http请求，并把结果写到全局变量中  

##测试结果中：
  1）吞吐率（Request per second）
吞吐率就是服务器并发处理能力的量化描述，单位是reqs/s，指的就是某个并发用户数下单位时间内处理的请求数。
某个并发用户数下单位时间内能处理的最大请求数，称之为最大吞吐率。同时必须明白的是吞吐率是基于并发用户数的，
也就是说吞吐率和并发用户数相关，同时不同的并发用户数下，吞吐率一般是不同的。同时在计算吞吐率的时候，也就
是与总的请求数与处理完这些请求需要的时间 的比值。同时在交互式的访问来说，吞吐率指标很好的反映了服务器承
受的压力，在容量规划的测试中，吞吐量也是一个重点关注的指标，因为其能够很好的说明系统级别的负载能力，同时，
在性能调优的过程中，吞吐率也有很重要的价值。因此在我们使用pythonAb进行压力测试的时候，通过模拟足够多的数
目的并发用户，分别持续发送一定的HTTP请求，并统计测试持续的总时间，计算出基于这种“压力”下的吞吐率，就
得到了一个平均计算值    

2）用户平均请求等待时间（Time per request）同时还包括服务器平均请求处理时间
用户平均请求等待时间主要是用户衡量服务器在一定并发用户数的情况下，对于单个用户的服务质量服务器平均请求处
理时间与前者相比，则用户衡量服务器的整体服务质量，它其实就是吞吐率的倒数。同时服务器平均请求等待时间与并
发数密切相关，也不能脱离并发数来描述服务器平均请求等待时间。     

3）并发用户数（n）
并发用户数就是指在某一时刻同时向服务器发送请求的用户总数，我们就举例说明并发用户数对服务器压力的影响，假
如100个用户同时向服务区分别进行10次请求，与一个用户向服务器连续进行1000次请求，一个用户向服务器连续进行
1000次请求的过程中，任何时刻服务器的网卡接受缓存区中只有来自该用户的1个请求，而100个用户同时向服务器分别
进行10次请求的过程中，服务器网卡接收缓冲区中最多有100个等待处理的请求，显然这时候服务器的压力更大。同时最
大并发数的控制也是非常重要的。它是有一定利益前提的，那就是服务器和用户双方所期待的最大利益，服务器希望支持
高并发数以及高吞吐率，而用户不管是多少，只是希望等待较少的时间，甚至是更快的响应速度。因此并发用户数的意义
在于了解服务器的承载能力之后，我们要结合用户规模考虑适当的扩展方案，当时对于同一个域名下URL的并发下载数是有
最大限制的，这是和浏览器的有一定的关系。




                                                        
