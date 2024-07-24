<h1>Spotify Morning News</h1>

<h2>About:</h2>

  
- Created using Python and AWS Lambda.
- July 2024 

<p>I'm not much of a news guy. However, I've been trying to practice with APIs this summer, 
  Spotify seemed like an obvious choice. I decided that I wanted to play a 
  <a href="https://open.spotify.com/show/5YRTZNTGT7MWhktYYpjR8v">news podcast</a> every
morning at 7:05 a.m. The tutorial is below, enjoy. </p>


<h2>Tutorial:</h2>

<h3>1. Set up a Spotify Developer Account</h3>
          <p> A) Once you create an account you will see this dashboard:</p>
          
 ![image](https://github.com/user-attachments/assets/2a76c7d2-d32a-4504-9f46-9b872f908fdc)
          <p> B) Create an App, and use this redirect URI: <b>http://localhost:8888/callback</b> </p>
          <p> C) You should now have access to your <b>Client</b> and <b>Client-Secret</b> ID's.</p>
          <p> D) Write these down, as we will need them in the future. </p>
