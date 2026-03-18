%%
%public
%class SimpleLexer
%unicode
%function lexx
%type Integer

%%

[0-9]+  { System.out.print("<" + yytext() + ">"); }
.|\n    { /* ignore others */ }
