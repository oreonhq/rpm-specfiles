%global source0_hash 18f63100d6f94385c6ed57a72073443e1a71a4acb4339491615d0f16d6ff01b2

%{?mingw_package_header}

%global pkgname flit-core
%global pypi_name flit_core

Name:           mingw-python-%{pkgname}
Summary:        MinGW Python %{pypi_name} library
Version:        3.12.0
Release:        3%{?dist}
BuildArch:      noarch

License:        BSD-2-Clause
Url:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}

BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-python3

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-python3

%description
MinGW Python %{pypi_name} library.

%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Python 3 %{pypi_name} library

%description -n mingw32-python3-%{pkgname}
MinGW Python 3 %{pypi_name} library.

%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Python 3 %{pypi_name} library

%description -n mingw64-python3-%{pkgname}
MinGW Python 3 %{pypi_name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build
# See https://flit.pypa.io/en/stable/bootstrap.html
# It is a pure python module, one wheel is sufficient for all
# %%mingw32_python3_version is the same as %%mingw64_python3_version
/usr/bin/python%{mingw32_python3_version} -m flit_core.wheel

%install
mkdir -p %{buildroot}%{mingw32_python3_sitearch}
mkdir -p %{buildroot}%{mingw32_python3_hostsitearch}
mkdir -p %{buildroot}%{mingw64_python3_sitearch}
mkdir -p %{buildroot}%{mingw64_python3_hostsitearch}

%mingw32_python3 bootstrap_install.py --installdir %{buildroot}%{mingw32_python3_sitearch} dist/flit_core-*.whl
%mingw32_python3_host bootstrap_install.py --installdir %{buildroot}%{mingw32_python3_hostsitearch} dist/flit_core-*.whl
%mingw64_python3 bootstrap_install.py --installdir %{buildroot}%{mingw64_python3_sitearch} dist/flit_core-*.whl
%mingw64_python3_host bootstrap_install.py --installdir %{buildroot}%{mingw64_python3_hostsitearch} dist/flit_core-*.whl

%files -n mingw32-python3-%{pkgname}
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/
%{mingw32_python3_hostsitearch}/%{pypi_name}/
%{mingw32_python3_hostsitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pkgname}
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/
%{mingw64_python3_hostsitearch}/%{pypi_name}/
%{mingw64_python3_hostsitearch}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
