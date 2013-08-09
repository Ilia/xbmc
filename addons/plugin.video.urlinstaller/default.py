import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os
import datetime
import time

ADDON = xbmcaddon.Addon(id='plugin.video.urlinstaller')



def CATEGORIES():
    dialog = xbmcgui.Dialog()
    import time
    url      =  SEARCH()
    path         =  xbmc.translatePath(os.path.join('special://home/addons','packages'))
    lib          =  os.path.join(path, 'my_url_installer.zip')
    addonfolder  =  xbmc.translatePath(os.path.join('special://home/addons',''))
    
    DownloaderClass(url,lib)
    time.sleep(3)
    xbmc.executebuiltin("XBMC.Extract(%s,%s)" %(lib,addonfolder))
    dialog.ok("URl Installer", "All Done","Next Time You Reboot Will Take Effect", "[COLOR yellow]Brought To You By XBMCHUB.COM[/COLOR]")
	        
def SEARCH():
        search_entered = 'http://is.gd/'
        keyboard = xbmc.Keyboard(search_entered, 'Please Enter Url For Install')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText() .replace(' ','%20')  # sometimes you need to replace spaces with + or %20
            if search_entered == None:
                return False          
        return search_entered    
 
def OPEN_URL(url):
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib2.urlopen( req )
    link= con.read()
    return link
    
    
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("URL Installer","Downloading & Copying File",'')
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        raise Exception("Canceled")
        dp.close()
    
    
    
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

        
               
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
   
        
#these are the modes which tells the plugin where to go
if mode==None or url==None or len(url)<1:
        CATEGORIES()
       
       
xbmcplugin.endOfDirectory(int(sys.argv[1]))
