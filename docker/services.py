import properties


class Services:
    SERVICES_NAMES = ['postgres']

    def get_start_command(self, service_name):
        if service_name == "postgres":
            return self._get_postgres_start_command()

    def get_enable_command(self, service_name):
        if service_name == "postgres":
            return self._get_postgres_enable_command()

    def get_stop_command(self, serivice_name):
        if serivice_name == "postgres":
            return self._get_postgres_stop_command()

    def _get_postgres_start_command(self):
        return ("docker run --name {container_name}"
                " -e POSTGRES_DB={db_name}"
                " -e POSTGRES_USER={user}"
                " -e POSTGRES_PASSWORD={passwd}"
                " -p {port}:{port}"
                " -d postgres:9.5.4").format(container_name=properties.POSTGRES_CONTAINER_NAME,
                                             db_name=properties.POSTGRES_DB_NAME,
                                             user=properties.POSTGRES_USER,
                                             passwd=properties.POSTGRES_PASSWORD,
                                             port=properties.POSTGRES_PORT)

    def _get_postgres_enable_command(self):
        return "docker start {container_name}".format(
            container_name=properties.POSTGRES_CONTAINER_NAME)

    def _get_postgres_stop_command(self):
        return "docker stop {container_name}".format(
            container_name=properties.POSTGRES_CONTAINER_NAME)
