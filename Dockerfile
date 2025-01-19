FROM public.ecr.aws/lambda/python:3.9

COPY . ${LAMBDA_TASK_ROOT}

RUN pip install --no-cache-dir -r ${LAMBDA_TASK_ROOT}/requirements.txt

RUN python -c "from services.ml_model import train_model; train_model()"

CMD ["app.handler"]
