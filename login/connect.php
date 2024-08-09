<?php
$server ="localhost";
$username="root";
$password="";
$dbname="database1";
$conn = mysqli_connect($server,$username,$password,$dbname);
if($conn){
    echo "sucessfully";
}
else{
die;
}
?>