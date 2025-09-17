# Tasks: FastAPI 학습 콘텐츠 추가

**Input**: Design documents from `/specs/002-fastapi/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/, quickstart.md

## Execution Flow (main)
```
1. Load plan.md from feature directory
   → If not found: ERROR "No implementation plan found"
   → Extract: tech stack, libraries, structure
2. Load optional design documents:
   → data-model.md: Extract entities → model tasks
   → contracts/: Each file → contract test task
   → research.md: Extract decisions → setup tasks
3. Generate tasks by category:
   → Setup: project init, dependencies, linting
   → Tests: contract tests, integration tests
   → Core: models, services, CLI commands
   → Integration: DB, middleware, logging
   → Polish: unit tests, performance, docs
4. Apply task rules:
   → Different files = mark [P] for parallel
   → Same file = sequential (no [P])
   → Tests before implementation (TDD)
5. Number tasks sequentially (T001, T002...)
6. Generate dependency graph
7. Create parallel execution examples
8. Validate task completeness:
   → All contracts have tests?
   → All entities have models?
   → All endpoints implemented?
9. Return: SUCCESS (tasks ready for execution)
```

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 3.1: Setup
- [x] T001 백엔드 의존성 설치 및 Docker 환경 설정 (backend/requirements.txt, Dockerfile, docker-compose.yml)
- [x] T002 [P] 프론트엔드 의존성 설치 (frontend/package.json)
- [x] T003 [P] 백엔드 린팅 및 포맷팅 도구 설정 (backend/pyproject.toml)
- [x] T004 [P] 프론트엔드 린팅 및 포맷팅 도구 설정 (frontend/.prettierrc.json)

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [x] T005 [P] 계약 테스트: GET /categories (backend/tests/contract/test_categories.py)
- [x] T006 [P] 계약 테스트: GET /categories/{category_id} (backend/tests/contract/test_categories.py)
- [x] T007 [P] 계약 테스트: GET /categories/{category_id}/tutorials (backend/tests/contract/test_tutorials.py)
- [x] T008 [P] 계약 테스트: GET /tutorials/{tutorial_id} (backend/tests/contract/test_tutorials.py)
- [x] T009 [P] 계약 테스트: POST /tutorials (backend/tests/contract/test_tutorials.py)
- [x] T010 [P] 계약 테스트: PUT /tutorials/{tutorial_id} (backend/tests/contract/test_tutorials.py)
- [x] T011 [P] 계약 테스트: DELETE /tutorials/{tutorial_id} (backend/tests/contract/test_tutorials.py)
- [x] T012 [P] 통합 테스트: 새로운 콘텐츠 추가 및 접근 시나리오 (frontend/tests/integration/test_content_flow.js)
- [x] T013 [P] 통합 테스트: 특정 튜토리얼 상세 조회 시나리오 (frontend/tests/integration/test_tutorial_view.js)

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [x] T014 [P] MongoDB 연결 설정 및 클라이언트 초기화 (backend/src/core/database.py)
- [x] T015 [P] Category 모델 정의 (backend/src/models/category.py)
- [x] T016 [P] Tutorial 모델 정의 (backend/src/models/tutorial.py)
- [x] T017 Category 서비스 (CRUD) 구현 (backend/src/services/category_service.py)
- [x] T018 Tutorial 서비스 (CRUD) 구현 (backend/src/services/tutorial_service.py)
- [x] T019 GET /categories 엔드포인트 구현 (backend/src/api/categories.py)
- [x] T020 GET /categories/{category_id} 엔드포인트 구현 (backend/src/api/categories.py)
- [x] T021 GET /categories/{category_id}/tutorials 엔드포인트 구현 (backend/src/api/tutorials.py)
- [x] T022 GET /tutorials/{tutorial_id} 엔드포인트 구현 (backend/src/api/tutorials.py)
- [x] T023 POST /tutorials 엔드포인트 구현 (backend/src/api/tutorials.py)
- [x] T024 PUT /tutorials/{tutorial_id} 엔드포인트 구현 (backend/src/api/tutorials.py)
- [x] T025 DELETE /tutorials/{tutorial_id} 엔드포인트 구현 (backend/src/api/tutorials.py)

## Phase 3.4: Frontend UI Implementation
- [x] T026 [P] CategoryList 컴포넌트 업데이트 (frontend/src/components/CategoryList.js)
- [x] T027 [P] TutorialList 컴포넌트 업데이트 (frontend/src/components/TutorialList.js)
- [x] T028 [P] TutorialViewer 컴포넌트 업데이트 (frontend/src/components/TutorialViewer.js)
- [x] T029 [P] API 서비스 레이어 업데이트 (frontend/src/services/api.js)
- [x] T030 [P] 라우팅 설정 및 페이지 연결 (frontend/src/App.js)

## Phase 3.5: Integration & Polish
- [x] T031 백엔드 미들웨어 설정 (CORS, 에러 핸들링) (backend/src/main.py)
- [x] T032 [P] 백엔드 단위 테스트 (backend/tests/unit/test_services.py)
- [x] T033 [P] 프론트엔드 단위 테스트 (frontend/tests/unit/test_components.js)
- [x] T034 [P] 성능 최적화 및 로깅 설정
- [x] T035 [P] 문서 업데이트 (README.md, API 문서)

## Dependencies
- T001-T004 (Setup) before T005-T035
- T005-T013 (Tests) before T014-T025 (Core Implementation)
- T014 (MongoDB 연결) before T015-T018 (Models, Services)
- T015-T016 (Models) before T017-T018 (Services)
- T017-T018 (Services) before T019-T025 (Endpoints)
- T019-T025 (Endpoints) before T026-T030 (Frontend UI)
- T026-T030 (Frontend UI) before T031-T035 (Integration & Polish)

## Parallel Example
```
# Launch T005-T011 (Contract Tests) together:
Task: "계약 테스트: GET /categories (backend/tests/contract/test_categories.py)"
Task: "계약 테스트: GET /categories/{category_id} (backend/tests/contract/test_categories.py)"
Task: "계약 테스트: GET /categories/{category_id}/tutorials (backend/tests/contract/test_tutorials.py)"
Task: "계약 테스트: GET /tutorials/{tutorial_id} (backend/tests/contract/test_tutorials.py)"
Task: "계약 테스트: POST /tutorials (backend/tests/contract/test_tutorials.py)"
Task: "계약 테스트: PUT /tutorials/{tutorial_id} (backend/tests/contract/test_tutorials.py)"
Task: "계약 테스트: DELETE /tutorials/{tutorial_id} (backend/tests/contract/test_tutorials.py)"

# Launch T015-T016 (Models) together:
Task: "Category 모델 정의 (backend/src/models/category.py)"
Task: "Tutorial 모델 정의 (backend/src/models/tutorial.py)"

# Launch T026-T030 (Frontend UI) together:
Task: "CategoryList 컴포넌트 업데이트 (frontend/src/components/CategoryList.js)"
Task: "TutorialList 컴포넌트 업데이트 (frontend/src/components/TutorialList.js)"
Task: "TutorialViewer 컴포넌트 업데이트 (frontend/src/components/TutorialViewer.js)"
Task: "API 서비스 레이어 업데이트 (frontend/src/services/api.js)"
Task: "라우팅 설정 및 페이지 연결 (frontend/src/App.js)"
```

## Notes
- [P] tasks = different files, no dependencies
- Verify tests fail before implementing
- Commit after each task
- Avoid: vague tasks, same file conflicts

## Task Generation Rules
*Applied during main() execution*

1. **From Contracts**:
   - Each contract file → contract test task [P]
   - Each endpoint → implementation task
   
2. **From Data Model**:
   - Each entity → model creation task [P]
   - Relationships → service layer tasks
   
3. **From User Stories**:
   - Each story → integration test [P]
   - Quickstart scenarios → validation tasks

4. **Ordering**:
   - Setup → Tests → Models → Services → Endpoints → UI → Polish
   - Dependencies block parallel execution

## Validation Checklist
*GATE: Checked by main() before returning*

- [x] All contracts have corresponding tests
- [x] All entities have model tasks
- [x] All tests come before implementation
- [x] Parallel tasks truly independent
- [x] Each task specifies exact file path
- [x] No task modifies same file as another [P] task