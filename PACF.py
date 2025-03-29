from statsmodels.graphics.tsaplots import plot_pacf
import yfinance as yf
from matplotlib import pyplot
tesla = yf.download('TSLA','2019-01-27', '2020-02-11')
plot_pacf(tesla['Close'], lags=20)
pyplot.show()