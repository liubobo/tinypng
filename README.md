# tinypng

一个循环压缩资源图片的工具，实测减少了ipa包大概30M的体积
功能描述：TinyPNG和TinyJPG网站提供了压缩和优化.png和.jpg格式图片的功能。虽然可以很轻松地使用网页版进行操作，但是在搭建个人博客的时候，调用网站提供的API更为方便快捷。tinify模块就是由TinyPNG提供的使用Python调用Tiny PNG API的模块。

获取API key

如果想调用TinyPNG的API，需要先在他们的网站TinyPNG Developer API上申请一个API key用于身份验证。只需要提供你的名字和邮箱地址就可以获得一个API key，API key会以链接的形式发到邮箱里。 
注意：无法使用qq邮箱申请key 

1.安装pip
2.pip install  tinify
3.在  https://tinypng.com 获取tinify.key  'cRIu54yRk8ubjhkNK4a3-DdKNUKHJdTm' ，这个key有次数限制，还请自行申请
3.python tinypng.py pic_dir
