%global source0_hash 65279f2ab73d7d9d42dd9efbe272e983ac2f8f1b9ee2fc073c84f0ff4c3d5ec0

%global forgeurl https://github.com/gorilla-co/odata-query
Version:        0.10.0b1
%forgemeta

Name:           python-odata-query
Release:        %autorelease
Summary:        An OData v4 query parser and transpiler for Python

License:        MIT
URL:            https://odata-query.readthedocs.io
Source0:        %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
odata-query is a library that parses OData v4 filter strings, and can convert
them to other forms such as Django Queries, SQLAlchemy Queries, or just plain
SQL.}

%description %_description

%package -n python3-odata-query
Summary:        %{summary}

%description -n python3-odata-query %_description

%pyproject_extras_subpkg -n python3-odata-query django sqlalchemy

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup
# Unpin pytest version, if it doesn't work, the build will fail
sed -i 's/pytest = { version = "^6.2 || ^7.0"/pytest = { version = ">=6.2"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files odata_query

%check
%tox

%files -n python3-odata-query -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
