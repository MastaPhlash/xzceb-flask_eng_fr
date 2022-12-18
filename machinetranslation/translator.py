from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv


load_dotenv('phlash.env')

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('url')
language_translator.set_disable_ssl_verification(True)
model_id = 'en-fr'
text_to_translate = 'Your content you want translate here'


def englishToFrench(englishText):
    
    #Translate
    translation = translatorInstance(apikey, url, englishText, 'en-fr')
    
    #Get translated text
    frenchText = translation['translations'][0]['translation']

    return frenchText


def frenchToEnglish(frenchText):
    
    #Translate
    translation = translatorInstance(apikey, url, frenchText, 'fr-en')
    
    #Get translated text
    englishText = translation['translations'][0]['translation']

    return englishText
