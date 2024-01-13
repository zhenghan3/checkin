# 每日签到 GitHub Action部署

## 功能简介

这个 GitHub Action 用于执行各种服务的每日签到任务。

## 如何配置

首先要fork本项目到自己的仓库，除了阿里网盘的refresh token是必要设置，其他都不是必要的。

1. **Fork 本仓库**: 点击本仓库右上角的 "Fork" 按钮。

2. **配置 Secrets**: 进入你 Fork 的仓库的 "Settings" > "Secrets" 页面，添加以下 Secrets：

   - `ALI_REFRESH_TOKEN`: 你的阿里云盘刷新令牌。这个链接教你如何获得 Refresh Token：https://alist.nn.ci/zh/guide/drivers/aliyundrive.html
   - `TY_USER`: 你的天翼云盘用户名。
   - `TY_PWD`: 你的天翼云盘密码。
   - `YOUDAO_COOKIE`: 你的有道云笔记签到 Cookie。
   - `PUSHPLUS_TOKEN`: 你的 Pushplus 令牌。
   - `SERVERCHAN_SENDKEY`: 你的 ServerChan 发送密钥。
   - `WECOM_TOKENS`: 你的企业微信令牌（如果有多个请用逗号分隔）。
   - `WECOM_WEBHOOK`: 你的企业微信 Webhook URL。
   - `BARK_DEVICEKEY`: 你的 Bark 设备密钥。
   - `FEISHU_DEVICEKEY`: 你的飞书设备密钥。
   - `TELEGRAM_TOKEN`: 你的 Telegram 机器人令牌。格式为 bot_token, chat_id （用英文逗号分隔）

3. **运行 GitHub Action**: 该 Action 预定在每天 UTC 0:00 运行。你可以在 "Actions" 标签页中查看工作流的运行状态。


## 配置 GitHub Actions

1. 在您的 GitHub 仓库中，确保存在 `.github/workflows/` 目录。
2. 创建或编辑一个 YML 文件，本项目是run.yml
3. 修改启动时间，可以根据自己的要求来（不修改就是用默认的）。以下是示例
   on:
  schedule:
    - cron: '0 5 * * *' 这里的是UTC时间，换算北京时间就是13点
    - 
## 支持的服务
支持的签到
- **阿里云盘**: 每日签到。
- **天翼云盘**: 每日签到。
- **有道云笔记**: 每日签到。
支持的推送有
- **Pushplus**: 通知服务。
- **ServerChan**: 通知服务。
- **企业微信（企业版微信）**: 通知服务。
- **Bark**: 通知服务。
- **飞书（Lark）**: 通知服务。
- **Telegram**: 通知服务。
后续待增加。。。。
感谢@boci,
