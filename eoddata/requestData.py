import logging
from zeep import Client
from datetime import date, datetime
import json


# EOD Result object
class EODResult():
    def __init__(self, quote_list=[], note_list=[], index_list=[], status_code=200, err_msg=""):
        self.quote_list = quote_list
        self.note_list = note_list
        self.index_list = index_list
        self.status_code = status_code
        self.err_msg = err_msg


# Note object
class Note():
    def __init__(self, row_idx=None, err_type=None, err_msg=None):
        self.row_idx = row_idx
        self.err_type = err_type
        self.err_msg = err_msg


# Quote object
class StockData():
    Symbol = None
    Description = None
    Name = None
    DateTime = None
    Open = 0.0
    High = 0.0
    Low = 0.0
    Close = 0.0
    Volume = 0.0
    OpenInterest = 0.0
    Previous = 0.0
    Change = 0.0
    Bid = 0.0
    Ask = 0.0
    PreviousClose = 0.0
    NextOpen = 0.0
    Modified = None


# Index object
class Index():
    def __init__(self, Symbol=None):
        self.Symbol = Symbol


# Create eoddata.com config object
class RequestData():
    client = Client("http://ws.eoddata.com/data.asmx?wsdl")
    login_token = ""
    function_name = 'Stocks'

    def login(self) -> bool:
        logging.info('Logging into eoddata.com')

        login_result = self.client.service.Login(
            # Username="dazacams@hotmail.com", Password="Analytics1!")
            Username="dazacams", Password="Analytics1!")
        print(login_result)
        self.login_token = login_result['Token']

        if not self.login_token:
            logging.error('Login to eoddata.com failed!')
            return False
        else:
            logging.info('Login to eoddata.com successful!')
            # TODO comment this later
            logging.info('Got login token ' + self.login_token)
            return True
        # Default Exchange: Australian Securities Exchange

    def get_data(self, eod_date: str, date_flag: bool, exchange: str = 'NASDAQ') -> EODResult:
        symbol_list = []
        quote_list = []
        note_list = []
        index_list = []

        if date_flag:
            logging.info("Calling API QuoteListByDate")
            result = self.client.service.QuoteListByDate(
                Token=self.login_token, Exchange=exchange, QuoteDate=eod_date)
        else:
            logging.info("Calling API QuoteList")
            result = self.client.service.QuoteList(
                Token=self.login_token, Exchange=exchange)

        if result['FUNDAMENTALS'] is not None:
            fundamentals = result['FUNDAMENTALS']['FUNDAMENTAL']
            for idx, item in enumerate(fundamentals):
                print(item)
        #print(result)
        if result['QUOTES'] is not None:
            quotes = result['QUOTES']['QUOTE']
            logging.info(f'Found {len(quotes)} stocks to download!')

            for idx, item in enumerate(quotes):
                try:
                    if item['DateTime'].date() == datetime.strptime(eod_date, '%Y%m%d').date() and item[
                        'Symbol'] not in symbol_list:  # Skip old and duplicate quotes
                        quote = StockData()
                        quote.Symbol = item['Symbol']
                        quote.Description = item['Description']
                        quote.Name = item['Name']
                        quote.DateTime = item['DateTime'].isoformat()
                        quote.Open = item['Open']
                        quote.High = item['High']
                        quote.Low = item['Low']
                        quote.Close = item['Close']
                        quote.Volume = item['Volume']
                        quote.OpenInterest = item['OpenInterest']
                        quote.Previous = item['Previous']
                        quote.Change = item['Change']
                        quote.Bid = item['Bid']
                        quote.Ask = item['Ask']
                        quote.PreviousClose = item['PreviousClose']
                        quote.NextOpen = item['NextOpen']
                        quote.Modified = item['Modified'].isoformat()
                        #print(item)
                        quote_list.append(quote)
                        symbol_list.append(quote.Symbol)

                except Exception as e:
                    print(e)
                    note = Note(idx + 1, str(type(e)), str(e))
                    note_list.append(note)

        index_list = self.get_indices()
        return EODResult(quote_list, note_list, index_list)

    def get_indices(self, exchange: str = 'NASDAQ') -> []:
        index_list = []

        result = self.client.service.FundamentalList(
            Token=self.login_token, Exchange=exchange)

        if result['FUNDAMENTALS'] is not None:
            indices = result['FUNDAMENTALS']['FUNDAMENTAL']
            print(indices)
            for idx, item in enumerate(indices):
                try:
                    if item['Sector'] == "Index":
                        index = Index(item['Symbol'])
                        index_list.append(index)

                except Exception as e:
                    print(e)

        return index_list


requestData = RequestData();
print(requestData.login())
eod_result = requestData.get_data("20220217", True, 'NASDAQ')
stock_data_param = json.dumps([quote.__dict__ for quote in eod_result.quote_list])
# print(stock_data_param)
