======================================================================
とにかくシンプルな Twitter クライアント
======================================================================

.. image:: https://raw.github.com/showa-yojyo/twclient/master/documentation/statuses.png
   :alt: タイムライン画面

.. image:: https://raw.github.com/showa-yojyo/twclient/master/documentation/userform-lists.png
   :alt: ユーザー詳細画面/リスト

.. image:: https://raw.github.com/showa-yojyo/twclient/master/documentation/property-list.png
   :alt: ユーザー詳細画面/リスト/プロパティー


Python を利用した習作。他の人は利用できないかもしれない。

Requirements
======================================================================
* Python_: 2.7.3
* PyQt_: GPL v4.9.4 for Python v2.7 (x86)
* `Python Twitter Tools`_: 1.7.2+ (``pip install twitter``)
* Dateutil: 2.1 (``pip install python-dateutil``)

How to Use
======================================================================
アプリの起動は次のように行う。

1. 初回起動のときに限り、テキストファイル ``timelines.ini.sample`` を適宜編集し、
   ファイル名を ``timelines.ini`` に変更して保存する。

2. 好みに応じて ``timelines.ini`` の内容を変更保存する。
   書式は既存の記述を参考にする。

   なお、文字コードが UTF-8 となっていることを確認すること。

2. ``twclient.pyw`` を実行する。

Motivation, Intention, and Specification
======================================================================
当サイト管理人は普段 `Echofon for Windows`_ を利用している。
シンプルで軽く、たいへん気に入っている。
だが下に示すような個人的不満がある。

* ユーザー画面「フォロー」ボタンや「お気に入り」ボタン等を誤クリックしてしまう。
  
  →閲覧専用モードが欲しい。
  むしろ、 **アプリ全体を「読み取り専用」動作だけで再構成する** というのはどうだろうか？
  もう一歩踏み込んで、Twitter アカウントがなくても利用できるクライアントというのは実現できるだろうか。

* 詳細画面のリストタブ内のリスト名をクリックしても、内容がタイムライン画面に展開されない。
  
  →タイムライン画面に展開したい。

* 詳細画面のウィンドウ背景に、現在表示中のユーザーに対応する背景画像が描画されない。
  
  →描画してもよいのではないだろうか。

* Twitter の仕様から生じる制限であり、まったく Echofon の責任ではないのだが、
  「保存した検索」機能の保存件数が少な過ぎる。
  
  →ソフト側で機能を実装したい。

* ステータスの「◯分前」「◯時間前」「◯日前」がうれしくない。

  →ツイート発生時刻で表記したい。

これらを解消するべく、Twitter クライアントを自作してみようと思い立った次第だ。
ちなみに、現在実装済みの機能は次の通り。

* アプリユーザーに Twitter アカウント情報を一切要求しない
* 検索リストを設定ファイルで指定
* 各ステータスのツイート発生時刻による表記 (JST)
* 詳細画面/リストで選択したリストを、コンテキストメニュー経由でメイン画面に表示

実装が難しそうな機能はだいたいわかってきた。

* ロード処理全般では UI を固めないようにすること

  →マルチスレッド化に挑戦した。あとは Loading indicator があると見栄えがよいのだが。

* 画像ファイル関連全般。インターネットからの取得、アイコン画像キャッシュ、表示を固めない、等々

  →ビューウィンドウをすべて ``QTextBrowser`` にしたので、アイコン画像周りはもう心配ないだろう。

License
======================================================================
See the LICENSE file.


.. _Python: http://www.python.org/
.. _Python Twitter Tools: http://mike.verdone.ca/twitter/
.. _PyQt: http://www.riverbankcomputing.co.uk/software/pyqt/intro
.. _Echofon for Windows: http://www.echofon.com/twitter/windows/
