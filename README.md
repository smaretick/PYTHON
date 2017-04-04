# PYTHON
miscellaneous Selenium Python code using geckodrive
GA.py & FCH.py log onto Google and do minimal navigation to GoogleAnalytics

TC.py logs into CellTrak & does some navigation (note: ERRs may occur due to slow navigation caused by connection speed)

Sun.py is simple BrowserStack test)

BA.py is a navigation of http://www.bloonaway.co.uk (Balloons Away)

It is necessary to log onto GA due to selenium creating a new instantiation of the browser each time it runs
  and therefore doesn't 'remember' options as it does on your desktop
