# Go instalation and configuration

While using to configure arm image, installing Go version 1.18 via apt packge manager is way to go.
```
sudo apt install golang -y
export GOPATH="$HOME/go"
export PATH="$GOPATH/bin:$PATH"
export GOROOT="/usr/lib/go"
```
Those commands should be in my dot files `.basrc` file
