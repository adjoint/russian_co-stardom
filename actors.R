library(igraph)
links2 <- read.csv("edges.csv", header=FALSE, row.names=NULL, sep=",")

newdata <- subset(links2, V1!=V2)

nodes <- read.csv("actors.csv", header=FALSE, row.names=NULL, sep=",")

net <- graph_from_data_frame(vertices=nodes, d=newdata, directed=F) 
#png('my_png1.png', width = 10000, height =10000)
#plot(net, vertex.size=0.25, edge.width=0.5, vertex.label=NA)
#dev.off()
distance_table(net, directed = FALSE)
paths <- c()

for (i in 1:3){
  #print(as.integer(nodes$V1[i]))
  paths[i] = all_shortest_paths(net, from=V(net)[i]) 
}
