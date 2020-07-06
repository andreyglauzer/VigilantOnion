/*
    Essa Yara tem como proposito buscar essas keywords no texto.
*/

rule core_keywords
{
    meta:
        author = "@KevTheHermit"
        score = 20

    strings:
        $antisec = "antisec" wide ascii nocase
        $hacked = "hacked by" wide ascii nocase
        $nmap_scan = "Nmap scan report for" wide ascii nocase
        $enabled_sec = "enable secret" wide ascii nocase
        $enable_pass = "enable password" wide ascii nocase
    condition:
        any of them

}

rule email_filter
{
    meta:
        author = "@kovacsbalu"
        score = 10
    strings:
	      $email_add = /\b[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)*\.[a-zA-Z-]+[\w-]\b/
    condition:
        any of them

}

rule powershell
{
    meta:
        author = "@KevTheHermit"
        score = 10

    strings:
        $a1 = "powershell" fullword wide ascii nocase
        $a2 = "IEX" fullword wide ascii nocase
        $a3 = "new-object" fullword wide ascii nocase
        $a4 = "webclient" fullword wide ascii nocase
        $a5 = "downloadstring" fullword wide ascii nocase
        $a6 = "-WindowStyle Hidden" fullword wide ascii nocase
        $a7 = "invoke" fullword wide ascii nocase
        $a8 = "bitsadmin" fullword wide ascii nocase
        $a9 = "certutil -decode" fullword wide ascii nocase
        $a10 = "hidden" fullword wide ascii nocase
        $a11 = "nop" fullword wide ascii nocase
        $a12 = "Invoke-" fullword wide ascii nocase
        $a13 = "FromBase64String(" fullword wide ascii nocase



        $not1 = "chocolatey" nocase
        $not2 = "XmlConfiguration is now operational" nocase
    condition:
        4 of ($a*) and not any of ($not*)

}

rule CryptoExchangeApi
{
    meta:
        description = "Contains Crypro Exchange API URL"
        author = "Jason Schorr (0xBanana)"
        score = 20
    strings:
    	$a = "api.binance.com" nocase wide ascii
      $a0 = "1btcxe.com/api" nocase wide ascii
      $a1 = "acx.io/api" nocase wide ascii
      $a2 = "anxpro.com/api" nocase wide ascii
      $a3 = "anybits.com/api" nocase wide ascii
      $a4 = "www.bcex.top" nocase wide ascii
      $a5 = "api.bibox.com" nocase wide ascii
      $a6 = "bit2c.co.il" nocase wide ascii
      $a7 = "api.bitfinex.com" nocase wide ascii
      $a8 = "api.bitfinex.com" nocase wide ascii
      $a9 = "api.bitflyer.jp" nocase wide ascii
      $aa = "api.bitforex.com" nocase wide ascii
      $ab = "bitibu.com" nocase wide ascii
      $ac = "bitlish.com/api" nocase wide ascii
      $ad = "www.bitmex.com" nocase wide ascii
      $ae = "bitsane.com/api" nocase wide ascii
      $af = "api.bitso.com" nocase wide ascii
      $ag = "www.bitstamp.net/api" nocase wide ascii
      $ah = "www.bitstamp.net/api" nocase wide ascii
      $ai = "api.bl3p.eu" nocase wide ascii
      $aj = "braziliex.com/api/v1" nocase wide ascii
      $ak = "btc-alpha.com/api" nocase wide ascii
      $al = "www.btcbox.co.jp/api" nocase wide ascii
      $am = "www.btcexchange.ph/api" nocase wide ascii
      $an = "btc-trade.com.ua/api" nocase wide ascii
      $ao = "www.btcturk.com/api" nocase wide ascii
      $ap = "www.buda.com/api" nocase wide ascii
      $aq = "bx.in.th/api" nocase wide ascii
      $ar = "cex.io/api" nocase wide ascii
      $as = "api.cobinhood.com" nocase wide ascii
      $at = "api.coinbase.com" nocase wide ascii
      $au = "api.prime.coinbase.com" nocase wide ascii
      $av = "api.pro.coinbase.com" nocase wide ascii
      $aw = "coincheck.com/api" nocase wide ascii
      $ax = "www.coinexchange.io/api/v1" nocase wide ascii
      $ay = "coinfalcon.com" nocase wide ascii
      $az = "webapi.coinfloor.co.uk:8090/bist" nocase wide ascii
      $aa1 = "coinmate.io/api" nocase wide ascii
      $aa2 = "api.coinone.co.kr" nocase wide ascii
      $aa3 = "api.crex24.com" nocase wide ascii
      $aa4 = "api.cryptonbtc.com" nocase wide ascii
      $aa5 = "www.deribit.com" nocase wide ascii
      $aa6 = "api.ethfinex.com" nocase wide ascii
      $aa7 = "api.fcoin.com" nocase wide ascii
      $aa8 = "api.flowbtc.com:8405/ajax" nocase wide ascii
      $aa9 = "www.fybse.se/api/SEK" nocase wide ascii
      $aa0 = "www.fybsg.com/api/SGD" nocase wide ascii
      $aab = "api.gatecoin.com" nocase wide ascii
      $aac = "api.gdax.com" nocase wide ascii
      $aad = "api.gemini.com" nocase wide ascii
      $aae = "getbtc.org/api" nocase wide ascii
      $aaf = "api.hitbtc.com" nocase wide ascii
      $aag = "api.hitbtc.com" nocase wide ascii
      $aah = "api.huobi.com" nocase wide ascii
      $aai = "ice3x.com/api" nocase wide ascii
      $aaj = "api.itbit.com" nocase wide ascii
      $aak = "www.jubi.com/api" nocase wide ascii
      $aal = "kuna.io" nocase wide ascii
      $aam = "api.lakebtc.com" nocase wide ascii
      $aan = "api.lbank.info" nocase wide ascii
      $aao = "api.liquid.com" nocase wide ascii
      $aap = "api.livecoin.net" nocase wide ascii
      $aaq = "api.mybitx.com/api" nocase wide ascii
      $aar = "mixcoins.com/api" nocase wide ascii
      $aas = "novaexchange.com/remote" nocase wide ascii
      $aat = "paymium.com/api" nocase wide ascii
      $aau = "api.quadrigacx.com" nocase wide ascii
      $aav = "www.rightbtc.com/api" nocase wide ascii
      $aaw = "www.southxchange.com/api" nocase wide ascii
      $aax = "api.theocean.trade/api" nocase wide ascii
      $aay = "api.therocktrading.com" nocase wide ascii
      $aaz = "www.tidebit.com" nocase wide ascii
      $ba = "open-api.uex.com/open/api" nocase wide ascii
      $bb = "api.vaultoro.com" nocase wide ascii
      $bc = "cryptottlivewebapi.xbtce.net:8443/api" nocase wide ascii
      $bd = "yunbi.com" nocase wide ascii
      $be = "api.zaif.jp" nocase wide ascii

    condition:
       any of them
}

rule aws_cli
{
    meta:
        author = "@KevTheHermit"
        score = 20

    strings:
        $a1 = "aws s3 " ascii
        $a2 = "aws ec2 " ascii
        $a3 = "aws ecr " ascii
        $a4 = "aws cognito-identity" ascii
        $a5 = "aws iam "ascii
        $a6 = "aws waf " ascii

    condition:
        any of them

}

rule sw_bucket
{
    meta:
        author = "@KevTheHermit"
        score = 20

    strings:
        $a1 = "s3.amazonaws.com" ascii

    condition:
        any of them

}

rule b64_exe
{
    meta:
        author = "@KevTheHermit"
        score = 10

    strings:
        $b64_exe = /\bTV(oA|pB|pQ|qA|qQ|ro)/
    condition:
        $b64_exe at 0

}

rule b64_elf
{
    meta:
        author = "@KevTheHermit"
        score = 10

    strings:
        $b64_elf = "f0VM"
    condition:
        $b64_elf at 0

}

rule b64_zip
{
    meta:
        author = "@KevTheHermit"
        score = 10

    strings:
        $b64_zip = "UEs"
    condition:
        $b64_zip at 0

}

rule b64_rar
{
    meta:
        author = "@KevTheHermit"
        score = 10

    strings:
        $b64_rar = "UmFy"
    condition:
        $b64_rar at 0

}


rule b64_gzip
{
    meta:
        author = "@KevTheHermit"
        score = 10

    strings:
        $b64_gzip = "H4sI"
    condition:
        $b64_gzip at 0

}

rule b64_url
{
    meta:
        author = "@KevTheHermit"
        score = 10

    strings:
        $a1 = "aHR0cDov" // http/s
        $a2 = "SFRUUDov" // HTTP/S
        $a3 = "d3d3Lg" // www.
        $a4 = "V1dXLg" // WWW.

        // ignore vendor certs in this rule. The certs rule will pick them up if we want them
        $not1 = "GlobalSign Root CA" nocase

        // Ignore data: uris. These are common in html, css, and svg files.
        $not2 = /data:[a-z0-9\/]+;(base64,)?aHR0cDov/ nocase
        $not3 = /data:[a-z0-9\/]+;(base64,)?SFRUUDov/ nocase
        $not4 = /data:[a-z0-9\/]+;(base64,)?d3d3Lg/ nocase
        $not5 = /data:[a-z0-9\/]+;(base64,)?V1dXLg/ nocase

    condition:
        any of ($a*) and not any of ($not*)

}

rule b64_doc
{
    meta:
        author = "@KevTheHermit"
        score = 10

    strings:
        $b64_doc = "0M8R4" // d0cf11
    condition:
        $b64_doc at 0

}

rule b64_rtf
{
    meta:
        author = "@KevTheHermit"
        score = 10

    strings:
        $b64_rtf = "e1xydGY" // {\rtf
    condition:
        $b64_rtf at 0

}

rule b64_docx
{
    meta:
        author = "@KevTheHermit"
        score = 10

    strings:
        $b64_zip = "UEs"
        $docx1 = "d29yZC9fcmVsc" // word/_rel
        $docx2 = "Zm9udFRhYmxl" // fontTable
        $docx3 = "ZG9jUHJvcHM" // docProps
        $docx4 = "Q29udGVudF9UeXBlcw" // Content_Types
        $docx5 = "c2V0dGluZ3M" //settings
    condition:
        $b64_zip at 0 and 3 of ($docx*)

}

rule b64_xml_doc
{
    meta:
        author = "@KevTheHermit"
        score = 10

    strings:
        $b64_xml = "PD94bWwg"
        $docx1 = "b3BlbmRvY3VtZW50" // opendocument
        $docx2 = "InBhcmFncmFwaCI" // "paragraph"
        $docx3 = "b2ZmaWNlL3dvcmQv" // office/word/
        $docx4 = "RG9jdW1lbnRQcm9wZXJ0aWVz" // DocumentProperties
    condition:
        $b64_xml at 0 and 3 of ($docx*)

}

rule db_connection
{
    meta:
        author = "@KevTheHermit"
        score = 20

    strings:
        $a = /\b(mongodb|http|https|ftp|mysql|postgresql|oracle):\/\/(\S*):(\S*)@(\S*)\b/
        $n1 = "#EXTINF"
        $n2 = "m3u8"

    condition:
        $a and not any of ($n*)
}

rule db_structure
{
    meta:
        author = "@KevTheHermit"
        score = 20

    strings:
        $a = "CREATE TABLE" nocase
        $b = "INSERT INTO" nocase
        $c = "VALUES" nocase
        $d = "ENGINE" nocase
        $e = "CHARSET" nocase
        $f = "NOT NULL" nocase
        $g = "varchar" nocase
        $h = "PRIMARY KEY"

    condition:
        5 of them
}

rule db_create_user
{
    meta:
        author = "@KevTheHermit"
        score = 20

    strings:
        $a = "GRANT ALL PRIVILEGES" nocase
        $b = "IDENTIFIED BY" nocase
        $c = "GRANT SELECT" nocase
        $d = "CREATE USER" nocase

    condition:
        2 of them
}

rule php_obfuscation
{
    meta:
        author = "@KevTheHermit"
        score = 20

    strings:
        $a = "eval(" nocase
        $b = "gzinflate(" nocase
        $c = "base64_decode("
        $d = "\\142\\x61\\163\\145\\x36\\x34\\137\\144\\x65\\x63\\x6f\\x64\\x65"
        $e = "str_rot13("

    condition:
        2 of them
}

rule XP_Investimentos
{
    meta:
        author = "@andreyglauzer"
        score = 100

    strings:
        $xpinvestiments1 = "labmec.com.br"
        $xpinvestiments2 = "owaxpi.com.br"
        $xpinvestiments3 = "bancoxp.com.br"
        $xpinvestiments4 = "sigaoespecialista.com.br"
        $xpinvestiments5 = "representantexpe.com.br"
        $xpinvestiments6 = "seunegociosemlimites.com.br"
        $xpinvestiments7 = "testadordabolsa.com.br"
        $xpinvestiments8 = "invistanabolsa.com.br"
        $xpinvestiments9 = "xppro.com.br"
        $xpinvestiments10 = "xpishoppingfinanceiro.com.br"
        $xpinvestiments11 = "xpisf.com.br"
        $xpinvestiments12 = "xpconnect.com.br"
        $xpinvestiments13 = "xpir.com.br"
        $xpinvestiments14 = "xpinvestor.com.br"
        $xpinvestiments15 = "xpconnectxpi.com.br"
        $xpinvestiments16 = "xpagro.com.br"
        $xpinvestiments17 = "webmailxpi.com.br"
        $xpinvestiments18 = "compareantesdeinvestir.com.br"
        $xpinvestiments19 = "expertxp.com.br"
        $xpinvestiments20 = "novostalentosxp.com.br"
        $xpinvestiments21 = "xpnews.com.br"
        $xpinvestiments22 = "universidadexp.com.br"
        $xpinvestiments23 = "xpcsaffinity.com.br"
        $xpinvestiments24 = "xpinvestimentos.com.br"
        $xpinvestiments25 = "xpadvisors.com"
        $xpinvestiments26 = "xpinvestimentos.com"
        $xpinvestiments27 = "xpinvestimentos.net"
        $xpinvestiments28 = "xpcorretoradeseguros.com.br"
        $xpinvestiments29 = "xpseguros.com.br"
        $xpinvestiments30 = "xpeducacao.com.br"
        $xpinvestiments31 = "xpadvisory.com.br"
        $xpinvestiments32 = "xpsecurities.com"
        $xpinvestiments33 = "xpe.com.br"
        $xpinvestiments34 = "xpcs.com.br"
        $xpinvestiments35 = "tecfinance.com.br"
        $xpinvestiments36 = "xpgestao.com.br"
        $xpinvestiments37 = "xpaai.com.br"
        $xpinvestiments38 = "xpcorretora.com.br"
        $xpinvestiments39 = "xpi.com.br"
        $xpinvestiments40 = "agenteinvest.com.br"
        $xpinvestiments41 = "clearcorretora.com.br"
        $xpinvestiments42 = "clearctvm.com.br"
        $xpinvestiments43 = "allianceasset.com.br"
        $xpinvestiments44 = "clear.com.br"
        $xpinvestiments45 = "clearobjetivos.com.br"
        $xpinvestiments46 = "distribuainvestimentos.com.br"
        $xpinvestiments47 = "grupoxp.com.br"
        $xpinvestiments48 = "xpinforma.com.br"
        $xpinvestiments49 = "expertxp.com"
        $xpinvestiments50 = "xpsecurities.com.br"
        $xpinvestiments51 = "xpcorretoraseguros.com.br"
        $xpinvestiments52 = "assessoriadeinvestimentos.com.br"
        $xpinvestiments53 = "clear-informa.com.br"
        $xpinvestiments54 = "sistemas-clear.com.br"
        $xpinvestiments55 = "clearinvestimentos.com.br"
        $xpinvestiments56 = "corretoraxp.com.br"
        $xpinvestiments57 = "xdex.com.br"
        $xpinvestiments58 = "xpi.co.uk"
        $xpinvestiments59 = "xpsecurities.co.uk."
        $xpinvestiments60 = "xp.com.br"
        $xpinvestiments61 = "xpmalls.com.br"
        $xpinvestiments62 = "xpi.us"
        $xpinvestiments63 = "71.82.170.in-addr.arpa"
        $xpinvestiments64 = "68.82.170.in-addr.arpa"
        $xpinvestiments65 = "69.82.170.in-addr.arpa"
        $xpinvestiments66 = "70.82.170.in-addr.arpa"
        $xpinvestiments67 = "frontlinetraders.com.br"
        $xpinvestiments68 = "xdexnews.com.br"
        $xpinvestiments69 = "xdexcontato.com.br"
        $xpinvestiments70 = "xpvista.com.br"
        $xpinvestiments71 = "xpassetmanagement.com.br"
        $xpinvestiments72 = "xpasset.com.br"
        $xpinvestiments73 = "niveldeservicoxp.com.br"
        $xpinvestiments74 = "resolvetudonaxp.com.br"
        $xpinvestiments75 = "vistarealestate.com.br"
        $xpinvestiments76 = "leadr.com.br"
        $xpinvestiments77 = "xpsegurosnews.com.br"
        $xpinvestiments78 = "xpinstitucional.com.br"
        $xpinvestiments79 = "bulltf.com.br"
        $xpinvestiments80 = "xpprivate.com"
        $xpinvestiments81 = "xpprivate.ch"
        $xpinvestiments82 = "vistainvestimentos.com.br"
        $xpinvestiments83 = "xpmfo.com"
        $xpinvestiments84 = "offsitelideresxp.com"
        $xpinvestiments85 = "xpfo.com.br"
        $xpinvestiments86 = "xpinc.com.br"
        $xpinvestiments87 = "projetolucianaseabr.com.br"
        $xpinvestiments88 = "xpstoreoficial.com.br"
        $xpinvestiments89 = "invistaspiti.com.br"
        $xpinvestiments90 = "xp-recruiting.com"
        $xpinvestiments91 = "bulltf.com.br"
        $xpinvestiments92 = "xpinc.com"
        $xpinvestiments93 = "invistaspiti.com.br"
        $xpinvestiments94 = "xpempresas.com.br"
        $xpinvestiments95 = "rico.com.vc"
        $xpinvestiments96 = "ricohomebrker.com.br"
        $xpinvestiments97 = "meumilhao.com.br"
        $xpinvestiments98 = "oqueeserrico.com.br"
        $xpinvestiments99 = "ricoinvestimentos.com.br"
        $xpinvestiments100 = "ricotrade.com.br"
        $xpinvestiments101 = "sourica.com.br"
        $xpinvestiments102 = "ricoeducacional.com.vc"
        $xpinvestiments103 = "ricocomvc.com.br"
        $xpinvestiments104 = "ricocomvc.com"
        $xpinvestiments105 = "linktrade.com.br"
        $xpinvestiments106 = "linktrade.net.br"
        $xpinvestiments107 = "eusourico.com.br"
        $xpinvestiments108 = "octotrade.com.br"
        $xpinvestiments109 = "ricoinvest.com.br"
        $xpinvestiments110 = "8investimentos.com.br"
        $xpinvestiments111 = "8trade.com.br"
        $xpinvestiments112 = "octocorretora.com.br"
        $xpinvestiments113 = "octoctvm.com.br"
        $xpinvestiments114 = "octoinvest.com.br"
        $xpinvestiments115 = "octoinvestimentos.com.br"
        $xpinvestiments116 = "ricohb.com.br"
        $xpinvestiments117 = "momentosrico.com.vc"
        $xpinvestiments118 = "directainvest.com.br"
        $xpinvestiments119 = "banifinvest.com.br"
        $xpinvestiments120 = "rico.com.br"
        $xpinvestiments121 = "tesourodireto.com.vc"
        $xpinvestiments122 = "ricoseguros.com.vc"
        $xpinvestiments123 = "ricoseguros.com.br"
        $xpinvestiments124 = "rico.b.br"
        $xpinvestiments125 = "ricoseguros.b.br"
        $xpinvestiments126 = "ricoseguro.b.br"
        $xpinvestiments127 = "ricoseguro.com.vc"
        $xpinvestiments128 = "ricoseguros.com.br"
        $xpinvestiments129 = "rico.trade"
        $xpinvestiments130 = "radarinvestimentos.com.br"
        $xpinvestiments131 = "moneyupinvest.com.br"
        $xpinvestiments132 = "ricomais.com.vc"
        $xpinvestiments133 = "maisrico.com.vc"
        $xpinvestiments134 = "oprimorico.com.br"
        $xpinvestiments135 = "ocodigodariqueza.com.br"
        $xpinvestiments136 = "xpenergia.com.br"
        $xpinvestiments137 = "bancoxpi.com.br"
        $xpinvestiments138 = "americainvest.com.br"
        $xpinvestiments139 =  "bulltf.com.br"
        $xpinvestiments140 =  "Xp Investimentos"
        $xpinvestiments141 =  "XpInvestimentos"
        $xpinvestiments142 =  "Grupo XP"
        $xpinvestiments143 =  "GrupoXP"
        $xpinvestiments144 =  "Corretora clear"
        $xpinvestiments145 =  "Corretoraclear"
        $xpinvestiments146 =  "Clear corretor"
        $xpinvestiments147 =  "Clearcorretor"
        $xpinvestiments148 =  "Rico correcora"
        $xpinvestiments149 =  "Ricocorrecora"
        $xpinvestiments150 =  "corretora rico"
        $xpinvestiments151 =  "corretorarico"

    condition:
        1 of them
}