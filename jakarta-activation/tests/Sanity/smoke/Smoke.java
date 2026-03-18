import jakarta.activation.DataHandler;
import jakarta.activation.DataSource;
import jakarta.activation.MimeType;
import jakarta.activation.MimeTypeParseException;

public class Smoke
{
	public static void main(String[] args)
	{
		System.out.println(DataHandler.class.getCanonicalName());
		System.out.println(DataSource.class.getCanonicalName());
		System.out.println(MimeType.class.getCanonicalName());
		System.out.println(MimeTypeParseException.class.getCanonicalName());
	}
}
