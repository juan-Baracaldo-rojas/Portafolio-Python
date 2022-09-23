#import urllib.request
from ibm_watson import LanguageTranslatorV3
from ibm_watson import SpeechToTextV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize
from pandas import DataFrame as datF
url_s2t = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/233e20e0-803f-42ec-8b61-a7a3ddd4beba"
iam_apikey_s2t = "Qb50xmrBVuyB5Unk5YcHi_Ixmjuo5mcsvZKefAqBxWo6"
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
print(s2t)
print(type(s2t))
#url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/PolynomialRegressionandPipelines.mp3'
filename='PolynomialRegressionandPipelines.mp3'
#filename='pv.mp3'
#urllib.request.urlretrieve(url, filename)
with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
    #print(response.result)
    df=datF(json_normalize(response.result['results'],"alternatives"))
    print(df.head())
    print(response)
#Palabra a traducir 
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
print(type(recognized_text))
url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/29349739-555d-4690-99a0-18cdd6b1d7a4'
apikey_lt='KWRgB0jQZvH6_-lREzF8cxDEGRFB4x45rlH848Q8-5H1'
version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
print(language_translator)
json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
translation_response = language_translator.translate(\
    #text=recognized_text, model_id='es-en')
    text=recognized_text, model_id='en-es')
print(translation_response)
translation=translation_response.get_result()
print(translation)
spanish_translation =translation['translations'][0]['translation']
print(spanish_translation)
translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()
translation_eng=translation_new['translations'][0]['translation']
print(translation_eng)
French_translation=language_translator.translate(
    text=translation_eng , model_id='en-fr').get_result()

print(French_translation['translations'][0]['translation'])
