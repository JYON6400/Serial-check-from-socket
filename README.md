## PLCを想定したソケット通信を使用したサーバーアプリ

このプロジェクトは、Pythonのソケット通信を使用してサーバーとクライアント間でデータを送受信するアプリケーションです。製品シリアルを直前の履歴と比較します。

### サーバー側
#### 概要
サーバーは、クライアントからの接続を待機し、データを受信して処理します。クライアントから以下のデータを受信し、<br>
`ライン名,品番,シリアル番号`<br>
ライン名のフォルダ、品番名のCSVファイル、シリアル番号をCSVファイル内に書き込みます。
CSV書き込み前に、CSV内のデータと書き込みデータを比較し、シリアル番号の大きさを比較します。書き込みシリアル＞CSVシリアル＝TUREの場合はCSVへ上書きし、FALSEの場合はエラーを返します。


#### 実行方法
`server.py` スクリプトを実行します。サーバーは指定されたポートで待機し、クライアントからの接続を受け付けます。

#### エスケープ
サーバーが実行されている間、キーボードからのエスケープキーの入力を受け付けます。エスケープキーが押されると、サーバーが終了します。

### クライアント側

#### 概要
サーバ側のデバック用

#### 実行方法
`client.py` スクリプトを実行します。クライアントはサーバーに接続し、データを送信します。

#### データの送信
クライアントは、以下の形式でデータを送信します。
