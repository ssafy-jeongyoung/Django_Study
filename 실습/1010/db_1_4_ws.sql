SELECT
  first_name, phone, country
FROM
  users
WHERE
  country != '서울'
  AND phone LIKE '____51_______'
  OR phone LIKE '___51_______';