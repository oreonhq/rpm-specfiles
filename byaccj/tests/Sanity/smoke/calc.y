%{
%}

%token NUM
%left '+' '-'
%left '*' '/'

%%

exp : NUM { $$.ival = $1.ival; }
    | exp '+' exp { $$.ival = $1.ival + $3.ival; }
    | exp '-' exp { $$.ival = $1.ival - $3.ival; }
    | exp '*' exp { $$.ival = $1.ival * $3.ival; }
    | exp '/' exp { $$.ival = $1.ival / $3.ival; }
    | '(' exp ')' { $$.ival = $2.ival; }
    ;

%%

private String buf;

private void yyerror(String s) {
  throw new RuntimeException("Parse error: " + s);
}

private int yylex() {
  if (buf.isEmpty()) {
    return 0;
  }
  int ch = buf.charAt(0);
  buf = buf.substring(1);
  if (ch >= '0' && ch <= '9') {
    yylval.ival = ch - '0';
    while (!buf.isEmpty() && buf.charAt(0) >= '0' && buf.charAt(0) <= '9') {
      yylval.ival = yylval.ival * 10 + buf.charAt(0) - '0';
      buf = buf.substring(1);
    }
    return NUM;
  }
  return ch;
}

private int parse(String expr) {
  buf = expr;
  yyparse();
  return val_pop().ival;
}

public static void main(String args[])
{
  Parser par = new Parser(true);
  int res = par.parse(args[0]);
  System.out.println("RESULT is: " + res);
}
