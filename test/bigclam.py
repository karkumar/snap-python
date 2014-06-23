#
#   BigClam method for community detection
#
import sys
import snap


def bigClam(outFPrx = "", inFnm = "../as20Graph.txt", labelFNm="", optComs =100, minComs =5, maxComs =100, divComs =10, numThreads =4, stepAlpha =0.5, stepBeta = 0.5):

    print "Hello WOrld!"
    G = snap.LoadEdgeList(snap.PUNGraph, "data/coocurence_graph.txt", 0, 1)
    print "G: Nodes %d, Edges %d" % (G.GetNodes(), G.GetEdges())
    estCmtVV = snap.TIntVV()
    RAGM = snap.TAGMFast(G, 10, 10)

    optcoms = -1 
    if(optcoms == -1):
        print "finding number of communities \n"
        optcoms = RAGM.FindComsByCV(numThreads, maxComs, minComs, divComs, outFPrx, stepAlpha, stepBeta) 

    RAGM.NeighborComInit(optcoms)
    if(numThreads ==1 or G.GetEdges() <1000):
        RAGM.MLEGradAscent(0.0001, 1000 * G.GetNodes(), "", stepAlpha, stepBeta)
    else:
        RAGM.MLEGradAscentParallel(0.0001, 1000, numThreads, "", stepAlpha, stepBeta)

    RAGM.GetCmtyVV(estCmtVV)
    snap.DumpCmtyVV(OutFPrx+"cmtyvv.txt", estCmtVV, nidNameH)
    snap.SaveGephi(OutFPrx + "graph.gexf", G, EstCmtyVV, 1.5, 1.5, NIDNameH)


if __name__ == '__main__':

    
    # Parameters. 
    # o - Output Graph Data Prefix. 
    # i - Input edgelist file name. 
    # l - Input file name for node names (NodeID, Node label)
    # c - The number of communites , -1: detect automatically
    # mc - Minimum number of communities to try 
    # xc - Maximum number of communites to try 
    # nc - How many trials for the number of communities
    # nt - Number fo threads for parallelization 
    # sa - Alpha for backtracking line search 
    # sb - Beta for backtracking line search 
    
    outFPrx = ""
    inFNm  = "../as20Graph.txt"
    labelFNm = ""
    optComs = 100
    minComs =  5
    maxComs = 100
    divComs =10
    numThreads = 4
    stepAlpha = 0.5
    stepBeta =0.5

    bigClam()

    


