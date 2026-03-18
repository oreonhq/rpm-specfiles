import com.lmax.disruptor.dsl.Disruptor;
import com.lmax.disruptor.EventFactory;
import com.lmax.disruptor.RingBuffer;
import com.lmax.disruptor.util.DaemonThreadFactory;
import java.nio.ByteBuffer;

class LongEvent
{
    private long value;

    public void set(long value)
    {
        this.value = value;
    }
}

class LongEventFactory implements EventFactory<LongEvent>
{
    public LongEvent newInstance()
    {
        return new LongEvent();
    }
}

public class Smoke
{
    public static void main(String[] args) throws Exception
    {
	System.out.println("SMOKE TEST START");

        int bufferSize = 1024; 

        Disruptor<LongEvent> disruptor = 
                new Disruptor<>(LongEvent::new, bufferSize, DaemonThreadFactory.INSTANCE);

        disruptor.handleEventsWith((event, sequence, endOfBatch) ->
                System.out.println("Event: " + event));
        disruptor.start();

        RingBuffer<LongEvent> ringBuffer = disruptor.getRingBuffer();
        ByteBuffer bb = ByteBuffer.allocate(8);
        for (long l = 0; l < 10; l++)
        {
            bb.putLong(0, l);
            ringBuffer.publishEvent((event, sequence, buffer) -> event.set(buffer.getLong(0)), bb);
            Thread.sleep(100);
        }

	System.out.println("SMOKE TEST COMPLETE");
    }
}
