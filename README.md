# DjangoBlog
使用Django搭建个人博客网站
- `pip install -r requirement.txt` 安装最新依赖
- `python manage.py collectstatic` 收集静态文件
- `python manage.py migrate` 迁移数据库
- 重启 Nginx 和 Gunicorn 使改动生效
- `gunicorn --bind unix:/tmp/demo.com.socket blog.wsgi:application`
- [x] 支持MarkDown
- [x] 分类与归档
- [x] 评论
- [x] 统计文章阅读量
- [x] 文章摘要
- [x] 标签云
- [x] 分页
