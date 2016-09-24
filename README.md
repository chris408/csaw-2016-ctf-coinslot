# csaw-2016-ctf-coinslot
This is my solution for the CSAW 2016 CTF coinslot problem.

For this problem you would connect to a server that would print some output. You needed to process the output and then make the appropriate response.

    $ nc misc.chal.csaw.io 8000
    $0.07 <---- The server is requesting change for this amount of currency.
    $10,000 bills: 0
    $5,000 bills: 0
    $1,000 bills: 0
    $500 bills: 0
    $100 bills: 0
    $50 bills: 0
    $20 bills: 0
    $10 bills: 0
    $5 bills: 0
    $1 bills: 0
    half-dollars (50c): 0
    quarters (25c): 0
    dimes (10c): 0
    nickels (5c): 1
    pennies (1c): 2
    correct!
    $0.10 <--- the next amount requested by the server.
    $10,000 bills:

This would repeat for about 100 times per currency size. It started with .XX, then went to X.XX, then XX.XX, and so on until you were in the tens of thousands of dollars. A full run of the program would take around 8 minutes to process through.
It was a fun challenge that I enjoyed working my way though. 

The server side code was posted here by the CTF:
https://github.com/isislab/CSAW-CTF-2016-Quals/tree/master/Misc/coinslot
