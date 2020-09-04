# About

# Installation
Currently this package is not available on pypi. To install use the following command

<code>pip install -e git+https://github.com/HellstromIT/quickswitch.git@{tag to install}#egg=quickswitch</code>

Make sure you replace {tag to install} with a tag from https://github.com/HellstromIT/quickswitch/tags

There's no default search directories out of the box so to add a directory you wish to include run 

<code>qs --add full_path_to_directory</code>

The command will only search one level deep so if you have multiple levels that you wish to search you need to add them one at a time.

In order for the command to work correctly you will also need to create a function in your shell. The below functions assume that you want the command to be `qq`. 

After adding the relevant function restart your shell.

## Bash 
Add the following to your $HOME/.bashrc or in $HOME/.bash_functions.d/qq.sh

```
qq () {
  directory=$(qs)
  if [ -z "$directory" ]
  then
    echo
  else
    cd $directory
  fi
}
```

## Fish
Create a function in $HOME/.config/fish/functions/qq.fish

```
function qq
    set directory (qs)
    if set -q directory
        cd $directory
    else
        echo
    end
end
``` 

## zsh
Create a function in $HOME/.zshrc

```
qq () {
  directory=$(qs)
  if [ -z "$directory" ]
  then
    echo
  else
    cd $directory
  fi
}
```
