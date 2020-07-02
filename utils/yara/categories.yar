/*
  Esse arquivo são de regras para categoizar os sites.
*/

rule Search_Engine
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Search Engine"
        score = 10
    
    strings:
        $a = "search engine"
        $b = "search"
        $c = "searches"       
    condition:
        all of them
}

rule FTP
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria FTP"
        score = 20
    
    strings:
        $a = "access"
        $b = "user"
        $c = "group"
        $d = "date"
        $e = "size"
        $f = "name"
        $g = "<dir>"
        
    condition:
        all of them
}

rule Streaming
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Streaming"
        score = 10
    
    strings:
        $a = "tv series"
        $b = "video"
        $c = "music"
        $d = "play"
        $e = "player"
        $f = "audiobook"
        $g = "book"
        $h = "discover"
        $i = "upload"
        $j = "categories"
        $k = "browse"
        
    condition:
        5 of them
}

rule Login_Page
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Login Page"
        score = 5
    
    strings:
        $a = "username"
        $b = "password"
        $c = "login"
        $d = "remember me"
        $e = "forgotten password"
        
    condition:
        4 of them
}

rule Russian_Site
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Russian Site"
        score = 10
    
    strings:
        $a = "б"
        $b = "и"
        $c = "ч"
        $d = "й"
        $e = "ж"
        $f = "э"
        
    condition:
        all of them
}

rule Antibot
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Antibot"
        score = 5
    
    strings:
        $a = "anti-bot defence"
        $b = "spam security"
        $c = "anti-flood"
        
    condition:
        1 of them
}

rule Communications
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Communications"
        score = 30
    
    strings:
        $a = "forum"
        $b = "press"
        $c = "chat"
        $d = "hidden answers"
        $e = "discussion"
        $f = "mailbox"
        $g = "e-mail service"
        $h = "webmail"
        
    condition:
        3 of them
}

rule Libraries_Wikis
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Libraries Wikis"
        score = 30
    
    strings:
        $a = "find information"
        $b = "onion directory"
        $c = "hidden services"
        $d = "deep web e-mail services"
        $e = "deep web marketplaces"
        $f = "mailbox"
        $g = "deep web link directory"
        $h = "onion link directory"
        
    condition:
        3 of them
}

rule Core_Sites
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Core Sites"
        score = 30
    
    strings:
        $b = "Categoria introduction point"
        $c = "searches hidden"
        $e = "indexing information"
        
    condition:
        1 of them
}

rule Other_Languages
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Other Languages"
        score = 10
    
    strings:
        $a = "arabic"
        $b = "chinese"
        $c = "french"
        $d = "german"
        $e = "italian"
        $f = "japanese"
        $g = "polish"
        $h = "portuguese"
        $i = "russians"
        $j = "Spanish"
        
    condition:
        5 of them
}

rule Adult
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Adult"
        score = 0
    
    strings:
        $a = "hardcore"
        $b = "softcore"
        $c = "erotica"
        $d = "fetish"
        $e = "violence"
        $f = "escorts"
        $g = "polish"
        $h = "porn"
        $i = "spanking"
        
    condition:
        3 of them
}

rule Hosting
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Hosting"
        score = 10
    
    strings:
        $a = "domains"
        $b = "file hosting"
        $c = "pastebin"
        $d = "proxies"
        $e = "web hosting"
        $f = "file sharing"
        $g = "cmsms"
        $h = "onion site"
        $i = "apache"
        $j = "php"
        $k = "mysql"
        $l = ".onion domain"
        $m = "hosting"
        $n = "website"
        
    condition:
        3 of them
}

rule Personal
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Personal"
        score = 20
    
    strings:
        $a = "blog"
        $b = "books"
        $c = "pages"
        $d = "personal"

    condition:
        3 of them
}

rule Social
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Social"
        score = 20
    
    strings:
        $a = "bbs"
        $b = "chans"
        $c = "wiki"
        $d = "social network"
                
    condition:
        2 of them
}

rule Politics_and_Religion
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Politics and Religion"
        score = 10
    
    strings:
        $a = "activism"
        $b = "law"
        $c = "paranormal"
        $d = "politics"
        $e = "religion"
        $f = "whistleblowing"

    condition:
        3 of them
}

rule Developer
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Developer"
        score = 20
    
    strings:
        $a = "development"
        $b = "c++"
        $c = "c#"
        $d = "python"
        $e = "html"
        $f = "ruby"
        $g = "jupyter notebook"
        $h = "javascript"
        $i = "java"
                        
    condition:
        3 of them
}

rule Hacking
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Hacking"
        score = 40
    
    strings:
        $a = "hacker"
        $b = "blackbox"
        $c = "read team"
        $d = "redhat"
        $e = "blackhat"
        $f = "word"
        $g = "cracked"
        $h = "hacked"
        $i = "blueteam"
        $j = "phishing"
        $k = "malware"
        $l = "lamer"
        $m = "cracker"
        $n = "defacer"
        $o = "spyware"
        $p = "ciberpirata"
        $q = "freiro"
        $r = "scammers"
        $s = "uc"
        $t = "rat"
        $u = "ddos"
        $v = "fud"
        $x = "sql"
        $y = "xss"
        $z = "skid"
        $aa = "malware"
        $bb = "vps"
        $cc = "ansi bomb"
        $dd = "back door"
        $ee = "bot"
        $ff = "botnet"
        $gg = "buffer overflow"
        $hh = "cracker"
        $ii = "dox"
        $jj = "exploit"
        $kk = "rainbow table"
        $ll = "root"
        $mm = "reverse engineering"
        $nn = "shell"
        $oo = "script kiddie"
        $pp = "spoof"
        $qq = "sql injection"
        $rr = "trojan"
        $ss = "worm"
        $tt = "zero day exploit"
        $uu = "hacking tools"
        $vv = "ransomware"
        $xx = "cybercrime"
        $not = "100% up"
                        
    condition:
        4 of them and not $not
}

rule Security
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Security"
        score = 20
    
    strings:
        $a = "sniffr"
        $b = "wash"
        $d = "shield"
        $e = "private"
        $f = "strategic"
        $g = "intelligence"
        $h = "safe"
        $j = "anonymity"
                        
    condition:
        3 of them
}

rule Games
{
    meta:
        author = "@andreyglauzer"
        info = "Categoria Games"
        score = 5
    
    strings:
        $a = "poker"
        $b = "games"
        $c = "multiplayer"
        $d = "play free"
        $e = "play"
        $f = "casino"
                       
    condition:
        3 of them
}

rule Drug {
    meta:
        author = "@andreyglauzer"
        info = "Categoria Drug"
        score = 0
    
    strings:
        $a = "drugs"
        $b = "drug-shop"
        $c = "drug shop"
        $d = "acid"
        $e = "asteroid"
        $f = "berry"
        $g = "cocaine"
        $h = "lsd"
        $i = "mdma"
        $j = "skunk"
        $k = "cannabis"
                       
    condition:
        4 of them
}

rule Guns {
    meta:
        author = "@andreyglauzer"
        info = "Categoria Guns"
        score = 0
    
    strings:
        $a = "guns"
        $b = "sauer"
        $c = "ruguer"
        $d = "glock"
        $e = "colt"
        $f = "pistols"
        $g = "rifles"
        $h = "weapons" 

    condition:
        3 of them
}

rule Shop {
    meta:
        author = "@andreyglauzer"
        info = "Categoria Shop"
        score = 20
    
    strings:
        $a = "shop"
        $b = "price"
        $c = "buy item"
        $e = "products"
        $f = "ship"
        $g = "delivery"
        $h = "payment"
        $i = "bitcoin"
        $j = "buy now"
        $k = "marketplace"
        $l = "market"
        $m = "fast and secure shipping"
        $n = "high quality counterfeits"
        $o = "special propositions"
        $p = "counterfeit"
        $q = "bitcoin"
        $r = "wallet"
        $s = "store"
        $t = "order"
        $u = "products"
        $v = "quantity"

    condition:
        4 of them
}