<?php
session_start();
include ("connect.php");
if($_SERVER['REQUEST_METHOD']=="POST"){
    $username=$_POST['username'];
    $password=$_POST['password'];
    if (!empty($username) && !empty($password) && !is_numeric($username)){
        $query="select * from login where username='$username'";
        $result=mysqli_query($conn,$query);
        if($result){
            if($result && mysqli_num_rows($result)>0)
            {
                $userdata=mysqli_fetch_assoc($result);
                if($userdata['password']==$password){
                    header("location:welcome.php");
                    die;
                }

            }
        }
    
    echo "<script type='text/javascript'>alert('correct username or password')</script>";

}
else{

 echo "<script type='text/javascript'>alert('worng username or password')</script>";

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
       <center><h1>LOGIN</h1>
      
       
       </center> 
      
    </nav>
<div class="container">
    
    <form action="tr.html" method="post">
        <label for="name">Username:</label><br> 
        <input type="text" id="name" class="box" name="username" placeholder="enter the username..."><br><br>
        
        <label for="password">Password:</label><br>
        <input type="password" id="password" class="box" name="password" placeholder="enter the password..."><br><br>
       
        <button type="submit" name="submit" value="sign up" >Login</button>

    </form><br>
   
</div>
</body>
</html>
