# coding:utf-8
import numpy as np
import link

num_iter = 100
num_candidates = 100 #output 100 url
def Rank(urls):
    alpha = 0.85
    
    G = link.linkDic(urls)
    M, node2index, index2node = Generate_Transfer_Matrix(G)
    result = PageRank(M, alpha, urls[0], node2index, index2node)
    #print(result)
    return result

def PageRank(M, alpha, root, node2index, index2node):
    """
    Personal Rank in matrix formation
    :param M: transfer probability matrix
    :param index2node: index2node dictionary
    :param node2index: node2index dictionary
    :return:type of list of tuple, ex.
    [(node1, prob1),(node2, prob2),...]
    """
    result = []
    n = len(M)
    v = np.zeros(n)
    #print(node2index[root])
    v[node2index[root]] = 1
    while np.sum(abs(v - (alpha*np.matmul(M,v) + (1-alpha)*v))) > 0.0001:
        v = alpha * np.matmul(M, v) + (1-alpha)*v
    for ind, prob in enumerate(v):
        result.append((index2node[ind], prob))
    result = sorted(result, key=lambda x:x[1], reverse=True)[:num_candidates]
    return result

def Generate_Transfer_Matrix(G):
    """generate transfer matrix given graph"""
    index2node = dict()
    node2index = dict()
    for index,node in enumerate(G.keys()):
        node2index[node] = index
        index2node[index] = node
    # num of nodes
    n = len(node2index)
    # generate Transfer probability matrix M, shape of (n,n)
    M = np.zeros([n,n])
    for node1 in G.keys():
        for node2 in G[node1]:
            # FIXME: some nodes not in the Graphs.keys, may incur some errors
            try:
                M[node2index[node2],node2index[node1]] = 1/len(G[node1])
            except:
                continue
    return M, node2index, index2node


if __name__ == '__main__':
    urls = ["http://www.sdust.edu.cn/", "http://xy.sdust.edu.cn/", "http://xy.sdust.edu.cn/index.php?m=Index&a=articlelist&cate_id=16",
    "http://xy.sdust.edu.cn/index.php?m=Index&a=article&id=2235"]
    url = Rank(urls)
    for each in url:
        print(each)