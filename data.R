
library(snow)

data=read.csv('KAGGLE_NO_ZEROS_TRAIN.csv')
data$id=paste0(data$store_nbr,"_",data$item_nbr)

data_k=data[,c('id','date','units')]


k=3
ind=sample(1:nrow(data_k),1000)
test=data_k[ind,]
train=data_k[-ind,]


calc_dist=function(y,x)
{
  x=strptime(x,'%Y-%m-%d')
  y=strptime(y,'%Y-%m-%d')
  
  return (difftime(y,x,units="days"))
  
}

par_test=function(x)
{
  
  dis=sapply(train[train$id==x['id'],'date'],calc_dist,x['date'])
  
  dis1=data.frame(units=train[train$id==x['id'],'units'],dist=dis)
  colnames(dis1)=c('units','dist')
  dis1=dis1[order(-dis1$dist),'units'][1:k]
  return (mean(dis1))
}

dist=apply(test,1,par_test)
head(dist)
head(test)
