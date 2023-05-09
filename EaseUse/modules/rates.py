def rates():
    from bs4 import BeautifulSoup
    import requests

    print("\nAVAILABLE CURRENCY CODES --> \n'AED' 'AFN' 'ALL' 'AMD' 'ANG' 'AOA' 'ARS' 'AUD' 'AWG' 'AZN' 'BAM' 'BBD' 'BDT' 'BGN' 'BHD' 'BIF' 'BMD' 'BND' 'BOB' 'BRL' 'BSD' 'BTN' 'BWP' 'BYN' 'BZD' 'CAD' 'CDF' 'CHF' 'CLP' 'CNY' 'COP' 'CRC' 'CUC' 'CUP' 'CVE' 'CZK' 'DJF' 'DKK' 'DOP' 'DZD' 'EGP' 'ERN' 'ETB' 'EUR' 'FJD' 'FKP' 'GBP' 'GEL' 'GGP' 'GHS' 'GIP' 'GMD' 'GNF' 'GTQ' 'GYD' 'HKD' 'HNL' 'HRK' 'HTG' 'HUF' 'IDR' 'ILS' 'IMP' 'INR' 'IQD' 'IRR' 'ISK' 'JEP' 'JMD' 'JOD' 'JPY' 'KES' 'KGS' 'KHR' 'KMF' 'KPW' 'KRW' 'KWD' 'KYD' 'KZT' 'LAK' 'LBP' 'LKR' 'LRD' 'LSL' 'LYD' 'MAD' 'MDL' 'MGA' 'MKD' 'MMK' 'MNT' 'MOP' 'MRU' 'MUR' 'MVR' 'MWK' 'MXN' 'MYR' 'MZN' 'NAD' 'NGN' 'NIO' 'NOK' 'NPR' 'NZD' 'OMR' 'PAB' 'PEN' 'PGK' 'PHP' 'PKR' 'PLN' 'PYG' 'QAR' 'RON' 'RSD' 'RUB' 'RWF' 'SAR' 'SBD' 'SCR' 'SDG' 'SEK' 'SGD' 'SHP' 'SLL' 'SOS' 'SPL*' 'SRD' 'STN' 'SVC' 'SYP' 'SZL' 'THB' 'TJS' 'TMT' 'TND' 'TOP' 'TRY' 'TTD' 'TVD' 'TWD' 'TZS' 'UAH' 'UGX' 'USD' 'UYU' 'UZS' 'VEF' 'VND' 'VUV' 'WST' 'XAF' 'XCD' 'XDR' 'XOF' 'XPF' 'YER' 'ZAR' 'ZMW' 'ZWD'")
    frm = input("\nCurrency Code to Exchange--> ").strip().upper()
    amt = float(input("Amount of Exchange--> ").strip())
    too = input("Exchanged Currency Code--> ").strip().upper()

    url =f'https://www.xe.com/currencyconverter/convert/?Amount={amt}&From={frm}&To={too}'

    res = requests.get(url)
    doc = BeautifulSoup(res.content,'html.parser')
    frst = doc.find(class_='result__ConvertedText-sc-1bsijpp-0 gwvOOF').text
    conv = doc.find(class_='result__BigRate-sc-1bsijpp-1 iGrAod').text

    print("\n\n\t",frst,conv)

