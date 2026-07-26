%global source0_hash fa66a3cd324abd27ad8e65908d7af48d8198c0c185aeb22189cf40516de25941

%global sum Entity Relation Diagrams generation tool
%global desc \
ERAlchemy generates Entity Relation (ER) diagram (like the one below) from \
databases or from SQLAlchemy models.

Name:           eralchemy
Version:        1.5.0
Release:        3%{?dist}
Summary:        %{sum}

License:        Apache-2.0
URL:            https://github.com/eralchemy/eralchemy
Source0:        %pypi_source

Requires:       python3-%name = %version-%release
BuildRequires:  python3-devel

BuildArch:      noarch

%description
%desc

%package -n python3-%name
Summary:        %sum

%description -n python3-%name
%desc

%generate_buildrequires
#%%pyproject_buildrequires -x test
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

sed -i 's/graphviz >= 0.20.3/graphviz/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l eralchemy

%check
# Testsuite in progress: https://src.fedoraproject.org/rpms/eralchemy/pull-request/4
#%%pyproject_check_import
#%%pytest

%files
%license LICENSE
%doc README.md
%_bindir/eralchemy

%files -n python3-%name -f %pyproject_files
%license LICENSE

%changelog
%autochangelog
