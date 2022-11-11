# ondu_streamlit
Panasonic社製アプリ「OND'U(おんどゆー)」を自動整形するプログラムを、Streamlitで実装したものです。 

## バージョンについて
(以下は作成した日付です。実際にコミットしたのは2022年11月以降になります)

- 2021/10/4  1.0 ipynbで実行用
- 2021/11/11 1.1 
- 2021/11/18 1.2 
- 2022/05/06 2.0 streamlitで実行
- 2022/05/08 2.1 
- 2022/05/08 2.2
- 2022/05/10 2.3   


## 背景
2019年12月〜2021年11月まで自分が運営していたサークルで用いるために作成したものです。
新型コロナウイルスの感染症対策として、大学の規定上、練習参加者全員の直近2週間の体温記録を毎回顧問の先生に送るという業務がありました。
効率化のため、体温記録用Panasonic社製アプリ「OND'U(おんどゆー)」を導入しました。このアプリは、各メンバーが自分の体温を登録し、それを運営者が集計できる仕様となっています。
しかし、このアプリででの出力は大学側で必要なフォーマットと異なる点や、サークルメンバーへの体温記録確認の連絡の際のプライバシーを管理する必要がある点など、このアプリだけでは不十分な点があります。（時間をかければ解決できますが、週２回この業務をやるには時間的コストがかかります）

## 概要まとめ
そのため、streamlitを用いて、OND'Uでの出力を自動で整形し出力するアプリを作成しました。
