# !/usr/bin/python
# coding=utf-8
import sys,getopt
from abLog import logger
from pressurer import Pressurer
from show import Show


'''
程序的入口函数，根据可选参数情况执行相应命令
并定义了一个全局的logger用于调试
'''
VERSION = 0.0


def ab(opts, http):
    #opts,args = getopt.getopt(sys.argv[1:], "A:C:c:d:n:eghHip:qsSv:Vwx:X:y:z:")
    logger.debug(u'ab被调用')
    for key in opts:
        logger.debug(key)
    if opts.get('-h')!=None:
        logger.debug(u'显示帮助信息')
        from data.help import helpDict
        for key in helpDict:
            print '%s   %s' % (key,helpDict[key])
    if opts.get('-V')!=None:
        logger.debug(u'请求版本号')
        print u'VERSION: %.1f' % VERSION
    optsDict = dict(opts)
    logger.debug(optsDict)
    opts = dict(opts)
    url=http
    userCount = opts.get('-c',1)
    visitCount=opts.get('-n',1)
    userAgent=opts.get('-H',"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-Us) AppleWeb Kit/534.2 (KHTML, like Gecko) Chrome/6.0.447.0 Safari/534.2")
    outhString=opts.get('-A',None)
    cookie=opts.get('-C',None)
    postData=None
    proxy=None
    if opts.get('-p')!=None:
        method='POST'
        postData=opts.get('-p',None)
    elif opts.get('-i')!=None:
        method='HEAD'
    else:
        method='GET'
    if opts.get('-s')!=None:
        protocal='https'
    else:
        protocal = 'http'
    if opts.get('-x')!=None:
        proxy=opts.get('-X',None)
    else:
        pass

    parDict={}
    parDict['url']=url
    parDict['userCount']=int(userCount)
    parDict['visitCount']=int(visitCount)
    parDict['userAgent']=userAgent
    parDict['outhString']=outhString
    parDict['cookie']=cookie
    parDict['method']=method
    parDict['postData']=postData
    parDict['protocal']=protocal
    parDict['proxy']=proxy
    pressurer=Pressurer(**parDict)
    resault=pressurer.getCondition()


    #上面的resault为获得的结果，下面处理展示部分

    show=Show(resault)

    fileName =""
    def createNameFor(suffix):
        import datetime
        return ('%s_user_%s_visit_host_%s_%s.%s'%(userCount,visitCount,url,datetime.datetime.now(),suffix)).replace(' ','_')
        pass
    if opts.get('-w')!=None:
        fileName=createNameFor('html')
        print u'Create file %s'%fileName
        show.outToHTML(fileName)
    if opts.get('-g')!=None:
        fileName=createNameFor('TSV')
        print u'Create file %s'%fileName
        show.outToTSV(fileName)
    if opts.get('-e')!=None:
        fileName=createNameFor('csv')
        print u'Create file %s'%fileName
        show.outToCSV(fileName)
    return show.outToStdout()


def tran_command(command):
    dic = {}
    temp = command.split(' ')
    result = []
    http=""
    for i in range(0,temp.__len__()):
        if temp[i]!=' ' and temp[i].__len__()!=0:
            result.append(temp[i])

    for i in range(0, result.__len__()):
        if(result[i]=="-h" or result[i]=="-v" or result[i]=="-H" or result[i]=="-V"):
            dic[temp[i]]=''

        if(result[i]=="-c" or result[i]=="-n" or result[i]=="-C" or result[i]=="-N"):
            dic[result[i]] = result[i+1]
            i=i+1

        if(result[i]=="-e" or result[i]=="-E"):
            http = result[i+1]
            dic[result[i]] = result[i + 1]
            i=i+1
    return ab(dic, http)