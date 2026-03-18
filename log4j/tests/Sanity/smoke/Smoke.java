import org.apache.logging.log4j.*;

public class Smoke
{
    public static void main(String[] args)
    {
	Logger log = LogManager.getLogger(Smoke.class);
	log.error("Hello from Log4J");
	System.out.println("SMOKE TEST COMPLETE");
    }
}
