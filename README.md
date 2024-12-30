# ����ָ��

SYSU 2024������ѧ�ڼ�����Ӿ���ҵ
���ڶ�����������ǩArcFaceLoss��Plant Pathology-2021��������������ӻ�

## ��������


### ��װ����

���Լ�������Ŀ¼��

```bash
git clone https://github.com/Chen1un17/ArcFace_PSA_SwinTransformer.git
conda create -n vis python=3.8
conda activate vis
pip install -r requirements.txt
```

### ·������

��`evaluate.py`��`train.py`�ж���`data_dir`��·�����ã���Ҫ�����Լ���·���������þ���·��������������

### ���в���

1. ѵ��ģ��
����Ŀ��Ŀ¼�������������ʼѵ����
���Ҫʹ�ü�ǿ���ģ�ͣ���Ҫ��`check_dir`��·����Ϊ`checkpoints_enhanced/best_model.pth`

```bash
python src/main.py --mode train

```

ѵ�������У����ģ�ͽ������� `checkpoints/best_model.pth`

2. ����ģ��

ѵ����ɺ�ʹ��������������֤��������ģ�����ܣ�

```bash

python src/main.py --mode evaluate

```

3. ����ģ��

��`evaluate.py`��val_csv��val_images��������Ϊ����

```python

    val_csv = os.path.join(data_dir, 'processed_test_labels.csv')
    val_images = os.path.join(data_dir, 'test', 'images')

```

����ʹ�ò��Լ�����ģ��

4. ���ӻ�ģ�;���

���п��ӻ��ű������� Grad-CAM ���ӻ������

��EfficientNet���п��ӻ�

```bash

python src/visualize.py

```

��EVA-CLIP���п��ӻ�

```bash

python src/attentionvis.py

```

��ArcPSASwinTransformer���п��ӻ�
```bash
python src/arcvis.py
```

���ɵĿ��ӻ� GIF �ļ��������� `outputs/example.gif`

Ч����
![alt text](example.gif)
![alt text](gifs/95cd695ad68c78a4.gif)
![alt text](Swin.png)
![alt text](SwinCheck.png)