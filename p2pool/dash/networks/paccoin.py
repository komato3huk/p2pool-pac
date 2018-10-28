import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'c8e5612c'.decode('hex')
P2P_PORT = 7112
ADDRESS_VERSION = 55
SCRIPT_ADDRESS_VERSION = 10
RPC_PORT = 7111
RPC_CHECK = defer.inlineCallbacks(lambda dashd: defer.returnValue(
            'paccoinaddress' in (yield dashd.rpc_help()) and
            not (yield dashd.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('dash_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('dash_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'PAC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'PaccoinCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/PaccoinCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.paccoincore'), 'dash.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://usa.pacblockexplorer.com:3002/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://usa.pacblockexplorer.com:3002/address/'
TX_EXPLORER_URL_PREFIX = 'http://usa.pacblockexplorer.com:3002/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUST_THRESHOLD = 0.001e8
