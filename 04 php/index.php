<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Tutorial</title>
    <style>
        .container {            
            padding: 10px;
            background-color: aquamarine;
        }

        input{
            width: 80%;

        }

        .btn-container{
            display: flex; 
            justify-content: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>participation form</h1>
        <form action="index.php" method="get">
            <input type="text" name="name" id="name" placeholder="enter name"><br>
            <input type="text" name="name" id="name" placeholder="enter name"><br>
            <input type="number" name="age" id="age" placeholder="enter age"><br>
            <select name="gender" id="gender">
                <option value="male">male</option>
                <option value="female">female</option>
            </select><br>   
            <div class="btn-container">
                <button class="btn">submit</button>
                <button class="btn">reset</button>
            </div>
        </form>
    </div>
</body>
</html>
