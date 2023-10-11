-- id, title, content 만들기
CREATE TABLE article(
  id INTEGER PRIMARY KEY AUTOINCREMENT, -- NOT NULL + UNIQUE = PRIMARY KEY
  -- AUTOINCREMENT : 자동으로 1씩 증가하면서 넣어줌
  title TEXT NOT NULL,
  content TEXT NOT NULL
);

-- 삭제 : DROP
DROP TABLE article;

-- data를 넣는 방법 : INSERT
INSERT INTO article (id, title, content)
    VALUES (2, 'Hi', 'BAAMMMMM');