%global source0_hash c590a0a5b00363397ca04e3921475f4ed978f875d15bde24e0e52209bba0b431

%global pypi_name pyforgejo

Name:           python-%{pypi_name}
Version:        2.0.5
Release:        2%{?dist}
Summary:        A client library for accessing the Forgejo API

License:        MIT

URL:            https://codeberg.org/harabat/pyforgejo
Source0:        %{pypi_source %pypi_name}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
A client library for accessing the Forgejo API

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A client library for accessing the Forgejo API

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p0

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %pypi_name -L

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
