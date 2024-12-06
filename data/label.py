import os
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

# ���� train_label.csv �ļ���·��
csv_path = '/home/visllm/program/plant/plant_dataset/val/val_label.csv'  # ���滻Ϊ����ʵ��·��

# ��ȡ CSV �ļ�
df = pd.read_csv(csv_path)
print('ԭʼ���ݿ�')
print(df.head())

# �����������
classes = [
    'scab', 'healthy', 'frog_eye_leaf_spot', 'rust', 'complex',
    'powdery_mildew'
]


# ���庯��������ǩ�ַ������Ϊ�б�
def split_labels(label_str):
    # �Կո�Ϊ�ָ�����ֱ�ǩ
    return label_str.split()


# Ӧ�ú���������һ���µ��У�������ǩ�б�
df['labels_list'] = df['labels'].apply(split_labels)

print('\n���������ݿ�')
print(df.head())

# ʹ�� MultiLabelBinarizer ���� One-Hot ����
mlb = MultiLabelBinarizer(classes=classes)

# ��ϲ�ת����ǩ�б�
labels_one_hot = mlb.fit_transform(df['labels_list'])

# �����ת���� DataFrame�����ڲ鿴
labels_one_hot_df = pd.DataFrame(labels_one_hot, columns=mlb.classes_)

print('\nOne-Hot ����ı�ǩ��')
print(labels_one_hot_df.head())

# ��ͼƬ���ƺͱ����ı�ǩ�ϲ�
final_df = pd.concat([df['images'], labels_one_hot_df], axis=1)

print('\n���յ����ݿ�')
print(final_df.head())

# �����Ҫ�����Խ����������ݱ��浽�µ� CSV �ļ�
final_df.to_csv('processed_val_labels.csv', index=False)
