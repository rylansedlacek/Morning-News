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
          <p> a) Once you create an account you will see this dashboard:</p>
          
 ![image](https://github.com/user-attachments/assets/2a76c7d2-d32a-4504-9f46-9b872f908fdc)
          <p> b) Create an App, and use this redirect URI: <b>http://localhost:8888/callback</b> </p>
          <p> c) You should now have access to your <b>Client</b> and <b>Client-Secret</b> ID's.</p>
          ![image](https://github.com/user-attachments/assets/a6cc4fc9-a14c-4cb3-82ea-af65992e9604)
          <p> d) Write these down, as we will need them in the future. </p>

<h3>2. Set up an AWS Account and Lambda Function</h3>
          <p> a) First create an AWS account</p>
          <p> b) Now, navigate to <b>IAM Dashboard</b> on AWS. You can just search this at the top</p>
          <p> c) Select Roles from the side menu</p>
        
![image](https://github.com/user-attachments/assets/0850c008-0f1e-4330-9408-59f5f9b76874)
          <p> d) Now create a new Role with the following permissions:<p>
          <li>AWSLambdaBasicExecutionRole</li>
          <li>CloudWatchEventsFullAccess</li>
          <br></br>
          <p> (I just named mine "LambdaWithCloudWatchAccess")</p>
          <p> e) Now, navigate to the <b>Lambda Dashboard</b></p>
          <p> f) Using the screenshot as a guide, set up a new Lambda Function.</p>

  ![image](https://github.com/user-attachments/assets/e1569848-529c-4518-8a77-bfb1f0095f11)


<h3>3. Get Podcast URI, Refresh Token, and Device ID</h3>
      <p>a) Getting a Podcast URI is simple, copy this part of the url:</p>
  
  ![image](https://github.com/user-attachments/assets/0a802af0-5e51-40c7-80b8-13054b22bf9b)
      <p>b) Then just add <b>spotify:show:WHATYOUCOPIEDHERE</b></p>
      <p>c) Getting the Refresh Token is a bit tricky, first get your Authorization Code:</p>
      
      https://accounts.spotify.com/authorize?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&scope=YOUR_SCOPES
  <p>d) Now using <b>Curl</b> enter the following into your terminal:</p>
  
      curl -X POST "https://accounts.spotify.com/api/token" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -H "Authorization: Basic YOUR_BASE64_ENCODED_CLIENT_ID_AND_SECRET" \
        -d "grant_type=authorization_code" \
        -d "code=YOUR_AUTHORIZATION_CODE" \
        -d "redirect_uri=YOUR_REDIRECT_URI"
  <p>e) After running, you should get your Authorization Code, write that down!</p>
  <p>f) To get your Device-ID, first REPLACE the information in <b>getaccess.py</b> (I have it commented.)</p>
  <p>g) Now, ensure that the device you want to use is <b>ACTIVELY USING SPOTIFY</b></p>
  <p>h) Run the program, and write down your Device-ID</p>

<h3>4. Set up Lambda Environmental Variables</h3>
  <p>a) First Navigate to the <b>Function Pane</b> from the Lambda Dashboard</p>
  <p>b) Head into your previously created Function's Dashboard</p>
  <p>c) Then head to the Configuration Panel</p>

![image](https://github.com/user-attachments/assets/68f4e262-619c-4f10-8a90-a2a82d4e7e8a)
  <p>d) Using those values from <b>Steps ONE and THREE</b>, create the following Environmental Variable <b>KEY VALUE PAIRS:</b></p>

![image](https://github.com/user-attachments/assets/7569cce1-5928-4bcd-8f3c-aaf9063cd847)

<h3>5. Create ZIP file with Code and Requests Python Lib</h3>
  <p>Lambda only has a few Python Libraries, so we'll need to install requests on our own. I did so on my terminal.</p>
  <br>
  <p>a) First create a directory:</p>

    mkdir myCoolDir
  <p>b) Go into it:</p>

    cd myCoolDir

  <p>c) Now type the following:</p>

    pip install requests --target .

  <p>d) Ok, now create a new python file called <b>lambda_function.py</b> (MUST BE NAMED THIS!!) </p>

    vim lambda_function.py
  <p>e) Paste the code from the file named the SAME THING inside of this repo.</p>
  <p>f) Now type the following to zip the file for our use:</p>

    zip -r lambda_function.zip myCoolDir

  <p>g) Using something like <b>FileZilla</b> or <b>STP?</b> download this to your local machine</p>
  <p>h) Then inside of your Function Dashboard, upload that zip file</p>
  <p>i) Make sure to Deploy your code, if not done automatically.</p>

![image](https://github.com/user-attachments/assets/2d8246e2-2d92-4d97-92ec-e6e295bd8270)

<h3>6. Test it before Scheduling</h3>

  <p>a) First open up your device, and then open <b>Spotify</b></p>
  <p>b) Now create a new Test Event, clicking this button:</p>

![image](https://github.com/user-attachments/assets/8e82e2e2-e01c-4882-9d2c-46d6d3ec3938)

  <p>c) Be sure to change the JSON section to be blank, as we require no input: </p>

    {}
  <p>d) Go ahead and run the Test, and check your device to see if the podcast has began to play.</p>
  <p>e) If you recieve an ERROR, ensure your device has Spotify OPENED!</p>
  <p>f) Any other errors may be caused if one of your access keys was entered incorrectly.</p>

<h3>6. Set up a Scheduler</h3>
  <p>a) Navigate to the AWS EventBridge Scheduler</p>
  <p>b) Click the Create Schedule button on the dashboard </p>
  <p>c) For our example we are going to run this code EVERYDAY at 7:05 AM</p>
  
  ![image](https://github.com/user-attachments/assets/11917efd-c201-4959-ba01-d7b97509339b)

  <p>d) On the next page select the following, using your Function in the REDBOX</p>

  ![image](https://github.com/user-attachments/assets/b992a9bb-6a77-48e7-9444-822a614f9453)

  <p>e) Finally, in the Settings Panel select the Create New Role option, and leave the defaults</p>

  ![image](https://github.com/user-attachments/assets/ef4c3a5a-3a56-4581-9c71-4bb550bcd93b)

  <p>f) Review, and save your scheduled event</p>
  <p>g) Wait till the next day and listen to your show automatically!</p>

