public class Main
{
    public static void
    main(String[] args)
        throws Exception
    {
        SimpleLexer lexer = new SimpleLexer(
            new java.io.StringReader(args[0]));
        lexer.lexx();
    }
}
