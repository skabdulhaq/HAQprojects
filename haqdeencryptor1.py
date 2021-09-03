import os,tempfile

logos = ['''
888    888                         8888888b.  8888888888        .d8888b.           8888888888 888b    888                                    888                     
888    888                         888  "Y88b 888              d88P  "88b          888        8888b   888                                    888                     
888    888                         888    888 888              Y88b. d88P          888        88888b  888                                    888                     
8888888888  8888b.   .d88888       888    888 8888888           "Y8888P"           8888888    888Y88b 888  .d8888b 888d888 888  888 88888b.  888888  .d88b.  888d888 
888    888     "88b d88" 888       888    888 888              .d88P88K.d88P       888        888 Y88b888 d88P"    888P"   888  888 888 "88b 888    d88""88b 888P"   
888    888 .d888888 888  888       888    888 888              888"  Y888P"        888        888  Y88888 888      888     888  888 888  888 888    888  888 888     
888    888 888  888 Y88b 888       888  .d88P 888              Y88b .d8888b        888        888   Y8888 Y88b.    888     Y88b 888 888 d88P Y88b.  Y88..88P 888     
888    888 "Y888888  "Y88888       8888888P"  8888888888        "Y8888P" Y88b      8888888888 888    Y888  "Y8888P 888      "Y88888 88888P"   "Y888  "Y88P"  888     
                         888                                                                                                    888 888                              
                         888                                                                                               Y8b d88P 888                              
                         888                                                                                                "Y88P"  888                              


''','''
.-..-.               .---.  .--.    .--.     .--. .-..-.                       .-.           
: :; :               : .  :: .--'  : .; ;   : .--': `: :                      .' `.          
:    : .--.   .---.  : :: :: `;     ;  '_   : `;  : .` : .--. .--. .-..-..---.`. .'.--. .--. 
: :: :' .; ; ' .; :  : :; :: :__   : :;` ;  : :__ : :. :'  ..': ..': :; :: .; `: :' .; :: ..'
:_;:_;`.__,_;`._. ;  :___.'`.__.'  `.__._;  `.__.':_;:_;`.__.':_;  `._. ;: ._.':_;`.__.':_;  
                : :                                                 .-. :: :                 
                :_:                                                 `._.':_;                 

''', '''
_//     _//                       _/////    _////////         _/         _////////_///     _//                               _//                
_//     _//                       _//   _// _//             _// _//      _//      _/ _//   _//                               _//                
_//     _//   _//     _//         _//    _//_//            _//           _//      _// _//  _//   _///_/ _///_//   _//_/ _//_/_/ _/ _//   _/ _///
_////// _// _//  _//_/  _//       _//    _//_//////         _///         _//////  _//  _// _// _//    _//    _// _// _/  _// _// _//  _// _//   
_//     _//_//   _//_/  _//       _//    _//_//            _//           _//      _//   _/ _//_//     _//      _///  _/   _//_//_//    _//_//   
_//     _//_//   _// _//_//       _//   _// _//             _// _//      _//      _//    _/ // _//    _//       _//  _// _// _// _//  _// _//   
_//     _//  _// _///   _//       _/////    _////////         _/         _////////_//      _//   _///_///      _//   _//      _//  _//   _///   
                        _///                                                                                 _//     _//                        


''','''
.##..##...####....####...........#####...######...........#####...........######..##..##...####...#####...##..##..#####...######...####...#####..
.##..##..##..##..##..##..........##..##..##..............##...##..........##......###.##..##..##..##..##...####...##..##....##....##..##..##..##.
.######..######..##.###..........##..##..####.............##.##...........####....##.###..##......#####.....##....#####.....##....##..##..#####..
.##..##..##..##..##..##..........##..##..##..............##.##.#..........##......##..##..##..##..##..##....##....##........##....##..##..##..##.
.##..##..##..##...#####..........#####...######...........#####...........######..##..##...####...##..##....##....##........##.....####...##..##.
.................................................................................................................................................

''','''
                                                                                                                                                                       
 _|    _|                          _|_|_|    _|_|_|_|        _|            _|_|_|_|  _|      _|                                            _|                          
 _|    _|    _|_|_|    _|_|_|      _|    _|  _|            _|  _|          _|        _|_|    _|    _|_|_|  _|  _|_|  _|    _|  _|_|_|    _|_|_|_|    _|_|    _|  _|_|  
 _|_|_|_|  _|    _|  _|    _|      _|    _|  _|_|_|          _|_|  _|      _|_|_|    _|  _|  _|  _|        _|_|      _|    _|  _|    _|    _|      _|    _|  _|_|      
 _|    _|  _|    _|  _|    _|      _|    _|  _|            _|    _|        _|        _|    _|_|  _|        _|        _|    _|  _|    _|    _|      _|    _|  _|        
 _|    _|    _|_|_|    _|_|_|      _|_|_|    _|_|_|_|        _|_|  _|      _|_|_|_|  _|      _|    _|_|_|  _|          _|_|_|  _|_|_|        _|_|    _|_|    _|        
                           _|                                                                                              _|  _|                                      
                           _|                                                                                          _|_|    _|                                      


''','''
.##.....##....###.....#######.....########..########......####.......########.##....##..######..########..##....##.########..########..#######..########.
.##.....##...##.##...##.....##....##.....##.##...........##..##......##.......###...##.##....##.##.....##..##..##..##.....##....##....##.....##.##.....##
.##.....##..##...##..##.....##....##.....##.##............####.......##.......####..##.##.......##.....##...####...##.....##....##....##.....##.##.....##
.#########.##.....##.##.....##....##.....##.######.......####........######...##.##.##.##.......########.....##....########.....##....##.....##.########.
.##.....##.#########.##..##.##....##.....##.##..........##..##.##....##.......##..####.##.......##...##......##....##...........##....##.....##.##...##..
.##.....##.##.....##.##....##.....##.....##.##..........##...##......##.......##...###.##....##.##....##.....##....##...........##....##.....##.##....##.
.##.....##.##.....##..#####.##....########..########.....####..##....########.##....##..######..##.....##....##....##...........##.....#######..##.....##

''', '''
##     ##    ###     #######     ########  ########      ####       ######## ##    ##  ######  ########  ##    ## ########  ########  #######  ########  
##     ##   ## ##   ##     ##    ##     ## ##           ##  ##      ##       ###   ## ##    ## ##     ##  ##  ##  ##     ##    ##    ##     ## ##     ## 
##     ##  ##   ##  ##     ##    ##     ## ##            ####       ##       ####  ## ##       ##     ##   ####   ##     ##    ##    ##     ## ##     ## 
######### ##     ## ##     ##    ##     ## ######       ####        ######   ## ## ## ##       ########     ##    ########     ##    ##     ## ########  
##     ## ######### ##  ## ##    ##     ## ##          ##  ## ##    ##       ##  #### ##       ##   ##      ##    ##           ##    ##     ## ##   ##   
##     ## ##     ## ##    ##     ##     ## ##          ##   ##      ##       ##   ### ##    ## ##    ##     ##    ##           ##    ##     ## ##    ##  
##     ## ##     ##  ##### ##    ########  ########     ####  ##    ######## ##    ##  ######  ##     ##    ##    ##           ##     #######  ##     ## 

''','''
 #     #                  ######  #######      ##       ####### #     #                                                
 #     #   ##    ####     #     # #           #  #      #       ##    #  ####  #####  #   # #####  #####  ####  #####  
 #     #  #  #  #    #    #     # #            ##       #       # #   # #    # #    #  # #  #    #   #   #    # #    # 
 ####### #    # #    #    #     # #####       ###       #####   #  #  # #      #    #   #   #    #   #   #    # #    # 
 #     # ###### #  # #    #     # #          #   # #    #       #   # # #      #####    #   #####    #   #    # #####  
 #     # #    # #   #     #     # #          #    #     #       #    ## #    # #   #    #   #        #   #    # #   #  
 #     # #    #  ### #    ######  #######     ###  #    ####### #     #  ####  #    #   #   #        #    ####  #    # 
                                                                                                                       

''','''
██╗  ██╗ █████╗  ██████╗     ██████╗ ███████╗       ██╗       ███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ██████╗ 
██║  ██║██╔══██╗██╔═══██╗    ██╔══██╗██╔════╝       ██║       ██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████║███████║██║   ██║    ██║  ██║█████╗      ████████╗    █████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██████╔╝
██╔══██║██╔══██║██║▄▄ ██║    ██║  ██║██╔══╝      ██╔═██╔═╝    ██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██╔══██╗
██║  ██║██║  ██║╚██████╔╝    ██████╔╝███████╗    ██████║      ███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚══▀▀═╝     ╚═════╝ ╚══════╝    ╚═════╝      ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                           

''','''
 ____  ____                   ______   ________     ___        ________  ____  _____                                  _                   
|_   ||   _|                 |_   _ `.|_   __  |  .' _ '.     |_   __  ||_   \|_   _|                                / |_                 
  | |__| |   ,--.    .--. _    | | `. \ | |_ \_|  | (_) '___    | |_ \_|  |   \ | |   .---.  _ .--.  _   __  _ .--. `| |-' .--.   _ .--.  
  |  __  |  `'_\ : / /'`\' ]   | |  | | |  _| _   .`___'/ _/    |  _| _   | |\ \| |  / /'`\][ `/'`\][ \ [  ][ '/'`\ \| | / .'`\ \[ `/'`\] 
 _| |  | |_ // | |,| \__/ |   _| |_.' /_| |__/ | | (___)  \_   _| |__/ | _| |_\   |_ | \__.  | |     \ '/ /  | \__/ || |,| \__. | | |     
|____||____|\'-;__/ \__.; |  |______.'|________| `._____.\__| |________||_____|\____|'.___.'[___]  [\_:  /   | ;.__/ \__/ '.__.' [___]    
                        |__]                                                                        \__.'   [__|                          

''','''
 __    __       ___       ______          _______   _______                _______ .__   __.   ______ .______     ____    ____ .______   .___________.  ______   .______      
|  |  |  |     /   \     /  __  \        |       \ |   ____|     ___      |   ____||  \ |  |  /      ||   _  \    \   \  /   / |   _  \  |           | /  __  \  |   _  \     
|  |__|  |    /  ^  \   |  |  |  |       |  .--.  ||  |__       ( _ )     |  |__   |   \|  | |  ,----'|  |_)  |    \   \/   /  |  |_)  | `---|  |----`|  |  |  | |  |_)  |    
|   __   |   /  /_\  \  |  |  |  |       |  |  |  ||   __|      / _ \/\   |   __|  |  . `  | |  |     |      /      \_    _/   |   ___/      |  |     |  |  |  | |      /     
|  |  |  |  /  _____  \ |  `--'  '--.    |  '--'  ||  |____    | (_>  <   |  |____ |  |\   | |  `----.|  |\  \----.   |  |     |  |          |  |     |  `--'  | |  |\  \----.
|__|  |__| /__/     \__\ \_____\_____\   |_______/ |_______|    \___/\/   |_______||__| \__|  \______|| _| `._____|   |__|     | _|          |__|      \______/  | _| `._____|
                                                                                                                                                                              


''','''
 __    __       ___       ______          _______   _______                _______ .__   __.   ______ .______     ____    ____ .______   .___________.  ______   .______      
|  |  |  |     /   \     /  __  \        |       \ |   ____|     ___      |   ____||  \ |  |  /      ||   _  \    \   \  /   / |   _  \  |           | /  __  \  |   _  \     
|  |__|  |    /  ^  \   |  |  |  |       |  .--.  ||  |__       ( _ )     |  |__   |   \|  | |  ,----'|  |_)  |    \   \/   /  |  |_)  | `---|  |----`|  |  |  | |  |_)  |    
|   __   |   /  /_\  \  |  |  |  |       |  |  |  ||   __|      / _ \/\   |   __|  |  . `  | |  |     |      /      \_    _/   |   ___/      |  |     |  |  |  | |      /     
|  |  |  |  /  _____  \ |  `--'  '--.    |  '--'  ||  |____    | (_>  <   |  |____ |  |\   | |  `----.|  |\  \----.   |  |     |  |          |  |     |  `--'  | |  |\  \----.
|__|  |__| /__/     \__\ \_____\_____\   |_______/ |_______|    \___/\/   |_______||__| \__|  \______|| _| `._____|   |__|     | _|          |__|      \______/  | _| `._____|
                                                                                                                                                                              

''','''
    __  __                 ____   ______   ___        ______ _   __                           __              
   / / / /____ _ ____ _   / __ \ / ____/  ( _ )      / ____// | / /_____ _____ __  __ ____   / /_ ____   _____
  / /_/ // __ `// __ `/  / / / // __/    / __ \/|   / __/  /  |/ // ___// ___// / / // __ \ / __// __ \ / ___/
 / __  // /_/ // /_/ /  / /_/ // /___   / /_/  <   / /___ / /|  // /__ / /   / /_/ // /_/ // /_ / /_/ // /    
/_/ /_/ \__,_/ \__, /  /_____//_____/   \____/\/  /_____//_/ |_/ \___//_/    \__, // .___/ \__/ \____//_/     
                 /_/                                                        /____//_/                         

''',]
import random
print(random.choice(logos))

alphabits= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," "]


def Haq_encryptor_decryptor(en_de,input_text,pass_set):
    final_txt = ""
    pass_set_open = True
    final_print = "En"
    if en_de == "decode" or en_de == "de":
        final_print = "De"
        pass_set_open = False
    if pass_set_open == False:
        pass_set = pass_set*-1
    for en_de_int in input_text:
        position = alphabits.index(en_de_int)
        final = alphabits[position+pass_set]
        final_txt +=final
    suff = random.randint(0,123456)
    name = f"{final_print}crypted_{suff}.txt"
    with open(name, "w") as text :
        text.write(final_txt)
    print(f"your {final_print}crypted text is in the desktop named '{name}' ")
end = False
while end == False :
    goto_fun = False
    options = input("To encrypt message type 'encode' or 'en'\nTo decrypt message type 'decode' or 'de'\n ").lower()
    if options == "encode" or options == "en":
        txt = input("Type your message\n")
        goto_fun = True
        passnumber = int(input("Please create a passcode of decryption \n[NOTE-: passcode must be in between (1 to 999), Make it Unique...] \n"))
    elif options =="decode" or options == "de":
        txt = input("Type your message\n")
        passnumber = int(input("Please Enter a passcode of decryption\n"))
        goto_fun = True
    while goto_fun == True:
        Haq_encryptor_decryptor(en_de = options, input_text = txt, pass_set=passnumber )
        exit = input("To Encode or Decode type other message type YES \nTo Exit type NO\n").upper()
        if exit == "NO":
            end = True
            goto_fun = False
        elif exit == "YES":
            goto_fun = False
input("Enter to exit")