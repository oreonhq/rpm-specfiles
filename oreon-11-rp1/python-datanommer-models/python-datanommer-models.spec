%global source0_hash 36990209b94c2b834701cab243323044e6e77a2a9ea9f1ae86b039e4604d450f

Name:           python-datanommer-models
Version:        1.5.0
Release:        %autorelease
Summary:        SQLAlchemy models for datanommer

License:        GPL-3.0-or-later
URL:            https://github.com/fedora-infra/datanommer
Source:         %{pypi_source datanommer_models}

BuildArch:      noarch
BuildRequires:  python3-devel

# Test dependencies
#BuildRequires:  python3dist(pytest)
#BuildRequires:  python3dist(pytest-postgresql)

%global _description %{expand:
SQLAlchemy models for datanommer. }

%description %_description

%package -n python3-datanommer-models
Summary:        %{summary}

%description -n python3-datanommer-models %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n datanommer_models-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L datanommer

# The tests suites requires the messaging schema that are currently not packaged
# in Fedora. We can try to make the %%pytest macro running later when they are available.
%check
%pyproject_check_import -t

%files -n python3-datanommer-models -f %{pyproject_files}
%doc README.*
%doc NEWS.*
%license LICENSE

%changelog
%autochangelog
