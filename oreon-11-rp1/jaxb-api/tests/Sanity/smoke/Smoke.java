import jakarta.xml.bind.JAXB;
import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBElement;
import jakarta.xml.bind.Marshaller;
import jakarta.xml.bind.Unmarshaller;

public class Smoke
{
	public static void main(String[] args)
	{
		System.out.println(JAXB.class.getCanonicalName());
		System.out.println(JAXBContext.class.getCanonicalName());
		System.out.println(JAXBElement.class.getCanonicalName());
		System.out.println(Marshaller.class.getCanonicalName());
		System.out.println(Unmarshaller.class.getCanonicalName());
	}
}
