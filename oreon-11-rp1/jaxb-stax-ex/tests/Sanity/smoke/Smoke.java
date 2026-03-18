import org.jvnet.staxex.Base64Data;
import org.jvnet.staxex.NamespaceContextEx;
import org.jvnet.staxex.XMLStreamReaderEx;
import org.jvnet.staxex.XMLStreamWriterEx;

public class Smoke
{
	public static void main(String[] args)
	{
		System.out.println(Base64Data.class.getCanonicalName());
		System.out.println(NamespaceContextEx.class.getCanonicalName());
		System.out.println(XMLStreamReaderEx.class.getCanonicalName());
		System.out.println(XMLStreamWriterEx.class.getCanonicalName());
	}
}
