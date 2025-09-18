# Week 2

### Grading

Task #|Points|Description|
-----|:---:|----------|
[Task 1](#task-1-choose-a-or-b) | 1 | Browsers and Banking Security ***or*** Certifcates
[Task 2](#task-2-cards-and-payments) | 1 | Cards and Payments
[Task 3](#task-3-card-fraud) | 1 | Card Fraud
[Task 4](#task-4-wazuh) | 1 | SIEM Wazuh 

---

# Tasks

### Task 1: Choose A ***or*** B

#### Task 1A: Browsers and Banking Security

Online Banking is of the most lucrative targets for phishing and scams. How do our browsers protect us against them?

Look at the following snippets from a browsers address bar:

![Bank image 1](https://github.com/ouspg/SecurityEngineering/blob/main/Week2_Banking_and_Payments/Images/bank_1.png)

![Bank image 2](https://github.com/ouspg/SecurityEngineering/blob/main/Week2_Banking_and_Payments/Images/bank_2.png)

![Bank image 3](https://github.com/ouspg/SecurityEngineering/blob/main/Week2_Banking_and_Payments/Images/bank_3.png)

**Questions:**

- What does the "Not Secure" warning mean in the first picture and what risks does visiting sites with the warning pose?
  Answer:- The "Not Secure" warning means the connection is not secure. It is not trustable to use. It may affect our personal data and information.
         - Also, The banking sector always have to use HTTPS to encrypt our password and account details. The banking site without HTTPS is insecure and never be used. So we can judge that it is a phishing or scam.

- Why does the second site show up as "trusted" to the browser?
  Answer:- It is secure to use because it uses a valid HTTPS connection which is encrypted.
         - It also shows that connection is private and secure to use. 

- What other ways are there to detect a phishing/scam site? 
    - Are there any tools available online?
  Answer:- Yes, there are some tools available online to detect the scam sites.
For Example - Password manager - It can be used to protect us from login any unknown website. If site is unknown then password and login details will not automatically filled which we have already saved for our known website.
            - URL scanner- It can be used to check and verify the URL website.

- What is typosquatting and how does it relate to the pictures?
    - What is **UDRP** and how does it help with combatting typosquatting?
    - If you were to own the domain **ouspg.org** and would be running your crypto banking application at **bank.ouspg.org**, what domains could you monitor for warning signs of possible phishing attempts against your customers?
  Answer:- Typosquatting means where hacker uses the same domain with misspelling.
         - UDRP stands for Uniform Domain-Name Dispute-Resolution Policy. It is established by thr internet corporation for resolving the dispute like typosquatting. trademark can file a case against disputed domain and trademark have to prove that dispute domain is similar to their trademark and used for bad faith. By doing this, the disputed domain can be canceled.
         - If the original domain is "ouspg.org", then the hacker can use domains like "ouspg.net", "ouspg.com", "ouspg.bank", "bank.ouspg.org", "ousp.org"      


#### Task 1B: Certificates

You have probably seen the following kind of warning when browsing the internet:

![Certificate image 1](https://github.com/ouspg/SecurityEngineering/blob/main/Week2_Banking_and_Payments/Images/certificate_1.png)

**Questions:**

- What are digital certificates used for?
    - Why are certificates important for online payments and banking security?
    - What other uses do certificates have?
 Answer:- Digital certificates is like digital document which proves its identity and domain.
        - To make an online payment and banking security certification is important to encrypt the customer's personal data like password, account details etc.
        - Authentification is also important which proves that we are connected to the correct website.
        - Other use of certificates is to encrypt emails, To sign in the software applications and secure the connections.

- What kind of attacks does TLS mitigate and why is this important for online banking?
- How do browsers use certificates for ensuring browsing security?
    - What does the warning in the picture above mean?
  Answer:- TLS encrypts the connection and protect our personal information. Hacker can not attack without a valid certificate for bank's domain.
         - To ensure browser's security, browser always check the cerificates. When we visit any website, the website itself sends the certificate to the browser and browser validate that certificate. Also browser match the domain name.
         - The warning "Your connection is not private" is showing that the connection is not encrypted and also it might be possible that cerification process has been failed or cerificate is no longer valid. Domain name might also be different.

**Certificate Authorities**

Read the following entries on Certificate Authorities and Certificate Transparency and answer questions:

https://en.wikipedia.org/wiki/Certificate_authority  
https://en.wikipedia.org/wiki/Certificate_Transparency  
https://certificate.transparency.dev/howctworks/  
https://www.ecb.europa.eu/pub/pubbydate/html/index.en.html  

**Questions:**

- Why would it be bad if a trusted certificate authority was compromised?
- Why is certificate transparency important?
Answer:- If certificate authority was compromised, the consequences would occur. The hacker could create a same fake website for bank.
         They could read passwords, financial details, and private messages, without triggering any browser warnings. This can be harmful for bank customers.
       - Certificate transparency is very important. The bak can moniter any certificate issued for their domain. If they see one they didn't request, they immediately know it's fraudulent and can take action. The Certificate proves its identity and attacker can not login any random website easily.
---

### Task 2: Cards and Payments

**Read the following:**

https://en.wikipedia.org/wiki/Payment_card  
https://en.wikipedia.org/wiki/EMV  
https://en.wikipedia.org/wiki/Multi-factor_authentication  

**Questions: Payments**

- Why do modern payment cards use a chip and not a magnetic stripe?
Answer:- In magnetic stripe, it is easy to copy the data and use every time that data for fraud because magnetic stripe contains same expiry date and card number.
         In Chip method, it creates a unique number after the payment and attacker can not copy that. If attacker do that then it is useless for future transactions. Chip generate one time use code, which is verfied by bank. Hence, the chip is safe and easy to use for making transactions.

- What are EMV Certificates and why are they relevant for payment protection?
Answer:- EMV cerificates provides authentification and attacker can not edit the data or make any transactions.

- What attacks exist against payment cards?
    - Card-not-present?
    - Contactless payment?
Answer:- The most attacks are nowadays are online where physical card is not required. We all make payments through our mobile and through CVV number. So online fraud can be happen related to the CVV, expiray date, card number etc.
       - In contactless payment, we use NFC payment method which is more safe than other. It can be possible that attacker can track the NFC and hack the data.

**Questions: MFA**

- How is multi-factor authentication (MFA) used in banking?
Answer:- MFA use for more security. If one authentification is compromised, attacker still cannot login into the bank's official website without completing all the authentification. Authentification can be password login, after that OTP verfication can be used for the confirmation.

- How does multi-factor authentication increase payment security?
Answer:- In MFA, if password compromised, still attcker cannot access the website or account. Attacker have to get the OTP code and other verification details to know our account details. Overall MFA increase the payment security in many ways.

- What MFA methods are you using in you daily life?
Answer:- I generally use biometrics to unlock any apps in my mobile. Moreover I received OTP for login security via SMS. Also I use authentification app for more security reasons.

- What attacks exists against different forms of 2FA?
    - Time-based-one-time-password?
    - Text Message?
Answer:- Attacker can ask real time code like OTP by creating a fake website like bank.
       - OTP is received via text message, so attacker can try to hack the text messages first to read the OTP.
---

### Task 3: Card Fraud

One part of understanding payment card security is monitoring how the cards are used for frauds. The following articles are reports on card fraud by the European Central Bank and will give you an overview of how the fraud landscape has evolved between 2008-2019. Read through the articles and then answer the questions in the questions section.

**Read the following reports:**


https://www.ecb.europa.eu/pub/pdf/cardfraud/cardfraudreport201207en.pdf  
https://www.ecb.europa.eu/pub/cardfraud/html/ecb.cardfraudreport202008~521edb602b.en.html  
https://www.ecb.europa.eu/pub/cardfraud/html/ecb.cardfraudreport202110~cac4c418e8.en.html  

**Supporting Resources:**

https://www.ecb.europa.eu/pub/pubbydate/html/index.en.html (Search: "Fraud")  
https://www.ecb.europa.eu/paym/intro/mip-online/2018/html/1803_revisedpsd.en.html  


**Questions:**

Write a summary (max 700 words) on "Evolution of card fraud" in which you answer **at least** the following questions:

- What kinds of card fraud exist?
    - How does card fraud type prevalence differ geographically?
Answer:- 1) Geographical breakdowns of counterfeit card present fraud
         2) Geographical distribution of card fraud
         3) A country-by-country and regional perspective on card fraud

- How has the fraud landscape changed between 2008-2019? Why?
    - What type of fraud has seen a notable increase during the last decade?
    - What technologies or regulations have had an impact on card fraud?
 Answer:- The CNP fraud system become more powerful and increased in the last decade.
        - EMV chip and CNP transactions had an most impact on card fraud.

- How has the transaction landscape changed in the same period?
    - What kind of transactions have become increasingly popular?
Answer:- online transactions and cashless transactions have become increasingly popular.
    - What kind of transactions have had a high risk of being fraudulent?
Answer:- CNP transaction have had a high risk of being fraudulent.
        - Has this changed at all during 2008-2019?
Answer:- No drastic change occured in the fraud but yes securities are more powerful than before.
- What effect has internet and e-commerce had on card fraud?
Answer:- Internet and e-commerce had an most important effect on card fraud. People are more likely to do shopping online and use more internet than before.                Hence, online fraud system drastically increased.
- Why is preventing data breaches important in preventing card fraud?
    - How does payment card tokenisation help in this?
 Answer:- It  is important to prevent CNP fraud. payment card tokenisation is a security measure where the actual card details are replaced by unique digital identifiers (tokens) which can be parametrised to be used in a restricted way.  For example, a token provisioned to a mobile phone could be setup to only initiate proximity payments from that particular device by a given cardholder, where the trusted consumer device itself becomes a multi-factor authenticator.


-Anything interesting you found?
Answer:- Report contains the fraud information and highlight the most of the areas.

---

### Task 4: [Wazuh](https://www.wazuh.com)

---

> **note**
> Task tested to work on v4.9.0, written and designed on v4.5.1. v4.9 has a couple of known issues with details being unable to be read from events. If you face issues, fallback to e.g v4.5.1, which still works.

---

Wazuh is an free and open source "unified XDR and SIEM protection for endpoints and cloud workloads." In this task we are going to focus more on the [SIEM](https://www.gartner.com/en/information-technology/glossary/security-information-and-event-management-siem) side of things. Take a look at their [website](https://wazuh.com/platform/siem/) and [github](https://github.com/wazuh/wazuh) to familiarize yourself with the capabilities and features Wazuh SIEM offers.

Start of with deploying the Wazuh [single-node on Docker](https://documentation.wazuh.com/current/deployment-options/docker/wazuh-container.html). You should go through the documentation to understand what's going on, but the following commands should be enough:

```console
git clone https://github.com/wazuh/wazuh-docker.git -b <VERSION NUMBER e.g v4.9.0 or v4.5.1>
cd wazuh-docker/single-node
docker-compose -f generate-indexer-certs.yml run --rm generator
docker-compose up -d
```

You can access the Wazuh (WUI)WebUI at your localhost, to do this go to [https://localhost](https://localhost). By default Wazuh uses self signed certs and you won't be directed to the site directly, instead click the advanced tab and find the button for "Accept the risk and continue". This will direct you to the site, and from then on you should be able to use it normally.

Next deploy an agent or agents. You can deploy the agent(s) on your own platform(server, desktop, etc...) or the course virtual machine. For the course virtual machine use the "installation from source" --> "installing Wazuh agent from sources". Arch linux, the course VM uses pacman for package management so you could use that. [Installation alternatives](https://documentation.wazuh.com/current/deployment-options/wazuh-from-sources/wazuh-agent/index.html) in the documents.  

For other environments, find the appropriate [installation documention](https://documentation.wazuh.com/current/installation-guide/wazuh-agent/index.html), many can be installed in the Wazuh WUI(Web User Interface), for windows, choose windows and fill out the details, run the command and start the agent. For the ip address of the server, you can use your internal ip address.

Create a directory named integrity and add a file to it, then enable FIM(File Integrity Monitoring) on your agent(s) on that folder, you should also set the scan frequency at around 60 seconds, so you won't have to wait for the events. 

You are to trigger the FIM with atleast two different events. Then answer the questions below.

**What to return:**
1. What rule descriptions did you get?
2. What are the MITRE ATT&CK techniques(include ID) Wazuh reports for these events?
3. What is the reported MITRE techniques for deleting files or directories inside monitored directories?
4. Explain in your own words where, when and why should these systems be used, would they be helpful in banking.
5. Add a screenshot of your integrity monitoring events tab.

### Feedback
Be sure to give feedback on these tasks. Do you feel these to be the kind of skills you might need or want?
