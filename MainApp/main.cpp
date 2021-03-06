#include "MainApp.h" //主窗口

#include <QApplication>
#include <QSplashScreen>

#ifdef _WIN32
  #include <windows.h>
#elif __linux__
  #include <unistd.h> //使用sleep函数

#endif

int main(int argc, char *argv[])
{
  QApplication a(argc, argv); // 声明一个Qt应用
  a.setStyle(QString("Fusion")); // 设置应用基本风格, Fusion可以兼容多平台, 实际上所有的样式表都是更改过的
  QImage img; // 准备启动画面的图片
  img.load(":/imgs/assets/isae-splash.png");
  QSplashScreen splash(QPixmap::fromImage(img));
  splash.show(); // 展示
  sleep(1); // TODO: 插件增多之后注释掉此行, 这里仅仅只是为了展示splash的效果.
  MainApp w; // 声明主窗口, 加载所有插件.
  splash.finish(&w); // 主窗口加载完毕后关掉启动画面
  w.show(); // 让主窗口显示出来
  return a.exec(); // 进入事件循环
}
