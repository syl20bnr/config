" ----------------------------------------------
"       Bartevil's Vim configuration files
" ----------------------------------------------

:filetype plugin on              "enable filetype plugins
let mapleader ='\'               "mapleader for additional functions
let maplocalleader ='|'          "mapleader for additional functions
syntax on                        "syntax highlighting
set background=dark              "solarized color
colorscheme solarized
set encoding=utf-8
set rtp+=~/.config/powerline/powerline/bindings/vim

" From mswin.vim -------------------------------

" backspace and cursor keys wrap to previous/next line
set backspace=indent,eol,start whichwrap+=<,>,[,]
" backspace in Visual mode deletes selection
vnoremap <BS> d

" Properties -----------------------------------
set tabpagemax=9999              "Allows to open a lot of different tabs at startup
set showtabline=0                "Never show tab line
set autoread                     "Auto read file modifications
set cursorline                   "Highlight current line
set nocompatible
set nocursorcolumn               "Highlight current column
set guioptions-=T                "remove toolbar
set guioptions-=b                "Added horizontal scroll bar
set guioptions-=r                "remove right-hand scroll bar
set guioptions-=l                "remove left-hand scroll bar
set incsearch                    "jumps to search word as you type
set hlsearch                     "highlight all search results
set ignorecase                   "ignore case during search
set smartcase                    "enable case sensitive search when a caps is entered
set smarttab                     "use tabs at the start of a line, spaces elsewhere
set number                       "line numbers
set smartindent                  "quto indent on new lines
set tabstop=4                    "number of spaces to make a tab
set shiftwidth=4                 "for shift/tabbing
set nowrap                       "no word wrapping
set nobackup                     "disable swap, backup files
set nowritebackup                "no backup file on writing
set noswapfile                   "no swap file
"set foldmethod=indent            "always used automatic fold based on indentation
set guioptions-=m                "remove menu bar
set clipboard=unnamedplus        "yank/past to both system clipboard
"set colorcolumn=80               "print margin
"disable beeps
set noeb vb t_vb=
au GUIEnter * set vb t_vb=

"Following three lines remove the auto copy function from VIM
set guioptions-=a
set guioptions-=A
set guioptions-=aA

" what to show when I hit :set list
set listchars=tab:\|_,nbsp:·,trail:·,extends:·,precedes:·
set list

" only letters for showmarks plugin
let g:showmarks_enable=1
let g:showmarks_include="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

" tabbed buffers management
:nmap <C-t> :tabnew<cr>
:nmap <C-S-tab> :tabprevious<cr>
:nmap <C-tab> :tabnext<cr>
:nmap <C-left> :tabprevious<cr>
:nmap <C-right> :tabnext<cr>
:nmap <C-h> :tabprevious<cr>
:nmap <C-l> :tabnext<cr>
:map <C-t> :tabnew<cr>
:map <C-S-tab> :tabprevious<cr>
:map <C-tab> :tabnext<cr>
:map <C-left> :tabprevious<cr>
:map <C-right> :tabnext<cr>
:map <C-h> :tabprevious<cr>
:map <C-l> :tabnext<cr>
:imap <C-t> :tabnew<cr>
:imap <C-S-tab> :tabprevious<cr>
:imap <C-tab> :tabnext<cr>
:imap <C-left> :tabprevious<cr>
:imap <C-right> :tabnext<cr>
:imap <C-h> :tabprevious<cr>
:imap <C-l> :tabnext<cr>
:imap <C-t> <ESC>:tabnew<cr>

" show / hide menu
nnoremap <F11> :if &go=~#'m'<Bar>set go-=m<Bar>else<Bar>set go+=m<Bar>endif<CR>
nnoremap <F12> :if &showtabline=~0<Bar>set showtabline=2<Bar>else<Bar>set showtabline=0<Bar>endif<CR>

" insert and remove blank lines without moving cursor and entering insert mode
" Ctrl-j/k deletes blank line below/above, and Alt-j/k inserts.
nnoremap <silent><C-j> m`:silent +g/\m^\s*$/d<CR>``:noh<CR>
nnoremap <silent><C-k> m`:silent -g/\m^\s*$/d<CR>``:noh<CR>
nnoremap <silent><A-j> :set paste<CR>m`o<Esc>``:set nopaste<CR>
nnoremap <silent><A-k> :set paste<CR>m`O<Esc>``:set nopaste<CR>

" remap escape
ino fd <esc>
vno v <esc>

" Enable neocomplcache
"let g:neocomplcache_enable_at_startup=1

" Remove popup for file attribut changes
autocmd FileChangedRO * echo "File changed: Read-Only state changed."
autocmd FileChangedShell * echo "File changed: Content changed."
" End Properties ------------------------------

set diffexpr=MyDiff()
function MyDiff()
  let opt = '-a --binary '
  if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif
  if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif
  let arg1 = v:fname_in
  if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif
  let arg2 = v:fname_new
  if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif
  let arg3 = v:fname_out
  if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif
  let eq = ''
  if $VIMRUNTIME =~ ' '
    if &sh =~ '\<cmd'
      let cmd = '""' . $VIMRUNTIME . '\diff"'
      let eq = '"'
    else
      let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'
    endif
  else
    let cmd = $VIMRUNTIME . '\diff'
  endif
  silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3 . eq
endfunction

" tabs caption -------------------------------

" set up tab labels with tab number, buffer name, number of windows
function! GuiTabLabel()
  let label = ''
  let bufnrlist = tabpagebuflist(v:lnum)

  " Append the tab number
"  let label .= v:lnum.': '
  let label = v:lnum.' '

  " Append the buffer name
  let name = bufname(bufnrlist[tabpagewinnr(v:lnum) - 1])
  if name == ''
    " give a name to no-name documents
    if &buftype=='quickfix'
      let name = '[Quickfix List]'
    else
      let name = '[No Name]'
    endif
  else
    " get only the file name
    let name = fnamemodify(name,":t")
  endif
  let label .= name

  " Add '*' if one of the buffers in the tab page is modified
  for bufnr in bufnrlist
    if getbufvar(bufnr, "&modified")
      let label .= '*'
      break
    endif
  endfor

  " Append the number of windows in the tab page
"  let wincount = tabpagewinnr(v:lnum, '$')
"  return label . '  [' . wincount . ']'
  return label
endfunction

set guitablabel=%{GuiTabLabel()}

" set up tab tooltips with every buffer name
function! GuiTabToolTip()
  let tip = ''
  let bufnrlist = tabpagebuflist(v:lnum)

  for bufnr in bufnrlist
    " separate buffer entries
    if tip!=''
      let tip .= " \n "
    endif

    " Add name of buffer
    let name=bufname(bufnr)
    if name == ''
      " give a name to no name documents
      if getbufvar(bufnr,'&buftype')=='quickfix'
        let name = '[Quickfix List]'
      else
        let name = '[No Name]'
      endif
    endif
    let tip.=name

    " add modified/modifiable flags
    if getbufvar(bufnr, "&modified")
      let tip .= ' [+]'
    endif
    if getbufvar(bufnr, "&modifiable")==0
      let tip .= ' [-]'
    endif
  endfor

  return tip
endfunction

set guitabtooltip=%{GuiTabToolTip()}

" end tabs caption --------------------------

" Search for selected text ------------------
" http://vim.wikia.com/wiki/VimTip171
let s:save_cpo = &cpo | set cpo&vim
if !exists('g:VeryLiteral')
  let g:VeryLiteral = 0
endif

function! s:VSetSearch(cmd)
  let old_reg = getreg('"')
  let old_regtype = getregtype('"')
  normal! gvy
  if @@ =~? '^[0-9a-z,_]*$' || @@ =~? '^[0-9a-z ,_]*$' && g:VeryLiteral
    let @/ = @@
  else
    let pat = escape(@@, a:cmd.'\')
    if g:VeryLiteral
      let pat = substitute(pat, '\n', '\\n', 'g')
    else
      let pat = substitute(pat, '^\_s\+', '\\s\\+', '')
      let pat = substitute(pat, '\_s\+$', '\\s\\*', '')
      let pat = substitute(pat, '\_s\+', '\\_s\\+', 'g')
    endif
    let @/ = '\V'.pat
  endif
  normal! gV
  call setreg('"', old_reg, old_regtype)
endfunction

vnoremap <silent> * :<C-U>call <SID>VSetSearch('/')<CR>/<C-R>/<CR>
vnoremap <silent> # :<C-U>call <SID>VSetSearch('?')<CR>?<C-R>/<CR>
vmap <kMultiply> *

nmap <silent> <Plug>VLToggle :let g:VeryLiteral = !g:VeryLiteral
  \\| echo "VeryLiteral " . (g:VeryLiteral ? "On" : "Off")<CR>
if !hasmapto("<Plug>VLToggle")
  nmap <unique> <Leader>vl <Plug>VLToggle
endif
let &cpo = s:save_cpo | unlet s:save_cpo
" End Search for selected text ----------------

" Status line customization -------------------
set laststatus=2                    "always display status line
set noshowmode                      "do not show mode

" old
"function! StatuslineColorInsertMode()
"	set statusline=Inserting...%=ln:\ %l\ \|\ col:\ %v\ \|\ pos:\ %p%%\ of\ %L\ lines\ 
"	hi StatusLine guibg=DarkRed guifg=White gui=NONE
"endfunction
"function! StatuslineColorNormalMode()
"	set statusline=File:\ %t\ \|\ Type:\ %y\ \|\ Char:\ ascii=\%03.3b\ \|\ hexa=\%02.2B\ %=ln:\ %l\ \|\ col:\ %v\ \|\ pos:\ %p%%\ of\ %L\ lines\ 
"	hi StatusLine guibg=DarkGreen guifg=White gui=NONE
"endfunction
"" default colors
"call StatuslineColorNormalMode()
"
"" set the status line up to change the status line based on mode
"au InsertEnter * call StatuslineColorInsertMode()
"au InsertLeave * call StatuslineColorNormalMode()

" End of Status line customization -----------

"Set window size
if has("gui_running")
  " GUI is running or is about to start.
  " Maximize gvim window.
  set lines=56 columns=140
endif

:tabfirst

