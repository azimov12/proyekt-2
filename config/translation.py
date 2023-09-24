from modeltranslation.translator import TranslationOptions, translator
from polls.models import Noutbook

class NoutbookModelTranslationOptions(TranslationOptions):
    fields = ('noutbook_name', 'information')  


translator.register(Noutbook, NoutbookModelTranslationOptions)