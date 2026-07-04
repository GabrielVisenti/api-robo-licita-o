from app.models.municipio import Municipio
from app.services.importers.base_importer import BaseImporter


class MunicipioImporter(BaseImporter):

    def __init__(self, municipio_service, municipio_repository):
        super().__init__()
        self.municipio_service = municipio_service
        self.municipio_repository = municipio_repository

    def executar(self):
        self.iniciar()

        print("=" * 60)
        print("GV Radar - Importação de Municípios")
        print("=" * 60)

        municipios = self.municipio_service.buscar_municipios()
        self.total = len(municipios)

        print(f"Municípios encontrados: {self.total}")
        print()

        for item in municipios:

            codigo_ibge = item["codigo_ibge"]
            nome = item["nome"]
            uf = item["uf"]

            if self.municipio_repository.existe_codigo_ibge(codigo_ibge):
                self.ignorados += 1
                self.processados += 1
            else:
                municipio = Municipio(
                    codigo_ibge=codigo_ibge,
                    nome=nome,
                    uf=uf,
                )

                self.municipio_repository.criar(municipio)

                self.criados += 1
                self.processados += 1

            if self.processados % 250 == 0:
                print(f"Processados: {self.processados}/{self.total}")

        self.municipio_repository.salvar_alteracoes()
        self.finalizar()