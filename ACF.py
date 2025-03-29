from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_acf
import yfinance as yf
tesla = yf.download('TSLA','2019-01-27', '2020-02-11')
plot_acf(tesla['Close'], lags=20)
pyplot.show()