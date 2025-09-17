# Data Model: FastAPI 학습 콘텐츠 추가

## 개요
기존 `Category` 및 `Tutorial` 엔티티를 MongoDB에 맞게 재정의합니다. MongoDB의 유연한 스키마를 활용하되, Pydantic을 사용하여 데이터 유효성을 보장합니다.

## 엔티티 정의

### Category
- **설명**: FastAPI 학습 콘텐츠를 분류하는 카테고리 정보.
- **MongoDB Collection**: `categories`
- **필드**:
    - `id`: `ObjectId` (MongoDB의 기본 ID, Pydantic에서는 `str`로 처리)
    - `name`: `str` (카테고리 이름, 필수)
    - `description`: `str` (카테고리 설명, 선택 사항)

### Tutorial
- **설명**: 실제 FastAPI 학습 콘텐츠의 상세 정보.
- **MongoDB Collection**: `tutorials`
- **필드**:
    - `id`: `ObjectId` (MongoDB의 기본 ID, Pydantic에서는 `str`로 처리)
    - `title`: `str` (튜토리얼 제목, 필수)
    - `category_id`: `ObjectId` (참조하는 `Category`의 ID, 필수, Pydantic에서는 `str`로 처리)
    - `content`: `str` (튜토리얼 내용, Markdown 형식, 필수)
    - `order`: `int` (카테고리 내 튜토리얼 순서, 필수)
    - `created_at`: `datetime` (생성일시, 기본값: 현재 시간)
    - `updated_at`: `datetime` (수정일시, 기본값: 현재 시간, 업데이트 시 자동 갱신)

## 관계
- `Tutorial` 엔티티는 `category_id` 필드를 통해 `Category` 엔티티를 참조합니다. 이는 MongoDB의 참조(Reference) 방식으로 구현됩니다.

## 유효성 검사 (Pydantic)
- 각 엔티티는 FastAPI에서 Pydantic 모델을 사용하여 데이터 유효성을 검사합니다.
- `ObjectId`는 Pydantic의 `BeforeValidator` 등을 사용하여 `str` 타입으로 변환 및 유효성 검사를 수행할 수 있습니다.

---
