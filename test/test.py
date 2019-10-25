from spoken2written.utils import Units,Currency,Decontraction
from spoken2written.text2digits import Text2Digits

DISTANCE = {
    'centimeter':'cm',
    'meter':'m',
    'millimeters':'mm',
    'kilometer':'km',
    'miles':'mi',
    'foot':'ft' }

WEIGHTS = {
    'tonne':'t',
    'kilogram':'kg',
    'hectogram':'hg',
    'decagram':'dag',
    'gram':'g',
    'decigram':'dg',
    'centigram':'cg',
    'milligram':'mg'
}

spoken_text = """
    My mobile number is double nine nine five one six seven triple one. 
    The cost of mobile is 48 thousand rupees. It is not easy to crack UPSC examination. People do give double attempts to clear it.
    Double standards jokes aren't tolerate here.My weight is 54 kilogram.I live 16 kilometers away from my office.
    """ 


# decontraction: 

spoken_text = Decontraction.decontraction(spoken_text)
print("Text after decontraction:")
print(spoken_text)
print("-"*80)

# test_1 : numbers to digit coversion
spoken_text = Text2Digits().convert(spoken_text)

print("The text after numeric word to numbers is:")
print(spoken_text)
print("-"*80)

#currency replacement by symbol
spoken_text = Currency().currency(spoken_text)
print("After currency symbol replacement:")
print(spoken_text)
print("-"*80)

# Measurement replacements
spoken_text = Units.unit(spoken_text,WEIGHTS)
print("After units replacement by abbrevation:")
print(spoken_text)
print("-"*80)



