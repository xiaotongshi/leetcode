import matplotlib.pyplot as plt

def roc_auc(preds, labels):
    db = list(zip(preds, labels))
    rank = [label for pred, label in sorted(db, key=lambda x: x[0], reverse=True)] #按照score降序排列
    real_P = sum(labels) # real label is positive
    real_N = len(labels) - real_P # real label is negative

    #计算ROC坐标点
    xy_arr = []
    tp, fp = 0, 0			
    for i in range(len(rank)):
        if rank[i] == 1:
            tp += 1
        else:
            fp += 1
        xy_arr.append([fp/real_N,tp/real_P])

    #计算曲线下面积
    auc = 0			
    prev_x = 0
    for x,y in xy_arr:
        if x != prev_x:
            auc += (x - prev_x) * y
            prev_x = x

    print("the auc is %s."%auc)

    # 计算loss
    p = []
    n = []
    loss = 0
    for i in range(len(preds)):
        if labels[i] == 1:
            p.append(preds[i])
        else:
            n.append(preds[i])
    for i in range(len(p)):
        for j in range(len(n)):
            if n[j] > p[i]:
                loss += 1
            elif n[j] == p[i]:
                loss += 0.5
    auc = 1 - loss/(len(p)*len(n))
    print("the auc is %s."%auc)

    # 用排序误差计算
    accumulated_neg = 0
    rank_loss = 0
    for i in range(len(rank)):
        if rank[i] == 1:
            rank_loss += accumulated_neg # 目前有多少个负样本分数大于正样本
        else:
            accumulated_neg += 1
    rank_loss /= (real_P*real_N)
    auc = 1 - rank_loss
    print("the auc is %s."%auc)
    
    # x = [_v[0] for _v in xy_arr]
    # y = [_v[1] for _v in xy_arr]
    # plt.title("ROC curve of %s (AUC = %.4f)" % ('svm',auc))
    # plt.xlabel("False Positive Rate")
    # plt.ylabel("True Positive Rate")
    # plt.plot(x, y)# use pylab to plot x and y
    # plt.show()# show the plot on the screen


# preds = [0.9, 0.4, 0.3, 0.2, 0.6, 0.5]
# labels = [1, 1, 0, 0, 1, 0]
preds = [0.9, 0.7, 0.6, 0.55, 0.52, 0.4, 0.38, 0.35, 0.31, 0.1]
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
roc_auc(preds, labels)