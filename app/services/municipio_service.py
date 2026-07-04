import httpx


class MunicipioService:

    UFS = [
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",
        "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
        "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO",
    ]

    IBGE_URL_POR_UF = (
        "https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
    )

    def buscar_municipios(self):
        municipios = []

        for uf in self.UFS:
            url = self.IBGE_URL_POR_UF.format(uf=uf)

            response = httpx.get(
                url,
                timeout=60,
            )

            response.raise_for_status()

            for item in response.json():
                municipios.append({
                    "codigo_ibge": str(item["id"]),
                    "nome": item["nome"],
                    "uf": uf,
                })

        return municipios