

# ***DeepSeek 本地服务部署***

## 1. 硬件要求 ##
要求独显 要用 英伟达 3070 以上显卡。
没有的话，使用CPU+内存可以跑，但是很吃内存、很慢。
我用ThinkPad笔记本，无独显，CPU 1240P+16G内存可以跑，大概1s生成2-5个字。内存占用15G，CPU占用80%+。

## 2. 软件要求 ##
可采用windows. 理论上 Linux, MacOS 都支持，但我主要在windows上开发运行。


## 3. 使用说明 ##

### 3.0 安装本地 deekseek

#### 3.0.1 安装ollama

网络环境支持的，可以在官方下载ollama客户端

[ollma官方下载地址](https://ollama.com/download/windows)

如果网络受限的，可以在我的百度盘下载(windows版本)

[百度网盘下载地址](https://pan.baidu.com/s/1ZLGPGhywIM10Eu93wclH_w?pwd=b3h4)

![安装ollma](images/install_ollama.png)

### 3.0.2 下载或者复制本地模型文件

#### 3.0.2.1 官方通过ollama下载模型
打开PowerShell运行以下命令。

`ollama run deepseek-r1:8b`

#### 3.0.2.2 第三方下载模型
复制模型文件到 C:/User/当前用户名/ 下

通过百度网盘下载
[百度网盘下载地址](https://pan.baidu.com/s/1SxvCtL_B8zJYdg-nCqYccA?pwd=u65e)

![复制模型](images/save_ollama.png)

### 3.1 启动ollama本地服务 ###

确认本地模型已经安装好

`ollama list`

![本地模型展示](images/ollama_list.png)


### 3.2 使用命令行模式跟deepseek对话

`ollama run deepseek-r1:8b`

![本地运行deepseek命令行](images/run_dp_cmd.png)

### 3.3 在python调用ollama服务

直接安装安装 ollama 的包
`pip install ollama`

然后在代码里调用




### 3.3 启动ollma本地API服务

Ollama自带本地服务的API，使用以下命令启动这个API服务

`ollama serve`


![启动本地服务](images/ollama_serve.png)


### 3.2 使用我的脚本验证启动成功 ###

安装Python依赖

`pip install -r ./requirements.txt`

![python里调用ollama](images/py_chat_ollama.png)


### 3.3 启动ollama本地服务

![验证ollama服务](images/test_ollama_api.png)

### 3.4 使用python把这个服务以API形式提供出来
这个形式我参考了chatGLM API的脚本

![运行我的API服务](images/run_my_api.png)

### 3.5 验证测试我提供的API服务

![验证我的API服务](images/run_result.png)

### 3.6 使用Gradio构建图形用户界面

运行我的例子:

![运行gradio](images/run_gradio.png)

进行问答:

![运行演示](images/gradio_demo.png)
