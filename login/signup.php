<?php
session_start();
include ("connect.php");


if ($_SERVER['REQUEST_METHOD'] == "POST") {
  

$username=$_POST['username'];

$contact=$_POST['contactno'];
$password=$_POST['password'];
$email=$_POST['email'];
if (!empty($email) &&!empty($password) &&! is_numeric($email))
{
    $query="insert into login values('$username','$contact','$password','$email')";
    mysqli_query($conn,$query);
    echo"<script type='text/javascript'> alert('successfully Registration')</script>";
}
else{
    echo "<script type='text/javascript'>alert('please enter vaild information')</script>";

}


}


    
?>





<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .navbar h1 {
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
          color: blue;
         border-radius: 10px;
        }
        h3{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        }
        h2{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        }
        .container{
            background: white;
            position: absolute;
            display:block;
            color: black;
            padding: 30px 60px ;
            margin-left: 550px; 
            border: 2px solid yellow;
            border-radius: 5px;
            
        }
        input{
           
            border:3px solid brown;
            border-radius: 5px;
        }
        .box{
            padding: 8px 70px;
        }
        button{
          margin-left: 100px; 
          color: white;
          background: brown;
          padding: 10px 20px;
          border-radius: 5px;
          font-size: larger;
        }
        label{
            font-size: larger;
            border-radius: 5px solid black;
            font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif    ;
            
                
        }
         
    </style>
</head>
<body style="background-color: orange;">
    <nav class="navbar">
       <center><h1>SIGN UP</h1>
      
       
       </center> 
      
    </nav>
<div class="container">
    <h2>HELLO</h2>
    <h3>Please fill this form to create account...!</h3>
    <form action="" method="post">
        <label for="name">Username:</label><br> 
        <input type="text" id="name" class="box" name="username" placeholder="enter the username..."><br><br>
        <label for="phone">Contact.No:</label><br>
        <input type="phone" name="contactno" id="phone" class="box" placeholder="enter the contact no..."><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" class="box" name="password" placeholder="enter the password..."><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" class="box" name="email" placeholder="enter the email..."><br><br>
        <button type="submit" name="submit" value="sign up" >Sign Up</button>

    </form><br>
    <u class="line"><a href="welcome.php">Already have an account Click Here for login.!</a></u>
</div>
</body>
</html>
