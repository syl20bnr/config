set background=light
hi clear
if exists("syntax_on")
  syntax reset
endif
let g:colors_name = "bartevil"
"comment

hi Comment guifg=#c00000
hi Constant guifg=#000080
hi Cursor guifg=white guibg=black
hi CursorColumn guibg=gray78
hi CursorIM gui=None
hi CursorLine guibg=gray70
hi DiffAdd guibg=lightblue
hi DiffChange guibg=plum1
hi DiffDelete gui=bold guifg=blue guibg=lightcyan
hi DiffText gui=bold guibg=red
hi Directory guifg=blue
hi Error guifg=white guibg=red
hi ErrorMsg guifg=white guibg=red
hi FoldColumn guifg=darkblue
hi Folded guifg=#808080 guibg=grey gui=underline
hi Function guifg=#008000
hi Identifier guifg=#008000 gui=bold
hi Ignore guifg=gray90
hi IncSearch guifg=#ff9900 guibg=#e0ffff
hi LineNr guifg=black guibg=#bbbbbb
hi MatchParen guifg=black guibg=yellow
hi ModeMsg gui=bold
hi MoreMsg gui=bold guifg=seagreen
hi NonText guifg=gray68 guibg=#bbbbbb
hi Normal guifg=black guibg=gray79
hi Pmenu guibg=#000000 guifg=#ffffff
hi PmenuSbar guibg=#000000 guifg=#ffffff
hi PmenuSel gui=bold guibg=#ff0000 guifg=#ffffff
hi PmenuThumb gui=bold guibg=#ffffff guifg=#ffffff
hi PreProc gui=bold guifg=#0000c0
hi Question gui=bold guifg=seagreen
hi Search guibg=yellow
hi SignColumn guifg=darkblue guibg=grey
hi Special guifg=slateblue
hi SpecialKey guifg=gray68
hi SpellBad gui=undercurl
hi SpellCap gui=undercurl
hi SpellLocal gui=undercurl
hi SpellRare gui=undercurl
hi Keyword gui=bold guifg=#000000
hi Statement gui=bold guifg=#000000
hi StatusLine gui=bold,reverse
hi StatusLineNC gui=reverse
hi TabLine gui=underline guibg=lightgrey
hi TabLineFill gui=reverse
hi TabLineSel gui=bold
hi Title gui=bold guifg=magenta
hi Todo gui=reverse guifg=#008000
hi Type gui=bold guifg=saddlebrown
hi Underlined gui=underline guifg=slateblue
hi VertSplit gui=reverse
hi Visual guibg=#eeeeee
hi VisualNOS gui=bold,underline
hi WarningMsg guifg=red
hi WildMenu guifg=black guibg=yellow
hi link Boolean Constant
hi link Character Constant
hi link Conditional Statement
hi link Debug Special
hi link Define PreProc
hi link Delimiter Special
hi link Exception Statement
hi link Float Constant
hi link Function Identifier
hi link Include PreProc
hi link Label Statement
hi link Macro PreProc
hi link Number Constant
hi link Operator Statement
hi link PreCondit PreProc
hi link Repeat Statement
hi link SpecialChar Special
hi link SpecialComment Special
hi link StorageClass Type
hi link String Constant
hi link Structure Type
hi link Tag Special
hi link Typedef Type
hi link vimVar Identifier
hi link vimFunc Function
hi link vimUserFunc Function
hi link helpSpecial Special
hi link vimSet Normal
hi link vimSetEqual Normal

