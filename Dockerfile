FROM python:3.13-slim

WORKDIR /app

# 필요한 패키지 및 PDM 설치
RUN apt update && apt install -y chromium-driver curl \
    && curl -sSL https://pdm-project.org/install-pdm.py | python3 - \
    && export PATH=/root/.local/bin:$PATH \
    && pdm --version

# PATH 환경변수 설정
ENV PATH="/root/.local/bin:${PATH}"

# 프로젝트 파일 복사
COPY pyproject.toml pdm.lock ./
COPY *.py ./

# 의존성 설치 (PDM)
RUN pdm install --prod --no-lock --no-editable

CMD ["pdm", "run", "python", "main.py"]
