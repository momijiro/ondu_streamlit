# ondu_streamlit(2022/11/11 作成中)
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

## streamlitに登録する手順
1. コードを作成
2. streamlitのアカウントを作成
3. streamlit上にコードをアップロードする
4. 発行されるURLをクリックすればいつでも使用できます(ただし、プライバシー保護のため非公開にしてあります)

## 普段の使用方法
1. OND'Uアプリで代表者としてデータを出力

2. streamlitでこのアプリを開いて、出力したファイルをアップロード

![スクリーンショット 2022-11-11 19 11 23](https://user-images.githubusercontent.com/82196701/201318153-ca513370-cce9-46ae-b065-51dd3903472c.png)

3. 記録を出している人一覧の名簿を表示することができる

![スクリーンショット 2022-11-11 19 23 37](https://user-images.githubusercontent.com/82196701/201320489-fc9a94e3-e482-4777-a166-a90cd47f3fe1.png)

4. 出していない人(記録が2週間分揃っていない人)のリストを表示することもできる

![スクリーンショット 2022-11-11 19 24 22](https://user-images.githubusercontent.com/82196701/201320612-08ec3a06-57ff-4030-bb84-1c1cd09201ef.png)

5. 学校に提出するフォーマットとして、Excelファイルを作成することもできる

![スクリーンショット 2022-11-11 19 24 49](https://user-images.githubusercontent.com/82196701/201320705-58a05e57-302f-42c3-9c67-89133ea648fd.png)


　
