# Writeup 2 - OSINT

Name: Andres Restrepo
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Andres Restrepo

## Assignment Writeup

### Part 1 (45 pts)

1. ejnorman84's real name is Eric J. Norman

2. ejnorman84 is a powerplant control specialist at Wattsamp Electric
His company's URL is http://wattsamp.net/

3. I found three usernames on a paste from pastebin found by searching "ejnorman84"
on DuckDuckGo. I found his Twitter by testing those usernames in Twitter. On his Twitter
I found his website and his gmail and protonmail addresses. I found his Instagram and Reddit
accounts on namechk.com.
On https://centralops.net/co/DomainDossier.aspx I found this information:
Admin Name: Eric Norman
Admin Organization:
Admin Street: 1300 Adabel Dr
Admin City: El Paso
Admin State/Province: TX
Admin Postal Code: 79835
Admin Country: US
Admin Phone: +1.2026562837
Admin Phone Ext:
Admin Fax:
Admin Fax Ext:
Admin Email: ejnorman84@gmail.com


4. The site's IP address is 157.230.179.99
I found it on https://centralops.net/co/DomainDossier.aspx where I also found these
DNS servers:
216.239.32.109
ns-cloud-d1.googledomains.com

216.239.34.109
ns-cloud-d2.googledomains.com

216.239.36.109
ns-cloud-d3.googledomains.com

216.239.38.109
ns-cloud-d4.googledomains.com

5. I found the wattsamp.net/robots.txt file where I found a flag

6. Running nmap on ports 1-5000 I found that ports 22 (ssh), 80 (http), and 1337 (waste)
were open.

7. At https://browserspy.dk/webserver.php I found that the web server is running on 
Apache/2.4.29 (Ubuntu)

8. On the robots file I found *CMSC389R-{n0_indexing_pls}
In the DNS server on securitytrails.com I found a txt with the flag *CMSC389R-{Do_you-N0T_See_this}
On the first photo of the Instagram I found the flag *CMSC389R-{LOOKING_CLOSELY_PAYS}
At the bottom of the wattsamp.net page source I found the flag *CMSC389R-{html_h@x0r_lulz}

### Part 2 (75 pts)

