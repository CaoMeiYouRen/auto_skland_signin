# auto_skland_signin

基于文字识别的森空岛自动签到脚本。

所有功能通过文字识别实现，无需 cookie，很少出现验证码，目前真正实用的签到工具。

## 功能
- 自动领取森空岛签到福利
  - 包括 明日方舟 等
- 支持企业微信、钉钉等多个推送渠道
  - 详情请前往 [onepush](https://github.com/y1ndan/onepush) 页面查看

## 环境要求(windows x64)

- python >=3.6
- 一个支持 adb 的模拟器

## 安装依赖

```sh
pip install -r requirements.txt
```

## 用法

1. 复制根目录下的 `config.example.yml` 文件，并改为 `config.yml`
2. 填写配置。

| 字段           | 是否必须 | 解释                                                         |
| -------------- | -------- | :----------------------------------------------------------- |
| ADB_PORT       | 必须     | 要连接的模拟器的 adb 端口，可查询各大模拟器文档获取          |
| ONEPUSH_CONFIG | 可选     | [onepush](https://github.com/y1ndan/onepush) 相关配置，支持企业微信、钉钉等多个推送渠道 |
| SIGNIN_GAMES   | 可选     | 要签到的游戏。名称必须和项目中的 `skland_bbs` 的 `key` 一致 |

3. 启动已安装好森空岛的模拟器

4. 确认 adb 可用。若不可用，请添加 adb 到环境变量

   ```sh
   adb devices
   ```
5. 运行 `python auto_skland_signin.py`
6. 查看运行结果

## 可能出现的问题

### 如何每日运行

- 可在`我的电脑`中添加系统任务来每日运行

- 修改脚本实现死循环运行

- 其他方式每日触发脚本运行

- 可参考 以下 bat 脚本。实际使用中需移除中文注释，并将 bat 文件放在本项目根目录下。

- ```bat
  chcp 65001
  @echo off
  @REM 请将下面的 VM_PATH 修改为你自己的模拟器的路径，此处以 MuMu 模拟器 12 为例
  set VM_PATH="D:\Program Files\MuMu\emulator\MuMuPlayer-12.0\shell"
  @REM 请将 MuMuPlayer.exe 修改 为你自己的模拟器名称
  start /d %VM_PATH% MuMuPlayer.exe
  
  @REM 等待模拟器启动
  timeout /t 90 /nobreak
  
  python auto_skland_signin.py
  
  @REM 等待任务执行完毕
  timeout /t 5 /nobreak
  
  @REM 关闭模拟器。请将要关闭的程序名称修改为你自己的模拟器名称
  taskkill /F /IM MuMuPlayer.exe
  taskkill /F /IM MuMuVMMHeadless.exe
  taskkill /F /IM MuMuVMMSVC.exe
  
  exit
  ```

### 有部分游戏未签到/签到失败

- 对于未绑定角色的游戏，固定签到失败。
- 可以修改配置中的 tab 排序，和项目中的一致即可
- 也可以修改森空岛的 tab 排序
- 为减少 tab 问题，可减少 tab 的数量，使之可以在一个屏幕内展示出来

## 作者


👤 **CaoMeiYouRen**

* Website: [https://blog.cmyr.ltd/](https://blog.cmyr.ltd/)
* GitHub: [@CaoMeiYouRen](https://github.com/CaoMeiYouRen)

## 📝 License

Copyright © 2024 [CaoMeiYouRen](https://github.com/CaoMeiYouRen).<br />
This project is [AGPL-3.0](https://github.com/CaoMeiYouRen/auto_skland_signin/blob/master/LICENSE) licensed.
