## Switching remote URLs from HTTPS to SSH



1. Open Terminal.

2. Change the current working directory to your local project.

3. List your existing remotes in order to get the name of the remote you want to change.

   Exemple:

   ```commonlisp
   $ git remote -v
   origin  https://github.com/catalpainternational/project_name.git (fetch)
   origin  https://github.com/catalpainternational/project_name.git (push)
   ```

4. Change your remote's URL from HTTPS to SSH with the `git remote set-url` command.

   ```commonlisp
   $ git remote set-url origin git@github.com:catalpainternational/project_name.git.git
   ```

5. Verify that the remote URL has changed.

``````commonlisp
$ git remote -v
# Verify new remote URL
origin  git@github.com:catalpainternational/project_name.git (fetch)
origin  git@github.com:catalpainternational/project_name.git (push)
``````

6. Checking `SSH`List :

   ``````typescript
   $ ls ~/.ssh
   authorized_keys  id_rsa  id_rsa.pub  known_hosts
   ``````

7. Copy  your `ssh` from  this file  `id_rsa.pub` and go to the github.com follow this link https://github.com/settings/keys and then click on button  `New SSH Key` and paste in ssh.

   ``````commonlisp
   $ cat ~/.ssh/id_rsa.pub
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCV+jO67aJ16Zlxd439/VuXxkFMwqHWlUcjiDLNuJMcP6b/t/dlHcjRT+fRLcgJiQVBd6HFwzVhbD7916AM8i3an5wGBI4I2ONjywwN7uzsXC4rFeIwY7bPRSX4MDHnJXmhnKmN1LhO3JPd+pr8jSwf0NTCnx98KKFkNTVNdIt+V9UQbxsIhS0eBMrUq9fHaqIRprvzkeNCwrHEIpUgIqTPw1SGYsQ8GuV5kCJYo3jvIEZyWVIpm2RTgkPyzotQauNEAjKHTDW89nwcQkpt2VlDFoJ9dI5asEoUmKGxF7RCFEH+QbA5rkVK+LNX/qNdt0oSbFUedOvuTKM2MlYmS6FcVwE1rVAyqdbuiAXF3prMNq4ZLhHUu/u+w4FrHCNObU5MlnbudWBeD2kVIsi58NjxV9XjrL+6cLh/Oyv4IHvk70EC7mYLW6cSUyH7Gs6LAHEJrgfUvgvBKirYSUMSP6BmF6WtoTouTBAaNHizHZYBqIbYQb15OKXF14axpAKekMRwAG4n656TC7Yk7b5kjzXuPX4FJPgCA7Z+wW0ozvyCGf2X6/KQCUCRpebRYK70Q2cIAyayei8N4gEUIb2VMfVQ3fmMrsZLjh8KhLYKMkb752so6N9r+Jd706O+udY2JUfnE88NbbEzHy4h8xB7twYbqAKbyKTXfd67kwc+X+mo4Q== dejesushonorio03@gmail.com
   ``````

