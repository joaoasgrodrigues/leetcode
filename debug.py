def teste():
    # Symbol       Value
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000
    
    # s = 'MCMXCIV'
    s = 'III'
    # s = 'LVIII'
    # s = 'MCMXCIV'
    
    roman_dict = {'I': 1,
                  'IV': 4,
                  'V':5,
                  'IX': 9,
                  'X': 10,
                  'XL':40,
                  'L': 50,
                  'XC':90,
                  'C': 100,
                  'CD':400,
                  'D': 500,
                  'CM':900,
                  'M': 1000}

    number = 0
    jump = False 
    for i in range(len(s)):
        if jump:
            jump = False
            continue 
        
        try:
            if (s[i] + s[i+1]) in roman_dict:
                number += roman_dict[s[i]+s[i+1]]
                jump = True
                print("-->", number)
                continue
        except:
            pass 

        number += roman_dict[s[i]]
        print("->", number)

            
    print(number)
teste()
