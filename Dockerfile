FROM public.ecr.aws/lambda/python:3.9

COPY . ${LAMBDA_TASK_ROOT}

RUN pip install --no-cache-dir fastapi mangum uvicorn

CMD ["lambda_handler.handler"]
