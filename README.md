# Spoken2written
A module for converting spoken English to written English. The layout/Class diagram of package is as follows.

![Package Layout](/images/layout.PNG)

## Features Implemented:
* Converted numerical words to digits.
    - double five == 55
    - triple nine eight four == 99984
* Decontraction of words.
* Currency representation.
* Units Abbrevations.
    - kilometer == km
    - meter == m


## Examples:
Let's have a look at some examples to gain more understanding.Below is the piece of spoken text taken for understading. 
```
    My mobile number is double nine nine five one six seven triple one. 
    The cost of mobile is 48 thousand rupees. 
    It is not easy to crack UPSC examination, people do give double attempts to clear it.
    Double standards jokes aren't tolerated here.
    My weight is 54 kilogram.I live 16 kilometers away from my office.
```
### Decontraction:
**Code**
```
    spoken_text = Decontraction.decontraction(spoken_text)
    print("Text after decontraction:")
    print(spoken_text)
```
**Output**
```
    My mobile number is double nine nine five one six seven triple one.
    The cost of mobile is 48 thousand rupees.
    It is not easy to crack UPSC examination, people do give double attempts to clear it.
    Double standards jokes are not tolerated here.
    My weight is 54 kilogram.I live 16 kilometers away from my office.
```
### numbers to digit coversion
**Code**
```
    spoken_text = Text2Digits().convert(spoken_text)
    print(spoken_text)
```
**Output**
```
    My mobile number is 9995167111.
    The cost of mobile is 48000 rupees.
    It is not easy to crack UPSC examination, people do give double attempts to clear it.
    Double standards jokes are not tolerated here.
    My weight is 54 kilogram. I live 16 kilometers away from my office.
```
### Currency Symbol
**Code**
```
    spoken_text = Currency().currency(spoken_text)
    print(spoken_text)
```
**Output**
```
    My mobile number is 9995167111.
    The cost of mobile is ₹48000.
    It is not easy to crack UPSC examination, people do give double attempts to clear it.
    Double standards jokes are not tolerated here.
    My weight is 54 kilogram. I live 16 kilometers away from my office.
```
### Units abbrevation
**Code**
```
    # dictionary of unit needs to pass explicitly {unit:abbrevation}
    spoken_text = Units.unit(spoken_text,WEIGHTS)
    print(spoken_text)
```
**Output**
```
    My mobile number is 9995167111.
    The cost of mobile is ₹48000.
    It is not easy to crack UPSC examination, people do give double attempts to clear it.
    Double standards jokes are not tolerated here.
    My weight is 54kg. I live 16 kilometers away from my office.
```
Observe, kilometers didn't got abbravated to kg , as only weights dictionary was passed.

## Future Expansion:
The below features can be added by adding respective class without prior testing.
* Text Abbreventions
    - Representing text using short form. i.e Thank you so much == tysm
    - Central Beauro of India == CBI
    - et cetera == Etc.
* Mathematical symbol representation.
    - plus,minus,division,modulo,integration,etc.
* Emoji Implementation.
* Add features for short notes preparation.
