# Whois-Feonix

a python script that let you query whois server in order to gather some possible information of a domain .

a simple Python script that allows user to simply perform a whois query for a specified website using the whois library.  This library is a Python wrapper around the whois service and allows you to get domain registration information such as the registrar, creation date, and other useful details.

# Step-by-Step Guide:

## **Installation**: 

1. Install the requirement dependencies.

```bash
apt install git
apt install python
```

2. Then clone the repository.

```bash
git clone http://github.com/evilfeonix/Whois-Feonix.git
```

3. Navigate to the directory.

```bash
cd Whois-Feonix
```

4. Install in requirement libraries.

```bash
pip install -r requirements
```

5. Runs the main script.

```bash
python3 who_is.py
```

# How it Works:

1. **Importing the whois library**: We use the whois module to query WHOIS information.
2. **`who-is.py` script**: This script takes a domain name as input and returns the WHOIS data for that domain. If an error occurs (e.g., if the domain does not exist), the script will catch it and print an error message.
3. **Input and Output**: The user is prompted to input a domain (e.g., example.com). The script then queries the WHOIS service for that domain and displays the returned data.
4. **Error Handling**: The script has basic error handling to catch invalid domain names or issues with querying WHOIS data.

# Example Output:

If you query a domain like mtn.ng, you may get an output similar to this:

```css
Enter the domain name (e.g., example.com): mtn.ng

WHOIS Data for mtn.ng
{
  "domain_name": "mtn.ng",
  "registrar": "GO54 Limited (formerly Whogohost Limited)",
  "registrar_url": "http://www.whogohost.com.ng",
  "reseller": null,
  "whois_server": "https://whois.whogohost.com",
  "referral_url": null,
  "updated_date": "2022-08-15 17:17:04",
  "creation_date": "2022-02-18 12:34:24",
  "expiration_date": "2027-02-18 00:00:00",
  "name_servers": [
    "ns1.mtnbusiness.net",
    "ns3.mtnbusiness.net"
  ],
  "status": [
    "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
    "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited"
  ],
  "emails": [
    "abuseteam@whogohost.com",
    "ifeoma.utah@mtn.com"
  ],
  "dnssec": "unsigned",
  "name": "Ifeoma Utah",
  "org": "MTN Nigeria Communications Plc",
  "address": "MTN Plaza",
  "city": "Ikoyi",
  "state": "Lagos",
  "registrant_postal_code": null,
  "country": "NG"
  ...
}
```
# Important Notes:
> **The WHOIS data returned is typically in a structured dictionary format, including information like**: _Registrar, Creation date, Expiration date, Name servers, Status (e.g., active, prohibited, etc.), Registrant contact information (if available)._

> **Rate Limiting**: _WHOIS servers may limit the number of queries you can perform in a short time. If you're querying many domains, you may encounter rate limits. Consider using a paid service for bulk queries or adding delays between queries._

# Support Us:
Follow us at our (github page)[https://github.com/evilfeonix]
Fork and Star our repositories

# Thank you for your support...

