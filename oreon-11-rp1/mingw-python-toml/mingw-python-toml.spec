%global source0_hash b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f

%{?mingw_package_header}

%global pypi_name toml

Name:           mingw-python-%{pypi_name}
Summary:        MinGW Python %{pypi_name}
Version:        0.10.2
Release:        15%{?dist}
BuildArch:      noarch

License:        MIT
Url:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}

BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build

%description
MinGW Python %{pypi_name}

%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name}

%description -n mingw32-python3-%{pypi_name}
MinGW Python 3 %{pypi_name}.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name}

%description -n mingw64-python3-%{pypi_name}
MinGW Python 3 %{pypi_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel

%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel

%files -n mingw32-python3-%{pypi_name}
%license LICENSE
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
