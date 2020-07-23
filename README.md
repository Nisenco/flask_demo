# flask_demo
init 

#### todo 未完成功能
#### dev  已完成功能

如果你需要在另一台机器上重新生成你的环境，将无法记住你必须安装哪些软件包，所以一般公认的做法是在项目的根目录中写一个requirements.txt文件，列出所有依赖的包及其版本。 生成这个列表实际上很简单：

(venv) $ pip freeze > requirements.txt
pip freeze命令将安装在虚拟环境中的所有软件包以正确的格式输入到requirements.txt文件中。 

现在，如果你需要在另一台计算机上创建相同的虚拟环境，无需逐个安装软件包，可以直接运行一条命令实现：

(venv) $ pip install -r requirements.txt
