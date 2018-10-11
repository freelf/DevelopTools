
## 缘起
因为日常工作中一直打包测试，传到蒲公英。手动打包过程非常耗费时间，期间使用了 fastlane 去打包，还是有些慢。想着打测试包只要把 .app 文件用文件夹包一层，然后压缩，改名为.ipa 就可以安装了。因为学了一点 Python，开始试着用 Python 写个脚本去打包。于是就有了这个脚本。打包的话，很快，而且打包完成会自动打开对应的网址。我们需要做的就是执行脚本，然后把网址复制到对应的群里。如果是用邮箱分发的话，这里可以用脚本发邮件。如果以后有需求，我会加上的。
脚本里面的注释很详细。大家可以看一下。很简单的哦。
## 使用
使用步骤：
1. 配置好证书。
2. 把设备调整为Generic iOS Device
3. 成功 build 工程
4. 需要修改里面几个配置：
appProductFileFullPath是 app 所在的文件夹，就是 Xcode 中 product文件夹下的.app的全路径。
payLoadPath和packageBagPath这两个只需要修改用户名就可以。
openUrl是蒲公英对应的 dashboard 界面。
PGYER_USER_KEY和PGYER_API_KEY是对应蒲公英账号的 key。
5. 执行脚本
注意：一定配置好证书，把设备设置为Generic iOS Device并且成功编译。
