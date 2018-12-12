"""
Not using Python Enum
The "value"/"name" proposition can make things
unnecessarily confusing for an SDK.
KISS applies here.
"""


class CheckoutSdkEnum:
    @classmethod
    def has_value(cls, value):
        return value is not None and \
            any(str(value).lower() == str(item).lower()
                for item in dir(cls)
                if not (item.startswith("__") or item == 'has_value'))


class PaymentType(CheckoutSdkEnum):
    Regular = 'Regular'
    Recurring = 'Recurring'
    MOTO = 'MOTO'


class PaymentStatus(CheckoutSdkEnum):
    Authorized = 'Authorized'
    Cancelled = 'Cancelled'
    Captured = 'Captured'
    Declined = 'Declined'
    Expired = 'Expired'
    PartiallyCaptured = 'Partially Captured'
    PartiallyRefunded = 'Partially Refunded'
    Pending = 'Pending'
    Refunded = 'Refunded'
    Voided = 'Voided'
    CardVerified = 'Card Verified'
    Chargeback = 'Chargeback'


class HTTPMethod(CheckoutSdkEnum):
    GET = 'GET'
    POST = 'POST'


# Python 3.4 does not support HTTPStatus
class HTTPStatus(CheckoutSdkEnum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    # will add more if ever needed - this is mainly to humour Python 3.4


class Currency(CheckoutSdkEnum):
    ALL = "ALL"
    STN = "STN"
    EEK = "EEK"
    BHD = "BHD"
    SCR = "SCR"
    DJF = "DJF"
    EGP = "EGP"
    MDL = "MDL"
    MZN = "MZN"
    BND = "BND"
    ZMK = "ZMK"
    SHP = "SHP"
    LBP = "LBP"
    AWG = "AWG"
    JMD = "JMD"
    KES = "KES"
    BYN = "BYN"
    KHR = "KHR"
    LAK = "LAK"
    MVR = "MVR"
    AOA = "AOA"
    TJS = "TJS"
    SVC = "SVC"
    GNF = "GNF"
    BRL = "BRL"
    MOP = "MOP"
    BOB = "BOB"
    CDF = "CDF"
    NAD = "NAD"
    LYD = "LYD"
    VUV = "VUV"
    QAR = "QAR"
    CLP = "CLP"
    HRK = "HRK"
    ISK = "ISK"
    FKP = "FKP"
    XCD = "XCD"
    NOK = "NOK"
    CUP = "CUP"
    VND = "VND"
    PEN = "PEN"
    KMF = "KMF"
    LVL = "LVL"
    MMK = "MMK"
    TRY = "TRY"
    VEF = "VEF"
    AUD = "AUD"
    TWD = "TWD"
    PKR = "PKR"
    SLL = "SLL"
    BGN = "BGN"
    LRD = "LRD"
    LKR = "LKR"
    XAF = "XAF"
    JOD = "JOD"
    ANG = "ANG"
    BSD = "BSD"
    CAD = "CAD"
    GIP = "GIP"
    MNT = "MNT"
    LTL = "LTL"
    BBD = "BBD"
    CLF = "CLF"
    BWP = "BWP"
    COP = "COP"
    PHP = "PHP"
    HUF = "HUF"
    FJD = "FJD"
    MWK = "MWK"
    THB = "THB"
    XPF = "XPF"
    RSD = "RSD"
    SAR = "SAR"
    UYU = "UYU"
    BZD = "BZD"
    SYP = "SYP"
    GMD = "GMD"
    SZL = "SZL"
    SBD = "SBD"
    ETB = "ETB"
    CHF = "CHF"
    MXN = "MXN"
    ARS = "ARS"
    GTQ = "GTQ"
    GHS = "GHS"
    NIO = "NIO"
    JPY = "JPY"
    BDT = "BDT"
    UZS = "UZS"
    SOS = "SOS"
    BTN = "BTN"
    NZD = "NZD"
    TZS = "TZS"
    IQD = "IQD"
    MGA = "MGA"
    DZD = "DZD"
    GYD = "GYD"
    USD = "USD"
    KWD = "KWD"
    CNY = "CNY"
    PYG = "PYG"
    SGD = "SGD"
    KZT = "KZT"
    PGK = "PGK"
    AMD = "AMD"
    GBP = "GBP"
    AFN = "AFN"
    CRC = "CRC"
    XOF = "XOF"
    YER = "YER"
    MRU = "MRU"
    DKK = "DKK"
    TOP = "TOP"
    INR = "INR"
    SDG = "SDG"
    DOP = "DOP"
    ZWL = "ZWL"
    UGX = "UGX"
    SEK = "SEK"
    LSL = "LSL"
    MYR = "MYR"
    TMT = "TMT"
    OMR = "OMR"
    BMD = "BMD"
    KRW = "KRW"
    HKD = "HKD"
    KGS = "KGS"
    BAM = "BAM"
    NGN = "NGN"
    ILS = "ILS"
    MUR = "MUR"
    RON = "RON"
    TND = "TND"
    AED = "AED"
    PAB = "PAB"
    NPR = "NPR"
    TTD = "TTD"
    RWF = "RWF"
    HTG = "HTG"
    IDR = "IDR"
    EUR = "EUR"
    KYD = "KYD"
    IRR = "IRR"
    KPW = "KPW"
    MKD = "MKD"
    SRD = "SRD"
    HNL = "HNL"
    AZN = "AZN"
    ERN = "ERN"
    CZK = "CZK"
    CVE = "CVE"
    BIF = "BIF"
    MAD = "MAD"
    RUB = "RUB"
    UAH = "UAH"
    WST = "WST"
    PLN = "PLN"
    ZAR = "ZAR"
    GEL = "GEL"
    ZMW = "ZMW"
