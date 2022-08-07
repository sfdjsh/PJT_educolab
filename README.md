# 목차

## [Front 진행 상황](#front-진행-상황)

[a. 과제](#a.-과제)

[b. 팝업](#b.-팝업)

[c. 회원가입](#c.-회원가입)

[d. 로그인&로그아웃](#d.-로그인-&-로그아웃)

[e. 페이지 접근 제한](#e.-페이지-접근-제한)

[f. 리프레시 토큰 발급](f.-리프레시-토큰-발급)

[g. 공통](g.-공통)



---





## Front 진행 상황

#### a. 과제

```
* 문제 : 새로고침 시 사용자 정보가 없어지기 때문에 백에서 데이터를 불러와야 함
* 문제 : 학생과 교사 연결이 제대로 되어있지 않음 - 회원 가입 시 특정 학교, 특정 학년, 특정 반에 대해서 계정을 만들어놓아야 할 것 같음

과제 목록
- 전체적인 틀은 잡아놓음
- pagination과 데이터 연결 필요
- 현재 데이터가 교사 페이지의 제출기한이 지나지 않은 과제뿐이므로 다른 데이터도 시도해볼 필요 있음
- 전체적으로 틀은 비슷하므로 큰 오류가 없을 것으로 예상됨

과제 생성/수정
- 교사 쪽에서 과제 생성하는 것은 기능 구현 완료 (첨부파일이 잘 저장되었는지 확인 필요)
- 학생 아이디로 시도해봐야 함
- 상세 페이지가 아직 구현되지 않았고 새로고침 시 사용자 정보를 불러올 수 없기 때문에 그 기능이 완료된 후에나 할 수 있을 것 같음
- 수정 시 데이터를 불러오는 것은 과제 상세 페이지에 들어갔을 때와 같은 url로 보낼 예정
(상세 url 데이터에 학년 반 추가해 보내달라고 요청)

과제 상세
- 전체적인 틀은 잡아놓음
- 교사 페이지에서는 아코디언으로 학생 정보가 보임 (현재 학생 정보가 없어서 볼 수 없음)
- 학생 페이지에서는 과제 제출 입력창과 파일 선택이 보임
- 첨부파일 부분 확인 완료
- 삭제 아직 미완료

과제 검색
- url 설정 완료
- 새로고침 시 과제 목록 페이지에 들어갔을 때와 같은 url로 요청 보냄
- 전체 과제 중에서 어떤 부분을 검색할 것인지, 검색한 단어를 포함하면 검색 결과에 노출시키는 것을 구현해야 함
```



### b. 팝업

```
한 번 팝업이 뜨고 다음에는 뜨지 않는 오류 수정해야 함
confirm과 alert v-if로 나누기
```



### c. 회원 가입

```
인증번호가 확인되었습니다 팝업이 뜨지 않는 오류 수정
회원가입 후 새로고침 구현
```



### d. 로그인 & 로그아웃

```
로그인, 로그아웃 후 새로고침 구현
```



### e. 페이지 접근 제한

```
로그인 여부, 사용자 유형에 따라 들어갈 수 있는 페이지 접근 제한
```



### f. 리프레시 토큰 발급

```
페이지가 새로고침될 때마다, 토큰 유효기간이 다가올 때마다 토큰 발급 구현 필요
```



### g. 공통

```
로딩이 길어질 경우에 로딩중임을 표시
```

