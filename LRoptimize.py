# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:00:26 2020

@author: renli
"""
import numpy as np
import numba as nb

class LogisticRegression:
    
    def __init__(self,learning_rate=1e-4,regularize_rate=1,seed=123456):
        self.learning_rate=learning_rate
        self.regularize_rate=regularize_rate
        self.seed=seed
    
    def sigmoid(self,X,theta):
        return 1/(1+np.exp(-np.matmul(X,theta)))
    
    def add_const(self,X):
        #to add intercept term in the regression, please manually add const column first
        I=np.ones((X.shape[0],1))
        return np.hstack((X,I))
    
    def cost_fcn(self,y,X,theta):
        I=np.ones(y.shape)
        return (
            np.matmul(-y.T,np.log(self.sigmoid(X,theta)))-
                                  np.matmul((I-y).T,
                                            np.log(I-self.sigmoid(X,theta)))
            )
    def fit_0(self,y,X):
        #original logistic regression
        from sklearn.linear_model import LogisticRegression
        model=LogisticRegression(penalty='none',fit_intercept=False)
        model.fit(X,y.reshape((-1,)))
        self.theta=model.coef_.T
        
    # def fit_1(self,y,X,max_iter=10000):
    #     #non-negative constraints
    #     self.theta=np.abs(np.random.randn(X.shape[1],1))
    #     np.random.seed(self.seed)
    #     lambda_=np.zeros(self.theta.shape)
    #     pre_cost=self.cost_fcn(y,X,self.theta)
    #     self.cost_record=np.zeros((max_iter,))
    #     for iter_ in range(max_iter):
    #         delta_theta=np.matmul(X.T,self.sigmoid(X,self.theta)-y)-lambda_
    #         self.theta=self.theta-self.learning_rate*delta_theta
    #         theta=self.theta
    #         cost=self.cost_fcn(y,X,self.theta)
    #         self.cost_record[iter_]=cost
    #         cost_movement=cost-pre_cost
    #         if np.abs(cost_movement)<1e-8:
    #             print('converged within iter({}).'.format(iter_))
    #             break
    #         pre_cost=cost
    #         delta_lambda_=self.theta
    #         lambda_=np.max(np.hstack((np.zeros(lambda_.shape),lambda_-self.regularize_rate*delta_lambda_)),
    #                         axis=1,keepdims=True)#to check np.max
    
    def fit_1(self,y,X,max_iter=10000):
        #non-negative constraints
        self.theta=np.abs(np.random.randn(X.shape[1],1))
        np.random.seed(self.seed)
        def lambda_(theta,delta_theta):
            res=(~((theta>=0) | (delta_theta<0))).astype(int)
            epsilon=1e-4 #define the speed of theta to restore to positive
            res=res*(delta_theta+epsilon)
            return res
            
        pre_cost=self.cost_fcn(y,X,self.theta)
        self.cost_record=np.zeros((max_iter,))
        for iter_ in range(max_iter):
            delta_theta=np.matmul(X.T,self.sigmoid(X,self.theta)-y)
            delta_theta=delta_theta-lambda_(self.theta,delta_theta)
            self.theta=self.theta-self.learning_rate*delta_theta
            theta=self.theta
            cost=self.cost_fcn(y,X,self.theta)
            self.cost_record[iter_]=cost
            cost_movement=cost-pre_cost
            if np.abs(cost_movement)<1e-8:
                print('converged within iter({}).'.format(iter_))
                break
            pre_cost=cost
            
            
    def fit_2(self,y,X,max_iter=10000):
        #rank-preserved constraints
        self.theta=np.abs(np.random.randn(X.shape[1],1))
        pre_cost=self.cost_fcn(y,X,self.theta)
        self.cost_record=np.zeros((max_iter,))
        for iter_ in range(max_iter):
            delta_theta=np.matmul(X.T,self.sigmoid(X,self.theta)-y)
            self.theta=self.theta-self.learning_rate*delta_theta
            for i in range(1,self.theta.shape[0]):
                if self.theta[i,0]>self.theta[i-1,0]:
                    self.theta[i,0]=self.theta[i-1,0]
            cost=self.cost_fcn(y,X,self.theta)
            self.cost_record[iter_]=cost
            cost_movement=cost-pre_cost
            if np.abs(cost_movement)<1e-8:
                print('converged within iter({}).'.format(iter_))
                break
            pre_cost=cost
            
    def predict(self,X,threshold=0.5):
        prob = self.sigmoid(X,self.theta)
        pred_y=(prob>=threshold).astype(int)
        return pred_y
    
    def score(self,y,X,metrics='confusion_matrix'):
        from sklearn.metrics import roc_auc_score
        from sklearn.metrics import roc_curve
        from sklearn.metrics import confusion_matrix
        import pandas as pd
        import seaborn as sns
        #mesure score
        pred_y=self.predict(X)
        if metrics=='confusion_matrix':
            conf_mat = pd.DataFrame(confusion_matrix(y,pred_y))
            sns.heatmap(conf_mat,annot=True)
            return conf_mat
        elif metrics=='roc_auc_score':
            fpr,tpr,thresholds=roc_curve(y,pred_y)
            plot_df=pd.DataFrame()
            plot_df['fpr']=fpr
            plot_df['tpr']=tpr
            sns.lineplot(x='fpr',y='tpr',data=plot_df)
            return roc_auc_score(y,pred_y)
        
def sigmoid(X,theta):
    return 1/(1+np.exp(-np.matmul(X,theta)))

def create_df(sample_num,theta,error_std=1,seed=123456):
    #simulate data
    theta=np.array(theta).reshape((-1,1))
    np.random.seed(seed)
    X=np.random.randn(sample_num,theta.shape[0])
    error=error_std*np.random.randn(sample_num,1)
    theta_err=np.vstack((theta,[[1]]))
    X_err=np.hstack((X,error))
    prob=sigmoid(X_err,theta_err)
    threshold=0.5
    y=(prob>=0.5).astype(int)
    return X,y
    
if __name__=="__main__":
    import matplotlib.pyplot as plt
    X,y=create_df(10000,[3,4,-2],1)
    model=LogisticRegression()
    model.fit_1(y,X)
    conf_mat=model.score(y,X,metrics='confusion_matrix')
    theta=model.theta
    plt.show()
    plt.plot(np.trim_zeros(model.cost_record))
    plt.show()