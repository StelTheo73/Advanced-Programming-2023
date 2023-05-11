FROM python

ENV AUTHOR=StelTheo73
ENV MAINTAINER=steltheo2001@gmail.com
ENV VERSION=1.0

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "-m", "MQTT"]
