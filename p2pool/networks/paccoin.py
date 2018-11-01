from p2pool.dash import networks

PARENT = networks.nets['paccoin']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
IDENTIFIER = '1C018FE4180BA411'.decode('hex')
PREFIX = '1C018FE1C3FFC012'.decode('hex')
COINBASEEXT = '2f5032506f6f6c2d5041432f'.decode('hex')
P2P_PORT = 2967
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 2968
BOOTSTRAP_ADDRS = 'p2p-spb.xyz p2p-south.xyz p2p-usa.xyz nn.p2pool.site msk.p2pool.site'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-pac'
VERSION_CHECK = lambda v: None if 1250100 <= v else 'Paccoin version too old. Upgrade to 12.5.1 or newer!'
