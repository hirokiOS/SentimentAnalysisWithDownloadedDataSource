# SentimentAnalysisWithDownloadedDataSource

Sentiment score fine-tuning for Hugging-face model. 
https://huggingface.co/ProsusAI/finbert

The BERT model based on Hagging face, and classifies the sentence into three levels. 
Data source path for this particular model must be instructed from the Author

The notebook is modifed based on the contents of book chapter 5 of the following book. 

大規模言語モデル入門, 2023年7月29日, 山田育矢　監修／著，鈴木正敏，山田康輔，李凌寒　著

Feel free to contact me via E-mail to my affiliation E-mail, or hirokifujii10@gmail.com

# 各ファイルの説明
次の３つのファイルは、上記の参考文献の書籍第5章、1-3節をベースとして開発されています。
Google Colab上での運用を想定していますが、ローカルでの運用の場合には、コード中でGoogle driveを指定している箇所について、それぞれ適切なパスの指定をお願い致します。
スクリプトのベースは東北大学のモデルとWrimeデータセットをベースに書かれていましたが、
以下ではAccernデータセットでの活用にフォーカスします。API,URL情報を入力して、通して実行して理解を深めてみてください。

### 1_original_accern_parse.ipynb
APIを経由したダウンロードと、データをファインチューニング用に加工した状態でのGoogle driveへの保存に対応しています。
2, 3においてAPI経由でダウンロードしたデータを活用して実行する場合は、このステップは不要です。
実施した加工については、acc_function中のConvertDfToHFData.pyをご参照ください。

Event_sentimentをベースとしたNeutral/Negative/Positiveの決定には, 閾値の設定が要求されます。

### 2-sentiment-analysis-finetunign-finbert.ipynb
APIを経由してダウンロードしたデータセットでprosusAI/finbertのモデルをファインチューンします。
ProsusAI/finbertの、Positive/Neutral/Negativeの感情分析結果が、利用したデータソースにおける感情を正解ラベルとし、これに近づくようにファインチューニングが行われます。

PrususAI/Finbert : https://huggingface.co/ProsusAI/finbert


### 3-sentiment-error-analysis-finbert.ipynb
学習したモデルを用いた感情分析の出力と、真のデータセットと比較した混合行列の作成、センチメントの異なるテキストの例示を行います。

# 活用方法
## APIの入力
API経由でデータを活用する場合には、必要箇所にAPIおよびURLをご記入ください。
デフォルトでは、以下のようになっています。取得したAPIおよびURLをオンラインに公開しないよう注意してください。
```
    accern_api_url = '< Vender provided URL should come here >'
    accern_token_url = '< Vendor provided token should come here >'
```

## Google colabでの運用方法
GPU理環境の環境統一を鑑みて、Google Colab上での運用を想定しています。ファイルの保存にはGoogle driveが必要で、そのためにはGoogleアカウントが必要であることにご留意ください。LLMファイルは大きいため、新規の作成を推奨いたします。
Github上の各ノートブックのページ、ノートブック中のセルのリンク先において、以下をクリックすることでGoogle colabのページに直接アクセスできます。
![img4](https://github.com/hirokiOS/SentimentAnalysisWithDownloadedDataSource/assets/149484706/a73a0461-d2c2-465c-bccd-095e0d2aa65f)

ローカルでダウンロードした本ソースコードをGoogle colab上にアップロードして運用する場合には、
https://colab.research.google.com/ のページより、ファイル-> ノートブックをアップロードからアップロードしての実行が可能です。
<img width="1165" alt="img1" src="https://github.com/hirokiOS/SentimentAnalysisWithDownloadedDataSource/assets/149484706/9a160176-d49f-4117-864e-46066d4d8561">

Jupyter notebookのColabへのアップロードに関するブログ記事などを併せて参考にしてください。

Python プログラミング入門 - 1-0. Colaboratory (Colab) の使い方 - https://utokyo-ipp.github.io/1/1-0.html


## 実行ランタイムのタイプを選択 

Google colabでは2023年11月現在ランタイムとしてGPU環境が提供されています。ランタイムのタイプを変更より、GPUを選択してください。テキストファイルの自然言語モデルへの読み込みやトレーニング時間について大きな差が出ます。

無料版での使用環境では、連続使用時間の上限、90分間アクセスがない場合に接続が切れるなどの制限があります。
使用環境にについては予告なく変更される可能性があります。

<img width="697" alt="img2" src="https://github.com/hirokiOS/SentimentAnalysisWithDownloadedDataSource/assets/149484706/b0a0c234-1913-4944-aed2-87b5d2ca6fef">
<img width="774" alt="img3" src="https://github.com/hirokiOS/SentimentAnalysisWithDownloadedDataSource/assets/149484706/fefe4cc2-ac8e-49ce-b86e-8f04717aa0e6">



## ユーザー定義モジュール(acc_function下)のファイルのインポート
ノートブック中では, 本Githubのソースコードをモジュールとして参照しています。(Notebook 1, 2中の以下の部分)  
```
    giturl1 = 'https://raw.githubusercontent.com/hirokiOS/SentimentAnalysisWithDownloadedDataSource/main/acc_function/ACCDFConcatenator.py'
    giturl2 = 'https://raw.githubusercontent.com/hirokiOS/SentimentAnalysisWithDownloadedDataSource/main/acc_function/ConvertDfToHFData.py'
```

上リンク先のGithubページが予告なく削除された場合は、acc_function下の関数を適切なディレクトリ下に配置してモジュールとしてインストールするか、ご自身でGithubなどにアップロードして新たにリンクしていただければと存じます。


