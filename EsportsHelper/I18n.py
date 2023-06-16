import argparse

import yaml


class I18n:
    def __init__(self, lang="zh_CN"):
        self.language = lang

    enUSI18n = {
        "无法找到最新版谷歌浏览器!如没有下载或不是最新版请检查好再次尝试": "The latest version of Google Chrome is not found.\nPlease check if Chrome downloaded or has the latest version.",
        "是否有谷歌浏览器?": "Is Google Chrome installed?",
        "是否打开着谷歌浏览器?请关闭后再次尝试": "Is Google Chrome running?Please close it and try again.",
        "生成WEBDRIVER失败!": "WebDriver generation failure!",
        "是不是网络问题?请检查VPN节点是否可用": "Is there a network problem? Check VPN availability if one connected",
        "无法打开Lolesports网页，网络问题，将于3秒后退出...": "Network problem: cannot open LolEsports website. Exiting in 3 seconds...",
        "自动登录失败,检查网络和账号密码": "Automatic login failed. Please check the network availability and account credentials.",
        "登录超时,检查网络或窗口是否被覆盖": "Login timeout. Please check the network availability or if the window is covered.",
        "好嘞 登录成功": "Logged in successfully.",
        "登录失败,检查账号密码是否正确": "Login failed. Please check if the account credentials are correct.",
        "使用浏览器缓存 自动登录成功": "Using browser cookies. Auto-login success.",
        "观看结束": "Watch finished.",
        "切换网页语言成功": "Web language switched successfully.",
        "切换网页语言失败": "Web language switch failed.",
        "无法登陆，账号密码可能错误或者网络出现问题": "Login failed: wrong credentials or network problem.",
        "开始重试": "Restarting.",
        "配置文件找不到": "Configuration file not found.",
        "按回车键退出": "Press Enter to exit.",
        "配置文件中没有账号密码信息": "There are no account credentials in the configuration file.",
        "检查间隔配置错误,已恢复默认值": "Incorrect interval configuration. The default value has been restored.",
        "睡眠时间段配置错误,已恢复默认值": "Incorrect sleep time period. The default value has been restored.",
        "最大运行时间配置错误,已恢复默认值": "The maximum runtime set incorrectly. The default value has been restored.",
        "代理配置错误,已恢复默认值": "Incorrect proxy configuration. The default setting has been restored.",
        "用户数据userDataDir路径配置错误,已恢复默认值": "Incorrect UserDataDirectory path configuration. The default setting has been restored.",
        "语言配置错误,已恢复zh_CN默认值": "Incorrect language configuration. The default language zh_CN has been restored.",
        '正常观看 可获取奖励': "is live and being watched.",
        "观看异常 重试中...": "is live, but watch attempt was unsuccessful. Retrying...",
        "观看异常": "Watch system work anomaly.",
        "检查掉落失败": "Drops check failed.",
        "掉落提醒失败": "Drop alert failed.",
        "掉落提醒失败 重试中...": "Drop alert failed. Retrying...",
        "无法打开Lolesports网页，网络问题": "Network error. Cannot open LolEsports website.",
        "登录中...": "Logging in...",
        "账密 提交成功": "Account credentials inserted...",
        "网络问题 登录超时": "Network error. Login timeout.",
        "请输入二级验证代码:": "Please enter 2FA code:",
        "二级验证代码提交成功": "2FA code submitted successfully.",
        "免密登录失败,请去浏览器手动登录后再行尝试": "Authentication failure. Please log in manually using browser and try again.",
        "检查掉落数失败": "Failed to check drop count.",
        "开始检查...": "Start checking...",
        "本次运行掉落总和:": "Session  Drops: ",
        '运行掉落总和:': 'Session Drops: ',
        "生涯总掉落:": "Lifetime Drops: ",
        "没有赛区正在直播": "No live broadcasts.",
        "个赛区正在直播中": "match currently live.",
        "赛区正在直播中": "matches currently live.",
        "处于休眠时间，检查时间间隔为1小时": "During the sleep period, the check interval is 1 hour.",
        "下一次检查在:": "Next check at:",
        "预计结束程序时间:": "Time left until the program will auto-close:",
        "对应窗口找不到": "The corresponding window cannot be found.",
        "发生错误": "An error has occurred.",
        "获取比赛列表失败": "Failed to get live broadcasts list.",
        "比赛结束": "Broadcast ended.",
        "关闭已结束的比赛时发生错误": "An error occurred while closing finished broadcast.",
        "比赛跳过": " match skipped.",
        "关闭视频流失败.": "Failed to close stream.",
        "视频流关闭成功.": "Stream closed successfully.",
        "Twitch 160p清晰度设置成功": "Twitch stream quality successfully set to 160p.",
        "Twitch 160p清晰度设置失败": "Failed to set Twitch stream quality to 160p.",
        "无法设置 Twitch 清晰度.": "Unable to set Twitch stream quality.",
        "Youtube 144p清晰度设置成功": "YouTube stream quality successfully set to 144p.",
        "Youtube 清晰度设置失败": "Failed to set YouTube stream quality.",
        "无法设置 Youtube 清晰度.可能是误判成youtube源,请联系作者": "Unable to set YouTube stream quality.Stream possibly was misidentified as YouTube source. Please contact the developer.",
        "下一场比赛时间:": "Next broadcast at:",
        "获取下一场比赛时间失败": "Failed to get next broadcast time.",
        "获取掉落数失败": "Failed to get drops count.",
        "本次运行掉落详细:": "Details of this session drops:",
        "统计掉落失败": "Failed to count drops.",
        "初始化掉落数失败": "Failed to initialize drop count.",
        "小傻瓜，出事啦": "Hey, something is wrong.",
        "错误提醒发送成功": "Error alert sent successfully.",
        "错误提醒发送失败": "Failed to send error alert.",
        "异常提醒成功": "Exception error alert successful.",
        "异常提醒失败": "Exception error alert failed.",
        "下载override文件失败": "Failed to import override file.",
        "正在准备中...": "Preparing...",
        "不支持的操作系统": "Unsupported OS.",
        "程序设定运行时长已到，将于60秒后关机,请及时做好准备工作": "The program has reached the set runtime. The system will shut down in 60 seconds. Please prepare accordingly.",
        "关闭所有窗口时发生异常": "An exception occurred while closing all windows.",
        "所有窗口已关闭": "All tabs closed.",
        "处于休眠时间...": "Sleeping...",
        "预计休眠状态将持续到": "The sleep period will last until",
        "点": "o'clock.",
        "通知类型配置错误,已恢复默认值": "Incorrect notification type configuration. The default setting has been restored.",
        "从Github获取参数文件失败, 将尝试从Gitee获取": "Failed to get parameter file from GitHub. Trying to get it from Gitee.",
        "获取参数文件成功": "Parameter file successfully imported.",
        "获取参数文件失败": "Failed to import parameter file.",
        "休眠时间结束": "Waking up...",
        "进入休眠时间": "Going to sleep now...",
        "(检查下一场比赛时 过滤失效的比赛 ->": "(Filtering invalid broadcasts when checking next broadcast ->",
        "总观看时长: ": "Overall hours watched: ",
        "日期: ": "Date: ",
        "下次检查在:": "Next check at:",
        "人观看": "Viewers",
        "掉落提醒成功": "Drop alert successful.",
        "检查赛区直播状态...": "Checking live broadcasts...",
        "识别到距离比赛时间较长 检查间隔为1小时": "Plenty of time until the next match. Checking interval set to 1 hour.",
        "提醒: 由于已关闭统计掉落功能,webhook提示掉落功能也将关闭": "Tip: The drop count function has been disabled, the drop notification function will also be disabled.",
        "获取LoLEsports网站失败，正在重试...": "Getting to LoLEsports website failed, retrying...",
        "获取LoLEsports网站失败": "Getting to LoLEsports website failed.",
        "获取reward网站失败，正在重试...": "Getting to reward website failed, retrying...",
        "获取reward网站失败": "Getting to reward website failed.",
        "秒后重试...": " seconds until retry...",
        "标题: ": "Stream Title: ",
        "Twitch: 刷新": "Twitch: Refresh",
        "检查掉落数...": "Checking drops number...",
        "出错, 未知": "Error, unknown",
        "Youtube: 刷新": "Youtube: Refresh",
        "检测奖励标识失败": "Failed to detect reward img.",
        "Twitch: 解除静音成功": "Twitch: Unmute successfully.",
        "Twitch: 解除静音失败": "Twitch: Failed to unmute.",
        "Twitch: 解除暂停成功": "Twitch: Unpause successfully.",
        "Twitch: 解除暂停失败": "Twitch: Failed to unpause.",
        "Youtube: 解除静音成功": "Youtube: Unmute successfully.",
        "Youtube: 解除静音失败": "Youtube: Failed to unmute.",
        "Youtube: 解除暂停成功": "Youtube: Unpause successfully.",
        "Youtube: 解除暂停失败": "Youtube: Failed to unpause.",
        "初始化掉落数": "Initializing drops number.",
        "获取队伍信息重试中...": "Retrying to get team info...",
        "获取观看人数信息重试中...": "Retrying to get viewers info...",
        '比赛结束 等待关闭': 'Match ended. Waiting to close.',
        "调试截图成功": "Debug screenshot successful.",
        "调试截图失败": "Debug screenshot failed.",
        "==!!! 新版本可用 !!!==\n===下载:": "==!!! New version available !!!==\n===Download:",
        "获取最新版本失败": "Failed to get latest version.",
        "当前IP地址获取最新版本过于频繁, 请过段时间再试": "Current IP address has been used to get the latest version too frequently. Please try again later.",
        "当前版本: ": "Current version: ",
        "最新版本: ": "Latest version: ",
        "统计掉落数出错,掉落数小于0": "Error counting drops, drops number less than 0.",
        "5秒后开始重试": "Retrying in 5 seconds.",
        "出现异常,登录失败": "An exception occurred, login failed.",
        "无法登录，账号密码可能错误或者网络出现问题": "Unable to login, account or password may be incorrect or there may be a network problem.",
        "如果还不行请尝试重装谷歌浏览器": "If it still doesn't work, try reinstalling Google Chrome.",
        "找不到配置文件": "Configuration file not found.",
        "配置文件错误": "Configuration file error.",
        "或可以尝试用管理员方式打开": "Or try opening it as an administrator.",
        "程序被终止": "Program terminated.",
        "获取地址URL失败": "Failed to get URL.",
        "获取冠军队伍失败": "Failed to get champion team.",
        "Youtube: 设置清晰度时发生错误": "Youtube: Error setting quality.",
        "Youtube: 检查直播发生错误": "Youtube: Error checking live broadcast.",
        "Twitch: 检查直播发生失败": "Twitch: Error checking live broadcast.",
        "Twitch: 设置清晰度发生错误": "Twitch: Error setting quality.",
        "配置文件格式错误": "Configuration file format error.",
        '请检查是否存在中文字符以及冒号后面应该有一个空格': 'Please check if there are Chinese characters and there should be a space after the colon.',
        '配置路径如有单斜杠请改为双斜杠': 'If there is a single slash in the configuration path, change it to a double slash.',
        "桌面提醒成功发送": "Desktop notification sent successfully.",
        "桌面提醒发送失败": "Desktop notification failed to send.",
        "程序退出": "Program exited.",
        "Riot原因,reward页面出现异常无法正常加载": "Riot Error, reward page exception cannot be loaded normally.",
        '程序启动时间: ': 'Program startup time: ',
        "观看人数: ": "Viewers: ",
        "接受cookies": "Accept cookies",
        "未找到cookies按钮(正常情况)": "Cookies button not found (normal)",
        "接受cookies失败": "Failed to accept cookies",
        "今日": "TODAY",
        '于': 'FROM',
        '获得': 'GET',
        '通过': 'BY',
        '新的掉落!': 'NEW DROP!',
        '今日: ': 'TODAY: ',
        '日': '',
        "未找到奖励标识": "Reward mark not found",
        "Twitch: 检查直播间是否在线失败": "Twitch: Failed to check if the live is online",
        "只看模式已开启,已忽略不看模式配置": "Only mode is turned on, ignore the configuration of disWatching mode",
        "最大同时观看数配置错误,已恢复默认值3": "Maximum number of streams configuration error, default value has been restored to 3",
        "进错直播间,正在重新进入": "Entered the wrong live broadcast, re-entering",
        "上午": "AM",
        "下午": "PM",
        "凌晨": "AM",
        "写入掉落历史文件失败": "Failed to write drop history file",
        "读取掉落记录失败": "Failed to read drop history file",
        "推送掉落失败": "Failed to push drop notification",
        "总掉落文件生成中...": "Generating total drop file...",
        "写入总掉落文件失败": "Failed to write total drop file",
    }
    zhTWI18n = {
        "生成WEBDRIVER失败!": "生成WEBDRIVER失敗!",
        '无法找到最新版谷歌浏览器!如没有下载或不是最新版请检查好再次尝试': '無法找到最新版谷歌瀏覽器!如沒有下載或不是最新版請檢查好再次嘗試',
        '是否有谷歌浏览器?': '是否有谷歌瀏覽器?',
        "是不是网络问题?请检查VPN节点是否可用": "是不是網路問題?請檢查VPN節點是否可用",
        "是否打开着谷歌浏览器?请关闭后再次尝试": "是否開啟著谷歌瀏覽器?請關閉後再次嘗試",
        '无法打开Lolesports网页，网络问题，将于3秒后退出...': '無法開啟Lolesports網頁，網路問題，將於3秒後退出...',
        '自动登录失败,检查网络和账号密码': '自動登入失敗,檢查網路和帳號密碼',
        '好嘞 登录成功': '好ㄉ 登入成功',
        '使用浏览器缓存 自动登录成功': '使用瀏覽器快取 自動登入成功',
        '观看结束': '觀看結束',
        "切换网页语言成功": '切換網頁語言成功',
        '切换网页语言失败': '切換網頁語言失敗',
        '无法登陆，账号密码可能错误或者网络出现问题': '無法登陸，帳號密碼可能錯誤或者網路出現問題',
        '开始重试': '開始重試',
        '配置文件找不到': '配置檔案找不到',
        '按回车键退出': '按回車鍵退出',
        "配置文件错误": "配置檔案錯誤",
        '配置文件中没有账号密码信息': '配置檔案中沒有帳號密碼資訊',
        '检查间隔配置错误,已恢复默认值': '檢查間隔配置錯誤,已恢復預設值',
        '睡眠时间段配置错误,已恢复默认值': '睡眠時間段配置錯誤,已恢復預設值',
        '最大运行时间配置错误,已恢复默认值': '最大執行時間配置錯誤,已恢復預設值',
        '代理配置错误,已恢复默认值': '代理配置錯誤,已恢復預設值',
        '用户数据userDataDir路径配置错误,已恢复默认值': '使用者資料userDataDir路徑配置錯誤,已恢復預設值',
        '语言配置错误,已恢复zh_CN默认值': '語言配置錯誤,已恢復zh_CN預設值',
        '正常观看 可获取奖励': '正常觀看 可獲取獎勵',
        '观看异常 重试中...': '觀看異常 重試中...',
        '观看异常': '觀看異常',
        '检查掉落失败': '檢查掉落失敗',
        '掉落提醒失败': '掉落提醒失敗',
        '无法打开Lolesports网页，网络问题': '無法開啟Lolesports網頁，網路問題',
        '登录中...': '登入中...',
        '账密 提交成功': '帳密 提交成功',
        '网络问题 登录超时': '網路問題 登入超時',
        '请输入二级验证代码:': '請輸入二級驗證程式碼:',
        '二级验证代码提交成功': '二級驗證程式碼提交成功',
        '免密登录失败,请去浏览器手动登录后再行尝试': '免密登入失敗,請去瀏覽器手動登入後再行嘗試',
        '检查掉落数失败': '檢查掉落數失敗',
        '开始检查...': '開始檢查...',
        '本次运行掉落总和:': '本次執行掉落總和:',
        '运行掉落总和:': '執行掉落總和:',
        '生涯总掉落:': '生涯總掉落:',
        '没有赛区正在直播': '沒有賽區正在直播',
        '个赛区正在直播中': '個賽區正在直播中',
        '赛区正在直播中': '賽區正在直播中',
        '处于休眠时间，检查时间间隔为1小时': '處於休眠時間，檢查時間間隔為1小時',
        '下一次检查在:': '下一次檢查在:',
        '预计结束程序时间:': '預計結束程式時間:',
        '对应窗口找不到': '對應視窗找不到',
        '发生错误': '發生錯誤',
        '获取比赛列表失败': '獲取比賽列表失敗',
        '比赛结束': '比賽結束',
        '关闭已结束的比赛时发生错误': '關閉已結束的比賽時發生錯誤',
        '比赛跳过': '比賽跳過',
        '关闭视频流失败.': '關閉影片流失敗.',
        '视频流关闭成功.': '影片流關閉成功.',
        'Twitch 160p清晰度设置成功': 'Twitch 160p清晰度設定成功',
        'Twitch 160p清晰度设置失败': 'Twitch 160p清晰度設定失敗',
        '无法设置 Twitch 清晰度.': '無法設定 Twitch 清晰度.',
        'Youtube 144p清晰度设置成功': 'Youtube 144p清晰度設定成功',
        'Youtube 清晰度设置失败': 'Youtube 清晰度設定失敗',
        '无法设置 Youtube 清晰度.可能是误判成youtube源,请联系作者': '無法設定 Youtube 清晰度.可能是誤判成youtube源,請聯絡作者',
        '下一场比赛时间:': '下一場比賽時間:',
        '获取下一场比赛时间失败': '獲取下一場比賽時間失敗',
        '获取掉落数失败': '獲取掉落數失敗',
        '本次运行掉落详细:': '本次執行掉落詳細:',
        '统计掉落失败': '統計掉落失敗',
        '初始化掉落数失败': '初始化掉落數失敗',
        '小傻瓜，出事啦': '小傻瓜，出事啦',
        '错误提醒发送成功': '錯誤提醒傳送成功',
        '错误提醒发送失败': '錯誤提醒傳送失敗',
        '异常提醒成功': '異常提醒成功',
        '异常提醒失败': '異常提醒失敗',
        '下载override文件失败': '下載override檔案失敗',
        '正在准备中...': '正在準備中...',
        '不支持的操作系统': '不支援的作業系統',
        '程序设定运行时长已到，将于60秒后关机,请及时做好准备工作': '程式設定執行時長已到，將於60秒後關機,請及時做好準備工作',
        '关闭所有窗口时发生异常': '關閉所有視窗時發生異常',
        '所有窗口已关闭': '所有視窗已關閉',
        '处于休眠时间...': '處於休眠時間...',
        '预计休眠状态将持续到': '預計休眠狀態將持續到',
        '点': '點',
        '通知类型配置错误,已恢复默认值': '通知型別配置錯誤,已恢復預設值',
        "当前IP地址获取最新版本过于频繁, 请过段时间再试": "當前IP地址獲取最新版本過於頻繁, 請過段時間再試",
        "获取参数文件成功": "獲取參數檔案成功",
        "获取参数文件失败": "獲取參數檔案失敗",
        '休眠时间结束': '休眠時間結束',
        '进入休眠时间': '進入休眠時間',
        '(检查下一场比赛时 过滤失效的比赛 ->': '(檢查下一場比賽時 過濾失效的比賽->',
        '总观看时长: ': '總觀看時長: ',
        '日期: ': '日期: ',
        '下次检查在:': '下次檢查在:',
        '人观看': '人觀看',
        "观看人数: ": "觀看人數: ",
        '掉落提醒成功': '掉落提醒成功',
        "掉落提醒失败 重试中...": "掉落提醒失敗 重試中...",
        '检查赛区直播状态...': '檢查賽區直播狀態...',
        '识别到距离比赛时间较长 检查间隔为1小时': '識別到距離比賽時間較長 檢查間隔為1小時',
        '提醒: 由于已关闭统计掉落功能,webhook提示掉落功能也将关闭': '提醒: 由於已關閉統計掉落功能,webhook提示掉落功能也將關閉',
        "获取LoLEsports网站失败，正在重试...": "獲取LoLEsports網站失敗，正在重試...",
        "获取reward网站失败，正在重试...": "獲取reward網站失敗，正在重試...",
        "获取reward网站失败": "獲取reward網站失敗",
        "秒后重试..." : "秒後重試...",
        "标题: ": "標題: ",
        "Twitch: 刷新": "Twitch: 刷新",
        "检查掉落数...": "檢查掉落數...",
        "出错, 未知": "出錯, 未知",
        "Youtube: 刷新": "Youtube: 刷新",
        "检测奖励标识失败": "檢測獎勵標識失敗",
        "Twitch: 解除静音成功": "Twitch: 解除靜音成功",
        "Twitch: 解除静音失败": "Twitch: 解除靜音失敗",
        "Twitch: 解除暂停成功": "Twitch: 解除暫停成功",
        "Twitch: 解除暂停失败": "Twitch: 解除暫停失敗",
        "Youtube: 解除暂停失败": "Youtube: 解除暫停失敗",
        "Youtube: 解除暂停成功": "Youtube: 解除暫停成功",
        "Youtube: 解除静音失败": "Youtube: 解除靜音失敗",
        "Youtube: 解除静音成功": "Youtube: 解除靜音成功",
        "初始化掉落数": "初始化掉落數",
        "获取队伍信息重试中...": "獲取隊伍資訊重試中...",
        "获取观看人数信息重试中...": "獲取觀看人數資訊重試中...",
        '比赛结束 等待关闭': '比賽結束 等待關閉',
        "调试截图成功": "調試截圖成功",
        "调试截图失败": "調試截圖失敗",
        "==!!! 新版本可用 !!!==\n===下载:": "==!!! 新版本可用 !!!==\n===下載:",
        "获取最新版本失败": "獲取最新版本失敗",
        "获取最新版本过于频繁, 请过段时间再试": "獲取最新版本過於頻繁, 請過段時間再試",
        "最新版本: ": "最新版本: ",
        "当前版本: ": "當前版本: ",
        "统计掉落数出错,掉落数小于0": "統計掉落數出錯,掉落數小於0",
        "登录超时,检查网络或窗口是否被覆盖": "登入超時,檢查網路或視窗是否被覆蓋",
        "登录失败,检查账号密码是否正确": "登入失敗,檢查帳號密碼是否正確",
        "5秒后开始重试": "5秒後開始重試",
        "出现异常,登录失败": "出現異常,登入失敗",
        "无法登录，账号密码可能错误或者网络出现问题": "無法登入，帳號密碼可能錯誤或者網路出現問題",
        "如果还不行请尝试重装谷歌浏览器": "如果還不行請嘗試重裝谷歌瀏覽器",
        "找不到配置文件": "找不到配置檔案",
        "或可以尝试用管理员方式打开": "或可以嘗試用管理員方式打開",
        "程序被终止": "程式被終止",
        "获取地址URL失败": "獲取地址URL失敗",
        "获取冠军队伍失败": "獲取冠軍隊伍失敗",
        "Youtube: 设置清晰度时发生错误": "Youtube: 設定清晰度時發生錯誤",
        "Youtube: 检查直播发生错误": "Youtube: 檢查直播發生錯誤",
        "Twitch: 检查直播发生失败": "Twitch: 檢查直播發生失敗",
        "Twitch: 设置清晰度发生错误": "Twitch: 設定清晰度發生錯誤",
        "配置文件格式错误": "配置檔案格式錯誤",
        '请检查是否存在中文字符以及冒号后面应该有一个空格': '請檢查是否存在中文字元以及冒號後面應該有一個空格',
        '配置路径如有单斜杠请改为双斜杠': '配置路徑如有單斜線請改為雙斜線',
        "桌面提醒成功发送": "桌面提醒成功發送",
        "桌面提醒发送失败": "桌面提醒發送失敗",
        "程序退出": "程式退出",
        "Riot原因,reward页面出现异常无法正常加载": "Riot原因,reward頁面出現異常無法正常載入",
        '程序启动时间: ': '程式啟動時間: ',
        "接受cookies": "接受cookies",
        "未找到cookies按钮(正常情况)": "未找到cookies按鈕(正常情況)",
        "接受cookies失败": "接受cookies失敗",
        "今日": "今日",
        '通过': '通過',
        '获得': '獲得',
        '于': '於',
        '新的掉落!': '新的掉落!',
        '今日: ': '今日: ',
        '日': '日',
        "未找到奖励标识": "未找到獎勵標識",
        "Twitch: 检查直播间是否在线失败": "Twitch: 檢查直播間是否線上失敗",
        "只看模式已开启,已忽略不看模式配置": "只看模式已開啟,已忽略不看模式配置",
        "最大同时观看数配置错误,已恢复默认值3": "最大同時觀看數配置錯誤,已恢復預設值3",
        "进错直播间,正在重新进入": "進錯直播間,正在重新進入",
        "上午": "上午",
        "下午": "下午",
        "凌晨": "凌晨",
        "写入掉落历史文件失败": "寫入掉落歷史檔案失敗",
        "读取掉落记录失败": "讀取掉落記錄失敗",
        "推送掉落失败": "推送掉落失敗",
        "总掉落文件生成中...": "總掉落檔案生成中...",
        "写入总掉落文件失败": "寫入總掉落檔案失敗",
    }

    def install(self, lang):
        self.language = lang

    def getText(self, text, color):
        """
        A function that formats text with a specified color based on the given language.

        Args:
            text (str): The text to be formatted.
            color (str): The color to format the text with, specified using BBCode format.

        Returns:
            str: The formatted text with the specified color and language.
        """
        rawText = text
        language_map = {
            "zh_CN": f"[{color}]{text}[/{color}]",
            "en_US": f"[{color}]{self.enUSI18n.get(text, f'{rawText} No translation there. Please contact the developer.')}[/{color}]",
            "zh_TW": f"[{color}]{self.zhTWI18n.get(text, rawText)}[/{color}]"
        }
        return language_map.get(self.language, text)

    def getLog(self, text):
        """
        Logs the given text with language support.

        Args:
            text (str): The text to be logged.

        Returns:
            str: The logged text in the specified language, or the original text if translation is not available.
        """
        rawText = text
        language_map = {
            "zh_CN": rawText,
            "en_US": self.enUSI18n.get(text, f"{rawText} No translation there. Please contact the developer."),
            "zh_TW": self.zhTWI18n.get(text, rawText)
        }
        return language_map.get(self.language, text)


parser = argparse.ArgumentParser(
    prog='EsportsHelper.exe', description='EsportsHelper help you to watch matches')
parser.add_argument('-c', '--config', dest="configPath", default="./config.yaml",
                    help='config file path')
args = parser.parse_args()
try:
    with open(args.configPath, "r", encoding='utf-8') as f:
        configFile = yaml.safe_load(f)
    language = configFile.get("language", "zh_CN")
except Exception:
    language = "zh_CN"
    print("Fail: use zh_CN")

i18n = I18n()
i18n.install(language)
