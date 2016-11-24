setwd("/Users/laurabecerra52/Documents/Trabajo final MCPP")
base<-read.csv("BASE.csv")

#Estadisticas descriptivas de la base
summary(base)

#Para ponerle nombres a los puntos
deptos=row.names(base) 
row.names(base) <-base$depto

#Deja solo datos numericos para poder hacer principal components
names<-base[,1]
base<-base[,-c(1)]

#Componentes Principales
pr.out=prcomp(base, scale=TRUE)
#Resultados Componentes principales
pr.out$rotation

#Grafica 1 y 2 componente
biplot(pr.out, scale=0,cex = rep(0.5))

#Porcentaje de la varianza explicado por cada componente
pr.var=pr.out$sdev^2
pr.var
pve=pr.var/sum(pr.var)
pve

plot(pve, xlab="Principal Component", ylab="Proportion of Variance Explained", 
     ylim=c(0,1),type='b')
plot(cumsum(pve), xlab="Principal Component", ylab=" Cumulative Proportion of Variance Explained", 
     ylim=c(0,1), type='b')



#Clusters
km.out=kmeans(base,2,nstart=20)
km.out
km.out$cluster

#esto no funciona porque solo se puede para dos dimensiones
plot(base, col=(km.out$cluster+1), main="K-Means Clustering Results with K=2", 
     xlab="", ylab="", pch=20, cex=2)


#factor analysis
fit <- factanal(x=base, 3, rotation="varimax")
?biplot
