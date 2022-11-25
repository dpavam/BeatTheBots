# BeatTheBots

### This is a trial script with non-profit purposes to corroborate if obtaining high-demand football tickets for Real Madrid is at all possible. 
### The idea of this script is to replicate the actions of a normal user and try to beat the bots and scalpers that flood the ticketing website. 

## Libraries: 
  - pip install selenium
  - pip install webdriver-manager
  
## Browser requirements:
- Google Chrome
  
### How it works
- Execute the file `ticket_function.py`
 This should open a Chrome tab with the link to the tickets for the desired match. The script takes care of the rest. 

- *Do not minimise the window*, leave it in the background instead. 

The script will attempt to scroll down to the stadium's sections, select the available blocks, and click on an available seat to lock it. If it fails, it refreshes the site and starts again. 

## Considerations

The current method can search for about 4 minutes, after this the site does not behave properly. When this time is reached, 3 beeps will ring to alert the user it is time to re-execute the file. 

If by any chance the script finds there is an available ticket, it beeps *once* and attempts to select the available seat. If there is no red seat selected, it means a bot secured it. 

## Update
After executing this script for 2 weeks, it was found that tickets do become available but are impossible to secure. A potential hypothesis is that tickets are always taken by scalpers and only purchased after a user buys one on their re-sale webiste. 
This behaviour was mostly seen in the hours prior to the RM-FCB match. 

It is recommended that captchas and secure bot eliminations are incoorporated into the website. 

