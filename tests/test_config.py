from hidro_mg_rag.config import schema


def test_schema_uses_default_catalog(monkeypatch):
    monkeypatch.delenv("UC_CATALOG", raising=False)
    assert schema("bronze") == "workspace.bronze"


def test_schema_uses_env_catalog(monkeypatch):
    monkeypatch.setenv("UC_CATALOG", "hidro_mg_rag")
    assert schema("gold") == "hidro_mg_rag.gold"
