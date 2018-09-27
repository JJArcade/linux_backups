set expandtab
set tabstop=4
set softabstop=4
set shiftwidth=4

set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'pangloss/vim-javascript'
Plugin 'tmhedberg/simpylfold'
Plugin 'L9'

call vundle#end()
filetype plugin indent on
