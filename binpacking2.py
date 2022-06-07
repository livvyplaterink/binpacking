#this file executes the heuristic: orders the items and bins, places the items in the bins, and then performs a postprocessing step (currently the postprocessing step is executed 3 times in order to double check the cost but the extra postprocessing steps have thus far not changed the cost)

import random
from sorting import *

#randomly choosing the number of items from a list 
item_number_list = [1000, 1200, 1300, 800, 900]
item_number = random.choice(item_number_list)
print(item_number)

#randomly assigning volumes valued between 1 and 20 to the items
item_volume = {}
for i in range(item_number):
    item_volume["i" + str(i+1)] = random.randint(1, 20)
print(item_volume)

#choosing the number of bins (number of items / 2) 
bin_number = int(item_number / 2)

#randomly assigning volumes valued between 20 and 60 and costs valued between 1 and 10 to the bins 
bin_volume = {}
bin_cost = {}
for i in range(bin_number):
    bin_volume["b" + str(i+1)] = random.randint(20, 60)
    bin_cost["b" + str(i+1)] = random.randint(1, 10)
print(bin_volume)
print(bin_cost)


#item_volume = {'i1': 8, 'i2': 20, 'i3': 12, 'i4': 8, 'i5': 1, 'i6': 3, 'i7': 20, 'i8': 15, 'i9': 17, 'i10': 2, 'i11': 6, 'i12': 2, 'i13': 18, 'i14': 9, 'i15': 13, 'i16': 17, 'i17': 14, 'i18': 10, 'i19': 10, 'i20': 7, 'i21': 17, 'i22': 8, 'i23': 20, 'i24': 17, 'i25': 6, 'i26': 13, 'i27': 6, 'i28': 18, 'i29': 9, 'i30': 4, 'i31': 11, 'i32': 9, 'i33': 10, 'i34': 11, 'i35': 11, 'i36': 6, 'i37': 17, 'i38': 5, 'i39': 13, 'i40': 2, 'i41': 7, 'i42': 5, 'i43': 14, 'i44': 8, 'i45': 2, 'i46': 4, 'i47': 7, 'i48': 11, 'i49': 10, 'i50': 10, 'i51': 14, 'i52': 20, 'i53': 16, 'i54': 19, 'i55': 10, 'i56': 18, 'i57': 4, 'i58': 14, 'i59': 6, 'i60': 17, 'i61': 2, 'i62': 6, 'i63': 13, 'i64': 8, 'i65': 11, 'i66': 5, 'i67': 14, 'i68': 7, 'i69': 14, 'i70': 17, 'i71': 2, 'i72': 3, 'i73': 5, 'i74': 10, 'i75': 20, 'i76': 4, 'i77': 2, 'i78': 20, 'i79': 9, 'i80': 4, 'i81': 6, 'i82': 4, 'i83': 6, 'i84': 4, 'i85': 12, 'i86': 20, 'i87': 8, 'i88': 10, 'i89': 7, 'i90': 1, 'i91': 1, 'i92': 11, 'i93': 14, 'i94': 8, 'i95': 15, 'i96': 18, 'i97': 3, 'i98': 3, 'i99': 9, 'i100': 18, 'i101': 8, 'i102': 8, 'i103': 18, 'i104': 20, 'i105': 14, 'i106': 8, 'i107': 8, 'i108': 19, 'i109': 11, 'i110': 12, 'i111': 8, 'i112': 19, 'i113': 6, 'i114': 19, 'i115': 20, 'i116': 20, 'i117': 11, 'i118': 16, 'i119': 8, 'i120': 7, 'i121': 3, 'i122': 13, 'i123': 3, 'i124': 2, 'i125': 5, 'i126': 11, 'i127': 1, 'i128': 3, 'i129': 10, 'i130': 7, 'i131': 15, 'i132': 5, 'i133': 15, 'i134': 1, 'i135': 6, 'i136': 6, 'i137': 9, 'i138': 20, 'i139': 10, 'i140': 3, 'i141': 5, 'i142': 8, 'i143': 17, 'i144': 11, 'i145': 1, 'i146': 10, 'i147': 20, 'i148': 8, 'i149': 18, 'i150': 14, 'i151': 19, 'i152': 6, 'i153': 19, 'i154': 20, 'i155': 2, 'i156': 11, 'i157': 14, 'i158': 8, 'i159': 8, 'i160': 7, 'i161': 19, 'i162': 4, 'i163': 3, 'i164': 6, 'i165': 14, 'i166': 11, 'i167': 17, 'i168': 16, 'i169': 10, 'i170': 9, 'i171': 10, 'i172': 6, 'i173': 12, 'i174': 8, 'i175': 11, 'i176': 15, 'i177': 15, 'i178': 10, 'i179': 18, 'i180': 4, 'i181': 1, 'i182': 6, 'i183': 19, 'i184': 15, 'i185': 4, 'i186': 1, 'i187': 9, 'i188': 17, 'i189': 10, 'i190': 11, 'i191': 11, 'i192': 8, 'i193': 7, 'i194': 19, 'i195': 17, 'i196': 6, 'i197': 12, 'i198': 17, 'i199': 2, 'i200': 20, 'i201': 13, 'i202': 5, 'i203': 9, 'i204': 11, 'i205': 3, 'i206': 16, 'i207': 19, 'i208': 10, 'i209': 7, 'i210': 20, 'i211': 16, 'i212': 14, 'i213': 14, 'i214': 9, 'i215': 6, 'i216': 10, 'i217': 12, 'i218': 7, 'i219': 7, 'i220': 5, 'i221': 7, 'i222': 6, 'i223': 1, 'i224': 8, 'i225': 5, 'i226': 2, 'i227': 8, 'i228': 13, 'i229': 6, 'i230': 6, 'i231': 10, 'i232': 19, 'i233': 13, 'i234': 14, 'i235': 4, 'i236': 4, 'i237': 15, 'i238': 17, 'i239': 15, 'i240': 13, 'i241': 11, 'i242': 13, 'i243': 19, 'i244': 14, 'i245': 16, 'i246': 14, 'i247': 4, 'i248': 9, 'i249': 8, 'i250': 3, 'i251': 8, 'i252': 19, 'i253': 15, 'i254': 1, 'i255': 13, 'i256': 16, 'i257': 10, 'i258': 7, 'i259': 17, 'i260': 10, 'i261': 13, 'i262': 2, 'i263': 20, 'i264': 20, 'i265': 17, 'i266': 6, 'i267': 6, 'i268': 6, 'i269': 9, 'i270': 15, 'i271': 19, 'i272': 19, 'i273': 10, 'i274': 10, 'i275': 16, 'i276': 17, 'i277': 15, 'i278': 9, 'i279': 19, 'i280': 10, 'i281': 12, 'i282': 7, 'i283': 8, 'i284': 6, 'i285': 7, 'i286': 4, 'i287': 8, 'i288': 10, 'i289': 17, 'i290': 4, 'i291': 15, 'i292': 16, 'i293': 8, 'i294': 4, 'i295': 2, 'i296': 20, 'i297': 13, 'i298': 18, 'i299': 4, 'i300': 3, 'i301': 10, 'i302': 8, 'i303': 6, 'i304': 5, 'i305': 13, 'i306': 6, 'i307': 20, 'i308': 2, 'i309': 17, 'i310': 1, 'i311': 7, 'i312': 14, 'i313': 3, 'i314': 20, 'i315': 5, 'i316': 17, 'i317': 13, 'i318': 9, 'i319': 5, 'i320': 1, 'i321': 12, 'i322': 13, 'i323': 11, 'i324': 10, 'i325': 6, 'i326': 11, 'i327': 1, 'i328': 2, 'i329': 14, 'i330': 4, 'i331': 11, 'i332': 2, 'i333': 17, 'i334': 8, 'i335': 20, 'i336': 20, 'i337': 9, 'i338': 4, 'i339': 20, 'i340': 9, 'i341': 7, 'i342': 19, 'i343': 18, 'i344': 9, 'i345': 11, 'i346': 7, 'i347': 12, 'i348': 12, 'i349': 17, 'i350': 14, 'i351': 20, 'i352': 11, 'i353': 7, 'i354': 5, 'i355': 11, 'i356': 10, 'i357': 16, 'i358': 15, 'i359': 4, 'i360': 17, 'i361': 20, 'i362': 16, 'i363': 2, 'i364': 17, 'i365': 11, 'i366': 12, 'i367': 10, 'i368': 3, 'i369': 3, 'i370': 2, 'i371': 13, 'i372': 14, 'i373': 1, 'i374': 2, 'i375': 18, 'i376': 10, 'i377': 11, 'i378': 19, 'i379': 12, 'i380': 4, 'i381': 9, 'i382': 9, 'i383': 8, 'i384': 1, 'i385': 15, 'i386': 10, 'i387': 9, 'i388': 13, 'i389': 14, 'i390': 14, 'i391': 16, 'i392': 6, 'i393': 9, 'i394': 12, 'i395': 9, 'i396': 16, 'i397': 18, 'i398': 9, 'i399': 5, 'i400': 20, 'i401': 4, 'i402': 19, 'i403': 6, 'i404': 11, 'i405': 9, 'i406': 20, 'i407': 14, 'i408': 16, 'i409': 9, 'i410': 1, 'i411': 17, 'i412': 8, 'i413': 11, 'i414': 16, 'i415': 4, 'i416': 9, 'i417': 12, 'i418': 9, 'i419': 17, 'i420': 7, 'i421': 6, 'i422': 16, 'i423': 4, 'i424': 17, 'i425': 17, 'i426': 6, 'i427': 14, 'i428': 1, 'i429': 19, 'i430': 13, 'i431': 7, 'i432': 3, 'i433': 13, 'i434': 19, 'i435': 20, 'i436': 2, 'i437': 6, 'i438': 5, 'i439': 8, 'i440': 20, 'i441': 14, 'i442': 19, 'i443': 17, 'i444': 16, 'i445': 17, 'i446': 18, 'i447': 8, 'i448': 1, 'i449': 18, 'i450': 8, 'i451': 3, 'i452': 8, 'i453': 9, 'i454': 19, 'i455': 8, 'i456': 6, 'i457': 12, 'i458': 8, 'i459': 9, 'i460': 10, 'i461': 18, 'i462': 12, 'i463': 7, 'i464': 17, 'i465': 16, 'i466': 9, 'i467': 9, 'i468': 15, 'i469': 16, 'i470': 4, 'i471': 10, 'i472': 4, 'i473': 2, 'i474': 4, 'i475': 14, 'i476': 10, 'i477': 12, 'i478': 7, 'i479': 9, 'i480': 11, 'i481': 2, 'i482': 20, 'i483': 12, 'i484': 15, 'i485': 17, 'i486': 16, 'i487': 1, 'i488': 10, 'i489': 5, 'i490': 2, 'i491': 15, 'i492': 16, 'i493': 14, 'i494': 4, 'i495': 9, 'i496': 17, 'i497': 9, 'i498': 16, 'i499': 17, 'i500': 16, 'i501': 5, 'i502': 2, 'i503': 13, 'i504': 2, 'i505': 10, 'i506': 11, 'i507': 10, 'i508': 18, 'i509': 16, 'i510': 4, 'i511': 16, 'i512': 17, 'i513': 1, 'i514': 2, 'i515': 13, 'i516': 2, 'i517': 15, 'i518': 11, 'i519': 15, 'i520': 4, 'i521': 12, 'i522': 3, 'i523': 6, 'i524': 19, 'i525': 8, 'i526': 1, 'i527': 3, 'i528': 18, 'i529': 11, 'i530': 11, 'i531': 15, 'i532': 11, 'i533': 2, 'i534': 5, 'i535': 3, 'i536': 12, 'i537': 8, 'i538': 11, 'i539': 7, 'i540': 19, 'i541': 12, 'i542': 11, 'i543': 18, 'i544': 3, 'i545': 7, 'i546': 13, 'i547': 8, 'i548': 10, 'i549': 5, 'i550': 12, 'i551': 13, 'i552': 18, 'i553': 7, 'i554': 3, 'i555': 14, 'i556': 3, 'i557': 5, 'i558': 20, 'i559': 20, 'i560': 7, 'i561': 9, 'i562': 8, 'i563': 19, 'i564': 5, 'i565': 15, 'i566': 19, 'i567': 3, 'i568': 15, 'i569': 8, 'i570': 14, 'i571': 10, 'i572': 10, 'i573': 13, 'i574': 12, 'i575': 5, 'i576': 12, 'i577': 10, 'i578': 13, 'i579': 5, 'i580': 17, 'i581': 9, 'i582': 15, 'i583': 11, 'i584': 10, 'i585': 10, 'i586': 10, 'i587': 7, 'i588': 1, 'i589': 5, 'i590': 1, 'i591': 4, 'i592': 3, 'i593': 14, 'i594': 17, 'i595': 1, 'i596': 13, 'i597': 16, 'i598': 15, 'i599': 3, 'i600': 19}

#bin_volume = {'b1': 42, 'b2': 41, 'b3': 23, 'b4': 40, 'b5': 27, 'b6': 56, 'b7': 53, 'b8': 59, 'b9': 44, 'b10': 20, 'b11': 42, 'b12': 41, 'b13': 22, 'b14': 34, 'b15': 26, 'b16': 52, 'b17': 36, 'b18': 20, 'b19': 38, 'b20': 36, 'b21': 40, 'b22': 57, 'b23': 25, 'b24': 56, 'b25': 58, 'b26': 58, 'b27': 45, 'b28': 51, 'b29': 54, 'b30': 44, 'b31': 41, 'b32': 39, 'b33': 46, 'b34': 38, 'b35': 40, 'b36': 36, 'b37': 26, 'b38': 56, 'b39': 34, 'b40': 53, 'b41': 41, 'b42': 52, 'b43': 31, 'b44': 51, 'b45': 53, 'b46': 60, 'b47': 51, 'b48': 42, 'b49': 51, 'b50': 49, 'b51': 59, 'b52': 58, 'b53': 60, 'b54': 36, 'b55': 31, 'b56': 58, 'b57': 51, 'b58': 46, 'b59': 29, 'b60': 44, 'b61': 56, 'b62': 37, 'b63': 56, 'b64': 20, 'b65': 55, 'b66': 37, 'b67': 49, 'b68': 35, 'b69': 39, 'b70': 43, 'b71': 60, 'b72': 25, 'b73': 44, 'b74': 31, 'b75': 20, 'b76': 54, 'b77': 52, 'b78': 53, 'b79': 56, 'b80': 55, 'b81': 31, 'b82': 40, 'b83': 53, 'b84': 20, 'b85': 56, 'b86': 25, 'b87': 48, 'b88': 25, 'b89': 56, 'b90': 27, 'b91': 47, 'b92': 38, 'b93': 32, 'b94': 58, 'b95': 34, 'b96': 22, 'b97': 22, 'b98': 43, 'b99': 36, 'b100': 49, 'b101': 42, 'b102': 30, 'b103': 20, 'b104': 42, 'b105': 56, 'b106': 37, 'b107': 52, 'b108': 25, 'b109': 25, 'b110': 34, 'b111': 38, 'b112': 44, 'b113': 41, 'b114': 44, 'b115': 35, 'b116': 41, 'b117': 29, 'b118': 52, 'b119': 32, 'b120': 25, 'b121': 49, 'b122': 27, 'b123': 52, 'b124': 22, 'b125': 30, 'b126': 57, 'b127': 42, 'b128': 23, 'b129': 21, 'b130': 24, 'b131': 26, 'b132': 27, 'b133': 23, 'b134': 43, 'b135': 34, 'b136': 52, 'b137': 59, 'b138': 37, 'b139': 50, 'b140': 36, 'b141': 40, 'b142': 46, 'b143': 60, 'b144': 25, 'b145': 58, 'b146': 34, 'b147': 42, 'b148': 49, 'b149': 39, 'b150': 38, 'b151': 46, 'b152': 39, 'b153': 40, 'b154': 32, 'b155': 56, 'b156': 26, 'b157': 53, 'b158': 52, 'b159': 27, 'b160': 37, 'b161': 39, 'b162': 41, 'b163': 60, 'b164': 46, 'b165': 31, 'b166': 55, 'b167': 54, 'b168': 38, 'b169': 36, 'b170': 36, 'b171': 51, 'b172': 35, 'b173': 27, 'b174': 56, 'b175': 60, 'b176': 38, 'b177': 21, 'b178': 53, 'b179': 44, 'b180': 28, 'b181': 40, 'b182': 30, 'b183': 60, 'b184': 56, 'b185': 45, 'b186': 28, 'b187': 33, 'b188': 36, 'b189': 36, 'b190': 21, 'b191': 44, 'b192': 43, 'b193': 27, 'b194': 32, 'b195': 53, 'b196': 57, 'b197': 45, 'b198': 60, 'b199': 58, 'b200': 46, 'b201': 53, 'b202': 48, 'b203': 56, 'b204': 41, 'b205': 42, 'b206': 35, 'b207': 35, 'b208': 60, 'b209': 50, 'b210': 20, 'b211': 45, 'b212': 46, 'b213': 30, 'b214': 36, 'b215': 37, 'b216': 32, 'b217': 59, 'b218': 60, 'b219': 47, 'b220': 56, 'b221': 43, 'b222': 52, 'b223': 43, 'b224': 54, 'b225': 25, 'b226': 21, 'b227': 41, 'b228': 22, 'b229': 30, 'b230': 36, 'b231': 50, 'b232': 46, 'b233': 39, 'b234': 58, 'b235': 35, 'b236': 40, 'b237': 58, 'b238': 51, 'b239': 48, 'b240': 44, 'b241': 56, 'b242': 28, 'b243': 34, 'b244': 30, 'b245': 34, 'b246': 40, 'b247': 58, 'b248': 27, 'b249': 59, 'b250': 34, 'b251': 43, 'b252': 22, 'b253': 34, 'b254': 39, 'b255': 51, 'b256': 36, 'b257': 56, 'b258': 22, 'b259': 60, 'b260': 35, 'b261': 43, 'b262': 25, 'b263': 37, 'b264': 46, 'b265': 49, 'b266': 55, 'b267': 54, 'b268': 32, 'b269': 45, 'b270': 37, 'b271': 20, 'b272': 35, 'b273': 52, 'b274': 49, 'b275': 56, 'b276': 48, 'b277': 27, 'b278': 30, 'b279': 41, 'b280': 24, 'b281': 35, 'b282': 26, 'b283': 58, 'b284': 26, 'b285': 50, 'b286': 23, 'b287': 54, 'b288': 43, 'b289': 48, 'b290': 36, 'b291': 46, 'b292': 57, 'b293': 58, 'b294': 32, 'b295': 55, 'b296': 35, 'b297': 27, 'b298': 55, 'b299': 20, 'b300': 48}

#bin_cost = {'b1': 1, 'b2': 3, 'b3': 1, 'b4': 8, 'b5': 3, 'b6': 5, 'b7': 6, 'b8': 5, 'b9': 10, 'b10': 10, 'b11': 4, 'b12': 5, 'b13': 9, 'b14': 9, 'b15': 2, 'b16': 5, 'b17': 10, 'b18': 7, 'b19': 1, 'b20': 5, 'b21': 4, 'b22': 2, 'b23': 4, 'b24': 1, 'b25': 10, 'b26': 2, 'b27': 4, 'b28': 10, 'b29': 7, 'b30': 5, 'b31': 10, 'b32': 9, 'b33': 7, 'b34': 10, 'b35': 2, 'b36': 9, 'b37': 2, 'b38': 9, 'b39': 1, 'b40': 1, 'b41': 8, 'b42': 6, 'b43': 4, 'b44': 3, 'b45': 1, 'b46': 7, 'b47': 5, 'b48': 3, 'b49': 7, 'b50': 7, 'b51': 3, 'b52': 5, 'b53': 6, 'b54': 1, 'b55': 1, 'b56': 9, 'b57': 7, 'b58': 8, 'b59': 8, 'b60': 1, 'b61': 3, 'b62': 4, 'b63': 8, 'b64': 8, 'b65': 9, 'b66': 3, 'b67': 8, 'b68': 7, 'b69': 5, 'b70': 2, 'b71': 5, 'b72': 2, 'b73': 4, 'b74': 8, 'b75': 7, 'b76': 2, 'b77': 5, 'b78': 8, 'b79': 2, 'b80': 1, 'b81': 1, 'b82': 6, 'b83': 7, 'b84': 1, 'b85': 8, 'b86': 7, 'b87': 2, 'b88': 3, 'b89': 10, 'b90': 9, 'b91': 10, 'b92': 1, 'b93': 6, 'b94': 4, 'b95': 10, 'b96': 4, 'b97': 6, 'b98': 9, 'b99': 1, 'b100': 4, 'b101': 1, 'b102': 7, 'b103': 5, 'b104': 1, 'b105': 7, 'b106': 6, 'b107': 5, 'b108': 4, 'b109': 7, 'b110': 9, 'b111': 1, 'b112': 4, 'b113': 2, 'b114': 8, 'b115': 3, 'b116': 2, 'b117': 6, 'b118': 1, 'b119': 10, 'b120': 4, 'b121': 7, 'b122': 2, 'b123': 8, 'b124': 4, 'b125': 4, 'b126': 5, 'b127': 8, 'b128': 8, 'b129': 3, 'b130': 5, 'b131': 5, 'b132': 7, 'b133': 4, 'b134': 7, 'b135': 10, 'b136': 6, 'b137': 9, 'b138': 10, 'b139': 7, 'b140': 3, 'b141': 3, 'b142': 7, 'b143': 6, 'b144': 3, 'b145': 10, 'b146': 4, 'b147': 7, 'b148': 7, 'b149': 9, 'b150': 8, 'b151': 1, 'b152': 7, 'b153': 4, 'b154': 3, 'b155': 5, 'b156': 10, 'b157': 5, 'b158': 3, 'b159': 3, 'b160': 8, 'b161': 4, 'b162': 10, 'b163': 9, 'b164': 2, 'b165': 6, 'b166': 1, 'b167': 5, 'b168': 5, 'b169': 8, 'b170': 6, 'b171': 10, 'b172': 8, 'b173': 10, 'b174': 3, 'b175': 2, 'b176': 1, 'b177': 8, 'b178': 7, 'b179': 2, 'b180': 5, 'b181': 1, 'b182': 7, 'b183': 2, 'b184': 10, 'b185': 3, 'b186': 7, 'b187': 10, 'b188': 9, 'b189': 7, 'b190': 2, 'b191': 10, 'b192': 2, 'b193': 6, 'b194': 2, 'b195': 6, 'b196': 2, 'b197': 4, 'b198': 5, 'b199': 4, 'b200': 8, 'b201': 1, 'b202': 5, 'b203': 8, 'b204': 7, 'b205': 9, 'b206': 9, 'b207': 3, 'b208': 10, 'b209': 2, 'b210': 5, 'b211': 8, 'b212': 5, 'b213': 7, 'b214': 9, 'b215': 5, 'b216': 1, 'b217': 10, 'b218': 3, 'b219': 3, 'b220': 5, 'b221': 8, 'b222': 8, 'b223': 10, 'b224': 4, 'b225': 7, 'b226': 1, 'b227': 4, 'b228': 4, 'b229': 8, 'b230': 1, 'b231': 9, 'b232': 4, 'b233': 9, 'b234': 5, 'b235': 8, 'b236': 7, 'b237': 7, 'b238': 1, 'b239': 3, 'b240': 4, 'b241': 8, 'b242': 10, 'b243': 5, 'b244': 7, 'b245': 7, 'b246': 8, 'b247': 5, 'b248': 3, 'b249': 8, 'b250': 3, 'b251': 10, 'b252': 3, 'b253': 7, 'b254': 8, 'b255': 4, 'b256': 7, 'b257': 8, 'b258': 2, 'b259': 9, 'b260': 1, 'b261': 10, 'b262': 4, 'b263': 8, 'b264': 4, 'b265': 7, 'b266': 10, 'b267': 8, 'b268': 7, 'b269': 5, 'b270': 3, 'b271': 4, 'b272': 10, 'b273': 5, 'b274': 7, 'b275': 10, 'b276': 7, 'b277': 3, 'b278': 1, 'b279': 6, 'b280': 3, 'b281': 5, 'b282': 6, 'b283': 9, 'b284': 7, 'b285': 4, 'b286': 6, 'b287': 7, 'b288': 9, 'b289': 10, 'b290': 5, 'b291': 3, 'b292': 3, 'b293': 1, 'b294': 4, 'b295': 1, 'b296': 9, 'b297': 7, 'b298': 7, 'b299': 5, 'b300': 2} 



#ordering items in I according to non-increasing order of volume
ordered_items = []
for key in item_volume:
    ordered_items.append(key)
item_sort(item_volume, ordered_items, 0, len(ordered_items)-1) 
print("ordered items: " + str(ordered_items))


#ordering bins in K according to non-decreasing order of the ratio c_j/V_j and non-decreasing order of V_j when the cost ratios c_j/V_j are equal
ordered_bins = []
cv_ratio = {} 
for key in bin_volume: 
    ordered_bins.append(key)
    cv_ratio[key] = bin_cost[key] / bin_volume[key]
bin_sort_cv(cv_ratio, bin_volume, ordered_bins, 0, len(ordered_bins)-1)
print("cv ratio: " + str(cv_ratio))
print("ordered bins " + str(ordered_bins))


#defining filled bins set S
filled_bins = {}
filled_bin_volume = {}
ordered_filled_bins = []
print(ordered_items)
print(ordered_bins)


#placing items in bins
for i in ordered_items: 
    print(ordered_filled_bins)

    #if S is empty, put the largest item i into the first bin in K that accomodates i
    if len(ordered_filled_bins) == 0: 
        for l in ordered_bins:
            print("i: " + str(i))
            print("l: " + str(l))
            if item_volume[i] > bin_volume[l]:
                print("item volume:  " + str(item_volume[i]))
                print("bin volume: " + str(bin_volume[l]))
                print("item " + str(i) + " of volume " + str(item_volume[i]) + " too large for bin " + str(l) + " with volume " + str(bin_volume[l]))
                continue 
            print("item volume:  " + str(item_volume[i]))
            print("bin volume: " + str(bin_volume[l]))
            print("item " + str(i) + " of volume " + str(item_volume[i]) + " fits in bin " + str(l) + " with volume " + str(bin_volume[l]))
            filled_bins[l] = [i]
            filled_bin_volume[l] = bin_volume[l] - item_volume[i]
            ordered_filled_bins.append(l)
            #ordering bins in S according to non-increasing order of remaining volume and non-decreasing order of c_j/V_j when the remaining volumes are equal  
            bin_sort_volume(cv_ratio, filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins) - 1)
            print("filled bins: " + str(filled_bins))
            print("ordered filled bins: " + str(ordered_filled_bins))
            print("filled bin volume: " + str(filled_bin_volume))
            break

    else: 
        #if S is not empty, and if i can be accomodated into a bin in S, then place it into the bin in S with the max free space
        for b in ordered_filled_bins:
            print("i: " + str(i))
            print("b: " + str(b))
            print("item volume:  " + str(item_volume[i]))
            print("bin volume: " + str(filled_bin_volume[b]))
            if item_volume[i] <= filled_bin_volume[b]:
                print("item " + str(i) + " of volume " + str(item_volume[i]) + " fits in bin " + str(b) + " with remaining volume " + str(filled_bin_volume[b]))
                filled_bins[b].append(i)
                filled_bin_volume[b] = filled_bin_volume[b] - item_volume[i]
                #ordering bins in S according to non-increasing order of remaining volume and non-decreasing order of c_j/V_j when the remaining volumes are equal
                bin_sort_volume(cv_ratio, filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins) - 1)
                print("filled bins: " + str(filled_bins))
                print("ordered filled bins: " + str(ordered_filled_bins))
                print("filled bin volume: " + str(filled_bin_volume))
                break 

            #if S is not empty and if i cannot be accomodated into a bin in S, then place it into the first bin in K that can accommodate i
            if b == ordered_filled_bins[len(ordered_filled_bins)-1]:
                if item_volume[i] > filled_bin_volume[b]:
                    print("item " + str(i) + " of volume " + str(item_volume[i]) + " too large for bin " + str(b) + " with remaining volume " + str(filled_bin_volume[b]))
                    for j in ordered_bins:
                        print("i: " + str(i))
                        print("j: " + str(j))
                        print("item volume " + str(item_volume[i]))
                        print("new bin volume " + str(bin_volume[j]))
                        if j in filled_bins: 
                            print(str(j) + " is in filled_bins")
                            continue
                        if item_volume[i] > bin_volume[j]: 
                            print("item " + str(i) + " of volume " + str(item_volume[i]) + " too large for new bin " + str(j) + " with volume " + str(bin_volume[j]))
                            continue
                        print("item " + str(i) + " of volume " + str(item_volume[i]) + " fits in new bin " + str(j) + " with volume " + str(bin_volume[j]))
                        filled_bins[j] = [i]
                        filled_bin_volume[j] = bin_volume[j] - item_volume[i]
                        ordered_filled_bins.append(j)
                        #ordering bins in S according to non-increasing order of remaining volume and non-decreasing order of c_j/V_j when the remaining volumes are equal
                        bin_sort_volume(cv_ratio, filled_bin_volume, ordered_filled_bins, 0, len(ordered_filled_bins) - 1) 
                        print("filled bins: " + str(filled_bins))
                        print("ordered filled bins: " + str(ordered_filled_bins))
                        print("filled bin volume: " + str(filled_bin_volume))
                        break
                    break
print(filled_bins)
cost = 0
for b in filled_bins:
    cost+=bin_cost[b]
print(cost)


#defining unfilled bin set K\S
unfilled_bins = [] 
for j in ordered_bins: 
    if j not in ordered_filled_bins: 
        unfilled_bins.append(j)
#print(unfilled_bins)
#print(item_volume)


print(ordered_filled_bins)

print(item_volume)
print(bin_volume)
print(bin_cost)

print("original cost: " + str(cost))

#ordering bins in K\S according to non-decreasing order of cost and non-increasing order of volume when costs are equal  
bin_sort_cost(bin_cost, bin_volume, unfilled_bins, 0, len(unfilled_bins) -1)
for n in range(len(ordered_filled_bins)):
    #print(n)
    b = ordered_filled_bins[n]
    #print(b)
    v_b = 0
    for i in filled_bins[b]:
        v_b += item_volume[i]
    for k in unfilled_bins:
        #print("k: " + str(k) + " volume: " + str(bin_volume[k]))
        #print( "bin: " + str(b) + " item volume: " + str(v_b))
        #print( "k: " + str(k) + " bin cost: " + str(bin_cost[k]))
        #print( "b: " + str(b) + " bin cost: " + str(bin_cost[b]))
        if (bin_volume[k] >= v_b) and (bin_cost[k] < bin_cost[b]):
            filled_bins[k] = filled_bins[b]
            filled_bin_volume[k] = bin_volume[k] - v_b
            del filled_bins[b]
            del filled_bin_volume[b]
            unfilled_bins.append(b)
            unfilled_bins.remove(k)
            #print(filled_bins)
            #print(filled_bin_volume)
            ordered_filled_bins[n] = k
            #print(ordered_filled_bins)
            bin_sort_cost(bin_cost, bin_volume, unfilled_bins, 0, len(unfilled_bins) -1)
            #print(unfilled_bins)
            break



cost = 0
for b in filled_bins: 
    cost += bin_cost[b]
print("final cost: " + str(cost))

for n in range(len(ordered_filled_bins)):
    #print(n)
    b = ordered_filled_bins[n]
    #print(b)
    v_b = 0
    for i in filled_bins[b]:
        v_b += item_volume[i]
    for k in unfilled_bins:
        #print("k: " + str(k) + " volume: " + str(bin_volume[k]))
        #print( "bin: " + str(b) + " item volume: " + str(v_b))
        #print( "k: " + str(k) + " bin cost: " + str(bin_cost[k]))
        #print( "b: " + str(b) + " bin cost: " + str(bin_cost[b]))
        if (bin_volume[k] >= v_b) and (bin_cost[k] < bin_cost[b]):
            print("k: " + str(k) + " volume: " + str(bin_volume[k]))
            print( "bin: " + str(b) + " item volume: " + str(v_b))
            print( "k: " + str(k) + " bin cost: " + str(bin_cost[k]))
            print( "b: " + str(b) + " bin cost: " + str(bin_cost[b]))
            filled_bins[k] = filled_bins[b]
            filled_bin_volume[k] = bin_volume[k] - v_b
            del filled_bins[b]
            del filled_bin_volume[b]
            unfilled_bins.append(b)
            unfilled_bins.remove(k)
            #print(filled_bins)
            #print(filled_bin_volume)
            ordered_filled_bins[n] = k
            #print(ordered_filled_bins)
            bin_sort_cost(bin_cost, bin_volume, unfilled_bins, 0, len(unfilled_bins) -1)
            #print(unfilled_bins)
            break 

for i in item_volume: 
    for b in ordered_filled_bins:
        if i in filled_bins[b]: 
            break
        if b == ordered_filled_bins[len(ordered_filled_bins)-1]: 
            if i not in filled_bins[b]: 
                print(i)

cost = 0
for b in filled_bins:
    cost += bin_cost[b]
print("final cost: " + str(cost))

for n in range(len(ordered_filled_bins)):
    #print(n)
    b = ordered_filled_bins[n]
    #print(b)
    v_b = 0
    for i in filled_bins[b]:
        v_b += item_volume[i]
    for k in unfilled_bins:
        #print("k: " + str(k) + " volume: " + str(bin_volume[k]))
        #print( "bin: " + str(b) + " item volume: " + str(v_b))
        #print( "k: " + str(k) + " bin cost: " + str(bin_cost[k]))
        #print( "b: " + str(b) + " bin cost: " + str(bin_cost[b]))
        if (bin_volume[k] >= v_b) and (bin_cost[k] < bin_cost[b]):
            print("k: " + str(k) + " volume: " + str(bin_volume[k]))
            print( "bin: " + str(b) + " item volume: " + str(v_b))
            print( "k: " + str(k) + " bin cost: " + str(bin_cost[k]))
            print( "b: " + str(b) + " bin cost: " + str(bin_cost[b]))
            filled_bins[k] = filled_bins[b]
            filled_bin_volume[k] = bin_volume[k] - v_b
            del filled_bins[b]
            del filled_bin_volume[b]
            unfilled_bins.append(b)
            unfilled_bins.remove(k)
            #print(filled_bins)
            #print(filled_bin_volume)
            ordered_filled_bins[n] = k
            #print(ordered_filled_bins)
            bin_sort_cost(bin_cost, bin_volume, unfilled_bins, 0, len(unfilled_bins) -1)
            #print(unfilled_bins)
            break

cost = 0
for b in filled_bins:
    cost += bin_cost[b]
print("final cost: " + str(cost))

print(filled_bins)
