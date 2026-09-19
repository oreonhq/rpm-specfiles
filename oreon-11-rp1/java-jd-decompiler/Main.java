import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.IOException;

import org.jd.core.v1.api.loader.Loader;
import org.jd.core.v1.api.loader.LoaderException;
import org.jd.core.v1.api.printer.Printer;
import org.jd.core.v1.ClassFileToJavaSourceDecompiler;

/**
Fully based on: https://github.com/java-decompiler/jd-core/blob/master/README.md
**/
public class Main {
    public static void main(String[] args) throws Exception {
        Loader loader = new Loader() {
        @Override
        public byte[] load(String internalName) throws LoaderException {
            InputStream is = this.getClass().getResourceAsStream("/" + internalName + ".class");
                if (is == null) {
                    return null;
                } else {
                    try (InputStream in=is; ByteArrayOutputStream out=new ByteArrayOutputStream()) {
                        byte[] buffer = new byte[1024];
                        int read = in.read(buffer);

                        while (read > 0) {
                out.write(buffer, 0, read);
                read = in.read(buffer);
                }
                        return out.toByteArray();
                    } catch (IOException e) {
                        throw new LoaderException(e);
                    }
                  }
            }
            @Override
            public boolean canLoad(String internalName) {
              return this.getClass().getResource("/" + internalName + ".class") != null;
            }
            };
    if (args.length == 0) {
        System.err.println("Usage:\n"+
        		   "1) Class in a jar file:\n"+
        		   "CLASSPATH=\"dirs:jars:with:contnet\" /usr/bin/java-jd-decompiler class/file/to/decompile\n"+
        		   "2) Class not in jar file\n"+
        		   "/usr/bin/java-jd-decompiler class/file/to/decompile\n");
        System.exit(1);
    } else {
        int r=0;
        int i=0;
        if (args.length != 1) {
          System.err.println("Warning, more then one class on input! Expect mess!");
        }
        for (String clazz: args) {
        i++;
        Printer printer = new Printer() {
        protected static final String TAB = "  ";
        protected static final String NEWLINE = "\n";

        protected int indentationCount = 0;
        protected StringBuilder sb = new StringBuilder();

        @Override public String toString() { return sb.toString(); }

        @Override public void start(int maxLineNumber, int majorVersion, int minorVersion) {}
        @Override public void end() {}

        @Override public void printText(String text) { sb.append(text); }
        @Override public void printNumericConstant(String constant) { sb.append(constant); }
        @Override public void printStringConstant(String constant, String ownerInternalName) { sb.append(constant); }
        @Override public void printKeyword(String keyword) { sb.append(keyword); }
        @Override public void printDeclaration(int type, String internalTypeName, String name, String descriptor) { sb.append(name); }
        @Override public void printReference(int type, String internalTypeName, String name, String descriptor, String ownerInternalName) { sb.append(name); }

        @Override public void indent() { this.indentationCount++; }
        @Override public void unindent() { this.indentationCount--; }

        @Override public void startLine(int lineNumber) { for (int i=0; i<indentationCount; i++) sb.append(TAB); }
        @Override public void endLine() { sb.append(NEWLINE); }
        @Override public void extraLine(int count) { while (count-- > 0) sb.append(NEWLINE); }

        @Override public void startMarker(int type) {}
        @Override public void endMarker(int type) {}
    };
        if (args.length != 1) {
          System.out.println("********************************************");
          System.out.println(i+") "+clazz+":");
          System.out.println("********************************************");
        }
        ClassFileToJavaSourceDecompiler decompiler = new ClassFileToJavaSourceDecompiler();
        try{
            decompiler.decompile(loader, printer, clazz);
        }catch (Exception ex){
            r=2;
            System.err.println("Error: "+clazz+" not found or other issue. Wrong classpath?");
            ex.printStackTrace();
            System.err.println("Have you set CLASSPATH variable?");
        }
      String source = printer.toString();
      System.out.println(source);
      }
    System.exit(r);
    }
  }
}
