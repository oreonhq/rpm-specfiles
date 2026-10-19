%global source0_hash b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f
%{?mingw_package_header}
%global pypi_name toml
Name:           mingw-python-%{pypi_name}
Summary:        MinGW Python toml
Version:        0.10.2
Release:        1%{?dist}
BuildArch:      noarch
License:        MIT
Url:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/m/mingw-python-toml/mingw-python-toml-%{version}.tar.gz
# oreon:deps
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-toml -f %{oreon_filedir}/mingw32-python3-toml.list
%files -n mingw64-python3-toml -f %{oreon_filedir}/mingw64-python3-toml.list

%changelog

%autochangelog
