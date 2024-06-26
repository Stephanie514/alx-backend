import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

// The Redis client setup
const client = redis.createClient();
const reserveSeatAsync = promisify(client.set).bind(client);
const getCurrentAvailableSeatsAsync = promisify(client.get).bind(client);

// Initializing seats to 50
reserveSeatAsync('available_seats', 50);

let reservationEnabled = true;

const queue = kue.createQueue();

queue.process('reserve_seat', async (job, done) => {
  try {
    const currentSeats = await getCurrentAvailableSeatsAsync();
    if (parseInt(currentSeats) <= 0) {
      throw new Error('Not enough seats available');
    }

    await reserveSeatAsync('available_seats', parseInt(currentSeats) - 1);
    if (parseInt(currentSeats) - 1 === 0) {
      reservationEnabled = false;
    }

    console.log(`Seat reservation job ${job.id} completed`);
    done();
  } catch (error) {
    console.error(`Seat reservation job ${job.id} failed: ${error.message}`);
    done(error);
  }
});

// server setup
const app = express();
const PORT = 1245;

app.get('/available_seats', async (req, res) => {
  try {
    const numberOfAvailableSeats = await getCurrentAvailableSeatsAsync();
    res.json({ numberOfAvailableSeats: parseInt(numberOfAvailableSeats) });
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  try {
    const currentSeats = await getCurrentAvailableSeatsAsync();
    if (parseInt(currentSeats) > 0) {
      queue.inactiveCount((err, total) => {
        if (total > 0) {
          queue.process('reserve_seat');
        }
      });
    }
  } catch (error) {
    console.error(`Queue processing error: ${error.message}`);
  }
});

// Starting server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
