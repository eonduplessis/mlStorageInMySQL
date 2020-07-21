# mlStorageInMySQL

Requires a valid MySQL DB server.
++
docker run -p 3306:3306 --name memories -e MYSQL_ROOT_PASSWORD=password -d mysql:5.6



DB scripts:
++
CREATE DATABASE mlmodels;

USE mlmodels;

CREATE TABLE models
(
    id INT unsigned NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    model_data LONGBLOB NULL,
    PRIMARY KEY (id)
);

INSERT INTO models (name, model_data) VALUES ('test_model', 'test_data');

COMMIT;
