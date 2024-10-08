# 1. 신경망 복습
- 이 책은 밑시딥의 속편으로 딥러닝의 가능성을 한층 더 깊게 탐험할 것이다.
- 이번 장에서는 신경망을 복습할 것이다.
- 효율을 높히고자 전편에서의 구현 규칙을 일부 변경하겠다

## 1.1 수학과 파이썬 복습

- 수학적 지식으로는 벡터 나 행렬 등을 알아야한다.
- 신경망을 원활하게 구현하기  위한 파이썬 코드 특히 넘파이를 사용한 코드도 리뷰한다.


### 1.1.1 벡터와 행렬

- 신경망에서는 벡터와 행렬 또는 텐서가 도처에서 등장한다.
- 벡터는 크기와 방향을 가진 양이다.
- 벡터는 숫자가 일렬로 늘어선 집합으로 표현할 수 있고 파이썬에서는 1차원 배열로 취급이 가능하다.
- 행렬은 숫자가 2차원 형태로 늘어선 것이다.

![그림 1-1](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-1.png)
- 이것은 행렬이다.

![그림 1-2](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-2.png)
- 이건 벡터다.

- 수학과 딥러닝등 많은 분야에서 열벡터 방식을 선호하지만 여기서 구현 편의를 위해 행벡터로 다루겟다.

- 수식에서의 벡터나 행렬은 X와 W 처럼 굵게 표기하여 단일 원소로 이루어진 스칼라 값과 구별한다.

- 코드에서 보듯이 벡터와 행렬은 np.array() 메서드로 생성할수 있다. 

- 이 메서드는 넘파이의 다차원 배열 클래스인 np.ndarray 클래스를 생성한다.

- np.ndarray 클래스에는 다양한 편의 메서드와 인스턴스 변수가 준비되어 있다.

- 위 코드에서는 shape 와 ndim을 이용했다.

### 1.1.2 행렬의 원소별 연산

- 이번에는 표현한 벡터와 행렬을 사용해 간단한 계산을 할것이다.


### 1.1.3 브로드 캐스트

- 넘파이의 다차원 배열에서는 형상이 다른 배열 끼리도 연산이 가능하다.

- 10이 앞의 크기에 맞춰 증식 하는것이 브로드 캐스트 이다.

![그림 1-3](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-3.png)


- 브로드 캐스트의 또 다른 예는 다음과 같다.

![그림 1-4](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-4.png)


### 1.1.4 벡터의 내적과 행렬의 곱

- 벡터의 내 수식은 다음과 같다.

![식 1-1](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/e%201-1.png)

- 여기서 2개의 벡터 x와 y가 있다고 가정한다. 그리고 식 1.1에서 보듯 벡터의 내적은 두 벡터에서 대응하는 원소들의 곱을 모두 더한것이다.

- 행렬의 곱은 다음과 같다.

![그림 1-5](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-5.png)

- 벡터의 내적과 행렬의 곱을 파이썬으로 구현하면 다음과 같은 코드가 나온다.
- 넘파이의 np.dot() 과 np.matmul() 메서드를 이용하면 쉽게 구현이 된다.

- 넘파이를 익히는데는 실제로 코딩해보면서 연습하는게 가장 좋다. 넘파이 경험을 쌓고싶은 사람은 100 numpy excercises 사이트를 추천한다.

### 1.1.5 행렬 형상 확인

- 행렬이나 벡터를 사용해 계산할 때는 그 형상에 주의해야한다.

- 그림 1-6 과 같이 형상확인이 중요하다

![그림 1-6](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-6.png)

## 1.2 신경망의 추론

- 신경망을 복습할 차례이다.
- 신경망에서 수행하는 작업은 학습과 추론이다. 이번절에서는 신경망 추론에 집중하고 학습은 다음 절에서 다룬다.

### 1.2.1 신경망 추론 전체 그림

- 신경망은 간단히 말하면 단순한 함수 라 할수 있다.
- 함수는 무엇인가를 입력하면 무엇인가를 출력하는 변환기 이다.
- 신경망도 함수처럼 입력을 출력으로 변환한다.

- 이번 절에서는 2차원 데이터를 입력하여 3차원 데이터를 출력하는 함수를 예로 들겠다
- 이 함수를 신경망으로 구현하려면 입력층에는 뉴런 2개를 출력층에는 3개를 각각 준비한다.

- 그리고 은닉층에 적당한 수의 뉴런을 배치한다.
- 그러면 그림 1-7과 같이 그림을 그릴수 있다.

![그림 1-7](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-7.png)

- 화살표에는 가중치와 뉴런의 값을 곱한다음 바이아스를 더해서 활성화 함수를 적용한 값이 다음 뉴런의 입력이 된다.
- 인접하는 층의 모든 뉴런과 연결 되어 있다는 뜻에서 완전 연결 계층 이라고 한다.
- 이건 2층 신경망이다.

![식 1-2](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/e%201-2.png)

- 식 1-2와 같이 은닉층의 뉴런은 가중치의 합으로 계싼 된다.

- 이것을 행렬로 한꺼번에 계산하면 다음과 같다.

![식 1-3](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/e%201-3.png)

- 그림 1-8 과 같이 행렬의 곱에서는 대응하는 차원의 원소 수가 일치해야한다.

![그림 1-8](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-8.png)

- 신경망의 추론이나 학습에서는 다수의 샘플 데이터를 한꺼번에 처리한다.
- 그럴라면 행렬 x의 각 행 각각에 데이터를 저장해야한다
- N개의 샘플 데이터를 미니배치로 한꺼번에 처리한다면 그림 1-9 처럼 된다.

![그림 1-9](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-9.png)

 - 완전 연결 계층에 의한 변환의 미니배치 버전을 파이썬으로 해본다.
 ![alt text](image.png)

 - 이 완전연결 계층에 의한 변환은 선형 변환이다 여기서 비선형 효과를 부여하는것이 활성화 함수이다.
 - 여기에서는 식 1-5인 시그모이드 함수를 사용한다.

 ![식 1-5](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/e%201-5.png)

 - 시그모이드는 다음 그림과 같다.
![그림 1-10](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-10.png)

- 시그모이드 함수는 임의의 실수를 입력받아 0에서 1 사이의 실수를 출력한다.

- 이것을 파이썬으로 구현해 본다.

- 이 시그모이드를 사용하여 방금 전의 은닉층 뉴런을 변환한다.

- 활성화 함수의 출력인 a(이를 활성화 라고 한다)를 다른 완전 연결 계층에 통과시켜 변환한다.

- 종합한 파이썬으로 작성해본다.
- 여기서 x의 형상은 10,2이다, 데이터 10개가 미니배치로 처리된다는 것이다.
- 최종 출력인 s의 형상은 (10,3)이다.

- 이 신경망은 3차원 데이터를 출력한다 따라서 각 차원의 값을 이요ㅕㅇ하여 3클래스 분류를 할수있다.

- 출력된 3차원 벡터의 각 차원은 각 클래스에 대응하는 점수가 된다.

### 1.2.2 계층으로 클래스화ㅣ 및 순전파 구현

- 신경망에서 하는 처리를 계층layer로 구현해본다

- 완전연결계층에 의한 변환을 Affine 계층으로, 시그모이드 함수에 의한 변환을 sigmoid 계층으로 구현할 것이다.
- 완전연결 계층에 의한 변환은 기하학에서의 아핀 변환에 해당하기 때문에 Affine 계층 이라고 지어ㅗㅆ다.

- 신경망에는 다양한 계층이 등장하는데 이 계층을 모두 파이썬 클래스로 구현할 것이다.

- 이 책에서는 이러한 계층을 구현할 때 다음의 구현 규칙을 따른다.
- 모든 계층은 forward() 와 backward()매서드를 가진다
- 모든 계층은 인스턴스 변수인 params 와 grads 를 가진다.

- forward 와 backward는 순전파와 역전파를 수행한다.
- params 는 가중치와 편향같은 매개변수를 담는 리스트이다.
- 마지막으로 grad는 params 에 저장된 각 매개변수에 대응하여 해당 매개변수의 기울기를 보관하는 리스트이다.

- 이번 절에서는 순전파만 구현할 것이므로 규칙 2개만 적용하겟다.
- forward 만 가지고 매개변수들은 params 인스턴스 변수에 보관하는 규칙만 사용한다


- 가장 먼저 구현할 계층은 sigmoid 계층이다.

- 주 변환 처리는 forward(x) 메서드가 담당한다.

- Sigmoid 계층에는 학습하는 매개변수가 따로 없으므로 인스턴스 변수인 params는 빈 리스트로 초기화

- Affine 계층의 구현을 보자
- Affine 계층은 초기화 될때 가중치와 편향을 받는다.
- Affine 계층의 매개변수이며 리스트인 params 인스턴스 변수에 보관한다.

- forward(x)는 순전파 처리를 구현한다.

![그림 1-11](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-11.png)

- 그림 1-11처럼 구성된 신경망을 구현할 것이다.

- 위 그림처럼 입력 x 가 Affine 계층 Sigmoid 계층 Affine 계층을 차례로 거쳐 점수인 S를 출력하게 된다.

- 이 신경망을 TwoLayerNet 이라는 클래스로 추상화 하고 주 추론 처리는 predict(x) 메서드로 구현한다.

- TwoLayerNet의 초기화 메서드 __init__은 먼저 가중치를 초기화 하고 3개의 개층을 생성한다

- 마지막으로 학습해야할 가중치 매개변수들을 params에 저장한다.

- 모든 계층은 자신의 학습 매개변수들을 인스턴스 변수인 params에 보관하고 있으므로 이 변수들을 더해주면 된다.

- 이처럼 매개변수들을 하나의 리스트에 보관하면 매개변수 갱신과 매개변수 저장을 손쉽게 처리할 수 있다.

## 1.3 신경망의 학습

- 학습되지 않은 신경망은 좋은 추론을 할수 없다.
- 그래서 학습을 먼저 수행하고 그 학습된 매개변수를 이용해 추론을 수행하는 흐름이 일반적이다.

- 신경망의 학습은 최적의 매개 변수 값을 찾는 작업이다ㅏ.

### 1.3.1 손실함수 

- 신경망 학습에는 학습이 얼마나 잘 되고 있는지를 알기 위한 척도가 필요하다
- 그 척도를 손실로 알수 있다.
- 손실은 학습 데이터와 신경망이 예측한 결과를 비교하여 예측이 얼마나 나쁜가를 산출한 단일 값 이다.

- 신경망의 손실은 손실 함수를 사용해 구한다.
- 다중 클래스 분류 신경망에서는 손실 함수로 주로 교차 엔트로피 오차를 사용한다.
- 교차 엔트로피 오차는 신경망이 출력하는 각 클래스의 "확률"과 "정답 레이블"을 이용해 구할수 있다.


- 지금까지 만든 신경망에서 손실을 구해본자
- 앞절의 신경망에 softmax 계층과 Cross Entropy Error 계층을 새로 추가한다.
- 이 신경망의 구성을 계층 관점에서 그리면 그림 1-12처럼 된다


![그림 1-12](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-12.png)

- x는 입력 데이터 t는 정답 레이블 L은 손실을 나타낸다.

- softmax 꼐층의 출력은 확률이되며 다음 계층인 Cross Entropy Error 계층에는 확률고 ㅏ정답 레이블이 입력된다.

- 소프트 맥스를 식으로 쓰면 다음과 같다.

![식 1-6](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/e%201-6.png)

- 위 식은 출력이 총 n개일때 k번째의 출력 yk를 구하는 계산식이다.

- 원소들의 합을 다 더하면 1이기 떄문에 각 원소가 나타낸 값은 확률이다.

- 소프트 맥스의 출력인 이 확률 값을 다음 차례인 교차 엔트로피 오차에 입력한 수식은 다음과 같다.

![식 1-7](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/e%201-7.png)

- t는 정답 레이블 이다. 정답 레이블은 원핫 벡터로 표기한다.

- 미니 배치를 고려하면 다음과 같이 나타낼수 있다.

![식 1-8](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/e%201-8.png)

- N 개로ㅓ 나눠서 1개당 평균 손실함수를 구해서 미니배치의 크기에 관계 없이 항상 일관된 값을 가지게 한다.

- 이 책에서는 소프트 맥스 함수와 교차 엔트로피 오차를 계산하는 계층을 Softmax with Loss 계층 하나로 구현한다.

- 따라서 신경망 계층 구성은 그림 1-13 처럼 된다.


![그림 1-13](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-13.png)

### 1.3.2 미분과 기울기

- 신경망 학습의 목표는 손실을 최소화 하는 매개변수를 찾는것이다.

- 이떄 중요한 것이 미분과 기울기 이다.



![식 1-9](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/e%201-9.png)

![식 1-10](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/e%201-10.png)


### 1.3.3 연쇄 법칙

- 학습 시 신경망은 학습 데이터를 주면 손실을 출력한다.

- 우리가 얻고 싶은 것은 각 매개변수에 대한 손실의 기울기 이다.

- 신경망의 기울기는 오차 역전파 법으로 구할수 있다.
- 오차 역 전파법을 이해하는 열쇠는 연쇄 법칙이다.
- 연쇄 법칙이란 합성 함수에 대한 미분 법칙이다.

### 1.3.4 계산 그래프

- 오차 역전파법을 설명하기 전에 계산 그래프 부터 설명한다.


![그림 1-15](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-15.png)

![그림 1-17](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-16.png)


![그림 1-18](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-18.png)

![그림 1-19](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-19.png)

![그림 1-20](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-20.png)

![그림 1-21](../DLFromScratch2-master/equations_and_figures_2/deep_learning_2_images/fig%201-21.png)