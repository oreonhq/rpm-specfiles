import com.sun.istack.ByteArrayDataSource;
import com.sun.istack.FinalArrayList;
import com.sun.istack.NotNull;
import com.sun.istack.Nullable;
import com.sun.istack.Pool;
import com.sun.istack.SAXException2;
import com.sun.istack.SAXParseException2;
import com.sun.istack.XMLStreamReaderToContentHandler;

import com.sun.istack.tools.DefaultAuthenticator;
import com.sun.istack.tools.MaskingClassLoader;
import com.sun.istack.tools.ProtectedTask;

public class Smoke
{
	public static void main(String[] args)
	{
		System.out.println(ByteArrayDataSource.class.getCanonicalName());
		System.out.println(FinalArrayList.class.getCanonicalName());
		System.out.println(NotNull.class.getCanonicalName());
		System.out.println(Nullable.class.getCanonicalName());
		System.out.println(Pool.class.getCanonicalName());
		System.out.println(SAXException2.class.getCanonicalName());
		System.out.println(SAXParseException2.class.getCanonicalName());
		System.out.println(XMLStreamReaderToContentHandler.class.getCanonicalName());

		System.out.println(DefaultAuthenticator.class.getCanonicalName());
		System.out.println(MaskingClassLoader.class.getCanonicalName());
		System.out.println(ProtectedTask.class.getCanonicalName());
	}
}
