# Instagram-Brute-Forcer
Brute forces multiple Instagram accounts for you.

## Information
This was made to show you how easy it is to target celebrities or friends and possibly expose their passwords. As most people have their date of birth, first and last name included in their passwords you can save time from manually trying all combinations with this simple brute forcer. Please do not use this, it is only meant for you to learn how hackers can use such a technique (the [Ava Rose hacker](https://github.com/zoony1337/Strong-Password-Generator/blob/master/README.md) inspired me and made me think he used a method like this) and possibly get into someone's account. However, if you choose to use this you are doing it at your own risk. I only spent 2 hours on this brute forcer so it can be improved. I just wanted you to get the idea of how it would work — you can of course add more combinations if you'd like.<br/>
Keep in mind that the API I used has kind of been patched from yesterday (when I started working on it and testing it), you sometimes get the rate limited 429 error code which would return the password as invalid even though it might be valid. This kind of proves that I'm uploading this for educational purposes only (it's not 100% functional anymore).

## Preview
![](https://i.imgur.com/6ksJKt3.png)
![](https://i.imgur.com/hN7u41x.gif)
![](https://i.imgur.com/f3Jk11t.png)
![](https://i.imgur.com/O28FZ3m.png)

## Usage
Attn: I mainly develop programs for Windows, so they would most likely not work if you're using another OS.<br/>
Run this command in CMD, terminal or PowerShell (if you don't already have the **InstagramAPI** module installed):
```
pip install InstagramAPI
```
**Brute force multiple targets:**
1. Paste your targets' usernames, birthdays, first and last names in Accounts.json — you can find celebrities' birthdays [here](https://www.famousbirthdays.com).
2. Run the script.
3. Type "1" and hit ENTER.
4. Sit back and wait for a valid password!

**Brute force your target using a custom passwordslist:**
1. Paste the passwords you'd like to try — you can find the most commonly used passwords [here](https://www.scrapmaker.com/data/wordlists/dictionaries/rockyou.txt).
2. Run the script.
3. Type "2" and hit ENTER.
4. Sit back and wait for a valid password!

## Legal Notice
This is illegal if you use this without the consent of the owners (in this case, the Instagram team). I am not accountable for anything you get into, this was just a speedrun to demonstrate how brute forcers work. This is 100% educational, please do not misuse this tool.
