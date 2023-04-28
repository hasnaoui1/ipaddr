FROM python
RUN pip install flask
RUN pip install pymongo 
WORKDIR /ipaddr
copy ./ ./
EXPOSE 2000
CMD ["python3" , "./api1mongo.py"]
