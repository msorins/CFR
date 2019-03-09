import os

class Config:
    UPLOAD_FOLDER = f'{os.getcwd()}/Uploads/'
    ALLOWED_EXTENSIONS = ['pdf']
    SECRET = 'IXN6K44L3WG2M1SCSW13HXQQ'
    SPELLCHECK_API_KEY = 'CC67BF08-E923-4088-8BC5-7C14A61B3D6A'
    BING_SPELLCHECK_KEY = 'bad43ccffa1040fe8844dea6137be049'
    BING_SPELLCHECK_ENDPOINT = 'https://api.cognitive.microsoft.com/bing/v7.0/SpellCheck'
