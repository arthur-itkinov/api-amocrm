from amocrm.v2 import tokens, Lead, Pipeline, Status, Company, Contact

with open('refresh_token.txt', 'r') as access:
    refresh_token = access.read()

tokens.default_token_manager(
    client_id="xxx", # client_id скопировать из настроек интеграции амосрм
    client_secret="xxx", # client_secret скопировать из настроек интеграции амосрм
    subdomain="xxx", # скопировать из настроек интеграции амосрм или из uri
    redirect_url="xxx", # скопировать из настроек интеграции амосрм
    storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
)
tokens.default_token_manager.init(code="xxx", skip_error=False) # cкопировать из настроек интеграции амосрм !!! действует 20 минут !!!
