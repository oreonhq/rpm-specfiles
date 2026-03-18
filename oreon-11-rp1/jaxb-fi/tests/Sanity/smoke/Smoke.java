import com.sun.xml.fastinfoset.EncodingConstants;
import com.sun.xml.fastinfoset.stax.StAXDocumentParser;
import com.sun.xml.fastinfoset.stax.StAXDocumentSerializer;
import org.jvnet.fastinfoset.EncodingAlgorithmIndexes;
import org.jvnet.fastinfoset.VocabularyApplicationData;

public class Smoke
{
	public static void main(String[] args)
	{
		System.out.println(EncodingConstants.class.getCanonicalName());
		System.out.println(StAXDocumentParser.class.getCanonicalName());
		System.out.println(StAXDocumentSerializer.class.getCanonicalName());
		System.out.println(EncodingAlgorithmIndexes.class.getCanonicalName());
		System.out.println(VocabularyApplicationData.class.getCanonicalName());
	}
}
