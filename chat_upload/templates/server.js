const express = require('express');
const app = express();
const multer = require('multer');

const upload = multer({ dest: 'uploads/' });

app.post('/home/upload/', upload.single('file'), (req, res) => {
  const file = req.file;
  const fromDate = req.body.fromDate;
  const toDate = req.body.toDate;

  console.log(`File uploaded: ${file.originalname}`);
  console.log(`From Date: ${fromDate}`);
  console.log(`To Date: ${toDate}`);

  // You can further process the uploaded file and date range here

  res.send('File uploaded successfully!');
});

app.listen(8000, () => {
  console.log('Server listening on port 8000');
});
