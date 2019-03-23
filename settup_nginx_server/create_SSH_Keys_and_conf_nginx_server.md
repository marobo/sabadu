# How To Create SSH Keys

The first step to configure SSH key authentication to your server is to generate an SSH key pair on your local computer.

To do this, we can use a special utility called `ssh-keygen`, which is included with the standard OpenSSH suite of tools. By default, this will create a 2048 bit RSA key pair, which is fine for most uses.

On your local computer, generate a SSH key pair by typing:

```
$ sudo apt install openssh-client
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/username/.ssh/id_rsa):
```

The utility will prompt you to select a location for the keys that will be generated. By default, the keys will be stored in the `~/.ssh` directory within your user's home directory. The private key will be called `id_rsa` and the associated public key will be called `id_rsa.pub`.

Usually, it is best to stick with the default location at this stage. Doing so will allow your SSH client to automatically find your SSH keys when attempting to authenticate. If you would like to choose a non-standard path, type that in now, otherwise, press ENTER to accept the default. If you had previously generated an SSH key pair, you may see a prompt that looks like this: Entry to server root:

```
/home/username/.ssh/id_rsa already exists.
Overwrite (y/n)?
```

If you choose to overwrite the key on disk, you will **not** be able to authenticate using the previous key anymore. Be very careful when selecting yes, as this is a destructive process that cannot be reversed.

```
Created directory '/home/username/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again: 
```

Next, you will be prompted to enter a passphrase for the key. This is an optional passphrase that can be used to encrypt the private key file on disk.

You may be wondering what advantages an SSH key provides if you still need to enter a passphrase. Some of the advantages are:

- The private SSH key (the part that can be passphrase protected), is never exposed on the network. The passphrase is only used to decrypt the key on the local machine. This means that network-based brute forcing will not be possible against the passphrase.
- The private key is kept within a restricted directory. The SSH client will not recognize private keys that are not kept in restricted directories. The key itself must also have restricted permissions (read and write only available for the owner). This means that other users on the system cannot snoop.
- Any attacker hoping to crack the private SSH key passphrase must already have access to the system. This means that they will already have access to your user account or the root account. If you are in this position, the passphrase can prevent the attacker from immediately logging into your other servers. This will hopefully give you time to create and implement a new SSH key pair and remove access from the compromised key.

Since the private key is never exposed to the network and is protected through file permissions, this file should never be accessible to anyone other than you (and the root user). The passphrase serves as an additional layer of protection in case these conditions are compromised.

A passphrase is an optional addition. If you enter one, you will have to provide it every time you use this key (unless you are running SSH agent software that stores the decrypted key). We recommend using a passphrase, but if you do not want to set a passphrase, you can simply press ENTER to bypass this prompt.

```
Your identification has been saved in /home/username/.ssh/id_rsa.
Your public key has been saved in /home/username/.ssh/id_rsa.pub.
The key fingerprint is:
a9:49:2e:2a:5e:33:3e:a9:de:4e:77:11:58:b6:90:26 username@remote_host
The key's randomart image is:
+--[ RSA 2048]----+
|     ..o         |
|   E o= .        |
|    o. o         |
|        ..       |
|      ..S        |
|     o o.        |
|   =o.+.         |
|. =++..          |
|o=++.            |
+-----------------+
```

Find `SSH KEYS`:

```
$ ls ~/.ssh/                 
authorized_keys  id_rsa  id_rsa.pub  known_hosts
```

Copy `SSH KEY`  with gedit text editor,

**Example :**

```
$ gedit ~/.ssh/id_rsa.pub
```

You will see the key's content, which may look something like this in your gedit text editor :

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNqqi1mHLnryb1FdbePrSZQdmXRZxGZbo0gTfglysq6KMNUNY2VhzmYN9JYW39yNtjhVxqfW6ewc+eHiL+IRRM1P5ecDAaL3V0ou6ecSurU+t9DR4114mzNJ5SqNxMgiJzbXdhR+j55GjfXdk0FyzxM3a5qpVcGZEXiAzGzhHytUV51+YGnuLGaZ37nebh3UlYC+KJev4MYIVww0tWmY+9GniRSQlgLLUQZ+FcBUjaqhwqVqsHe4F/woW1IHe7mfm63GXyBavVc+llrEzRbMO111MogZUcoWDI9w7UIm8ZOTnhJsk7jhJzG2GpSXZHmly/a/buFaaFnmfZ4MYPkgJD username@example.com
```



# How To Create Nginx with SSH Keys

The first step to configure `ngin server` is  login to root with your `IP_ADDRESS`:

`$ ssh root@128.199.133.236`

You will see the content, which may look something like this in your command:

```
Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-112-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.


Last login: Sun Jan 28 12:54:35 2018 from 103.238.116.7
root@ony:~# 
```

And then using `sudo apt-get`, update your package indexes and then install the service:

```
root@ony:~# sudo apt-get update
root@ony:~# sudo apt-get install nginx
```

For more details on the installation and setup process, follow our tutorial on [How To Install Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04).

## Check the status of nginx

You can check whether or not Nginx is running on your machine by entering the following into your command prompt:

```
root@ony:~# sudo systemctl status nginx
```

You will see the content, which may look something like this in your command:

```
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Sat 2018-01-27 02:13:41 UTC; 2 days ago
  Process: 2512 ExecStop=/sbin/start-stop-daemon --quiet --stop --retry QUIT/5 --pidfile /run/nginx.pid (code=exited, status=0/SUCC
  Process: 2523 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
  Process: 2520 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
 Main PID: 2527 (nginx)
    Tasks: 2
   Memory: 1.8M
      CPU: 95ms
   CGroup: /system.slice/nginx.service
           ├─2527 nginx: master process /usr/sbin/nginx -g daemon on; master_process on
           └─2528 nginx: worker process                           

Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.
lines 1-15/15 (END)
```

## Enable Nginx

By default, Nginx is configured to start automatically when the server boots. If desired, you can disable this behavior by typing:

```
root@ony:~# sudo systemctl disable nginx
```

To re-enable the service to start up at boot, type:

```
root@ony:~# sudo systemctl enable nginx
```

## Stopping, Starting, and Reloading Nginx

To stop your already-running Nginx server:

```
root@ony:~# sudo systemctl stop nginx
```

Once the server has been stopped, you can start it again by typing:

```
root@ony:~# sudo systemctl start nginx
```

To stop and then start Nginx again, type:

```
root@ony:~# sudo systemctl restart nginx
```

You also have the ability to reload Nginx without disrupting connections:

```
root@ony:~# sudo systemctl reload nginx
```

To learn more about `systemd` and the `systemctl` command, check out this [introduction to systemd essentials](https://www.digitalocean.com/community/tutorials/systemd-essentials-working-with-services-units-and-the-journal).

## Check configuration nginx file

```
root@ony:~# sudo nginx -t
```

You will see the content, which may look something like this in your command:

```
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Try `ls` sites-available to see default file:

```
root@ony:~# ls /etc/nginx/sites-available/
default 
```

Open the default file with vim and copy Virtual Host configuration example in the bottom You can move that to a different file under sites-available example give the new name of the file line  `my_test`and symlink that to sites-enabled/ to enable it. :

- Bottom of the `default`file.

```
# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
#server {
#       listen 80;
#       listen [::]:80;
#
#       server_name example.com;
#
#       root /var/www/example.com;
#       index index.html;
#
#       location / {
#               try_files $uri $uri/ =404;
#       }
#}   
```

- New`my_test` file:

```
# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
server {
        listen 80;
        listen [::]:80;

        server_name ony;

        root /var/www/ony;
        index index.html;

        location / {
                try_files $uri $uri/ =404;
        }
}
```

Create symlink with `my_test` file to sites-enabled/ to enable it. :

```
root@ony:~# ln -s /etc/nginx/sites-available/my_test /etc/nginx/sites-enabled/
```

This is the location of the default document root from which the actual web content is served. The document root can be changed by altering Nginx configuration files.

```
root@ony:~# ls /var/www/html/index
```

Made own `index.html` file inside that so we cant access the index we giving in `my_test` file:

```
root@ony:~# /var/www/html/index
```

Try Restart our nginx server:

```
root@ony:~# sudo systemctl restart nginx
```

And then go to your browser type your `IP_ADDRESS`  run with port `80`,

Example:

https://128.199.133.236:80/

Sites-available: file neebe la moris

Sites-enable: file moris

Copy public key: