CONT_NAME=monitoring-classroom-api

script: logs
	@ docker-compose run script

logs: api
	@ docker logs $(CONT_NAME)

api:
	@ docker-compose up -d api

clean:
	@ docker-compose down
