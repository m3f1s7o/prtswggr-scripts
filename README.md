# prtswggr-scripts
Automated scripts to help solving some labs of portswigger.

## Requirements
- You need to have `python3` to run this scripts, you can install it by:
```shell-session
$ sudo apt install python3
# or
$ sudo pacman -S python3
```
- And install `pwntools` and `requests` libraries:
```shell-session
$ pip3 install pwntools requests
```
- `Burp Suite` to capture the request
- `FoxyProxy` extension to proxy the request

## Run
For any of these scripts, once you have started your lab, you'll need to capture a request using Burp Suite to obtain the necessary cookies, follow these steps:
1. Turn on the Burp Proxy
2. Use FoxyProxy (or anothe extention) to proxy the request
3. Click on any product filter of the lab

![image](https://github.com/m3f1s7o/prtswggr-scripts/assets/65306021/f0202af5-a64b-4219-94b8-6d42e36e7475)

And use the values to fill up the fields in the script:

```shell-session
$ chmod +x ./cndtionl_rspnse.py
$ ./cndtionl_rspnse.py
```

![image](https://github.com/m3f1s7o/prtswggr-scripts/assets/65306021/30997fee-ee65-4b72-b572-8858c6acefb8)

---
## Script correspondence
| Script | Lab |
| --- | --- |
| cndtionl_rspnse.py | [Blind SQL injection with conditional responses](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses) |
| cndtionl_error.py | [Blind SQL injection with conditional errors](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors) |
