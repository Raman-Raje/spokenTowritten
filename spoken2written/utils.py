import re
from forex_python.converter import CurrencyCodes
from corpussplit import CorpusSplit
from pickle import load,dump


class Currency():
    """
    This class contains all utility functions required.
    """
    def __init__(self):
        
        # Loading already stored dictionary file
        with open("currency_dict.pkl","rb") as f:
            self.currency_dict = load(f)

    def currency(self,raw_text):
        """
        This function converts text currency to symbolic currency.
        """
        substr_arr, punctuation_arr = CorpusSplit().get_substr_punctuation(raw_text)

        updated = []

        for sent in substr_arr:
            sent = sent.strip()
            original = sent
            currency = False
            try:
                for cur,abb in self.currency_dict.items():
                    # update currency to plural form.
                    # abbrevations not handled.
                    cur = cur.lower()

                    if re.search(r"\d\s\b{}[s]*\b".format(cur), sent):
                        sent = Currency.update_sentance(sent, cur)
                        currency = True

                    cur = cur.split()[-1]

                    if re.search(r"\d\s\b{}[s]*\b".format(cur), sent):
                        sent = Currency.update_sentance(sent, cur)
                        currency = True

                    sent = sent.replace("  ", " ")

                    if currency:
                        sent = Currency.update_currency(abb, sent)
                        currency = False

                updated.append(sent)

            except Exception as e:
                print("Exception Caught:",e)
                updated.append(original)

        raw_text = "".join([sstr + punct + " " for sstr, punct in zip(updated, punctuation_arr)])
        return raw_text


    @staticmethod
    def update_sentance(sent, cur):
        sent = re.sub(cur + 's', "@@", sent) if cur + 's' in sent else re.sub(cur, "@@", sent)
        return sent

    @staticmethod
    def update_currency(abb, sent):
        """
        This method adds currency symbol in the sentance.
        """
        sent_ = sent.split(" ")

        try:

            symbol = CurrencyCodes().get_symbol(abb)
            number = str(sent_[sent_.index("@@") - 1])
            number = str(symbol) + number

            sent_[sent_.index("@@") - 1] = number
            sent_.remove("@@")

            return " ".join(sent_)

        except:
            return sent
                    
class Decontraction():
    """
    This class is used for decontraction of joint words. i.e won't = will not
    """

    @staticmethod
    def decontraction(phrase):
        """
        This function converts joint words to seperate. i.e. decontraction.
        """
        substr_arr = phrase.split('.')
        updated = []

        for string in substr_arr:
            original = string
            
            try:
                updated.append(Decontraction.split(string))
            except:
                updated.append(original)

        #raw_text = "".join([sstr + punct + " " for sstr, punct in zip(updated, punctuation_arr)])
        raw_text = ".".join(updated)
        return raw_text

    @staticmethod
    def split(phrase):
        phrase = re.sub(r"won\'t", "will not", phrase)
        phrase = re.sub(r"can\'t", "can not", phrase)

        # general
        phrase = re.sub(r"n\'t", " not", phrase)
        phrase = re.sub(r"\'re", " are", phrase)
        phrase = re.sub(r"\'s", " is", phrase)
        phrase = re.sub(r"\'d", " would", phrase)
        phrase = re.sub(r"\'ll", " will", phrase)
        phrase = re.sub(r"\'t", " not", phrase)
        phrase = re.sub(r"\'ve", " have", phrase)
        phrase = re.sub(r"\'m", " am", phrase)
        return phrase
    

class Units():
    """
    This class replaces measurements units by their abbrevation.
    e.g Kilometer = Km , Centimeter = cm
    """

    @staticmethod
    def unit(phrase,scale):
        """
        This function replaces all the occurances of distances by thier abbrevations.
        """
        assert type(scale) == dict, "Not supported data type. Please provide dictionary key:Abbrevation"
        
        substr_arr, punctuation_arr = CorpusSplit().get_substr_punctuation(phrase)
        updated = []

        regrex = Units.get_regrex(scale)

        for sent in substr_arr:
            sent = sent.strip()
            original = sent

            try:
                for i in re.findall(regrex,sent):
                    sent = re.sub(r'\b{}[s]*\b'.format(i),scale[i],sent)
                updated.append(sent)
                    
            except Exception as e:
                print("Exception caught:",e)
                updated.append(original)
                
        raw_text = "".join([sstr + punct + " " for sstr, punct in zip(updated, punctuation_arr)])
        return raw_text

    @staticmethod
    def get_regrex(scale):
        return '|'.join(scale.keys())