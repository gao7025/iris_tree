# -*- coding: utf-8 -*-
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics
from sklearn.metrics import classification_report


class TreeModel:
    def __int__(self):
        pass

    @staticmethod
    def load_data():
        iris = datasets.load_iris()
        iris_features = iris.data
        iris_target = iris.target
        feature_name = iris.feature_names
        train_x, test_x, train_y, test_y = train_test_split(iris_features,
                                                            iris_target,
                                                            test_size=0.3,
                                                            random_state=123)
        # print(pd.DataFrame(iris_features).corr())
        return train_x, test_x, train_y, test_y, feature_name

    def train_test_model(self):
        train_x, test_x, train_y, test_y, feature_name = self.load_data()
        model = tree.DecisionTreeClassifier(criterion='gini')
        model.fit(train_x, train_y)
        model.score(train_x, train_y)
        y_pre = model.predict(test_x)
        tree_matrix = metrics.confusion_matrix(test_y, y_pre)
        print('混淆矩阵：\n', tree_matrix)
        print('结果分类报告：\n', classification_report(test_y, y_pre))
        # print('准确率：{:.2%}'.format(metrics.accuracy_score(test_y, y_pre)))

        # 特征重要性
        # model.feature_importances_
        feature_important = pd.DataFrame([*zip(feature_name, model.feature_importances_)],
                                         columns=['features', 'Gini importance'])
        print('特征重要度：\n', feature_important.sort_values(by='Gini importance'))
        return model

    @staticmethod
    def plot_tree():
        model = self.train_test_model()
        feature_name = ['sepal length', 'sepal width', 'petal length', 'petal width']
        import graphviz
        dot_data = tree.export_graphviz(model,
                                        out_file=None,
                                        feature_names=feature_name,
                                        class_names=['setosa', 'versicolor', 'virginica'],
                                        filled=True,
                                        rounded=True
                                        )
        graph = graphviz.Source(dot_data)
        graph


if __name__ == '__main__':
    TreeModel().train_test_model()
