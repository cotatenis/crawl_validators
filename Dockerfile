# Here is the build image
FROM python:3.8.0-slim as builder
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --user -r requirements.txt
COPY . /app
# Here is the production image
FROM python:3.8.0-slim as app
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/main.py /app/main.py
COPY --from=builder /app/config.py /app/config.py
COPY --from=builder /app/rules/*.py /app/rules/
COPY --from=builder /app/settings.toml /app/settings.toml


WORKDIR /app
ENV PATH=/root/.local/bin:$PATH
ENTRYPOINT ["python", "main.py"]