import com.sun.xml.dtdparser.DTDEventListener;
import com.sun.xml.dtdparser.DTDHandlerBase;
import com.sun.xml.dtdparser.DTDParser;
import com.sun.xml.dtdparser.InputEntity;

public class Smoke
{
	public static void main(String[] args)
	{
		System.out.println(DTDEventListener.class.getCanonicalName());
		System.out.println(DTDHandlerBase.class.getCanonicalName());
		System.out.println(DTDParser.class.getCanonicalName());
		System.out.println(InputEntity.class.getCanonicalName());
	}
}
