set number " Show file line numbers
set mouse=a " To enable mouse interaction with it
set numberwidth=1 " size of the line numbers
set clipboard=unnamed " enable the nvim clipboard for the clipboard OS
syntax enable " enable hightlights syntaxis
set showcmd " show suggestions commands in this cmd line
set ruler " enable for nvim by default, but not in vim
set encoding=utf-8 " encode the plain text 
set showmatch " match the parethenses in a function, for example
set sw=4 " Indet with 4 spaces

set relativenumber " for better performance to move the source code

set laststatus=2 " enable the better line botton for information 
set noshowmode " disable to show modes (vim is a text editor based in modes)

" Plugins!
call plug#begin('~/.vim/plugged')

" Themes
Plug 'morhetz/gruvbox'

" IDE
Plug 'easymotion/vim-easymotion' " To move in the file very faster
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}

Plug 'mattn/emmet-vim'
Plug 'preservim/nerdcommenter'


call plug#end()


" Setting up for plugins
colorscheme gruvbox " set the theme
" For NerdTree
let NERDTreeQuitOnOpen=1
" For EasyMotion
let g:EasyMotion_do_mapping=1
" For Airline
let g:airline_powerline_fonts=1
let g:airline#extensions#tabline#enabled = 1
"For CoC
inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
" use <tab> for trigger completion and navigate to the next complete item
function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~ '\s'
endfunction

inoremap <silent><expr> <Tab>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<Tab>" :
      \ coc#refresh()

" use <c-space>for trigger completion
inoremap <silent><expr> <NUL> coc#refresh()


let mapleader = " "

nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>

" Tab navigation like Firefox or Edge
nmap <Leader>, :bp<CR>
nmap <Leader>. :bn<CR>

nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>
nmap <Leader>tt :wq<CR>

let g:tmux_navigator_no_mappings = 1

" nnoremap <silent> <C-b>h :TmuxNavigateLeft<CR>
" nnoremap <silent> <C-b>j :TmuxNavigateDown<CR>
" nnoremap <silent> <C-b>k :TmuxNavigateUp<CR>
" nnoremap <silent> <C-b>l :TmuxNavigateRight<CR>
" nnoremap <silent> <C-b>\ :TmuxNavigatePrevious<CR>

nnoremap <silent> <C-h> :TmuxNavigateLeft<CR>
nnoremap <silent> <C-j> :TmuxNavigateDown<CR>
nnoremap <silent> <C-k> :TmuxNavigateUp<CR>
nnoremap <silent> <C-l> :TmuxNavigateRight<CR>

" :imap kj<ESC>
:imap jj <Esc>

:vnoremap <Leader>y "+y

" For the problem characters
if !exists('g:airline_symbols')
        let g:airline_symbols = {}
    endif

    " unicode symbols
    let g:airline_left_sep = '»'
    let g:airline_left_sep = '▶'
    let g:airline_right_sep = '«'
    let g:airline_right_sep = '◀'
    let g:airline_symbols.crypt = '🔒'
    let g:airline_symbols.linenr = '☰'
    let g:airline_symbols.linenr = '␊'
    let g:airline_symbols.linenr = '␤'
    let g:airline_symbols.linenr = '¶'
    let g:airline_symbols.maxlinenr = ''
    let g:airline_symbols.maxlinenr = '㏑'
    let g:airline_symbols.branch = '⎇'
    let g:airline_symbols.paste = 'ρ'
    let g:airline_symbols.paste = 'Þ'
    let g:airline_symbols.paste = '∥'
    let g:airline_symbols.spell = 'Ꞩ'
    let g:airline_symbols.notexists = 'Ɇ'
    let g:airline_symbols.whitespace = 'Ξ'

    " powerline symbols
    let g:airline_left_sep = ''
    let g:airline_left_alt_sep = ''
    let g:airline_right_sep = ''
    let g:airline_right_alt_sep = ''
    let g:airline_symbols.branch = ''
    let g:airline_symbols.readonly = ''
    let g:airline_symbols.linenr = '☰'
    let g:airline_symbols.maxlinenr = ''
