# GitHub Copilot Handson コンテンツ

# はじめに
このリポジトリは、GitHub Copilotのハンズオンコンテンツを提供するためのリポジトリです。</br>
Codespacesで利用することを想定しています。

# 利用方法
GitHubの画面上から `Create codespace on main` をクリックしCodespacesを起動してください。

![](assets/image03.png)

# GitHub Copilot Chat開始方法
GitHub Copilot Chatは、左ペインの以下のアイコンをクリックすることで使用可能です。</br>
![image](assets/image04.png)

更に、GitHub Copilot Chatはコード上でInline Chatとしても使用可能です。</br>
行番号をクリック後、表示される黄色の星形のアイコンをクリックし、`Copilotを使用して変更する`をクリックしてください。</br>

![image](assets/image05.png)

![image](assets/image06.png)

Visual Studio 2022やVisual Studio Codeをご利用の場合は行番号をクリック後、表示される黄色の星形のアイコンをクリックしてください。

![image](assets/image07.png)


# ハンズオンコンテンツ
以下のディレクトリにコンテンツを用意しています。</br>
- [ハンズオン: コンソールアプリケーション作成（じゃんけんゲーム）](./handson/README.md)
- [ハンズオン: Web アプリケーション作成（じゃんけんゲーム）](./handson-webapp/README.md)


# GitHub Copilot チートシート
GitHub Copilotの使い方については、以下のチートシートを参照してください。
| 内容 | 操作方法 |
| --- | --- |
| 1行全ての提案を受け入れる | `Tab` キー |
| 提案をスペースごとに受け入れる | `Ctrl` + `→` キー |
| 提案を削除する | `Ctrl` + `←` キー |
| 提案を拒否する | `Esc` キー |
| 次の提案を表示する | `Alt` + `]` キー |
| 前の提案を表示する | `Alt` + `[` キー |
| 提案をまとめて表示する | `Ctrl` + `Enter` キー |

# GitHub Copilot Chat チートシート
GitHub Copilot Chatの使い方については、以下のチートシートを参照してください。
| 内容 | 操作方法 | Chat Window | Inline Chat |
| --- | --- | --- | --- |
| コードの内容を解説させる | /explain | 〇| 〇|
| 修正を提案させる | /fix | 〇| 〇|
| テストコードを提案させる | /tests | 〇| 〇|
| チャットの履歴を消去し、新たな会話を開始する | /clear | 〇| X |
| 使い方を表示する | /help | 〇| 〇|