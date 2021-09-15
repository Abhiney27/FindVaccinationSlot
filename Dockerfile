FROM centos:latest
RUN yum install net-tools -y
RUN yum install httpd -y
RUN yum install python3 -y
COPY requirements.txt /home
RUN pip3 install -r /home/requirements.txt
COPY CowinApp App
WORKDIR App
ENTRYPOINT ["python3", "app.py"]
EXPOSE 2708  2708                    
