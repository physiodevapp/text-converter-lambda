FROM public.ecr.aws/lambda/python:3.9-slim

WORKDIR /app

COPY . ${LAMBDA_TASK_ROOT}

RUN pip install --no-cache-dir flask mangum

EXPOSE 5000

CMD ["lambda_handler.handler"]