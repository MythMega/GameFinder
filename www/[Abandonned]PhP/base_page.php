<?php include 'include/base.php'; ?>

<h1>base page, start a new page from copying this one</h1>



<!DOCTYPE html>
<html lang="fr">
<head>
  <title>GF</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- my css -->
  <link rel="stylesheet" href="./css/style.css">
  <!-- Bootstrap -->
  <link rel="stylesheet" href="./css/bootstrap.css">
  <!-- jQuery library -->
  <script src="./js/jquery.min.js"></script>

  <!-- Popper JS -->
  <script src="./js/popper.min.js"></script>

  <!-- Latest compiled JavaScript -->
  <script src="./js/bootstrap.min.js"></script>
           
</head>
<body>
  
<!-- Menu de base -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Features</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Pricing</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Dropdown link
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <a class="dropdown-item" href="#">Action</a>
              <a class="dropdown-item" href="#">Another action</a>
              <a class="dropdown-item" href="#">Something else here</a>
            </div>
          </li>
        </ul>
      </div>
    </nav>
    <div class="banner_container"></div>
    <div class="container">
    </div>
</body>
</html>
