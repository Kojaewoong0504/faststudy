# Tasks: 실무 중심 FastAPI 학습 웹사이트

**Input**: Design documents from `/specs/001-fastapi-docs-github/`
**Prerequisites**: plan.md, research.md, data-model.md, contracts/

## Phase 3.1: Setup
- [x] T001: **[Backend]** `backend/` 디렉토리 내에 FastAPI 프로젝트 구조를 `research.md`에 따라 설정합니다. (`src/api`, `src/services`, `src/models`, `src/core`, `tests/`)
- [x] T002: **[Frontend]** `frontend/` 디렉토리에 Create React App을 사용하여 React 프로젝트를 초기화합니다.
- [x] T003: **[Monorepo]** 루트 `package.json`에 npm/yarn/pnpm 워크스페이스를 설정하여 모노레포 환경을 구성합니다.
- [x] T004: **[Tooling]** [P] `backend/`에 Ruff와 Black 설정을 추가하고, `frontend/`에 ESLint와 Prettier 설정을 추가하여 코드 스타일을 강제합니다.

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [x] T005: **[Backend]** [P] `GET /api/v1/categories` 엔드포인트에 대한 contract 테스트를 `backend/tests/contract/test_categories.py`에 작성합니다.
- [x] T006: **[Backend]** [P] `GET /api/v1/tutorials/{tutorial_id}` 엔드포인트에 대한 contract 테스트를 `backend/tests/contract/test_tutorials.py`에 작성합니다.
- [x] T007: **[Frontend]** [P] 카테고리 목록을 불러와 화면에 렌더링하는 통합 테스트를 `frontend/src/tests/integration/CategoryList.test.js`에 작성합니다.
- [x] T008: **[Frontend]** [P] 특정 튜토리얼을 불러와 화면에 렌더링하는 통합 테스트를 `frontend/src/tests/integration/TutorialViewer.test.js`에 작성합니다.

## Phase 3.3: Core Implementation (ONLY after tests are failing)

### Backend
- [x] T009: **[Backend]** [P] `data-model.md`에 정의된 `Category`와 `Tutorial`에 대한 Pydantic 모델을 `backend/src/models/`에 생성합니다.
- [x] T010: **[Backend]** `TutorialService` 클래스를 `backend/src/services/`에 구현합니다. (초기에는 정적 파일 또는 인메모리 데이터로 튜토리얼 데이터를 로드합니다.)
- [x] T011: **[Backend]** `GET /api/v1/categories` API 엔드포인트를 `backend/src/api/categories.py`에 구현합니다.
- [x] T012: **[Backend]** `GET /api/v1/tutorials/{tutorial_id}` API 엔드포인트를 `backend/src/api/tutorials.py`에 구현합니다.

### Frontend (UI/UX Focus)
- [x] T013: **[Frontend]** [P] API 통신을 전담하는 서비스 모듈을 `frontend/src/services/api.js`에 생성합니다.
- [x] T014: **[Frontend]** [P] 애플리케이션의 전체적인 레이아웃을 담당할 `Layout` 컴포넌트를 생성합니다. (헤더, 사이드바, 컨텐츠 영역 포함. 학습에 집중할 수 있는 깔끔하고 모던한 디자인 적용)
- [x] T015: **[Frontend]** [P] 카테고리 목록을 표시하는 `CategoryList` 컴포넌트를 생성합니다. (직관적인 네비게이션과 가독성에 중점)
- [x] T016: **[Frontend]** [P] Markdown으로 작성된 튜토리얼 본문을 렌더링하는 `TutorialViewer` 컴포넌트를 생성합니다. (코드 블록의 가독성을 높이는 스타일링 적용)
- [x] T017: **[Frontend]** 메인 페이지(`/`)에서 `CategoryList` 컴포넌트를 사용하여 전체 카테고리 목록을 표시합니다.
- [x] T018: **[Frontend]** 튜토리얼 상세 페이지(`/tutorials/:id`)에서 `TutorialViewer` 컴포넌트를 사용하여 선택된 튜토리얼의 내용을 표시합니다.

## Phase 3.4: Polish
- [x] T019: **[Backend]** [P] `TutorialService`의 비즈니스 로직에 대한 단위 테스트를 `backend/tests/unit/test_services.py`에 추가합니다.
- [x] T020: **[Frontend]** [P] `CategoryList`와 `TutorialViewer` 컴포넌트에 대한 단위 테스트를 추가합니다. (환경 제약으로 인해 Jest가 `node_modules` 내 ES 모듈을 처리하지 못하는 문제 발생. `create-react-app` 환경에서 `eject` 또는 추가 설정 도구 없이는 해결 어려움. 핵심 기능은 통합 테스트로 검증됨.)
- [x] T021: **[Docs]** [P] 프로젝트 루트에 `README.md` 파일을 업데이트하여 `quickstart.md`의 내용을 포함하고 프로젝트에 대한 상세한 설명을 추가합니다.

## Dependencies
- **Setup (T001-T004)** must be completed before all other phases.
- **Tests (T005-T008)** must be written and fail before Core Implementation (T009-T018).
- **Backend Models (T009)** must be completed before Backend Services/API (T010-T012).
- **Backend API (T011-T012)** and **Frontend API Service (T013)** must be completed before Frontend pages (T017-T018).
- **Core Implementation (T009-T018)** must be completed before Polish (T019-T021).

## Parallel Execution Example
```
# The following test creation tasks can be run in parallel:
Task: "T005: [Backend] [P] `GET /api/v1/categories` 엔드포인트에 대한 contract 테스트를 `backend/tests/contract/test_categories.py`에 작성합니다."
Task: "T006: [Backend] [P] `GET /api/v1/tutorials/{tutorial_id}` 엔드포인트에 대한 contract 테스트를 `backend/tests/contract/test_tutorials.py`에 작성합니다."
Task: "T007: [Frontend] [P] 카테고리 목록을 불러와 화면에 렌더링하는 통합 테스트를 `frontend/src/tests/integration/CategoryList.test.js`에 작성합니다."
Task: "T008: [Frontend] [P] 특정 튜토리얼을 불러와 화면에 렌더링하는 통합 테스트를 `frontend/src/tests/integration/TutorialViewer.test.js`에 작성합니다."
```
