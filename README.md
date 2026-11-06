# asset-samples — フリー素材サンプル集

AI生成画像とプロシージャル生成3Dモデルのフリー素材サンプル集です。検証・制作のたたき台として自由に使えます。

## 内容

| フォルダ | 内容 | 点数 |
|---|---|---|
| `images/backgrounds/` | 背景素材（風景・都市・抽象） | 8 |
| `images/note-illust/` | note記事挿絵風ビジネスイラスト（濃紺×金×クリーム） | 8 |
| `images/textures/` | テクスチャ・パターン素材 | 8 |
| `images/mv-scenes/` | MV風シネマティック背景 | 8 |
| `images/shoga-chan/` | しょうがちゃん バリエーション（ポーズ・衣装・季節） | 12 |
| `images/yakumi/` | やくみ組 イラスト | 10 |
| `images/shoga-chan-vol2/` | しょうがちゃん バリエーション第2弾（温泉・探検・宇宙服ほか） | 12 |
| `images/yakumi-vol2/` | やくみ組 イラスト第2弾（温泉旅行・運動会ほか） | 10 |
| `images/backgrounds-vol2/` | 背景素材 第2弾 | 8 |
| `models3d/props/` | ローポリ小道具 GLB 12点（trimeshでプロシージャル生成、生成スクリプト同梱） | 12 |
| `models3d/ginger-renders/` | しょうが（Ginger）モデルの6アングルレンダー | 6 |

## キャラクターと原典について

- 「しょうがちゃん」「やくみ組」は、3Dモデル集 [Cosm0rder/yakumigumi-3d-models](https://github.com/Cosm0rder/yakumigumi-3d-models) のキャラクターです。原典の3Dモデル・テクスチャは **CC0 1.0 Universal** で公開されています（商用利用・改変・再配布可、クレジット不要）。
- `images/shoga-chan/` と `images/yakumi/` は、その公式プレビュー画像を参照して生成AIで作成した二次的なイラストサンプルです。原典モデルのライセンス（CC0）とは別物として扱ってください。
- `models3d/ginger-renders/` は原典CC0モデルのGLBをレンダリングした画像です。原典モデル自体の利用条件は原典リポジトリのLICENSEに従います。

## 利用条件

- 本リポジトリの生成画像と `models3d/props/` の3Dモデルは、フリー素材として提供します。商用・非商用を問わず、改変・再配布を含めて自由に使えます。クレジット表記は不要です（原典リポジトリへのリンクは歓迎します）。
- 注意（要確認）: 生成画像はAI生成物です。AI生成物の権利関係の扱いは法域・用途によって異なる場合があります。権利関係が重要な用途では、利用者側で確認してください。また、画像の内容の正確性・特定用途への適合性は保証しません。
- 実在の人物・企業ロゴ・商標は含まないよう生成していますが、万一類似が気になる場合は利用を避けてください。

## 生成方法

- 画像: Codex CLI の imagegen で生成（2026-11-06）。
- 3D小道具: Python + trimesh によるプロシージャル生成（`models3d/props/gen_props.py`）。
- Gingerレンダー: 原典GLBを trimesh で読み込み、matplotlib で描画。
