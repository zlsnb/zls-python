# 赵老师学Python

![WechatIMG1](https:github.com/zls-python/Nine-year Compulsory Education/WechatIMG1.jpeg)

## 前提背景

* 为了能让来自昆明的会唱山歌的HR赵老师段时间内学会如何使用python创建了这个repo。
* 同时还有@黄大厨的git教程
* 最后还有我们的苏简单，什么python，git，超级简单
* 发起人:@zhouqi，@fuhailong

## 组织结构

### Python

* python基础知识
* python进阶
* python实战

### Git

* git原理
* git基本命令
* git实战
### Easy Things
> sql很简单啊
> python 超级简单（赵老师要哭了）
> git 也很简单啊（黄大厨已经哭了）
### 菜谱

> 不会python的司机，不是好HR
>
> 不会git的科研人员，不是好RD
>
> 不会说简答的超级简单，不是好BA
* 每日一菜
* 简单的菜


### 贡献力量
>  向本repo贡献代码流程
>
> * 首先fork到自己的github目录下面，`git clone` 到自己服务器上面，进行自己的新增添加等操作，然后`git add` ， 然后`git commit`，这样会自动检查格式，然后在`git push` 到远程的分支上面，新建pr，等待reveiw。
> * github 提交代码遇到的一些问题
>   - 本地的版本不是基于远程仓库的版本之上的，所以会有冲突，解决这个问题的尝试
>     - 首先git add remote upstream "上游仓库name",使用git remote -v 可以查看远程仓库和上游仓库的地址。通过git fetch upstream/develop，将远程的分支拉取到本地，git branch 只能查看本地的分支，也就是origin的分支，没有办法查看upstream的分支，但是可以使用git checkout up/develop 切换。然后需要切换到origin上面，通过git checkout upstream/develop . ，来把本地的分支更新一下，git merge upstream/develop，将拉取的upstream的分支和本地的分支合并。git push origin branch_name。但是有的时候会出现冲突的情况，这个可能需要进行回退，现在本地上面进行操作，git reset --hard commit_id，然后git push -f origin branch_name，强制覆盖到远程的仓库上面，这样远程仓库就进行了回滚，然后在执行之前的操作，就可以了。
