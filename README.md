# Data Analysis on Global Terrorism

> 테러 관련 데이터를 활용한 분석

## I. 분석 개요 및 배경

### 1. 분석 배경

* 올해 미군의 아프가니스탄 철군과 탈레반의 정권 재장악, 카불 공항 테러 등 충격을 주는 사건들이 있었다.
* 미국인들의 삶은 물론 전 세계의 현대사를 바꿔놓은 9.11 사태가 발생한지, 그리고 '테러와의 전쟁'이 선포된지 20년이 지난 오늘, 세상은 더 안전해졌을까?
* 우리 일상 속 드물게만 기억되던, 상기되던 이 "테러"라는건 얼마나, 어떻게 변해왔는지 그리고 왜 발생했는지 알아보고자 분석을 진행하였다.

### 2. 분석 목적/목표

* 1970년대~2010년대까지의 전세계 테러 관련 데이터를 활용하여 테러 활동 추이와 현황을 파악하고, 테러 활동의 원인/요인을 분석한다.
* 발견된 문제점과 이에 따른 향후 과제 제시한다.

### 3. 데이터 수집
* Kaggle에 공개 된 1970~2017년까지의 180,000 이상의 테러 활동/공격에 대한 데이터인 Global Terrorism Database (GTD)를 사용하였다.
* 135개의 컬럼이 존재하며, 해당 데이터에는 테러가 발생한 시점, 공격형태(암살, 폭탄 등), 국가, 지역(동아시아, 유럽 등), 부상자, 사망자, 테러의 발생 위도, 경도 정보 등이 있다,

## II. 분석 결과

### 9.11 사태 이후 20년, 세상은 테러로부터 더 안전해졌을까?

결론부터 얘기하자면, **아니다**.

### 테러 발생 건수

![image](https://user-images.githubusercontent.com/38115693/142788747-7925ff6f-70ec-4de0-97cb-dd6f2ec1a0cd.png)

- 2011년 이후 테러 활동 수는 급격히 증가하였다.
- 2000년대에, 2001년 9.11 사태 이후 조금의 감소를 보였던 테러 건수는, 미국의 이라크 침공과 아프가니스탄에 대한 군사적 개입, 중동 지역에서의 수니/시아파 간 분쟁 증가, 정정 불안, 전쟁 도구로 테러 활용, 경제 문제에 대한 불만 고조 등의 이유로 테러 활동이 증가하기 시작하였다.
- 이후, 2011년 불어온 민주화 운동의 바람 '아랍의 봄'에 중동과 북아프리카 전역으로 반정부 시위가 번졌고 각국의 권위주의 정권이 속속 몰락했다. 하지만 '아랍의 봄'의 여파로, 내전과 경제난 등으로 혼란 상태가 지속되고 치안이 약해진 틈을 타 이슬람국가(IS)의 부상 등 극단주의 무장 조직의 급격한 활동 증가와 세력 확장이 이루어졌다.

### 사망자

![image](https://user-images.githubusercontent.com/38115693/142792218-c23f9e05-6df4-4593-9f4c-6bb3e4940d97.png)

### 부상자

![image](https://user-images.githubusercontent.com/38115693/142792080-e6ea90be-a5dd-4859-aa6a-5ebaa9da2632.png)

- 테러 활동의 증가와 함께 사상자(사망자+부상자) 수 또한 급격히 증가하였다.

### 1970~2017년까지의 테러 현황을 살펴보면

### 공격 유형

![image](https://user-images.githubusercontent.com/38115693/142797166-2c96e95a-9c74-42cd-8ae3-3a4482d8ce46.png)

- 테러 공격 유형으로는 Bombing/Explosion이 그 수가 가장 많으며, 그 다음으로 Armed Assult가 많이 발생했다.

![image](https://user-images.githubusercontent.com/38115693/142797471-0fb3dcf8-bbc3-4b46-ac7e-8d9860e9ea52.png)

- 발생 건수뿐만 아니라, Bombing/Explosion에 의한 사상자가 테러 공격 유형 중 가장 많았으며, 이어서 Armed Assault가 두 번째로 많았다.

### 자살 공격

![image](https://user-images.githubusercontent.com/38115693/142800984-5fadbfeb-f210-48ab-9fcb-1ee4d66afe95.png)

- 그리고 Bombing/Explosion 테러 공격 유형의 약 7%가 자살 공격이었다.

### 테러 단체/그룹

![image](https://user-images.githubusercontent.com/38115693/142801093-b0960439-3da4-4183-8cc2-d59f4638e607.png)

- ('Unknown'을 제외한) Attacker가 파악이 된 테러 공격 중, Taliban에 의한 테러 활동이 가장 많았고, 다음으로 Islamic State, Shining Path (SL), FMLN 순으로 테러 활동 수가 가장 많았다.

### 테러 공격 타겟

![image](https://user-images.githubusercontent.com/38115693/142801209-59962c2a-889b-47c1-b4a3-c931e9fca303.png)

- 테러로 인한 피해자 중 민간(Private Citizens & Property)에 대한 공격 빈도수가 가장 많았으며, 그 다음 순으로 군대/군인(Military), 경찰(Police), 정부(Government (General)), 기업(Business)에 대한 공격이 많았다.

### 테러 목적/특성

![image](https://user-images.githubusercontent.com/38115693/142801816-5d5ccf98-14b3-43cb-b647-c66c07a1e3e2.png)

- 약 99%의 테러 활동이 정치, 경제, 종교, 또는 사회적 목적을 가진 것으로 나타났다.

![image](https://user-images.githubusercontent.com/38115693/142801833-dce37e90-7b5c-46ba-a047-fbf36b8c8724.png)

- 약 99%의 테러 활동이 더 큰 규모로 강압, 위협, 또는 홍보를 하려는 의도가 있었다.

![image](https://user-images.githubusercontent.com/38115693/142801873-bcc8a1de-eeeb-41de-a187-bb0c3c0ed548.png)

- 약 87%의 테러 활동이 국제 인도주의법에 위배되었다.

### 24시간 이상 지속 여부 

![image](https://user-images.githubusercontent.com/38115693/142802236-33307b8d-46e3-4847-adc6-2e77567a4529.png)

- 전체 테러 공격 중 약 95%가 24시간 미만, 약 5%의 테러만 24시간 이상 지속되었다.

![image](https://user-images.githubusercontent.com/38115693/142802273-4bb3d10c-36e4-4352-8a51-50b3c36acd15.png)

- 하지만 24시간 이상 지속된 테러 공격으로 인한 피해가 24시간 미만의 테러 공격보다 더 높은 평균 사상자를 냈다. 24시간 미만 테러 공격으로는 평균적으로 1.1명의 사상자(only victims)가 발생하였지만, 24시간 이상 지속된 테러 공격은 평균 2.1명의 사상자(only victims)가 발생했다. Victims와 Attackers 모두 합쳐서는 각각 평균 2.2명, 3.0명의 사상자가 발생했다.
- 테러 발생시 조기에, 신속히 진압 및 해결하는 것이 더 큰 피해를 막는데 중요 할 것으로 보인다.

### 테러 피해 상위 10개국

![image](https://user-images.githubusercontent.com/38115693/142802369-22d24bd8-6304-4c58-ae5d-c0b5038c6493.png)

- 1970년부터 2017년 사이 Iraq, Pakistan, Afghanistan, India 등의 순서로 가장 많은 테러가 발생 했다.

![image](https://user-images.githubusercontent.com/38115693/142802434-3a7edb9e-631c-4f19-8400-c79db839ae9d.png)

- Top 10 국가별 테러 건수와 사상자를 비교해 보면, Iraq, Afghanistan, Pakistan, India 등의 국가는 테러 발생 수에 비해 다른 국가들 보다 상대적으로 더 많은 사상자가 발생했다.

<img src="https://user-images.githubusercontent.com/38115693/142802702-359000a4-98d4-49b9-a150-f3dc905dddd6.png" width="30%">

- 10개 국가의 상위 공격 유형을 살펴보니, Iraq, Pakistan, Afghanistan, India의 Bombing/Explosion과 Armed Assault가 가장 큰 빈도수를 차지한다.

![image](https://user-images.githubusercontent.com/38115693/142802981-30b18126-740a-474f-b500-cde229e48431.png)

- 이는 위에서 언급했던, Bombing/Explosion과 Armed Assault로 인한 사상자 수가 다른 공격 유형에 비해 큰 것과 관계가 있는 것으로 생각된다.
- 위 4개 국가에선 큰 사상자를 만드는 Bombing/Explosion과 Armed Assault 발생 건수와 비율이 높다. 이 때문에, 4개 국가에선 테러 건수 대비 더 많은 사상자가 발생한 것 같다.

### 지역

![image](https://user-images.githubusercontent.com/38115693/142803108-06c0b0f5-2a43-4dad-814e-35a1c8b3ed0e.png)

- 지역별로 보면, Middle East & North Africa, South Asia, South America, Sub-Saharan Africa, Western Europe에서 가장 많은 테러가 발생했다.

![image](https://user-images.githubusercontent.com/38115693/142803144-b2487ba0-6d2a-47e2-a206-4a01cb4c28a2.png)

- 테러가 가장 많이 발생한 두 지역 MENA와 SA에서의 테러로인한 사상자 피해도 가장 크다.

![image](https://user-images.githubusercontent.com/38115693/142803310-fb13657d-aae2-459e-a196-3410ca1c8508.png)

- 위 두 지역에서 가장 많이 사용된 테러 공격 또한 Bombing/Explosion과 Armed Assault이다.

### 이제 연도별 및 10년 기간별로 나누어 테러 추이/경향를 살펴보면

### 10년 기간별 테러 발생 건수

![image](https://user-images.githubusercontent.com/38115693/142804121-42b06ae0-fec3-4394-a3cc-93974fa97c70.png)

### 10년 기간별 지역 변화

![image](https://user-images.githubusercontent.com/38115693/142804518-1d5fd4eb-426e-425c-8cb6-8df462472311.png)

- 1970년대 주로 서유럽에서 발생한 테러는 1980년대에는 라틴 아메리카, 1990년대 이후 중동·북아프리카·남아시아에서 주로 발생하였다.
- 특히, 2010년대에 중동·북아프리카·남아시아에서의 테러 발생 건수는 급격히 증가하였으며, 두 지역 외에도 사하라 사막 이남 아프리카 지역(Sub-Saharan Africa)과 동남아시아(Southeast Asia)에서도 크게 증가하였다.

![image](https://user-images.githubusercontent.com/38115693/142804548-37f9b645-6694-47be-8b43-a0024fcc3fe0.png)

### 10년 기간별 테러 조직 변화

![image](https://user-images.githubusercontent.com/38115693/142804931-137c60fb-65ca-4a7b-a367-0c759504a672.png)

- 2010년대에 테러/무장 단체 Taliban, Islamic State(ISIS), Al-Shabaab, Boko Haram에 의한 테러 활동 건수가 급격히 증가하였다.

![image](https://user-images.githubusercontent.com/38115693/142805555-079265b3-8033-44c4-b759-5f3964d4f8ca.png)

- 2000년대 초 이후 미국의 아프가니스탄 군사적 개입을 계기로 Taliban의 테러 활동이 증가하기 시작한 것으로 보이며, 2011년 이후 Taliban과 새롭게 등장한 ISIS의 테러 활동이 급격히 증가한 것을 볼 수 있다.

### 연도별 MENA, SA, Sub-Saharan Africa 지역에 대한 주요 테러 조직의 활동 변화

#### Middle East & North Africa 지역

![image](https://user-images.githubusercontent.com/38115693/142805984-5083f2d8-58bd-4a9a-be0a-7d4a2fa345aa.png)

#### South Asia 지역

![image](https://user-images.githubusercontent.com/38115693/142806029-d096bf9c-70e9-423a-a856-eaa502dd5dbe.png)

#### Sub-Saharan Africa 지역

![image](https://user-images.githubusercontent.com/38115693/142806068-2698c7cc-51a7-4475-a987-c2f5f3909082.png)

- 2011년 이후 South Asia 지역에선 Taliban이, Middle East & North Africa 지역에선 새롭게 등장한 ISIS(ISIL)가, Sub-Saharan Africa 지역에선 Al-Shabaab, Boko Haram 등의 조직들의 세력 확장과 활발한 테러 활동으로 테러 발생 건수가 급증 하였다.

### 연도별 테러 공격 유형 변화 

#### 공격 유형별

![image](https://user-images.githubusercontent.com/38115693/142806269-f23452ba-0b22-483e-b9c5-d7a06f02c46a.png)

- 테러 발생 건수 증가와 함께, Bombing/Explosion과 Armed Assault의 테러 사용 건수 또한 2011년 이후 급격히 증가하였다.

#### 자살 공격

![image](https://user-images.githubusercontent.com/38115693/142806345-3f7de4f5-ab67-44b0-8025-444942efaac7.png)

- 전체 테러 중 자살 공격의 비중이 크지는 않다

![image](https://user-images.githubusercontent.com/38115693/142806478-f2093f3c-eb5d-45de-b794-0ffabfd9e1f0.png)

- 하지만 명백하게, 자살 공격이 행해지는 빈도수는 과거에 비해 급격히 증가하였다.

### 연도별 테러 공격 타겟/피해 대상 변화

![image](https://user-images.githubusercontent.com/38115693/142806602-464e65a3-cf5a-4eed-8ce8-db01d15bbab2.png)

- 군인(Military), 경찰(Police) 그리고 정부기관(Government) 등이 많은 테러의 타겟(target/victim)이 되어 왔지만, 결국 가장 많은 피해를 입은건 바로 민간인(Private Citizens & Property)이다.

## III. 요약

2000년대 중반부터 증가하기 시작한 테러 활동은, 2011년 아랍의 봄을 기점으로 급격히 증가하였다. 평화와 안정에 대한 기대는 사라졌고, 기존의 테러 조직과 새롭게 등장한 테러 단체는 더욱 활발히 활동하며 세력을 키웠다. 테러 공격의 증가와 폭발물/폭탄 사용의 증가로 사상자 수 또한 급격히 증가하였다.

더욱이, 중동과 남아시아의 문제라고만 여겨졌던 "테러"는 어느새 사하라 이남 아프리카와 동남아시아로까지 확대되었다.

테러 활동 및 세력의 확대는 국제 테러단체들의 물리적인 이동의 영향도 있지만, 인터넷/디지털 상에서 테러단체들의 선동에 현혹되어 급진의식화 되거나 아랍과 무슬림에 대한 편견과 차별로 무슬림 이주민들이 폭력적 극단주의자가 되어버리는 '외로운 늑대(Lone Wolf)' 그리고 이로 인한 '자생 테러'의 발생은 전 세계적인 위협으로 떠올랐다. 

이번 데이터를 근거로 'Counter terrorism'을 위해 국제사회가 해야하는 것은 무엇인지 생각해 보았다.
1. 첫째, 불법적인 무기, 화학물 그리고 자금 거래에 대한 국제적인 모니터링 시스템을 구축해야 하며, 지속적이고 적극적인 모니터링과 대응으로 사전 예방(prevention)이 되어야 한다.
2. 둘째, 테러의 확산을 방지하기 위해 국민들에 대한 국가적인 교육과 관심 및 지원이 필요하다. 청년들과 무슬림 이주민 2-3세 자녀들이 극단적 폭력주의에 현혹되지 않고 자생적 테러리스트가 되지 않기 위해선, 그들에 대한 관심과 지원이 필요하며, 또한 무슬림에 대한 편견과 차별이 사라지도록 이를 위한 교육이나 프로그램이 필요하다. 그리고 SNS 등 플랫폼 기업들의 디지털/온라인 상에서의 혐오표현(hate speech)이나 폭력적 극단주의(violent extremism) 컨텐츠를 삭제하는 등 적극적인 모니터링과 대응도 필요하다.
