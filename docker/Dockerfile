FROM pytorch/pytorch:latest
#RUN pip install -r requirements.txt
COPY vgg16.py /app/vgg16.py
EXPOSE 8080
WORKDIR /app
CMD ['python','vgg16.py']
CMD ['python','layout_parser.py']
