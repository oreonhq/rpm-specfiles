import jakarta.xml.bind.annotation.XmlRootElement;

import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBException;
import jakarta.xml.bind.Marshaller;
import jakarta.xml.bind.Unmarshaller;

import java.io.InputStream;
import java.io.ByteArrayOutputStream;
import java.io.ByteArrayInputStream;

@XmlRootElement(namespace = "org.fedoraproject.jaxb.test.smoke")
class Data
{
	public String text = "default text";
	public int number = 123;
}

public class Smoke
{
	public static void main(String[] args) throws Exception
	{
		JAXBContext context = JAXBContext.newInstance(Data.class);
		Marshaller m = context.createMarshaller();
		m.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, Boolean.TRUE);
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		m.marshal(new Data(), baos);

		Unmarshaller um = context.createUnmarshaller();

		Data data;
		try (InputStream is = new ByteArrayInputStream(baos.toByteArray())) {
			data = Data.class.cast(um.unmarshal(is));
		}
		
		if (!data.text.equals("default text"))
		{
			throw new RuntimeException("Expected \"default text\", found \"" + data.text + "\"");
		}
		if (data.number != 123)
		{
			throw new RuntimeException("Expected 123, found " + String.valueOf(data.number));
		}
	}
}
