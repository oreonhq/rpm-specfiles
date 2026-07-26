%global source0_hash 71c37db75a0664325de149f43e2a712ec5fa1f90429a21dafbca005cb6767f94

%{?mingw_package_header}

%global mod_name pyqt5-sip
%global pypi_name pyqt5_sip

Name:           mingw-python-%{mod_name}
Summary:        MinGW Python %{pypi_name} library
Version:        12.18.0
Release:        1%{?dist}
BuildArch:      noarch

License:        GPL-2.0-only OR GPL-3.0-only
Url:            https://www.riverbankcomputing.com/software/sip/
Source0:        %{pypi_source}

BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build

%description
MinGW Python %{pypi_name} library.

%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Python 3 %{mod_name} library
Obsoletes:     mingw32-python3-%{pypi_name} < 12.11.0-2
Provides:      mingw32-python3-%{pypi_name} = %{version}-%{release}

%description -n mingw32-python3-%{mod_name}
MinGW Python 3 %{pypi_name} library.

%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Python 3 %{pypi_name} library
Obsoletes:     mingw64-python3-%{pypi_name} < 12.11.0-2
Provides:      mingw64-python3-%{pypi_name} = %{version}-%{release}

%description -n mingw64-python3-%{mod_name}
MinGW Python 3 %{pypi_name} library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel

%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel

%files -n mingw32-python3-%{mod_name}
%dir %{mingw32_python3_sitearch}/PyQt5/
%{mingw32_python3_sitearch}/PyQt5/sip*
%{mingw32_python3_sitearch}/pyqt5_sip-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%dir %{mingw64_python3_sitearch}/PyQt5/
%{mingw64_python3_sitearch}/PyQt5/sip*
%{mingw64_python3_sitearch}/pyqt5_sip-%{version}.dist-info/

%changelog
%autochangelog
