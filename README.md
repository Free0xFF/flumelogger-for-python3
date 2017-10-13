# flumelogger-for-python3
### 1. For python3
In pypi repo, flumelogger didn't compitable for python3, so I maintained it for python3.
Furthermore, this code give an example to configure logging package to use conf file, which allow 
developers output logs to more destinations.

### 2. improvement
A function for reconnect and re-append is added to improve the client's reliability.
When flume be offline, exception throws and client lose efficacy. We assume that 
client is losting connection with flume, and then trying to reconnect and re-append evnet.
