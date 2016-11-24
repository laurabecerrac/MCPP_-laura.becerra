# Datos grafico
oficinas <- c(672,689,691,701,665)
corresponsales <- c(44,63,91,119,148)
tiempo <- ts(df[, -1], start=2011, end=2015)
#ampliarlo
par(mar=c(5, 4, 4, 6) + 0.1)
#grafico 1 primero
plot(tiempo, oficinas, pch=16, axes=FALSE, ylim=c(600,720), xlab="", ylab="", 
     type="b",col="black", main="transacciones por oficina o corresponsal")
axis(2, ylim=c(0,1),col="black",las=1)  ## las=1 makes horizontal labels
mtext("Oficinas (millones)",side=2,line=2.5)
box()
#segundo eje
par(new=TRUE)
  plot(tiempo, corresponsales, pch=15,  xlab="", ylab="", ylim=c(20,200), 
      axes=FALSE, type="b", col="red")
mtext("Corresponsales (Millones)",side=4,col="red",line=4) 
axis(4, ylim=c(20,200), col="red",col.axis="red",las=1)
axis(1,pretty(range(tiempo),10))
mtext("tiempo",side=1,col="black", line=3)
#leyenda
legend("topleft",legend=c("oficinas","corresponsales bancarios"),
       text.col=c("black","red"),pch=c(16,15),col=c("black","red"))




#uso tecnolog??a
# Datos grafico
par(mar = rep(4, 4))
abonados <- c(46,49,50,55,57)
y <-penetracion <- c(100,105,107,116,119)
x <- barplot(abonados, 
             axes = FALSE,
             col = "blue", 
             xlab = "",
             ylab = "",
             ylim = c(0, 60) )[, 1]
mtext("penetracion %",side=2,line=2.5)
axis(1, at = x, labels = c("2011", "2012", "2013", "2014","2015"))
ats <- c(seq(0, 100, 15), 100); axis(4, at = ats, las = 2)
axis(3, at = x, labels = NA) 
par(new = TRUE)
plot(x = x, y = y, type = "b", col = "red", axes = FALSE, xlab = "", ylab = "")
axis(2, at = c(pretty(penetracion), max(penetracion)), las = 2) 
mtext(text="Numero de abonados y penetracion ", side = 3, line = 1)
box()
