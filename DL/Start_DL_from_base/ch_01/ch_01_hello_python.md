1권부터 3권까지 한번 읽었었으나 다시한번 정리하는 차원에서 정독 하고자 한다.

---

이 책은 동작하는 딥러닝을 직접 구현하며 깊히 이해할수 있도록 구성 되어있다.


---
# 1.1  파이썬이란?

- 파이썬은 간단하고 배우기 쉬운 프로그래밍 언어.
- 오픈소스라 무료로 자유롭게 이용이 가능.
- 넘파이나 사이파이 같은 수치 계산과 통계 처리를 다루는 탁월한 라이브러리가 존재.
- 카페, 텐서플로, 체이너, 테이노 등의 프레임 워크도 존재.
* 프레임워크랑 라이브러리의 차이점
    * 프레임 워크는 뼈대나 기반 구조를 뜻하고 제어의 역전 개념이 적용된 대표적인 기술.
    * 소프트웨어의 특정 문제를 해결하기 위해서 상호 협력하는 클래스와 인터페이스의 집합이라 할수 있으며 완성된 어플리케이션이 아닌 프로그래머가 완성시키는 작업을 해야한다.
    * 라이브러리는 단순 활용 가능한 도구들의 집합이다.

    * 라이브러리랑 프레임 워크의 차이는 제어 흐름에 대한 주도성이 누구에게 있는가에 있다.


# 1.2 파이썬 설치하기

- 파이썬은 2.x 버젼과 3.x 버젼이 있다 여기선 3버젼 을 사용한다.
- 사용하는 라이브러리는 최소화 한다. 넘파이와, matplotlib만 사용을 할것이다.
- 넘파이는 연산을 matplotlib는 그림을 담당한다.
- 아나콘다 배포판도 3버젼을 사용한다.

# 1.3 파이썬 인터 프리터
- 아나콘다에서 진행한다 코드는 ipynb에서 확인!

# 1.4 파이썬 스크립트 파일

- 인터프리터 방식은 파이썬 코드를 대화식으로 실행해보며 간단한 실험을 수행하기 좋았다.
- 하지만 긴 작업을 수행해야 한다면 매번 코드를 입력하는 방식은 불편하니 하나의 파일로 만들어서 해보자
- 하지만 ipynb는 인터프리터 방식을 이용한 스크립트를 저장하는 것이므로 편하다!!!!!

# 1.4.2 클래스

- 지금까지 int와 str 등의 자료형을 살펴봤다.
- 이번 절에서는 새로운 클래스를 정의해본다.
- 개발자가 직접 클래스를 정의하면 독자적인 자료형을 만들수 있다.
- 클래스에는 그 클래스만의 전용 함수(메서드)와 속성을 정의할 수도 있다.

- 클래스 정의에는 __init__ 라는 메서드가 있다.
- 클래스를 초기화하는 방법을 정의한 메서드이다.
- 이 초기화용 메서드를 생성자 라고도하며 클래스의 인스턴스가 만들어질때 한번만 불립니다.

- 메서드의 첫번째인수로 자신을나타내는 self를 명시적으로 사용하는것이 특징이다.
- 인스턴스 변수는 인스턴스별로 저장하는 변수이다 self.name

# 1.5 넘파이

- 딥러닝을 구현하다 보면 배열이나 행렬 계산이 많이 등장한다
- 넘파이의 배열 클래스인 numpy array 에는 편리한 메서드가 많이 존재 한다.

# 1.5.2 넘파이 배열 생성하기
- 코드는  ipynb에 있다.


# 1.5.3 넘파이의 산술 연산
- 코드는 ipynb에 있다.

# 1.5.4 넘파이의 N차원 배열
- 코드는 ipynb에 있다.

# 1.5.5 브로드 캐스트
- 넘파이에서는 형상이 다른 배열끼리도 계산이 가능하다.
- 코드에서는 2x2 행렬A에 스칼라값 10을 곱했다 그림 1-1과 같이 10 이라는 스칼라 값이 2x2행렬로 확대된 후 연산이 이루어 진다.

![pic1-1](./deep-learning-from-scratch-master/deep-learning-from-scratch-master/ch01/images/fig%201-1.png)

- 이 기능을 브로드캐스트 라고 한다!
- 다음 그림1-2 처럼 B가 자동으로 크기를 맞춰 브로드캐스트 한다.

![pic1-2](./deep-learning-from-scratch-master/deep-learning-from-scratch-master/ch01/images/fig%201-2.png)

# 1.5.6 원소접근
- 코드는 ipynb에 있다.

# 1.6 matplotlib
- matplotlib는 그래프를 그려주는 라이브러리 이다.
- 코드는 ipynb에 있다.

# 1.6.2 pyplot 의 기능
- 코드는 ipynb에 있다.

# 1.6.3 이미지 표시하기
- 이미지를 표시하는 기능도 있다.!
