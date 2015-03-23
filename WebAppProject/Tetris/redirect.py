def redirect(s):
    pages = {'index':0,'play':0,'game':0,'about':0,'userpage':0,'daily':0,'chalenge':0,'leaderboard':0}
    k = pages.keys()
    for i in s:
        for u in k:
            if pages[u] < len(u):
                if i == u[pages[u]]:
                    pages[u] += 1
    for u in k:
        pages[u] = (1.0*pages[u])/len(u)
    pages['404'] = 0.5
    m = '404'
    for u in k:
        if pages[u] > pages[m]:
            m = u
    print m
