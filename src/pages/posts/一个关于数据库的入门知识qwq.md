---
layout: "../../layouts/MarkdownPostLayout.astro"
title: "一个关于数据库的入门知识(1)qwq"
pubDate: 2025/5/18
auther: "青稞"
type: "技术"
---

最近C++理论结课，实不相瞒，这个课是一个相当相当水的课程，以至于我上课不是在做算法题，就是在看morden C++。
<br><br>
结课项目其实要求很简单，但是我有一点点想装x的念头，于是灵机一动。"哎！写个数据库！"
<br><br>
数据库是一个不算很麻烦的项目，但是真正写起来却相当麻烦。鏖战一个周末，终于写出来了。
<br><br>
在开始之前，先讲一下数据库的基本操作和基本的内容uwu
<br><br>
数据库由许多的表构成，而表又由基本元素构成
<br><br>
表(Table)有表名(table name) 行(row) 列(col)组成，其中又包含主键(Primary Key)(唯一标识表中每条记录的字段或字段组合)，外键(Foreign Key)(建立表与表之间关系的字段)
<br><br>
基本操作有 : 创表，删表，查表，改表
<br><br>
数据库同样有四个从底层到应用的分层：<br>
1. 应用部分(如连接服务器，UI界面等)
2. 解释器部分(sql_parser)
3. 持久化存储部分(序列化存储)
4. 基本操作部分(增删查改,基本组成)

<br><br>
然后就是实现的细节：~~倒不如说这才是重点~~
<br><br>
首先，表的结构并不是单个元素来组成的，而是建立了一个Column的结构体，且数据类型由enum实现
<br><br>
其次，表有主键，也就是所说的Primary Key，主键必须满足"唯一性"和"非空性"，修改后的值不能与表中现有主键重复。
<br><br>
在修改特定行列的元素时，遇到一个很低级但是很容易错的问题<br>
for(auto &it : rows)<br>
值得注意的一点是，这个地方必须必须是&来传入数据，否则修改虽然会显示成功，但是实际并未修改内容，只是修改了rows中单个元素的副本。<br><br>
在这次写数据库的过程中本来打算用B+树狠狠装一波X，然后耗时六个小时后，果断放弃(可恶，还是太菜了)<br><br>
所以取而代之的就是map<string,string> <br><br>
row的实现是一个很有意思的部分，它并非直接生成了一个行，而是一个键对应一个column的值，一个一个组起来形成了一行。
<br><br>
嗯，确实没想到居然也可以这么实现，相当有意思。
<br><br>
然后就是很顺利地完成了基本操作，稍微找了找序列化存储的办法，复现了一下，第四部分和第三部分就顺利完成了。
<br><br>
剩下两个部分难度有点大，还没有开始写qwq(真的不是我懒，这个周末已经写了16个小时的代码了，腱鞘炎都犯了QAQ)
<br><br>
详情如何，且听下回分解XD<br><br>