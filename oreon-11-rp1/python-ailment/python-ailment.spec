%global source0_hash af0cab93123a4db689bdc23f1ee00a0e5827d8ae00f83fcac871af6499ae7b47

%global pypi_name ailment

Name:           python-%{pypi_name}
Version:        9.2.158
Release:        5%{?dist}
Summary:        The angr intermediate language

License:        LicenseRef-Callaway-BSD
URL:            https://github.com/angr/ailment
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
 
%description
AIL is the angr intermediate language.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
AIL is the angr intermediate language.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
