# Markdown
하나의 확장자로, 구조를 나타내기 위한 언어
- 텍스트기반의 가벼운 마크업* *(Mark up)* 언어
- 문서의 구조와 내용을 쉽고 빠르게 적고자 탄생

  *마크업 = 태그를 이용하여 문서의 구조를 나타내는 것


## 텍스트 변경
---
### 1. 헤딩 : 글자 크기조절X, 제목 용도. 갯수 : 1~6개   

`예시 input`

```
# 헤딩1
## 헤딩2
### 헤딩3
#### 헤딩4
##### 헤딩5
###### 헤딩6  
```
`output`
# 헤딩1
## 헤딩2
### 헤딩3
#### 헤딩4
##### 헤딩5
###### 헤딩6  
---

### 2. 순서있는 리스트 : 번호매김이 있는 리스트
`예시 input`
```
1. 순서
2. 있는
3. 리스트
```
`output`
1. 순서
2. 있는
3. 리스트
---

### 3. 순서없는 리스트 : 번호매김이 없는 리스트
`예시 input`
```
- 갑
- 을
- 병
```
`output`
- 갑
- 을
- 병
---
### 4. 텍스트 강조 : 텍스트 스타일을 변경
4-1. 기울임  
`예시 input`
```
*text*
```    
`output`  
*text*   


4-2. 굵게  
`예시 input`
```
**text**
```    
`output`
**text**
  
4-3. 취소선  
`예시 input`
```
~~text~~
```    
`output`  
~~text~~

---
### 5. 코드의 표현 : 코딩 구문을 그대로 보여주기 위함
5-1. code block  
`예시 input`
```
(```) <-소괄호 없이 사용
print("Hello World!!!")
(```) <-소괄호 없이 사용
```
`output`
```
print("Hello World!!!")
```
5-2. 어떤 언어인지 표현  
`예시 input`
```
(```)python <-소괄호 없이 사용
print("어떤 언어인지 표현가능")
(```) <-소괄호 없이 사용
```
`output`
```python
print("어떤 언어인지 표현가능")
```

---
### 6. 링크전달 : 대괄호[]랑 소괄호()를 이용하여 링크 전달
`예시 input`
```
[답안지](https://github.com/ychoi-kr/wikidocs-chobo-python/blob/master/ch03/ridereader.py)
[진홍표](https://www.notion.so/hg-edu/c4cedd7e04b94469baadaecfc6ffbb5f)
```
`output`   
[답안지](https://github.com/ychoi-kr/wikidocs-chobo-python/blob/master/ch03/ridereader.py)  
[진홍표](https://www.notion.so/hg-edu/c4cedd7e04b94469baadaecfc6ffbb5f)

---
### 7. 이미지전달 :  느낌표! 및 대괄호[], 소괄호()를 이용하여 이미지 전달
너비와 높이는 수정 불가.

※ ![이미지 설명]`(이미지 경로)`  에서  
-이미지 경로 :  
case1하위폴더일 경우 `하위폴더/파일이름.확장자`  
상위폴더일 경우 `..파일이름.확장자`  
`예시 input`
```
![스노우보딩](images/im4/im4.jpg)  
![tEst](https://media.istockphoto.com/id/1357110609/ko/%EC%82%AC%EC%A7%84/%EA%B2%A8%EC%9A%B8-%EC%8A%A4%ED%8F%AC%EC%B8%A0-%EC%8B%9C%EC%A6%8C-%ED%9D%A5%EB%AF%B8-%EC%A7%84%EC%A7%84%ED%95%9C-%EC%8A%A4%EB%85%B8%EC%9A%B0-%EB%B3%B4%EB%93%9C.jpg?b=1&s=170667a&w=0&k=20&c=WntQ3rWVNHNKNOjHToNwiehlQMTp6U5gAGsdI86FShk=)
```
`output`
![스노우보딩](images/im4/im4.jpg)  
![tEst](https://media.istockphoto.com/id/1357110609/ko/%EC%82%AC%EC%A7%84/%EA%B2%A8%EC%9A%B8-%EC%8A%A4%ED%8F%AC%EC%B8%A0-%EC%8B%9C%EC%A6%8C-%ED%9D%A5%EB%AF%B8-%EC%A7%84%EC%A7%84%ED%95%9C-%EC%8A%A4%EB%85%B8%EC%9A%B0-%EB%B3%B4%EB%93%9C.jpg?b=1&s=170667a&w=0&k=20&c=WntQ3rWVNHNKNOjHToNwiehlQMTp6U5gAGsdI86FShk=)

### 특수기호 부르는 법 : 
- "-" : 하이픈 (대시)
- "/" : slash
- "\" : back slash
- "*" : asterisk (별, star)
- "`" : backtick 