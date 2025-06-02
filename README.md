# IP-TOOLS V3: Enhanced Network Security Toolkit

[![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/Amirprx3/IP-TOOLS.svg)](https://github.com/Amirprx3/IP-TOOLS/stargazers)

<p align="center">
  <a href="#persian"><strong>(توضیحات فارسی) Persian description</strong></a>
</p>

`IP-TOOLS` is a command-line network toolkit designed for network reconnaissance and analysis operations. What started as a set of simple scripts has now evolved into a comprehensive suite with an improved user interface, advanced features, and greater stability. Version 3 introduces significant enhancements to all three core tools: **IP-Finder**, **Port-Scanner**, and **WHOIS-Checker**.

This tool is designed for educational and authorized testing purposes only. The user is responsible for any illegal use.

## Table of Contents

- [Key Features](#key-features)
- [Tool Details](#tool-details)
  - [IP-FINDER (v2.0)](#1-ip-finder-v20)
  - [PORT-SCANNER (v2.0)](#2-port-scanner-v20)
  - [WHOIS-CHECKER (v2.0)](#3-whois-checker-v20)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Key Features

- **Interactive UI**: A user-friendly main menu with engaging animations for easy navigation between tools.
- **Comprehensive Toolkit**: Includes three powerful tools for IP information lookup, port scanning, and WHOIS querying.
- **Cross-Platform Compatibility**: Capable of running on various operating systems like Windows and Linux.
- **Multi-threading**: Utilizes threads to significantly speed up port scanning operations.
- **Advanced Data Analysis**: Provides colorful, categorized, and detail-rich output for better understanding of the results.
- **Automatic Dependency Check**: The main script checks for required libraries before execution.

## Tool Details

Each tool in this suite has been completely rewritten and improved:

### 1. IP-FINDER

This tool extracts comprehensive information about a specific IP or domain.

- **New Features**:
  - **Geolocation Information**: Displays the country, city, region, ISP, and organization providing the service.
  - **Multi-IP Support**: Identifies and displays all IP addresses associated with a domain.
  - **IP Type Check**: Detects the IP type (Public, Private, Reserved, etc.).
  - **Reverse DNS Lookup**: Finds the hostname from an IP address.
  - **Reachability Check**: Pings the target and checks common ports (like 80 and 443) to estimate the online status of services.

- **Example Output**:
  ```
  [+] Enter URL/Hostname (or "back" to return): google.com

  [*] Resolving google.com...
  [*] Checking connectivity...
  [*] Getting geolocation info...

  ============================================================
  Results for: google.com
  ============================================================
  [+] Primary IP: 142.250.185.78
  [+] IP Type: Public IP
  [+] Reverse DNS: mil04s42-in-f14.1e100.net
  [+] Host is reachable (ping successful)
  [+] Open ports: 80, 443

  [+] All IPs for this domain:
    1. 142.250.185.78

  [+] Geolocation Information:
    Country: United States
    Region: California
    City: Mountain View
    ISP: Google LLC
    Organization: Google LLC
    Timezone: America/Los_Angeles
    Coordinates: 37.422, -122.084
  ```

### 2. PORT-SCANNER (v2.0)

A fast and powerful port scanner with diverse capabilities.

- **New Features**:
  - **Multi-threaded Scanning**: Uses `ThreadPoolExecutor` to scan a large number of ports simultaneously, increasing speed.
  - **Multiple Scan Modes**:
    1.  **Quick Scan**: Checks common and well-known ports.
    2.  **Full Scan**: Scans all ports from 1 to 65535.
    3.  **Custom Range**: Allows specifying a custom range for scanning.
  - **Adjustable Threads**: Option to specify the number of threads to optimize performance based on system power.
  - **Progress Indicator**: Displays the scan progress percentage for long scans.
  - **Service Identification**: Shows the names of common services (like HTTP, FTP, SSH) next to the open port.

- **Example Output**:
  ```
  [+] Target (IP/Hostname): 93.184.216.34
  [*] Resolved 93.184.216.34 to 93.184.216.34

  ============================================================
  Target: 93.184.216.34
  Started at: 2025-06-02 10:30:00
  Threads: 200
  ============================================================
  [+] Port 80/tcp open (HTTP)
  [+] Port 443/tcp open (HTTPS)

  ============================================================
  Scan completed in 1.24 seconds
  Open ports found: 2
  ```

### 3. WHOIS-CHECKER

A tool for in-depth querying and analysis of domain registration information.

- **New Features**:
  - **Smart Analysis**:
    - **Domain Age Calculation**: Displays the age of the domain based on its creation date.
    - **Expiration Status**: Shows the remaining time until the domain expires, with color-coded warnings (red for critical, yellow for warning).
    - **Registrar Analysis**: Identifies popular registrars like GoDaddy and Cloudflare.
  - **Comprehensive Email Extraction**: Searches all fields of the WHOIS record to find contact emails.
  - **Structured Output**: Displays information in two separate sections: **Important Information** and **Raw Data**.
  - **Save Report**: Ability to save the complete results to a text file.

- **Example Output**:
  ```
  ======================================================================
                         IMPORTANT WHOIS INFORMATION
  ======================================================================
  Domain Name.............. example.com
  Registrar................ GoDaddy (Popular)
  Creation Date............ 1995-08-05 04:00:00
  Domain Age............... 29 years, 9 months
  Expiration Date.......... 2025-08-04 04:00:00
  Expiry Status............ Expires in 63 days (Warning)
  Last Updated............. 2024-07-01 10:00:00
  Status................... clientDeleteProhibited, clientTransferProhibited
  Name Servers............. 2 items
                           1. ns.example.com
                           2. ns2.example.com
  Contact Emails........... 1 items
                           1. abuse@example.com
  Owner/Organization....... Example Inc.
  Country.................. US
  ```

## Requirements

- **Python 3.6 or higher**
- Python Libraries:
  - `python-whois`
  - `requests`

## Installation

1.  First, clone the project from GitHub:
    ```bash
    git clone https://github.com/Amirprx3/IP-TOOLS.git
    cd IP-TOOLS_V3
    ```

2.  Install the project dependencies using `pip`. Create a `requirements.txt` file with the following content, then run the command:

    **Content of `requirements.txt`:**
    ```
    python-whois
    requests
    ```

    **Installation command:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the main script:
    ```bash
    python IP-TOOLS.py
    ```

2.  The program will display a main menu:
    * `1) IP-FINDER`: Find information about a domain or IP.
    * `2) PORT-SCANNER`: Scan the ports of a target.
    * `3) WHOIS-CHECKER`: Query WHOIS information for a domain.
    * `4) ABOUT`: Display information about the tool.
    * `5) EXIT`: Exit the program.

3.  Enter the number of your desired tool and follow the instructions for each section.

## Contributing

Contributions to this project are welcome. If you have an idea for an improvement or a bug fix, please **Fork** the repository, apply your changes in a new **Branch**, and then submit a **Pull Request**.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

<h1 id="persian">توضیحات فارسی (Persian description)</h1>

`IP-TOOLS`: یک مجموعه ابزار شبکه مبتنی بر خط فرمان است که برای انجام عملیات شناسایی و تحلیل شبکه طراحی شده است. این پروژه که در ابتدا با چند اسکریپت ساده آغاز شد، اکنون به یک جعبه‌ابزار جامع با رابط کاربری بهبودیافته، ویژگی‌های پیشرفته و پایداری بالا تبدیل شده است. نسخه 3 شامل بهبودهای چشمگیری در هر سه ابزار اصلی یعنی **IP-Finder**، **Port-Scanner** و **WHOIS-Checker** است.

این ابزار برای اهداف آموزشی و تست‌های مجاز طراحی شده است. مسئولیت هرگونه استفاده غیرقانونی بر عهده کاربر است.

## محتویات

- [ویژگی‌های کلیدی ](#ویژگیهای-کلیدی-فارسی)
- [جزئیات ابزارها ](#جزئیات-ابزارها-فارسی)
  - [IP-FINDER (نسخه 2.0)](#1-ip-finder-نسخه-20-فارسی)
  - [PORT-SCANNER (نسخه 2.0)](#2-port-scanner-نسخه-20-فارسی)
  - [WHOIS-CHECKER (نسخه 2.0)](#3-whois-checker-نسخه-20-فارسی)
- [نیازمندی‌ها ](#نیازمندیها-فارسی)
- [نصب و راه‌اندازی ](#نصب-و-راهاندازی-فارسی)
- [نحوه استفاده ](#نحوه-استفاده-فارسی)
- [مشارکت در پروژه ](#مشارکت-در-پروژه-فارسی)
- [مجوز ](#مجوز-فارسی)

## ویژگی‌های کلیدی 

- **رابط کاربری تعاملی**: منوی اصلی کاربرپسند با انیمیشن‌های جذاب برای ناوبری آسان بین ابزارها.
- **مجموعه ابزار جامع**: شامل سه ابزار قدرتمند برای یافتن اطلاعات IP، اسکن پورت و استعلام WHOIS.
- **سازگاری چندسکویی (Cross-platform)**: قابلیت اجرا بر روی سیستم‌عامل‌های مختلف مانند ویندوز و لینوکس.
- **پردازش چندنخی (Multi-threading)**: استفاده از نخ‌ها برای افزایش چشمگیر سرعت اسکن پورت‌ها.
- **تحلیل و نمایش پیشرفته اطلاعات**: خروجی‌های رنگی، دسته‌بندی‌شده و غنی از جزئیات برای درک بهتر نتایج.
- **بررسی خودکار نیازمندی‌ها**: اسکریپت اصلی قبل از اجرا، کتابخانه‌های مورد نیاز را بررسی می‌کند.

## جزئیات ابزارها 

هر یک از ابزارهای موجود در این مجموعه به‌طور کامل بازنویسی و بهبود یافته‌اند:

### 1. IP-FINDER

این ابزار اطلاعات کاملی را در مورد یک IP یا دامنه استخراج می‌کند.

- **قابلیت‌های جدید**:
  - **اطلاعات موقعیت جغرافیایی (Geolocation)**: نمایش کشور، شهر، منطقه، ISP و سازمان ارائه‌دهنده سرویس.
  - **پشتیبانی از چند IP**: شناسایی و نمایش تمام آدرس‌های IP مرتبط با یک دامنه.
  - **بررسی نوع IP**: تشخیص نوع IP (عمومی، خصوصی، رزرو شده و...).
  - **جستجوی معکوس DNS**: پیدا کردن نام هاست (Hostname) از روی آدرس IP.
  - **بررسی قابلیت دسترسی**: ارسال پینگ به هدف و بررسی اتصال به پورت‌های رایج (مانند 80 و 443) برای تخمین وضعیت آنلاین بودن سرویس‌ها.

- **مثال خروجی**:
  ```
  [+] Enter URL/Hostname (or "back" to return): google.com

  [*] Resolving google.com...
  [*] Checking connectivity...
  [*] Getting geolocation info...

  ============================================================
  Results for: google.com
  ============================================================
  [+] Primary IP: 142.250.185.78
  [+] IP Type: Public IP
  [+] Reverse DNS: mil04s42-in-f14.1e100.net
  [+] Host is reachable (ping successful)
  [+] Open ports: 80, 443

  [+] All IPs for this domain:
    1. 142.250.185.78

  [+] Geolocation Information:
    Country: United States
    Region: California
    City: Mountain View
    ISP: Google LLC
    Organization: Google LLC
    Timezone: America/Los_Angeles
    Coordinates: 37.422, -122.084
  ```

### 2. PORT-SCANNER

اسکنر پورت سریع و قدرتمند با قابلیت‌های متنوع.

- **قابلیت‌های جدید**:
  - **اسکن چندنخی**: استفاده از `ThreadPoolExecutor` برای اسکن همزمان تعداد زیادی پورت و افزایش سرعت.
  - **حالت‌های مختلف اسکن**:
    1.  **اسکن سریع**: بررسی پورت‌های متداول و شناخته‌شده.
    2.  **اسکن کامل**: بررسی تمام پورت‌ها از 1 تا 65535.
    3.  **اسکن سفارشی**: تعیین یک بازه دلخواه برای اسکن.
  - **تنظیم تعداد نخ‌ها**: امکان مشخص کردن تعداد نخ‌ها برای بهینه‌سازی عملکرد بر اساس قدرت سیستم.
  - **نمایش پیشرفت**: نمایش درصد پیشرفت اسکن در بازه‌های طولانی.
  - **شناسایی سرویس**: نمایش نام سرویس‌های رایج (مانند HTTP, FTP, SSH) در کنار پورت باز.

- **مثال خروجی**:
  ```
  [+] Target (IP/Hostname): 93.184.216.34
  [*] Resolved 93.184.216.34 to 93.184.216.34

  ============================================================
  Target: 93.184.216.34
  Started at: 2025-06-02 10:30:00
  Threads: 200
  ============================================================
  [+] Port 80/tcp open (HTTP)
  [+] Port 443/tcp open (HTTPS)

  ============================================================
  Scan completed in 1.24 seconds
  Open ports found: 2
  ```

### 3. WHOIS-CHECKER

ابزاری برای استعلام و تحلیل عمیق اطلاعات ثبت دامنه.

- **قابلیت‌های جدید**:
  - **تحلیل هوشمند اطلاعات**:
    - **محاسبه عمر دامنه**: نمایش سن دامنه بر اساس تاریخ ایجاد.
    - **وضعیت انقضا**: نمایش مدت‌زمان باقی‌مانده تا انقضای دامنه با هشدارهای رنگی (قرمز برای وضعیت بحرانی، زرد برای هشدار).
    - **تحلیل ثبت‌کننده (Registrar)**: شناسایی ثبت‌کننده‌های محبوب مانند GoDaddy و Cloudflare.
  - **استخراج کامل ایمیل‌ها**: جستجو در تمام فیلدهای رکورد WHOIS برای یافتن ایمیل‌های تماس.
  - **خروجی ساختاریافته**: نمایش اطلاعات در دو بخش مجزا: **اطلاعات مهم** و **داده‌های خام**.
  - **ذخیره گزارش**: قابلیت ذخیره کامل نتایج در یک فایل متنی.

- **مثال خروجی**:
  ```
  ======================================================================
                         IMPORTANT WHOIS INFORMATION
  ======================================================================
  Domain Name.............. example.com
  Registrar................ GoDaddy (Popular)
  Creation Date............ 1995-08-05 04:00:00
  Domain Age............... 29 years, 9 months
  Expiration Date.......... 2025-08-04 04:00:00
  Expiry Status............ Expires in 63 days (Warning)
  Last Updated............. 2024-07-01 10:00:00
  Status................... clientDeleteProhibited, clientTransferProhibited
  Name Servers............. 2 items
                           1. ns.example.com
                           2. ns2.example.com
  Contact Emails........... 1 items
                           1. abuse@example.com
  Owner/Organization....... Example Inc.
  Country.................. US
  ```

## نیازمندی‌ها 

- **پایتون نسخه 3.6 یا بالاتر**
- کتابخانه‌های پایتون:
  - `python-whois`
  - `requests`

## نصب و راه‌اندازی 

1.  ابتدا پروژه را از گیت‌هاب کلون کنید:
    ```bash
    git clone https://github.com/Amirprx3/IP-TOOLS.git
    cd IP-TOOLS_V3
    ```

2.  نیازمندی‌های پروژه را با استفاده از `pip` نصب کنید. یک فایل `requirements.txt` با محتوای زیر ایجاد کرده و سپس دستور را اجرا کنید:

    **محتوای فایل `requirements.txt`:**
    ```
    python-whois
    requests
    ```

    **دستور نصب:**
    ```bash
    pip install -r requirements.txt
    ```

## نحوه استفاده 

1.  اسکریپت اصلی را اجرا کنید:
    ```bash
    python IP-TOOLS.py
    ```

2.  برنامه یک منوی اصلی را به شما نمایش می‌دهد:
    * `1) IP-FINDER`: یافتن اطلاعات یک دامنه یا IP.
    * `2) PORT-SCANNER`: اسکن پورت‌های یک هدف.
    * `3) WHOIS-CHECKER`: استعلام اطلاعات WHOIS یک دامنه.
    * `4) ABOUT`: نمایش اطلاعات درباره ابزار.
    * `5) EXIT`: خروج از برنامه.

3.  شماره ابزار مورد نظر خود را وارد کرده و دستورالعمل‌های هر بخش را دنبال کنید.

## مشارکت در پروژه 

از هرگونه مشارکت در این پروژه استقبال می‌شود. اگر ایده‌ای برای بهبود یا رفع باگ دارید، لطفاً یک **Fork** از ریپازیتوری ایجاد کرده، تغییرات خود را در یک **Branch** جدید اعمال کنید و سپس یک **Pull Request** ارسال نمایید.

## مجوز 

این پروژه تحت مجوز [MIT](https://opensource.org/licenses/MIT) منتشر شده است.