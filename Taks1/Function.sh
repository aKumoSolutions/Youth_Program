#!/bin/bash

github () {
    read -p "Input the repository link here" link 
    git clone $link 
    echo "Clone Complete, opening with VSCode" 
    code . 
}