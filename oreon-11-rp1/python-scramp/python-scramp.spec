%global source0_hash fe055ebbebf4397b9cb323fcc4b299f219cd1b03fd673ca40c97db04ac7d107e

%global pypi_name scramp

Name:           python-%{pypi_name}
Version:        1.4.6
Release:        5%{?dist}
Summary:        Implementation of the SCRAM protocol

License:        MIT-0
URL:            https://github.com/tlocke/scramp
Source0:        %{pypi_source %{pypi_name} %{version}}
BuildArch:      noarch

%description
Scramp is pure-Python implementation of the SCRAM authentication protocol.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
# The dependencies needed for testing don’t get auto-generated.
BuildRequires:  python3dist(passlib)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)

%description -n python3-%{pypi_name}
Scramp is a pure-Python implementation of the SCRAM authentication protocol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
