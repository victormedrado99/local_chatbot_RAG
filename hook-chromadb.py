from PyInstaller.utils.hooks import collect_all

# Coletar todos os submódulos do chromadb
datas, binaries, hiddenimports = collect_all('chromadb')

# Adicionar imports ocultos específicos que podem estar faltando
hiddenimports += [
    'chromadb.telemetry',
    'chromadb.telemetry.product',
    'chromadb.telemetry.product.posthog',
    'chromadb.api',
    'chromadb.config',
    'chromadb.db',
    'chromadb.db.impl',
    'chromadb.db.impl.sqlite',
    'sqlite3',
    'pysqlite3',
]
