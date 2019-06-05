import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class header:
    def __init__(self):
        pass

    @property
    def start(self):
        headers = [
            'name',
            'onion',
            'cow',
            'bixaomesmoem',
        ]
        if 'name' == random.choice(headers):
            self.name()
        elif 'onion' == random.choice(headers):
            self.onion()
        elif 'cow' == random.choice(headers):
            self.cow()
        elif 'bixaomesmoem' == random.choice(headers):
            self.bixaomesmoem()
        else:
            self.cow()

    def bixaomesmoem(self):

        print(bcolors.FAIL + "\n                     (\__/)  " + bcolors.ENDC)
        print(bcolors.FAIL + "                 ⠀   (•ㅅ•)     Como você se sente " + bcolors.ENDC)
        print(bcolors.FAIL + "              　 ＿ノ ヽ ノ＼     usando o " + bcolors.ENDC)
        print(bcolors.FAIL + "               /　`/ ⌒Ｙ⌒ Ｙ　ヽ   VigilantOnion " + bcolors.ENDC)
        print(bcolors.FAIL + "              ( 　(三ヽ人　 /   |     " + bcolors.ENDC)
        print(bcolors.FAIL + "              |　ﾉ⌒＼ ￣￣ヽ　 ノ   (\/)  Como é " + bcolors.ENDC)
        print(bcolors.FAIL + "              ヽ＿＿＿＞､＿＿_／   (•ㅅ•)  de verdade \n\n" + bcolors.ENDC)
        print(bcolors.FAIL + "              V I G I L A N T  O N I O N " + bcolors.ENDC)
        print(bcolors.FAIL + "                      2019 " + bcolors.ENDC)
        print(bcolors.FAIL + "                   Version 1.2 \n\n" + bcolors.ENDC)
        print(bcolors.FAIL + "                   Developer by " + bcolors.ENDC)
        print(bcolors.FAIL + "                  Andrey Glauzer " + bcolors.ENDC)

    def name(self):
        print(bcolors.WARNING + "\n_______________________________________________________________________________________________" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "                                                                                             " + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "   ___    ______        ___________             ____________       _____                     " + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "    __ |  / /__(_)______ ___(_)__  /_____ _________  /__  __ \_________(_)____________       " + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "    __ | / /__  /__  __ `/_  /__  /_  __ `/_  __ \  __/  / / /_  __ \_  /_  __ \_  __ \\      "  + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "    __ |/ / _  / _  /_/ /_  / _  / / /_/ /_  / / / /_ / /_/ /_  / / /  / / /_/ /  / / /      "  + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "    _____/  /_/  _\__, / /_/  /_/  \__,_/ /_/ /_/\__/ \____/ /_/ /_//_/  \____//_/ /_/       "  + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "                 /____/                                                                      "  + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "                                                                                             "  + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "                               V I G I L A N T  O N I O N                                    "  + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "                                          2019                                               "  + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "                                                                                             "  + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "                                       Version 1.2                                           "  + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.WARNING + "_____________________________________________________________________________________________"  + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "                                                                                             "  + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "                                       Developer by                                          "  + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.FAIL + "                                      Andrey Glauzer                                         "  + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.WARNING + "_____________________________________________________________________________________________"  + bcolors.WARNING + "|\n\n" + bcolors.ENDC)

    def onion(sef):
        print(bcolors.WARNING + "\n__________________________________________________________________________________" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                                                                """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                               ~                                """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                              /~                                """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                        \  \ /**                                """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                         \ ////                                 """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                         // //                                  """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                        // //                                   """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                      ///&//                                    """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                     / & /\ \                                   """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                   /  & .,,  \                                  """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                 /& %  :       \                                """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                               /&  %   :  ;     `\                              """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                              /&' &..%   !..    `.\                             """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                             /&' : &''" !  ``. : `.\                            """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                            /#' % :  "" * .   : : `.\                           """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                           I# :& :  !"  *  `.  : ::  I                          """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                           I &% : : !%.` '. . : : :  I                          """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                           I && :%: .&.   . . : :  : I                          """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                           I %&&&%%: WW. .%. : :     I                          """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                            \&&&##%%%`W! & '  :   ,'/                           """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                             \####ITO%% W &..'  #,'/                            """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                               \W&&##%%&&&&### %./                              """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                 \###j[\##//##}/                                """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                    ++///~~\//_                                 """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                     \\ \ \ \  \_                                """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                     /  /    \                                  """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                                                                """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                                                                """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                            V I G I L A N T  O N I O N                          """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                       2019                                     """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                                                                """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                    Version 1.2                                 """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.WARNING + """________________________________________________________________________________""" + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                                                                """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                   Developer by                                 """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                   Andrey Glauzer                               """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.WARNING + "________________________________________________________________________________" + bcolors.WARNING + "|\n\n" + bcolors.ENDC)

    def cow(self):
        print(bcolors.WARNING + """\n_________________________________________________________________________________________""" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                                                                       """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                                                                       """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                 %whi                                                                  """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                  _---------.                                          """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                              .' #######   ;."                                         """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                   .---,.    ;@             @@`;   .---,..                             """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                 ." @@@@@'.,'@@            @@@@@',.'@@@@ ".                            """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                 '-.@@@@@@@@@@@@@          @@@@@@@@@@@@@ @;                            """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                    `.@@@@@@@@@@@@        @@@@@@@@@@@@@@ .'                            """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                      "--'.@@@  -.@        @ ,'-   .'--"                               """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                           ".@' ; @       @ `.  ;'                                     """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                             |@@@@ @@@     @    .                                      """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                              ' @@@ @@   @@    ,                                       """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                               `.@@@@    @@   .                                        """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                 ',@@     @   ;           ________________             """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                  (   3 C    )     /|___ / VigilantOnion! \            """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                  ;@'. __*__,."    \|--- \________________/            """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                 '(.,...."/%clr                                                        """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                                                                       """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                           V I G I L A N T  O N I O N                                  """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                    2019                                               """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                                                                       """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                 Version 1.2                                           """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.WARNING + """_______________________________________________________________________________________""" + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                                                                       """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                Developer by                                           """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.OKGREEN + """                                Andrey Glauzer                                         """ + bcolors.WARNING + "|" + bcolors.ENDC)
        print(bcolors.WARNING + "|" + bcolors.WARNING + """_______________________________________________________________________________________""" + bcolors.WARNING + "|\n\n" + bcolors.ENDC)
