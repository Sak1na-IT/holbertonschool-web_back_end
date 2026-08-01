const http = require('http');
const fs = require('fs');

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      const fields = {};

      students.forEach((student) => {
        const values = student.split(',');
        const firstName = values[0];
        const field = values[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstName);
      });

      let output = `Number of students: ${students.length}`;

      Object.keys(fields).forEach((field) => {
        output += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
      });

      resolve(output);
    });
  });
}

const database = process.argv[2];

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    readDatabase(database)
      .then((data) => {
        res.statusCode = 200;
        res.end(`This is the list of our students\n${data}`);
      })
      .catch((err) => {
        res.statusCode = 200;
        res.end(`This is the list of our students\n${err.message}`);
      });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
