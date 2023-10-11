SELECT
  *
FROM
  users
ORDER BY age
LIMIT 20 OFFSET 40;

CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);


-- zoo에서 weight가 100 미만인 요소를 모두 삭제
-- 하지만 ROLLBACK으로 다시 복구
-- 다시 zoo에서 eat가 omnivore인 것만 삭제
-- COMMIT으로 저장
-- 카운트 해보면 3이 출력됨
BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;