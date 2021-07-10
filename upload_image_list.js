const AWS = require("aws-sdk");
const multipart = require("parse-multipart");
const s3 = new AWS.S3();
const bluebird = require("bluebird");

exports.handler = function (event, context) {
  const result = [];

  const bodyBuffer = Buffer.from(event["body-json"].toString(), "base64");
  const boundary = multipart.getBoundary(event.params.header["content-type"]);
  const parts = multipart.Parse(bodyBuffer, boundary);
  const files = getFiles(parts);

  return bluebird
    .map(files, (file) => {
      console.log(`Upload Call`);
      return upload(file).then(
        (data) => {
          result.push(file.uploadFile.full_path);
          console.log(`data=> ${JSON.stringify(data, null, 2)}`);
        },
        (err) => {
          console.log(`s3 upload err => ${err}`);
        }
      );
    })
    .then((_) => {
      return context.succeed(
        { success: true, data: result }
      );
    });
};

const upload = function (file) {
  console.log(`putObject Call`);
  return s3.upload(file.params).promise();
};

const getFiles = function (parts) {
  const files = [];
  parts.forEach((part) => {

    const buffer = part.data
    const fileFullName = part.filename + "-" + Date.now();

    const filefullPath = "https://ayo-springboot-build.s3.ap-northeast-2.amazonaws.com/" + fileFullName;

    const params = {
      Bucket: "ayo-springboot-build",
      Key: fileFullName,
      Body: buffer,
    };

    const uploadFile = {
      size: buffer.toString("ascii").length,
      type: part.type,
      name: fileFullName,
      full_path: filefullPath,
    };

    files.push({ params, uploadFile });
  });
  return files;
};